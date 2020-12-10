from rest_framework import viewsets

from .serializers import HeroSerializer, OrderSerializer, EcommerceSerializer, ClientSerializer, TransporterSerializer
from .entities.nodes import Order, Ecommerce, Client, Transporter
from datetime import datetime
from rest_framework.response import Response
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
import uuid
import json
from .utils import relationsFactory
from neomodel.exceptions import CardinalityViolation
from neomodel import db
from django.conf import settings as conf_settings


@csrf_exempt
@api_view(['POST'])
def createEcommerce(request):
    
    data = JSONParser().parse(request)
    now = datetime.now()
    formatedDate = now.strftime("%Y-%m-%d_%H:%M:%S")
    dateJoined= {"commerceDateJoined":formatedDate}
    commerceId = {"commerceId":uuid.uuid4()} 
    data.update(commerceId)
    data.update(dateJoined)
    serializer = EcommerceSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data)
    return JsonResponse(serializer.errors, status=400)

@csrf_exempt
@api_view(['POST'])
def createOrder(request):
    
    data = JSONParser().parse(request)
    orderSubmitter= data['orderSubmitterId']
    data.pop('orderSubmitterId')
    orderId = uuid.uuid4()
    orderIdDic = {"orderId": orderId} 
    data.update(orderIdDic)
    serializer = OrderSerializer(data=data)
    if serializer.is_valid():
        try:
            serializer.save()
            order=Order.nodes.get(orderId=orderId)
            associateOrderToSubmiter(orderSubmitter,order)
        except :
            return JsonResponse("could not submit the order, please try again", status=400)
        return JsonResponse(serializer.data)
    return JsonResponse(serializer.errors, status=400)

@csrf_exempt
@api_view(['POST'])
def createClient(request):
    data = JSONParser().parse(request)
    now = datetime.now()
    formatedDate = now.strftime("%Y-%m-%d_%H:%M:%S")
    dateJoined= {"clientDateJoined":formatedDate}
    clientId = {"clientId":uuid.uuid4()} 
    data.update(clientId)
    data.update(dateJoined)
    serializer = ClientSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data)
    return JsonResponse(serializer.errors, status=400)

@csrf_exempt
@api_view(['POST'])
def createTransporter(request):
    data = JSONParser().parse(request)
    now = datetime.now()
    formatedDate = now.strftime("%Y-%m-%d_%H:%M:%S")
    defaultData = {"transporterId":uuid.uuid4(),"transporterLat":0.0, "transporterLong":0.0,'transporterDateLeaved': '-',"transporterDateJoined":formatedDate} 
    data.update(defaultData)
    serializer = TransporterSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data)
    return JsonResponse(serializer.errors, status=400)

@api_view()
def listEcommerces(request):
    ecommerces = Ecommerce.nodes.all()
    serializer = EcommerceSerializer(ecommerces, many=True)
    return JsonResponse(serializer.data, safe=False)

@api_view()
def listClients(request):
    clients = Client.nodes.all()
    serializer = ClientSerializer(clients, many=True)
    return JsonResponse(serializer.data, safe=False)

@api_view()
def listTransporters(request):
    transporters = Transporter.nodes.all()
    serializer = TransporterSerializer(transporters, many=True)
    return JsonResponse(serializer.data, safe=False)

@api_view()
def listOrders(request):
    orders = Order.nodes.all()
    serializer = OrderSerializer(orders, many=True)
    return JsonResponse(serializer.data, safe=False)

@api_view()
def getOrderById(request,oId):
     order = Order.nodes.get(orderId=oId)
     serializer = OrderSerializer(order)
     return JsonResponse(serializer.data, safe=False)



@csrf_exempt
@api_view(['POST'])
def assignOrderToTransporter(request):
    data = JSONParser().parse(request)
    orderId = data['orderId']
    transporterId = data['transporterId']
    order = Order.nodes.get(orderId=orderId)
    transporter= Transporter.nodes.get(transporterId=transporterId)
    try:
        order.assignedTo.connect(transporter)
        return JsonResponse({"relationship":"CREATED"}, safe=False)
    except  CardinalityViolation as e :
        return JsonResponse(e, status=400)

def listTransporterOrders(request,transporterId):
    query = 'MATCH (o:Order)-[r:ASSIGNED_TO]-(t:Transporter) where t.transporterId=$transporterId return o'
    params = {"transporterId":transporterId}
    results, meta = db.cypher_query(query, params)
    orders = [Order.inflate(row[0]) for row in results]
    serializer = OrderSerializer(orders, many=True)
    return JsonResponse(serializer.data, safe=False)




def listPotentialTransportersForOrder(request, orderId):
    order = Order.nodes.get(orderId=oId)
    params = {"orderId":orderId}
    # retrieve order submitter : e_commerce or direct client 
    query1 = 'MATCH (c:Ecommerce)-[:SUBMITTED]-(o:Order) where o.orderId=$orderId return c'
    query2 =  'MATCH (c:Client)-[:SUBMITTED]-(o:Order) where o.orderId=$orderId return c'
    results, meta = db.cypher_query(query, params)


def associateOrderToSubmiter(orderSubmitterId,order):
    client = None
    commerce = None
    try:
        client = Client.nodes.get(clientId=orderSubmitterId)
    except:
        pass

    try:
        commerce= Ecommerce.nodes.get(commerceId=orderSubmitterId)
    except :
        pass

    if client != None or commerce != None :
        if client == None :
            try:
                commerce.submitted.connect(order)
            except  CardinalityViolation as e :
                raise Exception(e)
        else:
            try:
                client.submitted.connect(order)
            except  CardinalityViolation as e :
                raise Exception(e)


    

    
    









