#!/usr/bin/env python
'''Conveniently embed youtube search results in IPython notebook'''

from googleapiclient.discovery import build
from IPython.display import YouTubeVideo

import os

import warnings

DEVELOPER_KEY = os.environ.get('IPYTUBE_API_KEY')

YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"


def search(query, **kwargs):
    '''Search youtube, and if any hits come up, return an IPython
    embed object.

    Parameters
    ----------
    query : str
        The query text

    kwargs
        additional keyword arguments

    See Also
    --------
    IPython.display.YouTubeVideo
    '''
    youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
                    developerKey=DEVELOPER_KEY)

    search_response = youtube.search().list(q=query, part="id,snippet",
                                            maxResults=1).execute()

    for result in search_response.get("items", []):
        if result["id"]["kind"] == "youtube#video":
            return YouTubeVideo(result['id']['videoId'], **kwargs)

    warnings.warn('No results found.')
    return None
