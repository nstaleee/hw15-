import requests
from pprint import pprint

url = 'https://script.google.com/macros/s/AKfycbyZPugDtdFm2uWePVygStAx5naJBuM58wrwCbOJkYMU_ITB0GaYoE1vKz8u2RF1QVJc/exec'
data = requests.get(url)

data_dict = data.json()

# pprint(data_dict)
result = sum([
    product['Ціна'] * product['залишок'] for product in
    data_dict['goods']
    if not product['Містить глютен']
])
pprint(result)
