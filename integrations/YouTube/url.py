import re
from integrations.YouTube.Errors import URLNotFoundException, InvalidURLException
from pytube_frontend.video_info import get_title
'''
url.py

@Author - Ethan Brown - ewbrowntech@gmail.com
@Version - 29 JAN 23

Extract a url from a message and verify that it is a YouTube video
'''


# Extract a URL from a message
def extract_url(messageContents):
    match = re.search(r'https://www.youtube.com/\S+|https://youtu.be/\S+', messageContents)
    if match:
        url = match.group(0)
        return url
    else:
        raise URLNotFoundException


# Check to see if URL corresponds to an available YouTube video
def verify_url(url):
    try:
        title = get_title(url)  # Attempting to get the title of an unavailable YouTube video will cause an exception
        return url
    except Exception:
        raise InvalidURLException