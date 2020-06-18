import requests
import json
from decimal import Decimal

api_url_base = 'https://d6bg74q53e.execute-api.us-east-1.amazonaws.com/dev/'
endPoint = 'api/gianini'

# Insert the product into my dynamoDB
def insert(product):

    response = requests.post(api_url_base + endPoint +
                             '/{0}/{1}'.format('Products', 'insert'), json=product)
    return response.json()