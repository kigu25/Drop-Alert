from dotenv import load_dotenv
import os
from discord_webhook import DiscordWebhook



def discord_webhook():

    load_dotenv()
    webhook_url = os.getenv("DISCORD_WEBHOOK_URL")
    webhook = DiscordWebhook(url=webhook_url, content="TEST WEBHOOK")
    response = webhook.execute()
