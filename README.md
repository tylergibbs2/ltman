# ltman


## Requirements

- Python 3.8.3+
- ffmpeg

## Installation

Ensure that `ffmpeg` is included in your PATH environment variable.

- `git clone https://github.com/tylergibbs2/ltman`
- `cd ltman`
- `python -m pip install -r requirements.txt`

## Usage

An item can be a URL, a path to a video file, a path to an audio file,
or a path to a text file. Text files must contain a list of items separated
by newlines.

Directly passing items to ltman
```sh
python -m ltman https://someurlhere/ https://anotherurl/ ...
```

Passing a file with items separated by newlines
```sh
python -m ltman input.txt
```

Combining all possible methods of passing items
```sh
python -m ltman https://url/ video.mp4 audio.mp3 input.txt
```