# Snake Game for Console

A simple Snake Game implemented in Python for the console.

### How to Play
Use arrow keys (w, a, s, d) to control the snake.
Navigate and eat the food (F) to grow and increase your score.
Enjoy the game!

### Requirements

- Python 3.x
- curses (Included with Python)

### Create a Virtual Environment (Optional but recommended)
On Linux/Mac:
```bash
python3 -m venv venv
```
On Windows:
```bash
python -m venv venv
```

### Activate the Virtual Environment
On Windows (PowerShell):
```bash
.\venv\Scripts\Activate
```

On Linux/Mac:
```bash
source venv/bin/activate
```


### Clone the Repository

```bash
git clone https://github.com/Momwhyareyouhere/Snake-Game-for-Console.git
cd Snake-Game-for-Console
```

### Install Packages
```bash
pip install -r requirements.txt
```

### Troubleshooting
Check Python Version:
Ensure that you are using a version of Python that includes the curses module. Most standard Python installations come with curses.

Install Windows Curses Library:
If you are using Python 3.9 or later on Windows, the windows-curses package may be needed. Install it using the following:
Linux:
```bash
sudo apt-get install libncurses5-dev libncursesw5-dev
```
Mac OS:
```bash
brew install ncurses
```
Windows:
```bash
pip install windows-curses
```

### Run the Game
On Windows:
```bash
python.exe snake_game.py
```

On Mac OS/Linux:
```bash
python snake_game.py
```

### Deactivate the Virtual Environment
```bash
deactivate
```

