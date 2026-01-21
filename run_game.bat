@echo off
echo Installing/Checking dependencies...
pip install -r requirements.txt
echo.
echo Starting Flappy Horse Game...
echo.
python flappy_horse.py
pause
