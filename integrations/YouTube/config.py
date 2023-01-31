import os
'''
config.py

@Author - Ethan Brown - ewbrowntech@gmail.com
@Version - 30 JAN 23

Configurations used by the Atto-Bot YouTube integration'''

storagePath = os.path.join(os.getcwd(), "storage")
statusMessaging = {
    "audioCommence": True,
    "audioComplete": True,
    "videoCommence": True,
    "videoComplete": True,
    "transcodeCommence": True,
    "transcodeComplete": True,
    "stitchCommence": True,
    "stitchComplete": True,
}
