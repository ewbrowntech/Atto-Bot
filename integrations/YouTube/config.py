import os

storagePath = os.path.join(os.getcwd(), "storage")
statusMessaging = {
    "audioCommence": False,
    "audioComplete": False,
    "videoCommence": False,
    "videoComplete": False,
    "transcodeCommence": True,
    "transcodeComplete": True,
    "stitchingCommence": True,
    "stitchingComplete": True,
}
