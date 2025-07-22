# 🚀 QWERK NFL Betting Platform - Deployment Guide

## Deploy to Streamlit Cloud (Recommended)

### Step 1: Prepare Your Repository
1. **Create a GitHub repository** for your QWERK platform
2. **Upload all files** from `C:\Users\sadow\CascadeProjects\qwerk-nfl-betting\` to GitHub
3. **Make sure these files are included:**
   - `app.py` (main application)
   - `requirements.txt` (dependencies)
   - `team_data.py` (NFL team data)
   - `config.py` (configuration)
   - `README.md` (documentation)
   - `.streamlit/config.toml` (Streamlit settings)

### Step 2: Deploy to Streamlit Cloud
1. **Go to:** [share.streamlit.io](https://share.streamlit.io)
2. **Sign in** with your GitHub account
3. **Click "New app"**
4. **Select your repository:** `your-username/qwerk-nfl-betting`
5. **Main file path:** `app.py`
6. **Click "Deploy!"**

### Step 3: Configure Your Custom Domain (sandwichtodd.com)
1. **In Streamlit Cloud dashboard:**
   - Go to your app settings
   - Find "Custom domain" section
   - Add `www.sandwichtodd.com`

2. **In your domain registrar (where you bought sandwichtodd.com):**
   - Create a CNAME record:
     - Name: `www`
     - Value: `your-app-name.streamlit.app`

### Step 4: Set Up Environment Variables (Optional)
If you want to use The Odds API:
1. **In Streamlit Cloud app settings:**
   - Go to "Secrets"
   - Add: `THE_ODDS_API_KEY = "your-api-key-here"`

## Alternative: Deploy to Netlify

### Step 1: Create Netlify-Compatible Files
Your project already has:
- `netlify.toml` (configuration)
- `.gitignore` (file exclusions)

### Step 2: Deploy to Netlify
1. **Go to:** [netlify.com](https://netlify.com)
2. **Sign up/Login**
3. **Drag and drop** your project folder
4. **Configure custom domain** to `sandwichtodd.com`

## 🎯 Recommended Approach: Streamlit Cloud

**Why Streamlit Cloud?**
- ✅ **Free hosting** for Streamlit apps
- ✅ **Easy custom domain** setup
- ✅ **Automatic updates** from GitHub
- ✅ **Built-in secrets** management
- ✅ **Optimized** for Streamlit performance

## 📱 Sharing with Friends & Family

Once deployed, your friends and family can access:
- **Primary URL:** `https://your-app-name.streamlit.app`
- **Custom Domain:** `https://www.sandwichtodd.com` (after DNS setup)

## 🔧 Post-Deployment Tips

1. **Test all features** on the live site
2. **Share the URL** with friends and family
3. **Monitor usage** in Streamlit Cloud dashboard
4. **Update code** by pushing to GitHub (auto-deploys)

## 🆘 Need Help?

If you encounter any issues:
1. Check Streamlit Cloud logs
2. Verify all files are in GitHub
3. Ensure requirements.txt is complete
4. Test locally first with `streamlit run app.py`

---

**Your QWERK NFL Betting Platform is ready to go live! 🏈✨**
