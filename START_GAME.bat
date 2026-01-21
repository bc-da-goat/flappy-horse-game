@echo off
title Flappy Horse Game Server
color 0A
cd /d "%~dp0"

echo.
echo ========================================
echo   FLAPPY HORSE GAME - STARTING SERVER
echo ========================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python is not installed or not in PATH!
    echo.
    echo Please install Python from python.org
    echo Or try using: py -m http.server 8000
    echo.
    pause
    exit /b 1
)

echo Python found! Starting server...
echo.
echo Make sure this window stays open!
echo.
echo The game will open in your browser.
echo.
echo If it doesn't open automatically, go to:
echo http://localhost:8000/index.html
echo.
echo Press Ctrl+C to stop the server
echo ========================================
echo.

REM Try python first, then py as fallback
python -m http.server 8000 2>nul
if errorlevel 1 (
    echo Trying with 'py' command instead...
    py -m http.server 8000
)

pause
