# desktuber
A Windows application to make your pngtuber (or anything, really) stay on your desktop, blink, and talk when you type.
Programmed in Python, desktuber relies on the tkinter and Pillow libraries.

Inspired by [veadotube](https://veado.tube/) and [Bongo Cat](https://store.steampowered.com/app/3419430/Bongo_Cat/).
Original Python code heavily references [Seebass22's tutorial](https://seebass22.github.io/python-desktop-pet-tutorial/2021/05/16/desktop-pet.html).

To use desktuber, clone this repository. \
Upload 4 pngs to the `assets` folder, following the naming conventions: `idle.png`, `talk.png`, `blink.png`, `talk_blink.png` \
Then, run `py main.py` from the `src` folder.

## Further implementation plans:
- _Convert codebase to C++_
- Fix transparency issues
- Make window resizeable
- Make tuber only speak on alphanumeric key presses

## Future GUI functionalities:
- Allow file uploading
- Allow ability to save presets

__code credits__:
- moving window: https://stackoverflow.com/a/74075517 
