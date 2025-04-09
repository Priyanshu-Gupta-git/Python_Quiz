# 🐍 Python Knowledge Constrictor - Quiz Game

Welcome to **Python Knowledge Constrictor**, a fun and interactive Python quiz game built using **Tkinter**.  
This game is designed to test your Python programming knowledge through a series of multiple-choice questions — all under time pressure! 🧠🔥

---

## 🎯 Features

- ✅ **12 Multiple Choice Questions** to test your Python skills  
- ⏳ **20-second countdown timer** for each question  
- 📊 **Progress bar** to show your question progress  
- 🧠 **Score evaluation**: Beginner, Intermediate, or Advanced  
- 🎨 **Attractive GUI** using Tkinter and emojis  
- 💻 **Standalone `.exe` version available** (no need for Python installed)  

---

## 🛠️ How to Run the Game (Source Code)

1. Make sure Python is installed (3.8 or above).
2. Install required module:
   ```bash
   pip install pillow
   ```
3. Run the script:
   ```bash
   python quiz_game.py
   ```

---

## 🧪 How I Created the `.exe` File using PyInstaller

I converted the Python script into a Windows executable using **PyInstaller** so users don’t need Python installed.

### Steps I Followed:

1. Installed PyInstaller:
   ```bash
   pip install pyinstaller
   ```

2. Converted script into `.exe`:
   ```bash
   pyinstaller --onefile --noconsole quiz_game.py
   ```

3. Found the `.exe` in the `dist` folder:
   ```
   dist/quiz_game.exe
   ```

### Explanation:
- `--onefile`: Combines everything into a single executable  
- `--noconsole`: Prevents console window from appearing (good for GUI apps)

---

## 📦 How I Created a Windows Installer using Inno Setup

To distribute the game like professional software, I created a setup file using **Inno Setup**.

### Steps I Followed:

1. Installed [Inno Setup](https://jrsoftware.org/isinfo.php)
2. Wrote this `.iss` script:
   ```iss
   [Setup]
   AppName=Python Knowledge Constrictor
   AppVersion=1.0
   DefaultDirName={pf}\PythonQuizGame
   DefaultGroupName=Python Knowledge Constrictor
   OutputBaseFilename=PythonQuizInstaller
   Compression=lzma
   SolidCompression=yes

   [Files]
   Source: "dist\quiz_game.exe"; DestDir: "{app}"; Flags: ignoreversion

   [Icons]
   Name: "{group}\Python Knowledge Constrictor"; Filename: "{app}\quiz_game.exe"
   ```

3. Compiled it with Inno Setup and got a `.exe` installer ready to share!

---


## 👤 Author Priyanshu Gupta 

Made with ❤️ using Python and Tkinter.  
If you enjoy this project, don’t forget to ⭐ the repo!

---

## 📃 License

This project is licensed under the **MIT License**.
