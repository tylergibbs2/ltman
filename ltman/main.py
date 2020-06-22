from typing import List

from ltman.ffmpeg import file_to_mp3, normalize_audio
from ltman.ytdl import download_link


def process_links(links: List[str]) -> List[bool]:
    """
    Process a list of links via the process_link function.

    Parameters
    ----------
    links: List[str]
        A list of links to process.

    Returns
    -------
    List[bool]:
        A list of result statuses.
    """
    return [process_link(link) for link in links]


def process_link(link: str) -> bool:
    """
    Processes a link for downloading (ytdl),
    converting (ffmpeg), and normalizing (ffmpeg).

    Parameters
    ----------
    link: str
        The link to process.

    Returns
    -------
    bool:
        The result of the processing.
    """
    downloaded = download_link(link)

    converted = file_to_mp3(downloaded)

    normalize_audio(converted)
