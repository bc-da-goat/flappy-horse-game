# 🐴 Flappy Horse Game

A Flappy Bird clone where you play as a flying horse, avoiding obstacles in the sky!

**[➡️ Deploy to GitHub Pages](GITHUB_PAGES_SETUP.txt)** | **[💰 Add Ads & Monetize](MONETIZATION_GUIDE.md)** | **[🚀 Quick Deploy](deploy_to_github.bat)**

## How to Play

- **Spacebar**: Make the horse jump/flap
- Avoid obstacles (meteors, missiles, UFOs, and airplanes) coming from the right
- Score points by successfully avoiding obstacles
- Game ends when you collide with an obstacle

## Installation

1. Make sure you have Python 3.6+ installed
2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Running the Game

### Option 1: Play in Web Browser (Recommended)
- **Windows**: Double-click `start_server.bat`
- **Mac/Linux**: Run `python start_server.py`
- The game will automatically open in your browser at `http://localhost:8000`

### Option 2: Desktop Version
- **Windows**: Double-click `run_game.bat`
- **Mac/Linux**: Run `python run_game.py` or `./run_game.py`

### Option 3: Run Directly
Simply run:
```
python flappy_horse.py
```

## Game Features

- **Player**: Flying horse with wings (controlled by spacebar)
- **Obstacles**: Various obstacles with different movement patterns:
  - Horizontal: Move straight across
  - Diagonal: Move diagonally and bounce off top/bottom
  - Oscillating: Move in a wave pattern
- **Background**: Scrolling background image
- **Score System**: Points increase as you avoid obstacles
- **Game Over Screen**: Shows final score with restart option

## Controls

- **Spacebar**: Jump/Flap
- **R**: Restart game (when game over)
- **ESC**: Quit game

Enjoy playing!

---

## 🚀 Deploy Your Game Online

Want to publish your game and make money from it? See:

- **[DEPLOYMENT_SUMMARY.md](DEPLOYMENT_SUMMARY.md)** - Complete guide to deployment and monetization
- **[GITHUB_PAGES_SETUP.txt](GITHUB_PAGES_SETUP.txt)** - Step-by-step GitHub Pages setup
- **[MONETIZATION_GUIDE.md](MONETIZATION_GUIDE.md)** - How to add ads and make money

**Quick Deploy:** Just run `deploy_to_github.bat` and follow the prompts!

---

## 📄 Files Included

### Game Files
- `index.html` - Main game (web version)
- `flappy_horse.py` - Desktop version (Python/Pygame)
- `Images/` - All game assets

### Deployment
- `deploy_to_github.bat` - Automated GitHub deployment
- `.gitignore` - Git configuration
- `privacy-policy.html` - Required for ads

### Documentation
- `DEPLOYMENT_SUMMARY.md` - Complete deployment guide
- `GITHUB_PAGES_SETUP.txt` - Quick setup guide
- `MONETIZATION_GUIDE.md` - Ad monetization guide
- `README_DEPLOYMENT.md` - Detailed deployment instructions

### Monetization
- `index_with_ads.html` - Template with ad placeholders
- `privacy-policy.html` - Privacy policy page (required for ads)

---

## 🎮 Play Online

Once deployed, your game will be live at:
```
https://YOUR_USERNAME.github.io/REPO_NAME/
```

Share it, promote it, and start earning! 💰
