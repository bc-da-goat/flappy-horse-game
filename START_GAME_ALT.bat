@echo off
title Flappy Horse Game Server
cd /d "%~dp0"

echo.
echo ========================================
echo   FLAPPY HORSE GAME - STARTING SERVER
echo ========================================
echo.

REM Try different Python commands
echo Checking for Python...
python --version >nul 2>&1
if not errorlevel 1 (
    echo Found: python
    echo Starting server on port 8000...
    echo.
    echo Open your browser and go to:
    echo http://localhost:8000/index.html
    echo.
    echo Keep this window open!
    echo Press Ctrl+C to stop
    echo ========================================
    echo.
    python -m http.server 8000
    goto :end
)

py --version >nul 2>&1
if not errorlevel 1 (
    echo Found: py
    echo Starting server on port 8000...
    echo.
    echo Open your browser and go to:
    echo http://localhost:8000/index.html
    echo.
    echo Keep this window open!
    echo Press Ctrl+C to stop
    echo ========================================
    echo.
    py -m http.server 8000
    goto :end
)

python3 --version >nul 2>&1
if not errorlevel 1 (
    echo Found: python3
    echo Starting server on port 8000...
    echo.
    echo Open your browser and go to:
    echo http://localhost:8000/index.html
    echo.
    echo Keep this window open!
    echo Press Ctrl+C to stop
    echo ========================================
    echo.
    python3 -m http.server 8000
    goto :end
)

echo.
echo ERROR: Python not found!
echo.
echo Please install Python from: https://www.python.org/downloads/
echo.
echo Or try running manually:
echo   python -m http.server 8000
echo   py -m http.server 8000
echo   python3 -m http.server 8000
echo.
pause

:end
