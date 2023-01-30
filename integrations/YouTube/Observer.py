from integrations.YouTube.config import statusMessaging
class Observer:
    def __init__(self, status):
        self.status = status

    async def audio_download_commence(self):
        if statusMessaging["audioCommence"]:
            await self.status.edit("Audio download commencing...")

    async def audio_download_complete(self):
        if statusMessaging["audioComplete"]:
            await self.status.edit("Audio download complete.")

    async def video_download_commence(self):
        if statusMessaging["videoCommence"]:
            await self.status.edit("Video download commencing...")

    async def video_download_complete(self):
        if statusMessaging["videoComplete"]:
            await self.status.edit("Video download complete.")

    async def transcode_commence(self):
        if statusMessaging["transcodeCommence"]:
            await self.status.edit("Transcode commencing...")

    async def transcode_complete(self):
        if statusMessaging["transcodeComplete"]:
            await self.status.edit("Transcode complete.")

    async def stitch_commence(self):
        if statusMessaging["stitchCommence"]:
            await self.status.edit("Stitch commencing. This might take a while...")

    async def stitch_complete(self):
        if statusMessaging["stitchComplete"]:
            await self.status.edit("Stitch complete.")