import os
from discord_webhook import DiscordWebhook, DiscordEmbed



def restock_webhook(item_name, price, store, itemID):
    product_url = f"https://www.{store}.com/se/product/{itemID}"
    webhook_url = os.getenv("DISCORD_WEBHOOK_URL")

    webhook = DiscordWebhook(url=webhook_url, username="Restock Alert")

    embed = DiscordEmbed(
        title=f"{item_name} — Restock detected",
        description=f"{store} has just restocked on {item_name}",
        url=product_url,
        color="E74C3C"
    )

    embed.set_author(name=f"Restock", icon_url=f"https://www.{store}.com/favicon.ico")

    embed.add_embed_field(name="Store", value=store, inline=True)
    embed.add_embed_field(name="Price", value=f"{price} kr", inline=True)
    embed.add_embed_field(name="\u200b", value=f"[Buy now]({product_url})", inline=False)

    embed.set_footer(text="Restock Alert", icon_url=f"https://www.{store}.com/favicon.ico")
    embed.set_timestamp()

    webhook.add_embed(embed)
    webhook.execute()


def pinger_webhook():
    webhook_url = os.getenv("DISCORD_PINGER_URL")

    webhook = DiscordWebhook(url=webhook_url, username="Pinger")

    embed = DiscordEmbed(
        title="VPS OK",
        description="VPS is still running - OK",
        color="008000"
    )

    embed.set_timestamp()

    webhook.add_embed(embed)
    webhook.execute()