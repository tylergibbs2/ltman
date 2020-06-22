import os
from typing import Tuple


def file_to_mp3(file_name: str) -> str:
    """
    Converts a specified file to mp3
    format.

    Parameters
    ----------
    file_name: str
        The file to convert to mp3.

    Returns
    -------
    str:
        The converted file name.
    """
    split = file_name.split(".")
    split[-1] = "mp3"
    output = ".".join(split)

    os.system(f"ffmpeg -y -i {file_name} -vn -c:a libmp3lame {output} -hide_banner -loglevel panic")
    os.remove(file_name)

    return output


def normalize_audio(file_name: str) -> None:
    """
    Normalizes audio for a specified file.

    Parameters
    ----------
    file_name: str
        The file name to normalize.

    Returns
    -------
    None
    """
    os.system(f"ffmpeg-normalize {file_name} -of output -c:a libmp3lame -ext mp3 -q --target-level -5")
    os.remove(file_name)
