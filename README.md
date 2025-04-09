
# 🐍 Python Knowledge Constrictor - Quiz Game

Welcome to **Python Knowledge Constrictor**, a fun and interactive Python quiz game built with **Tkinter**!

This quiz is designed to test your Python programming knowledge through multiple-choice questions with a timer. At the end of the quiz, you'll get a score and your knowledge level — Beginner, Intermediate, or Advanced!

---

## 🎮 Features

- ✅ 12 well-crafted Python MCQs
- ⏳ Countdown timer (20 seconds per question)
- 📊 Progress bar to track your quiz journey
- 🎯 Final score with level classification
- 💻 Easy-to-use graphical user interface (GUI)
- 🛠️ Windows installer available (built using Inno Setup)

---

## 🖥️ Technologies Used

- **Python 3**
- **Tkinter** (for GUI)
- **ttk Progressbar**
- **PIL (Pillow)** (optional, if image features are added)
- **Inno Setup** (for creating Windows executable installer)

---

## 🚀 How to Run

### 🔹 If Running from Source Code:

1. Make sure Python 3 is installed.
2. Install dependencies (if not already):
   ```bash
   pip install pillow
Run the script:


python quiz_game.py
🔹 If Using Windows Installer:
Download the .exe setup file from the Releases section (link to be updated).

Install the application using the setup wizard.

Launch the game from the Start Menu or Desktop shortcut.

🧠 Quiz Scoring System
Score Range	Level
0 - 15	Beginner
16 - 28	Intermediate
29 - 48	Advanced
Each correct answer carries different scores based on difficulty (e.g., 4, 5, or 6 points).


📦 Installer Creation (For Developers)
Installer created using Inno Setup. To build it:

Install Inno Setup.

Use a script like this to create the installer:


[Setup]
AppName=Python Quiz Game
AppVersion=1.0
DefaultDirName={pf}\PythonQuizGame
DefaultGroupName=Python Quiz Game
OutputDir=.\dist
OutputBaseFilename=PythonQuizInstaller

[Files]
Source: "dist\quiz_game.exe"; DestDir: "{app}"; Flags: ignoreversion

[Icons]
Name: "{group}\Python Quiz Game"; Filename: "{app}\quiz_game.exe"
Name: "{commondesktop}\Python Quiz Game"; Filename: "{app}\quiz_game.exe"
📃 License
This project is open-source and available under the MIT License.

🤝 Contributing
Pull requests are welcome! Feel free to suggest improvements or add new features.

📫 Contact
For queries or collaboration, feel free to reach out:

📧 Email: your-email@example.com
🐙 GitHub: yourusername

✨ Enjoy the quiz and level up your Python skills!


