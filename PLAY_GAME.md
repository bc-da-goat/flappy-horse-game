# How to Play Flappy Horse Game

## Quick Start

1. **Open a Command Prompt or PowerShell** in the game folder
2. **Run this command:**
   ```
   python -m http.server 8000
   ```
3. **Open your browser** and go to:
   ```
   http://localhost:8000/index.html
   ```

## Alternative: Use the Batch File

1. **Double-click `simple_server.bat`**
2. Wait for it to open your browser automatically
3. If it doesn't open, manually go to: `http://localhost:8000/index.html`

## Troubleshooting

### "Connection Refused" Error
- Make sure the server window is still open (don't close it!)
- Try a different port: `python -m http.server 8001`
- Then go to: `http://localhost:8001/index.html`

### "404 File Not Found" Error
- Make sure you're in the correct folder (the one with `index.html`)
- Try going to: `http://localhost:8000/` first to see the file list
- Click on `index.html` from there

### Game Not Loading
- Open browser console (F12) and check for errors
- Make sure all image files are in the `Images` folder
- Try refreshing the page (Ctrl+F5)

### Port Already in Use
- Close other programs using port 8000
- Or use a different port: `python -m http.server 8001`

## Direct File Access (No Server)

If the server doesn't work, you can also:
1. Right-click `index.html`
2. Select "Open with" → Your web browser
3. Note: Some features may not work without a server due to browser security
