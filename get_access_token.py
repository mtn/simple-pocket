import requests
from dotenv import load_dotenv
import os

if __name__ == "__main__":
    load_dotenv()

    data = {
        "consumer_key": os.getenv("CONSUMER_KEY"),
        "redirect_uri": "http://www.google.com",
    }
    resp = requests.post("https://getpocket.com/v3/oauth/request", data)
    code = str(resp.content).split("=")[1][:-1]

    print(
        f"Auth URL: https://getpocket.com/auth/authorize?request_token={code}&redirect_uri=http://www.google.com"
    )
    input()

    data = {"consumer_key": os.getenv("CONSUMER_KEY"), "code": code}
    resp = requests.post("https://getpocket.com/v3/oauth/authorize", data)
    access_token = str(resp.content).split("&")[0].split("=")[1]

    with open(".env", "w") as f:
        f.write(f"CONSUMER_KEY={os.getenv('CONSUMER_KEY')}\n")
        f.write(f"ACCESS_TOKEN={access_token}")
