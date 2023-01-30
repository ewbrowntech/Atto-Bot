class URLNotFoundException(Exception):
    """Raised when a message does not contain a YouTube URL"""
    pass


class InvalidURLException(Exception):
    """Raised when a URL does not link to an available YouTube video"""
    pass
