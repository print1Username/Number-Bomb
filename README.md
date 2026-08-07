# Number Bomb

[![Python Test](https://github.com/print1Username/Number-Bomb/actions/workflows/test.yml/badge.svg)](https://github.com/print1Username/Number-Bomb/actions/workflows/test.yml)

[English](README.md) | [Chinese](README-zh-cn.md)

Number Bomb is a simple Python guessing game with a graphical window. Before the game starts, you choose a number range and the number of chances. Then you try to guess the hidden number before your chances run out.

## Features

- Choose your own minimum and maximum number.
- Choose how many chances you have.
- The range updates after each wrong guess.
- The guessed number is excluded from the next range.
- Win page when you guess correctly.
- Game over page when your chances run out.
- Keyboard shortcuts for faster play.

## Requirements

You only need Python installed.

This project uses `tkinter`, which is included with most standard Python installations on Windows. You do not need to install extra packages to run the game.

Recommended version:

```bash
Python 3.10 or newer
```

## How To Run

1. Download or clone this project.
2. Open a terminal in the project folder.
3. Run the game:

```bash
python main.py
```

If `python` does not work, try:

```bash
py main.py
```

## How To Play

1. Enter a minimum value.
2. Enter a maximum value.
3. Enter the number of chances.
4. Click `Start`, or press `Enter`.
5. Type your guess.
6. Click `Guess`, or press `Enter`.

If your guess is too small, the minimum range will increase.

Example: if the range is `1 ~ 100` and you guess `50`, the new range can become `51 ~ 100`.

If your guess is too large, the maximum range will decrease.

Example: if the range is `1 ~ 100` and you guess `80`, the new range can become `1 ~ 79`.

You win if you guess the correct number before your chances run out.

You lose if you use all your chances. The game will show the correct answer.

## Keyboard Shortcuts

- `Enter`: activate the main button on the current page.
- `Esc`: open the exit confirmation window.
- In the exit confirmation window, `Enter` exits the program.
- In the exit confirmation window, `Esc` stays in the game.

## Project Structure

```text
Number Bomb/
|-- main.py
|-- src/
|   |-- App.py
|   |-- Games.py
|   `-- Windows.py
`-- assets/
    `-- icon.ico
```

## Notes For Beginners

- `main.py` starts the program.
- `src/App.py` controls the game pages and user actions.
- `src/Games.py` controls the random number, range, and chances.
- `src/Windows.py` contains the window and UI helper functions.

If the icon file is missing, the game can still run. It will only print a warning in the terminal.
## How To Build An EXE File

If you want to let other Windows users play the game without installing Python, you can package the project into an `.exe` file.

This project uses **PyInstaller** for packaging.

Important: the tool name is `pyinstaller`, not `pipinstaller`.

### 1. Install PyInstaller

Open a terminal and run:

```bash
pip install pyinstaller
```

If `pip` does not work, try:

```bash
py -m pip install pyinstaller
```

### 2. Open The Project Folder

In the terminal, go to this project folder.

Example:

```bash
cd "C:\Users\User\Documents\GitHub\Number Bomb"
```

If your project is in another location, replace the path with your own folder path.

### 3. Build The EXE

Run this command:

```bash
pyinstaller --onefile --windowed --name "Number Bomb" --icon assets/icon.ico main.py
```

What the command means:

- `--onefile`: creates one `.exe` file.
- `--windowed`: hides the black terminal window when the game starts.
- `--name "Number Bomb"`: sets the output file name.
- `--icon assets/icon.ico`: uses the icon file from the `assets` folder.
- `main.py`: tells PyInstaller which file starts the program.

### 4. Find The Finished EXE

After packaging, PyInstaller will create some new files and folders.

The finished game should be here:

```text
dist/Number Bomb.exe
```

This is the file you can send to other Windows users.

### What Are `dist`, `build`, And `.spec`?

After building, you may see these files:

```text
build/
dist/
Number Bomb.spec
```

Simple explanation:

- `dist/`: contains the final `.exe` file.
- `build/`: temporary files created during packaging.
- `Number Bomb.spec`: PyInstaller build settings.

For sharing the game, you usually only need the `.exe` file inside `dist/`.

You can delete `build/` if you want. PyInstaller can create it again next time.

You can keep the `.spec` file if you want to reuse the same build settings later.

### Rebuild The Game

If you change the Python code, run the PyInstaller command again:

```bash
pyinstaller --onefile --windowed --name "Number Bomb" --icon assets/icon.ico main.py
```

Then use the new `.exe` file from the `dist/` folder.
