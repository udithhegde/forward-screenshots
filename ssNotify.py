#!/usr/bin/env python
# pylint: disable=C0116,W0613
# This script monitors messages in a specifc telegram group ...
# and forwards only photos to a specified group using a bot account

from telethon import TelegramClient, events

# Enter you API ID and API hash here from https://my.telegram.org/
api_id = 321
api_hash = ''

client = TelegramClient('session1', api_id, api_hash)
client.start()
client1 = TelegramClient('session2', api_id, api_hash)
client1.start(bot_token='') # Enter your bot token here

grpToMonitor = -1001371184682
grpToForwrd = -728501203

@client.on(events.NewMessage(chats = grpToMonitor))
async def main(event):
    # Forward new message only if it is a photo
    if event.photo:
        await client1.send_message(grpToForwrd, 'Screenshot found')
        await event.forward_to(grpToForwrd)

client.run_until_disconnected()