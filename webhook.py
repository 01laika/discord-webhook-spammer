import requests
import crayons
import time
import json

headers = {"content-type": "application/json"}

hook = input(crayons.red("what is the webhook url?\t=> "))
content = input(crayons.red("input message to spam\t=> "))
data = {"content": content}
try: delay = float(input(crayons.red("delay per each message sent\t=> ")))
except ValueError:
    print(crayons.red("put a number in"))
else:
    print(crayons.green("[+] spam sent! [+]"))

    while True:
        time.sleep(delay)
        r = requests.post(hook, headers=headers, json=data)
        if r.status_code == 429:
            print(crayons.red("you are being rate limited!"))