import os
import requests
from utils.stores_info import build_product_url, build_image_url
from discord_webhook import DiscordWebhook, DiscordEmbed


def restock_webhook(item_name, price, store, product_id, imgUrl = ""):
    PRODUCT_URL = build_product_url(store, product_id)
    WEBHOOK_URL = os.getenv("DISCORD_WEBHOOK_URL")

    #Build the URL to the ImageLocation(URL)
    BUILT_IMG_URL = build_image_url(store, product_id, imgUrl)

    #fetch the data(image) from the ImageLocation(URL)
    image_data = fetch_product_image(BUILT_IMG_URL, store)

    webhook = DiscordWebhook(url=WEBHOOK_URL, username="Restock Alert")
    embed = DiscordEmbed(
        title=f"{item_name} — Restock detected",
        description=f"{store} has just restocked on {item_name}",
        url=PRODUCT_URL,
        color="E74C3C"
    )


    #Embed all the stuff into the message
    embed.set_author(name=f"Restock", icon_url=f"https://www.{store}.com/favicon.ico")

    embed.add_embed_field(name="Store", value=store, inline=True)
    embed.add_embed_field(name="Price", value=f"{price} kr", inline=True)
    embed.add_embed_field(name="\u200b", value=f"[Buy now]({PRODUCT_URL})", inline=False)

    #Add the file to the webhook then embed it.
    webhook.add_file(file=image_data, filename="product.jpg")
    embed.set_thumbnail(url="attachment://product.jpg")
    embed.set_footer(text="Restock Alert", icon_url=f"https://www.{store}.com/favicon.ico")
    embed.set_timestamp()

    webhook.add_embed(embed)
    webhook.execute()





def pinger_webhook():
    webhook_url = os.getenv("DISCORD_PINGER_URL")

    webhook = DiscordWebhook(url=webhook_url, username="VPS HealtCheck")

    embed = DiscordEmbed(
        title="VPS OK",
        description="VPS is still running - OK",
        color="008000"
    )

    embed.set_timestamp()

    webhook.add_embed(embed)
    webhook.execute()






def new_product_webhook(store, item_name, price, product_id ,imgUrl = ""):
    WEBHOOK_URL = os.getenv("DISCORD_NEW_PRODUCT_URL")
    BUILT_IMG_URL = build_image_url(store, product_id, imgUrl)

    image_data = fetch_product_image(BUILT_IMG_URL, store)

    webhook = DiscordWebhook(url=WEBHOOK_URL, username="ProductSniffer")
    embed = DiscordEmbed(
        title="New product detected",
        description=f"New product at {store} detected and added to DB",
        color="E74C3C"
    )

    embed.add_embed_field(name="Store", value=store, inline=True)
    embed.add_embed_field(name="Name", value=item_name, inline=True)
    embed.add_embed_field(name="Price", value=f"{price} kr", inline=True)


    webhook.add_file(file=image_data, filename="product.jpg")
    embed.set_thumbnail(url="attachment://product.jpg")
    embed.set_timestamp()

    webhook.add_embed(embed)
    webhook.execute()




#Function to get the actual image from the URL 
def fetch_product_image(image_url, store):
    response = requests.get(image_url, headers={"Referer": f"https://www.{store.lower()}.com"})
    return response.content