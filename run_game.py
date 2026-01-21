#!/usr/bin/env python3
"""
Launcher script for Flappy Horse Game
"""
import subprocess
import sys
import os

def check_and_install_dependencies():
    """Check if pygame is installed, install if not"""
    try:
        import pygame
        print("✓ Pygame is already installed")
    except ImportError:
        print("Installing pygame...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
        print("✓ Dependencies installed")

def main():
    print("=" * 50)
    print("  Flappy Horse Game Launcher")
    print("=" * 50)
    print()
    
    # Check dependencies
    check_and_install_dependencies()
    print()
    
    # Check if game file exists
    if not os.path.exists("flappy_horse.py"):
        print("ERROR: flappy_horse.py not found!")
        input("Press Enter to exit...")
        return
    
    print("Starting game...")
    print()
    print("-" * 50)
    
    # Run the game
    try:
        subprocess.run([sys.executable, "flappy_horse.py"])
    except KeyboardInterrupt:
        print("\n\nGame interrupted by user.")
    except Exception as e:
        print(f"\nERROR: Failed to run game: {e}")
        input("Press Enter to exit...")

if __name__ == "__main__":
    main()
