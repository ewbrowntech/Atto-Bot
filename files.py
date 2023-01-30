import os
import discord

async def serve_file(status, filepath):
    server = status.channel.guild
    uploadLimit = server.filesize_limit# The maximum file upload size in bytes
    filesize = os.stat(filepath).st_size
    if not filesize > uploadLimit:
        await status.edit("Here you go!", file=discord.File(filepath))
    else:
        await status.edit("File is too big! Uploading to AttoHost...")

def delete_file(filepath):
    os.remove(filepath)
