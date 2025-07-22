# 🏈 Welcome to the QWERK! 

An AI-powered NFL betting analysis platform that combines live odds, historical data, and machine learning to provide intelligent betting recommendations.

## 🚀 Features

### Core Functionality
- **Live NFL Odds Integration**: Real-time odds from SportsGameOdds.com API
- **AI-Powered Analysis**: LLM-driven betting recommendations with explanations
- **Historical Data**: 10+ years of NFL statistics and trends
- **Multi-Category Betting**: Spread, Totals, and Moneyline recommendations
- **Advanced Statistics**: Visual representations supporting each recommendation

### Betting Categories
1. **Against the Spread (ATS)**: 5 best spread bets with analysis
2. **Totals (Over/Under)**: 5 best total point bets with reasoning
3. **Moneyline**: 5 best straight-up winner picks with justification

### AI Analysis Features
- 4-line explanations for each recommendation
- Confidence levels (High/Medium/Low)
- Statistical visualizations supporting picks
- Historical performance tracking
- ROI and unit tracking

## 📊 Dashboard Sections

### 1. Live Analysis
- Real-time NFL games and odds
- AI-generated recommendations
- Interactive betting analysis
- Statistical support charts

### 2. Historical Data
- Team performance over 10+ years
- Win percentages and trends
- Points differential analysis
- Head-to-head comparisons

### 3. AI Insights
- Model performance metrics
- Confidence level distributions
- Methodology explanations
- Algorithm transparency

### 4. Performance Dashboard
- Overall win rates and ROI
- Monthly performance tracking
- Cumulative units won
- Streak tracking

## 🛠️ Setup Instructions

### Prerequisites
- Python 3.8+
- The Odds API key (free at the-odds-api.com)
- OpenAI API key (optional, for enhanced analysis)

### Installation

1. **Clone or download the project files**

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application:**
   ```bash
   streamlit run app.py
   ```

4. **Configure API keys:**
   - Enter your The Odds API key in the sidebar
   - Optionally add OpenAI API key for enhanced LLM analysis

## 🔧 API Integration

### The Odds API
- Primary source for live NFL odds
- Provides spread, totals, and moneyline data
- Real-time updates during NFL season
- Free tier: 500 requests/month
- Reliable and well-documented

### ESPN Data (Simulated)
- Historical NFL statistics
- Team performance metrics
- 10+ years of data for trend analysis

### OpenAI Integration (Optional)
- Enhanced LLM analysis
- More sophisticated explanations
- Improved recommendation quality

## 📈 How It Works

### Data Collection
1. Fetches live odds from SportsGameOdds API
2. Retrieves historical NFL data
3. Processes team statistics and trends

### AI Analysis
1. Analyzes current odds vs historical performance
2. Considers injuries, weather, and other factors
3. Generates confidence-rated recommendations
4. Creates supporting statistical visualizations

### Recommendation Engine
1. Produces 5 best bets per category
2. Provides 4-line explanations for each pick
3. Shows 2+ statistical charts supporting analysis
4. Tracks performance and adjusts algorithms

## 🎯 Key Metrics Tracked

- **Win Rate**: Percentage of successful recommendations
- **ROI**: Return on investment for betting units
- **Units Won**: Cumulative profit/loss tracking
- **Confidence Accuracy**: How well confidence levels predict outcomes
- **Category Performance**: Success rates by bet type

## 🚀 Deployment Options

### Local Development
```bash
streamlit run app.py
```

### Streamlit Cloud
1. Push code to GitHub
2. Connect to share.streamlit.io
3. Deploy with environment variables for API keys

### Other Platforms
- **Heroku**: Use Procfile for deployment
- **Railway**: Direct GitHub integration
- **Render**: Automatic deployments

## 🔒 Security Notes

- API keys are handled securely through Streamlit's input widgets
- No hardcoded credentials in the codebase
- Environment variables recommended for production

## 📝 Usage Tips

1. **Start with Mock Data**: The app works with simulated data if no API key is provided
2. **API Key Setup**: Enter your SportsGameOdds.com API key in the sidebar
3. **Explore Tabs**: Navigate through different sections for comprehensive analysis
4. **Track Performance**: Monitor the performance dashboard for ROI tracking

## 🔮 Future Enhancements

- Real-time ESPN data scraping
- More sophisticated ML models
- Live betting line movement tracking
- Mobile-responsive design
- User account and bet tracking
- Integration with sportsbooks
- Advanced statistical models (DVOA, EPA, etc.)

## ⚠️ Disclaimer

This application is for educational and entertainment purposes only. Sports betting involves risk, and past performance does not guarantee future results. Please gamble responsibly and within your means.

## 🤝 Contributing

Feel free to submit issues, feature requests, or pull requests to improve the QWERK platform!

---

**Built with ❤️ using Streamlit, Python, and AI**
