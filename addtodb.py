import requests
import random
import json

# for num in range(1,21):
#     r = requests.post('http://127.0.0.1:5050/store/store-{0}'.format(num))
#     print(r.status_code, r.reason)


for num in range(1,51):
    price = random.uniform(1.1, 50.9)
    store = random.randrange(172, 192)
    payload = { "price": price,
                "store_id": store
                }
    headers = {'content-type': 'application/json'}
    r = requests.post('http://127.0.0.1:5050/item/item-{0}'.format(num), data=json.dumps(payload), headers=headers)
    print(r.status_code, r.reason)