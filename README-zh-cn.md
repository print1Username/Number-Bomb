# 数字炸弹

[![Python Test](https://github.com/print1Username/Number-Bomb/actions/workflows/test.yml/badge.svg)](https://github.com/print1Username/Number-Bomb/actions/workflows/test.yml)

[English](README.md) | [中文](README-zh-cn.md)

数字炸弹是一个简单的 Python 猜数字小游戏，使用图形窗口运行。游戏开始前，玩家可以选择数字范围和机会次数。之后玩家需要在机会用完之前猜中隐藏数字。

## 功能

- 可以自定义最小值和最大值。
- 可以自定义猜测机会次数。
- 每次猜错后，数字范围会自动缩小。
- 玩家猜过的数字会从新范围中排除。
- 猜中后会进入胜利页面。
- 机会用完后会进入失败页面，并显示正确答案。
- 支持键盘快捷键。

## 运行需求

你只需要安装 Python。

本项目使用 `tkinter` 制作图形窗口。`tkinter` 通常已经包含在 Windows 的标准 Python 安装中，所以运行游戏不需要额外安装第三方套件。

建议版本：

```bash
Python 3.10 或更新版本
```

## 如何运行

1. 下载或克隆这个项目。
2. 在项目文件夹中打开终端。
3. 运行游戏：

```bash
python main.py
```

如果 `python` 指令无法使用，可以试试：

```bash
py main.py
```

## 如何游玩

1. 输入最小值。
2. 输入最大值。
3. 输入机会次数。
4. 点击 `Start`，或按下 `Enter`。
5. 输入你要猜的数字。
6. 点击 `Guess`，或按下 `Enter`。

如果猜的数字太小，最小范围会变大。

例子：如果当前范围是 `1 ~ 100`，你猜了 `50`，新的范围可能会变成 `51 ~ 100`。

如果猜的数字太大，最大范围会变小。

例子：如果当前范围是 `1 ~ 100`，你猜了 `80`，新的范围可能会变成 `1 ~ 79`。

如果在机会用完之前猜中正确数字，你就获胜。

如果机会全部用完仍然没有猜中，你就失败，游戏会显示正确答案。

## 键盘快捷键

- `Enter`：触发当前页面的主要按钮。
- `Esc`：打开退出确认窗口。
- 在退出确认窗口中，`Enter` 表示退出程序。
- 在退出确认窗口中，`Esc` 表示留在游戏中。

## 项目结构

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

## 给初学者的说明

- `main.py` 是程序入口，用来启动游戏。
- `src/App.py` 控制游戏页面和玩家操作。
- `src/Games.py` 控制随机数字、范围和机会次数。
- `src/Windows.py` 包含窗口和界面相关的辅助功能。

如果图标文件不存在，游戏仍然可以运行。程序只会在终端中显示一个警告。
## 如何打包成 EXE 文件

如果你想让其他 Windows 用户不安装 Python 也能直接玩这个游戏，可以把项目打包成 `.exe` 文件。

本项目使用 **PyInstaller** 进行打包。

注意：工具名称是 `pyinstaller`，不是 `pipinstaller`。

### 1. 安装 PyInstaller

打开终端，运行：

```bash
pip install pyinstaller
```

如果 `pip` 指令无法使用，可以试试：

```bash
py -m pip install pyinstaller
```

### 2. 打开项目文件夹

在终端中进入这个项目文件夹。

例子：

```bash
cd "C:\Users\User\Documents\GitHub\Number Bomb"
```

如果你的项目在其他位置，请把路径换成你自己的项目路径。

### 3. 打包 EXE

运行这个指令：

```bash
pyinstaller --onefile --windowed --name "Number Bomb" --icon assets/icon.ico main.py
```

这个指令的意思：

- `--onefile`：打包成一个 `.exe` 文件。
- `--windowed`：启动游戏时不显示黑色终端窗口。
- `--name "Number Bomb"`：设置输出文件名称。
- `--icon assets/icon.ico`：使用 `assets` 文件夹里的图标。
- `main.py`：告诉 PyInstaller 程序从哪个文件开始运行。

### 4. 找到打包完成的 EXE

打包完成后，PyInstaller 会产生一些新的文件和文件夹。

完成后的游戏文件通常在这里：

```text
dist/Number Bomb.exe
```

这个 `.exe` 文件就是可以发给其他 Windows 用户游玩的文件。

### `dist`、`build` 和 `.spec` 是什么？

打包后，你可能会看到这些文件：

```text
build/
dist/
Number Bomb.spec
```

简单说明：

- `dist/`：里面放着最终完成的 `.exe` 文件。
- `build/`：打包过程中产生的临时文件。
- `Number Bomb.spec`：PyInstaller 的打包设置文件。

如果只是要分享游戏，通常只需要发送 `dist/` 里面的 `.exe` 文件。

`build/` 可以删除。下次打包时 PyInstaller 会重新产生它。

`.spec` 文件可以保留。如果以后想用同样的设置重新打包，它会有用。

### 修改代码后重新打包

如果你修改了 Python 代码，需要重新运行 PyInstaller 指令：

```bash
pyinstaller --onefile --windowed --name "Number Bomb" --icon assets/icon.ico main.py
```

然后使用 `dist/` 文件夹里新的 `.exe` 文件。
