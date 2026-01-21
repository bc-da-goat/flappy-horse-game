# How to Add Ads to Your Flappy Horse Game

## Option 1: Google AdSense (Recommended)

### Step 1: Sign Up for Google AdSense

1. Go to [Google AdSense](https://www.google.com/adsense/start/)
2. Click "Get Started"
3. Sign in with your Google account
4. Fill out the application:
   - Website URL (your GitHub Pages URL)
   - Email address
   - Country
5. Accept terms and conditions
6. Submit application

**Note:** Google will review your application (can take 1-2 weeks). Requirements:
- You must be 18+ years old
- Website must have original content
- Website must comply with AdSense policies
- Need decent traffic (at least some visitors)

### Step 2: Get Your AdSense Code

Once approved:
1. Log into AdSense dashboard
2. Go to "Ads" → "By ad unit"
3. Click "Display ads" → "Create ad unit"
4. Choose "Banner" or "Display ad"
5. Select size (recommended: 728x90 for banner, 300x250 for sidebar)
6. Copy the ad code

### Step 3: Add Code to Your Game

You'll get code that looks like:

```html
<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-XXXXXXXXXXXXXXXX"
     crossorigin="anonymous"></script>

<ins class="adsbygoogle"
     style="display:inline-block;width:728px;height:90px"
     data-ad-client="ca-pub-XXXXXXXXXXXXXXXX"
     data-ad-slot="YYYYYYYYYY"></ins>
<script>
     (adsbygoogle = window.adsbygoogle || []).push({});
</script>
```

### Step 4: Update Your index.html

1. Add the AdSense script in the `<head>` section
2. Add ad units where you want them (top, bottom, sides)
3. Common placements:
   - Top banner (above game)
   - Bottom banner (below game)
   - Sidebar ads (left/right of game)
   - Interstitial ads (on game over screen)

### Step 5: Test

1. Deploy to GitHub Pages
2. Wait 20-30 minutes for ads to appear
3. Don't click your own ads (violates AdSense policy!)
4. Check AdSense dashboard for impressions

---

## Option 2: Alternative Ad Networks

If AdSense rejects you or you want more options:

### Media.net
- Good alternative to AdSense
- Powered by Yahoo/Bing
- Apply at: https://www.media.net/

### PropellerAds
- Accepts smaller sites
- Various ad formats
- Apply at: https://propellerads.com/

### AdThrive / Mediavine
- High-paying but requires lots of traffic
- Need 50k+ monthly pageviews
- Better for established sites

---

## Option 3: Sponsorships

For gaming sites, direct sponsorships can work:

1. **CrazyGames** - Submit your game to their platform
2. **Poki** - Game distribution platform
3. **Kongregate** - Gaming platform with ad revenue share
4. **Game licensing** - Sell your game to portals

---

## Maximizing Ad Revenue

### Tips:
1. **Traffic is key** - More visitors = more revenue
2. **Ad placement** - Test different positions
3. **Don't overdo it** - Too many ads = bad user experience
4. **Mobile-friendly** - Use responsive ads
5. **Page speed** - Ads slow down page, optimize everything else

### Promote Your Game:
- Reddit (r/WebGames, r/IndieGaming)
- Twitter with #gamedev hashtag
- Facebook gaming groups
- TikTok gameplay videos
- YouTube gameplay videos
- Share on Discord servers

### Expected Revenue:
- $1-5 per 1,000 impressions (CPM)
- Need thousands of daily visitors to make significant money
- Gaming sites typically have lower CPM than other niches

---

## Legal Requirements

### Privacy Policy
You MUST have a privacy policy if using ads. Include:
- What data is collected
- How ads use cookies
- User rights (GDPR compliance)
- Contact information

Use a generator: https://www.freeprivacypolicy.com/

### Terms of Service
Recommended to have:
- Usage rules
- Liability disclaimers
- Copyright information

### Cookie Consent
Required in EU (GDPR):
- Add cookie consent banner
- Use: https://www.cookiebot.com/ (free tier available)

---

## Quick Start Template

I've created `index_with_ads.html` - here's how to use it:

1. Get approved for AdSense
2. Replace `ca-pub-XXXXXXXXXXXXXXXX` with your AdSense publisher ID
3. Replace ad slot IDs with your actual ad unit IDs
4. Copy your game code into the file
5. Rename to `index.html` and deploy

---

## Important Notes

⚠️ **Don't click your own ads** - You'll get banned from AdSense
⚠️ **Be patient** - Building traffic takes time
⚠️ **Follow policies** - Read and follow all AdSense policies
⚠️ **Track performance** - Use Google Analytics to understand your traffic

Good luck with your game! 🎮💰
