import os
import discord
from integrations.Atto.Atto import upload_file
'''
files.py

@Author - Ethan Brown - ewbrowntech@gmail.com
@Version - 29 JAN 23

Manage the storage and serving of files used by Atto-Bot
'''

async def serve_file(status, filepath):
    server = status.channel.guild
    uploadLimit = server.filesize_limit# The maximum file upload size in bytes
    filesize = os.stat(filepath).st_size
    if not filesize > uploadLimit:
        # await status.edit("Here you go!", file=discord.File(filepath))
        url = upload_file(filepath)
        await status.edit("File uploaded to AttoHost: " + url)
    else:
        url = upload_file(filepath)
        await status.edit("File uploaded to AttoHost: " + url)

def delete_file(filepath):
    os.remove(filepath)
