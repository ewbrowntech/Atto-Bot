import os
import discord
from integrations.Atto.Atto import get_atto_addresses, upload_file
'''
files.py

@Author - Ethan Brown - ewbrowntech@gmail.com
@Version - 07 FEB 23

Manage the storage and serving of files used by Atto-Bot
'''

async def serve_file(status, filepath):
    server = status.channel.guild
    uploadLimit = server.filesize_limit  # The maximum file upload size in bytes
    filesize = os.stat(filepath).st_size
    if not filesize > uploadLimit:
        await status.edit("Here you go!", file=discord.File(filepath))
    else:
        url = upload_file(filepath)
        await status.edit("This file is too big for Discord, so I uploaded it to AttoHost!\n"
                          + get_atto_addresses()["download"] + url)

def delete_file(filepath):
    os.remove(filepath)
