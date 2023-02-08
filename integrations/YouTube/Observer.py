from integrations.YouTube.config import statusMessaging
'''
Observer.py

@Author - Ethan Brown - ewbrowntech@gmail.com
@Version - 29 JAN 23

Observer object that can be used to display status messages during the download, transcode, and stitching processes
'''


class Observer:
    def __init__(self, status):
        self.status = status

    async def audio_download_commence(self):
        if statusMessaging["audioCommence"]:
            await self.status.edit(content="Downloading audio stream...")

    async def audio_download_complete(self):
        if statusMessaging["audioComplete"]:
            await self.status.edit(content="Audio download complete.")

    async def video_download_commence(self):
        if statusMessaging["videoCommence"]:
            await self.status.edit(content="Downloading video stream...")

    async def video_download_complete(self):
        if statusMessaging["videoComplete"]:
            await self.status.edit(content="Video download complete.")

    async def transcode_commence(self):
        if statusMessaging["transcodeCommence"]:
            await self.status.edit(content="Transcoding video stream...")

    async def transcode_complete(self):
        if statusMessaging["transcodeComplete"]:
            await self.status.edit(content="Transcode complete.")

    async def stitch_commence(self):
        if statusMessaging["stitchCommence"]:
            await self.status.edit(content="Stitch commencing. This might take a while...")

    async def stitch_complete(self):
        if statusMessaging["stitchComplete"]:
            await self.status.edit(content="Stitch complete.")