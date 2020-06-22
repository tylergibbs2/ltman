import pathlib

import youtube_dl


ytdl_opts = {
    "format": "bestaudio/best",
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
        entry = info_dict["entries"][0]
        downloaded = f"{entry['title']}-{entry['id']}.{entry['ext']}"
        downloaded = youtube_dl.utils.sanitize_filename(downloaded, restricted=True)

    return downloaded
