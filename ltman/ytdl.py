import pathlib

import youtube_dl


ytdl_opts = {
    "format": "bestaudio/best",
    "quiet": True,
    "no_warnings": True,
    "outmpl": "%(title)s-%(id)s.%(ext)s",
    "restrictfilenames": True
}


def download_link(link: str) -> str:
    """
    Downloads a given link at the highest audio
    quality and returns the file location.

    Parameters
    ----------
    link: str
        The link to download.

    Returns
    -------
    str:
        The downloaded file's name.
    """
    with youtube_dl.YoutubeDL(ytdl_opts) as downloader:
        info_dict = downloader.extract_info(link, download=True)

        try:
            entry = info_dict["entries"][0]
        except KeyError:
            entry = info_dict

        downloaded = downloader.prepare_filename(entry)

    return downloaded
