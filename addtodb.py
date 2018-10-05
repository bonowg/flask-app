import requests
import random
import json



# for num in range(1,21):
#     r = requests.post('http://127.0.0.1:5050/store/store-{0}'.format(num), headers=headers)
#     print(r.status_code, r.reason)
headers = {
        "Authorization": "JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE1Mzg3NTY4MTcsImlhdCI6MTUzODc1NjUxNywibmJmIjoxNTM4NzU2NTE3LCJpZGVudGl0eSI6MX0.jNVOJkLBCQsv8U0mVUfXDf02e-ZNbgIiUdtmFIieQDM",
        "Content-Type": "application/json"
    }

for num in range(1,51):
    price = random.uniform(1.1, 50.9)
    store = random.randrange(1, 21)
    payload = { "price": price,
                "store_id": store
                }

    r = requests.post('http://127.0.0.1:5050/item/item-{0}'.format(num), data=json.dumps(payload), headers=headers)
    print(r.status_code, r.reason)