from typing import List

import tqdm
from validators import url, ValidationFailure

from ltman.ffmpeg import file_to_mp3, normalize_audio
from ltman.ytdl import download_link


def process_all(all_: List[str]) -> None:
    """
    Processes all strings and will pass
    it to the respective function.

    Parameters
    ----------
    all_: List[str]
        Any type of reference.

    Returns
    -------
    None
    """
    bar = tqdm.tqdm(
        bar_format="{l_bar}{bar}| {n_fmt}/{total_fmt}",
        total=len(all_),
        position=0
    )

    for item in all_:
        bar.set_description_str(f"Current item: {item}")

        if url(item) == True:
            process_link(item)
        else:
            normalize_audio(item)

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
