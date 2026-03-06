import os
import random
import sys

import discord
from dotenv import load_dotenv

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

RESPONSES = [
    "Better be seen at oxford than caught at john's",
    "rather go to oxford than st johns",
    "watch your mouth before you get sent to St Johns",
    "when do we demolish st johns again?",
    "they say st john's was built to make the rest of cambridge look better.",
    "the best part of visiting st johns is when you leave",
    "st john's: proof that even cambridge makes mistakes",
    "i'd rather supervise at anglia ruskin than step foot in john's",
    "st john's bridge of sighs is called that because everyone sighs when they see the rest of the college",
    "john's may have a bridge of sighs but the real sigh is their acceptance rate",
    "fun fact: st john's was founded in 1511 and hasn't improved since",
    "even the cam flows faster past john's, trying to get away",
    "st john's: where ambition goes to punt",
    "heard john's library has one book and it's a map to trinity",
    "john's students don't need a may ball, any excuse to leave the college is celebration enough",
]


@client.event
async def on_message(message: discord.Message) -> None:
    if message.author != client.user and "john" in message.content.lower():
        response = random.choice(RESPONSES)
        await message.reply(response)


if __name__ == "__main__":
    load_dotenv()
    token = os.getenv("DISCORD_TOKEN")
    if token is None:
        sys.exit(1)
    else:
        client.run(token)
