from files import serve_file, delete_file
from pytube_frontend.downloader import Downloader
from pytube_frontend.video_info import get_title, get_resolutions_streams
from pytube_frontend.streams import get_streams
from integrations.YouTube.config import storagePath
from integrations.YouTube.Observer import Observer
from integrations.YouTube.Errors import URLNotFoundException, InvalidURLException
from integrations.YouTube.url import extract_url, verify_url
from asyncio import TimeoutError

'''
YouTube.py

@Author - Ethan Brown - ewbrowntech@gmail.com
@Version - 29 JAN 23

Download YouTube videos via PyTube-Frontend
'''

async def process_download_command(message, client):
    # Determine what form of copy the user would like
    if message.content.startswith('!download-audio'):
        await perform_operation(message, 'audio')
    elif message.content.startswith('!download-video-only'):
        await perform_operation(message, 'video-only', client)
    elif message.content.startswith('!download-video'):
        await perform_operation(message, 'video', client)
    else:
        await message.reply('You must specify what type of copy you would like.\t'
                                   '-\tEX: "!download-video [YouTube URL]"')
        return

async def perform_operation(message, format, client=None):
    try:
        url = extract_url(message.content)
        url = verify_url(url)

        match format:
            case 'audio':
                status = await message.reply("Downloading **" + get_title(url) + "** as **.mp3**")
                try:
                    streams = get_streams(url)
                except KeyError:
                    await status.edit("I'm sorry, but this video is Age-Restricted.")
                    return
                observer = Observer(status)
                downloader = Downloader(observer)
                filepath = await downloader.get_audio_copy(None, streams, storagePath)
                await serve_file(status, filepath)

            case 'video-only':
                menu = await message.reply("Determining available resolutions...")
                try:
                    streams = get_streams(url)
                except KeyError:
                    await menu.edit("I'm sorry, but this video is Age-Restricted.")
                    return
                resolution = await select_resolution(client, message, menu, streams)
                status = menu
                observer = Observer(status)
                downloader = Downloader(observer)
                if resolution is not None:
                    await menu.edit("Downloading **" + get_title(url) + "** as **.mp4** in **" + resolution + "**...")
                    filepath = await downloader.get_video_only_copy(None, streams, resolution, True, storagePath)
                    await serve_file(status, filepath)

            case 'video':
                menu = await message.reply("Determining available resolutions...")
                try:
                    streams = get_streams(url)
                except KeyError:
                    await menu.edit("I'm sorry, but this video is Age-Restricted.")
                    return
                resolution = await select_resolution(client, message, menu, streams)
                status = menu
                observer = Observer(status)
                downloader = Downloader(observer)
                if resolution is not None:
                    await menu.edit("Downloading **" + get_title(url) + "** as **.mp4** in **" + resolution + "**...")
                    filepath = await downloader.get_video_copy(None, streams, resolution, True, storagePath)
                    await serve_file(status, filepath)


    except URLNotFoundException:
        await message.reply('No YouTube URL detected.')
        return
    except InvalidURLException:
        await message.reply("The specified video either does not exist, is private, or is otherwise available")
        return

async def select_resolution(client, message, menu, streams):
    resolutions = get_resolutions_streams(streams)
    emoji_number_map = {f"{1}\u20e3": 1, f"{2}\u20e3": 2, f"{3}\u20e3": 3, f"{4}\u20e3": 4, f"{5}\u20e3": 5,
                        f"{6}\u20e3": 6, f"{7}\u20e3": 7, f"{8}\u20e3": 8, f"{9}\u20e3": 9, f"{10}\u20e3": 10}
    await menu.edit(f"What resolution do you like?\n"
                    + "   ".join([f"{index + 1}) {res}" for index, res in enumerate(resolutions)]))
    for i in range(len(resolutions)):
        await menu.add_reaction(f"{i + 1}\u20e3")

    def check(reaction, user):
        # Check if the reaction is one of the options and if it's made by the user who initiated the command
        try:
            option = emoji_number_map[reaction.emoji]
        except KeyError:
            raise KeyError
        return reaction.message.id == menu.id and user == message.author

    try:
        # Wait for the user to click a reaction
        reaction, user = await client.wait_for('reaction_add', check=check, timeout=30.0)
    except TimeoutError:
        # Handle the timeout error
        pass
    except KeyError:
        # Handle the Key
        pass
    else:
        # Get the selected option by looking at the emoji in the reaction
        await menu.clear_reactions()
        return resolutions[emoji_number_map[reaction.emoji] - 1]
