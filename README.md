# TinyFactorio

Same Factorio in just the 12% of the size!
Download the exe from the release page and run it in the Factorio directory.

- Replaces all ambient music sounds with silence
- Replaces all non-english fonts with a empty dummy .ttf file
- Replaces all high-resolutin png's with dummy .png files
- Packs factorio.exe with UPX
- Removes the `tests` and `doc-html` directories
- Removes debugging info
- Removes changelog
- Removes campaign
- Runs `pngquant` on all >100kb graphics

Written in Python 3. If you want to make a new .exe, just run `pyinstaller tinyfactorio.spec` after modifying the tinyfactorio.py