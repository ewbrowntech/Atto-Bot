'''
Error.py

@Author - Ethan Brown - ewbrowntech@gmail.com
@Version - 29 JAN 23

Define error types used in the downloading of YouTube videos
'''

class URLNotFoundException(Exception):
    """Raised when a message does not contain a YouTube URL"""
    pass


class InvalidURLException(Exception):
    """Raised when a URL does not link to an available YouTube video"""
    pass
