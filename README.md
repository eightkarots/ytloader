# ytloader
Download youtube videos into audio/ video format.

This repo includes both the original python script and the executuble file so that Windows users do not have to worry about dealing with installing Python and/ or dependencies (sorry Linux and Mac users).
Simply copy your youtube URL into the prompt and the program will download it onto either the audio or video file.

If you want to convert the python file into an executable yourself, you can run this command on the project directory with PyInstaller:
`python -m PyInstaller --onefile yt_converter.py`
Additionally, you can choose to include the `--icon=icon.ico` flag to change the icon image for the executable. The icon file will also need to be located under the project directory.

Any further questions can forwarded to **@e8k_** on discord.
