from neomodel import (StructuredNode, StringProperty, DateProperty, IntegerProperty,
                     EmailProperty, DateTimeProperty, FloatProperty, UniqueIdProperty,
                     RelationshipTo, Relationship)
from neomodel.cardinality import One, OneOrMore
from neomodel.relationship_manager import ZeroOrMore
from .relations import OrderSubmit, OrderAssignment, OrderDelivery


class Order(StructuredNode):
    """
    docstring
    """
    orderId= UniqueIdProperty()
    clientName = StringProperty()
    clientPhoneNumber = StringProperty()
    clientEmail = EmailProperty()
    clientAdress = StringProperty()
    description = StringProperty()
    estimatedDeliveryTime = StringProperty()
    assignedTo=RelationshipTo('Transporter','ASSIGNED_TO',cardinality=One,model=OrderAssignment)   
    delivered = RelationshipTo('Client','IS_DELIVERED_TO',cardinality=OneOrMore,model=OrderDelivery)


class Ecommerce(StructuredNode):
    commerceId = UniqueIdProperty()
    commerceName = StringProperty()
    commerceURL =  StringProperty()
    commerceEmail = EmailProperty()
    commerceAdress = StringProperty()
    commercePhone = StringProperty()
    commerceDescription = StringProperty()
    commerceDateJoined = StringProperty()
    commerceDateLeaved = StringProperty(default="-")
    submitted = Relationship('Order','SUBMITTED',cardinality=OneOrMore,model=OrderSubmit)
    
   
class Transporter(StructuredNode):
    transporterId = UniqueIdProperty()
    transporterName = StringProperty()
    transporterEmail = EmailProperty()
    transporterAdress = StringProperty()
    transporterPhone = StringProperty()
    transporterNumId= StringProperty()
    transporterVehicule = StringProperty()
    transporterLong =  FloatProperty(default=0)
    transporterLat =  FloatProperty(default=0)
    transporterDateJoined = StringProperty()
    transporterDateLeaved = StringProperty(default="-")
    delivered = RelationshipTo('Order','HAS_DELIVERED',cardinality=OneOrMore,model=OrderDelivery)

class Client(StructuredNode):
    clientId = UniqueIdProperty()
    clientName = StringProperty()
    clientEmail = EmailProperty()
    clientAdress = StringProperty()
    clientPhone = StringProperty()
    clientDateJoined = StringProperty()
    clientDateLeaved = StringProperty(default="-")
    submitted = Relationship('Order','SUBMITTED',cardinality=OneOrMore,model=OrderSubmit)
    


    