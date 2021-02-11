import requests
import time
import json
import rich
from rich.console import Console
console = Console()

def main():
    hook = console.input("[bold green]input webhook url =>[/bold green] ")
    
    try:
        r = requests.get(hook)
        if r.json()["message"]:
            console.print("[bold red]invalid webhook![/bold red]\n")
            time.sleep(1)
            main()
    except KeyError:
        pass

    content = console.input("[bold green]input message to spam => ")
    headers = {"content-type": "application/json"}
    data = {"content": content}
    try:
        delay = float(console.input("[bold green]delay per each message sent => [/bold green]"))
    except ValueError:
        console.print("[bold red]put a number in[/bold red]")
        time.sleep(1)
        main()  
    else:
        console.print("""[bold red]  ctrl-c to stop!\n {!} spam sent {!}[/bold red]""")

        while True:
            time.sleep(delay)
            r = requests.post(hook, headers=headers, json=data)
            if r.status_code == 429:
                console.print("[bold red]you are being rate limited!")

if __name__ == "__main__":
    main()
