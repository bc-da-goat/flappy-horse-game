# Deploy Flappy Horse to GitHub Pages

## Step 1: Create GitHub Repository

1. Go to [GitHub](https://github.com) and sign in
2. Click the "+" icon in top right → "New repository"
3. Name it: `flappy-horse-game` (or any name you like)
4. Make it **Public** (required for GitHub Pages free hosting)
5. Don't initialize with README, .gitignore, or license
6. Click "Create repository"

## Step 2: Push Your Code to GitHub

Open a terminal in your project folder and run these commands:

```bash
# Initialize git repository
git init

# Add all files
git add .

# Commit files
git commit -m "Initial commit: Flappy Horse game"

# Add your GitHub repository as remote (replace with YOUR username and repo name)
git remote add origin https://github.com/YOUR_USERNAME/flappy-horse-game.git

# Push to GitHub
git branch -M main
git push -u origin main
```

## Step 3: Enable GitHub Pages

1. Go to your repository on GitHub
2. Click "Settings" tab
3. Scroll down to "Pages" in the left sidebar
4. Under "Source", select:
   - Branch: `main`
   - Folder: `/ (root)`
5. Click "Save"
6. Wait 2-5 minutes for deployment
7. Your game will be live at: `https://YOUR_USERNAME.github.io/flappy-horse-game/`

## Step 4: Access Your Game

Your game URL will be:
```
https://YOUR_USERNAME.github.io/flappy-horse-game/index.html
```

Or just:
```
https://YOUR_USERNAME.github.io/flappy-horse-game/
```

## Step 5: Update Your Game

Whenever you make changes:

```bash
git add .
git commit -m "Description of changes"
git push
```

GitHub Pages will automatically update in 1-2 minutes.

## Troubleshooting

### Images Not Loading
- Make sure the `Images` folder is committed to git
- Check that image paths are correct and case-sensitive
- Clear browser cache (Ctrl+F5)

### 404 Error
- Wait 5 minutes after enabling GitHub Pages
- Check that `index.html` is in the root of your repository
- Verify the repository is public

### Game Not Working
- Open browser console (F12) to see errors
- Check that all files are uploaded to GitHub
- Ensure image paths match exactly (case-sensitive on GitHub)

## Custom Domain (Optional)

1. Buy a domain (e.g., from Namecheap, Google Domains)
2. In GitHub repository settings → Pages → Custom domain
3. Enter your domain name
4. Update your domain's DNS settings with your domain provider
