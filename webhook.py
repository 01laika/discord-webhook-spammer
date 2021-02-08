import requests
import crayons
import time
import json

def main():
    hook = input(crayons.red("what is the webhook url?\t=> "))

    try:
        r = requests.get(hook)
        if r.json()["message"]:
            print(crayons.red("invalid webhook!\n"))
            time.sleep(1)
            main()
    except KeyError:
        pass

    content = input(crayons.red("input message to spam\t=> "))
    headers = {"content-type": "application/json"}
    data = {"content": content}
    try: delay = float(input(crayons.red("delay per each message sent\t=> ")))
    except ValueError:
        print(crayons.red("put a number in"))
    else:
        print(crayons.green("{+} spam sent! {+}\nctrl-c to stop!"))

        while True:
            time.sleep(delay)
            r = requests.post(hook, headers=headers, json=data)
            if r.status_code == 429:
                print(crayons.red("you are being rate limited!"))

if __name__ == "__main__":
    main()
