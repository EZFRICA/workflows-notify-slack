import config

from fastapi import FastAPI
from slack_sdk.webhook import WebhookClient

app = FastAPI()


@app.post("/notify/", status_code=201)
async def notify(message: str):
    url = config.SLACK_URL_WEBHOOK
    webhook = WebhookClient(url)

    response = webhook.send(text=message)
    return response.body
