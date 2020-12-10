from neomodel import Relationship, RelationshipTo, RelationshipFrom
from neomodel.cardinality import One
from neomodel.relationship_manager import ZeroOrMore
from ..entities.relations import OrderSubmit, OrderAssignment, OrderDelivery

def createCommerceOrdersRelation():
    ""
    return Relationship('Ecommerce','SUBMITED',zeroOrMore,model=OrderSubmit)

def createClientOrdersRelation():
    ""
    return Relationship('Client','SUBMITED',zeroOrMore,model=OrderSubmit)

def createOrderToTransporterRelation():
    ""
    return RelationshipTo('Order','ASSIGNED_TO',cardinality=One,model=OrderAssignment)

def createOrderDeliveredToClientRelation():
    ""
    return RelationshipTo('Order','DELIVERED_TO',cardinality=One,model=OrderDelivery)

def createTransporterDeliveredOrderRelation():
    ""
    return RelationshipTo('Transporter','HAS_DELIVERED',zeroOrMore,model=OrderDelivery)
     

