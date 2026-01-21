@echo off
echo ========================================
echo   Deploy Flappy Horse to GitHub Pages
echo ========================================
echo.

REM Check if git is installed
git --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Git is not installed!
    echo Please install Git from: https://git-scm.com/downloads
    echo.
    pause
    exit /b 1
)

echo Git is installed!
echo.

REM Check if this is first time setup
if not exist .git (
    echo First time setup detected...
    echo.
    
    set /p USERNAME="Enter your GitHub username: "
    set /p REPONAME="Enter repository name (e.g., flappy-horse-game): "
    set /p NAME="Enter your name for git config: "
    set /p EMAIL="Enter your email for git config: "
    
    echo.
    echo Setting up git...
    git config --global user.name "%NAME%"
    git config --global user.email "%EMAIL%"
    
    echo Initializing repository...
    git init
    git add .
    git commit -m "Initial commit: Flappy Horse game"
    git branch -M main
    git remote add origin https://github.com/%USERNAME%/%REPONAME%.git
    
    echo.
    echo Pushing to GitHub...
    git push -u origin main
    
    echo.
    echo ========================================
    echo   SUCCESS!
    echo ========================================
    echo.
    echo Your game will be available at:
    echo https://%USERNAME%.github.io/%REPONAME%/
    echo.
    echo Now go to GitHub and enable Pages:
    echo 1. Go to your repository
    echo 2. Settings -^> Pages
    echo 3. Source: main branch, / (root)
    echo 4. Save
    echo.
    echo Wait 5 minutes, then visit your URL!
    echo.
) else (
    echo Updating existing repository...
    echo.
    
    set /p MESSAGE="Enter commit message (or press Enter for default): "
    if "%MESSAGE%"=="" set MESSAGE=Updated game files
    
    git add .
    git commit -m "%MESSAGE%"
    git push
    
    echo.
    echo ========================================
    echo   Updated successfully!
    echo ========================================
    echo.
    echo Changes will appear in 1-2 minutes.
    echo.
)

pause
