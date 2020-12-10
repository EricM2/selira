from neomodel import ( StructuredRel, StringProperty, DateProperty, IntegerProperty, 
                        EmailProperty, DateTimeProperty, FloatProperty, UniqueIdProperty)
from datetime import datetime


class OrderSubmit(StructuredRel):
    submitDate = StringProperty(default=lambda: datetime.now().strftime("%Y-%m-%d_%H:%M:%S"))

class OrderDelivery(StructuredRel):
    deliveryDate = StringProperty(default=lambda: datetime.now().strftime("%Y-%m-%d_%H:%M:%S"))
    receiverName = StringProperty()
    receiverIdNumber = StringProperty()

class OrderAssignment(StructuredRel):
    assignmentDate = StringProperty(default=lambda: datetime.now().strftime("%Y-%m-%d_%H:%M:%S"))