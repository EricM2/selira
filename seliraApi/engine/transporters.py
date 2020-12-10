
import googlemaps
import environ
from django.conf import settings as conf_settings


def evaluateDistance(transporterPosition, clientPosition):
    """
    docstring
    Evaluate the distance bettween the transporter and the client destination 
    """
    env = environ.Env()
    environ.Env.read_env()
    api_key = conf_settings.GOOGLE_MAPS_API_KEY
    #settings.GOOGLE_MAPS_API_KEY
    gmaps = googlemaps.Client(api_key)
    matrix = gmaps.distance_matrix(transporterPosition,clientPosition)
    distance = matrix['rows'][0]['elements'][0]['distance']['value']
    duration = matrix['rows'][0]['elements'][0]['duration']['value']
    res = {"distance": distance, "duration": duration}
    print (res)
    return res

def 


evaluateDistance('Calle de Carlos Daban, 22, 28019 Madrid', 'Nike Factory Store, Polígono industrial Parque Oeste, Avenida Europa, s/n, 28925 Alcorcón, Madrid')