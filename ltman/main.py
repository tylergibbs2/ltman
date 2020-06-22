from typing import List

import tqdm

from ltman.ffmpeg import file_to_mp3, normalize_audio
from ltman.ytdl import download_link


def process_links(links: List[str]) -> None:
    """
    Process a list of links via the process_link function.

    Parameters
    ----------
    links: List[str]
        A list of links to process.

    Returns
    -------
    None
    """
    bar = tqdm.tqdm(
        bar_format="{l_bar}{bar}| {n_fmt}/{total_fmt}",
        total=len(links),
        position=0
    )

    for link in links:
        bar.set_description_str(f"Current link: {link}")
        process_link(link)
        bar.update(1)


def process_link(link: str) -> None:
    """
    Processes a link for downloading (ytdl),
    converting (ffmpeg), and normalizing (ffmpeg).

    Parameters
    ----------
    link: str
        The link to process.

    Returns
    -------
    None
    """
    downloaded = download_link(link)

    converted = file_to_mp3(downloaded)

    normalize_audio(converted)
