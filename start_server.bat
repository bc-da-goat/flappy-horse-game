@echo off
echo Starting web server for Flappy Horse Game...
echo.
python start_server.py
if errorlevel 1 (
    echo.
    echo ERROR: Server failed to start!
    echo.
    echo Trying alternative method...
    echo.
    python -m http.server 8000
)
pause
