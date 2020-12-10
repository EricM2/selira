from django.urls import include, path
from rest_framework import routers
from . import views

#router = routers.DefaultRouter()
#router.register(r'orders', views.OrderViewSet, basename='orders')

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    #path('', include(router.urls)),
    path('orders/', views.listOrders),
    path('order/add/', views.createOrder),
    path('ecommerces/', views.listEcommerces),
    path('ecommerce/add/', views.createEcommerce),
    path('clients/', views.listClients),
    path('client/add/', views.createClient),
    path('transporters/', views.listTransporters),
    path('transporter/add/', views.createTransporter),
    path('order/to/transporter/', views.assignOrderToTransporter),
    path('transporter/assigned/orders/<str:transporterId>/', views.listTransporterOrders),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]