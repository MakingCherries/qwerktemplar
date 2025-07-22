"""
Configuration file for QWERK NFL Betting Analysis Platform
"""

import os
from typing import Optional

class Config:
    """Configuration class for API keys and settings"""
    
    # API Configuration
    SPORTS_API_KEY: Optional[str] = os.getenv('SPORTS_GAME_ODDS_API_KEY')
    OPENAI_API_KEY: Optional[str] = os.getenv('OPENAI_API_KEY')
    
    # SportsGameOdds.com API Settings
    SPORTS_API_BASE_URL = "https://api.sportsgameodds.com"
    SPORTS_API_ENDPOINTS = {
        "nfl_odds": "/nfl/odds",
        "nfl_games": "/nfl/games",
        "nfl_lines": "/nfl/lines"
    }
    
    # Application Settings
    APP_TITLE = "Welcome to the QWERK!"
    APP_ICON = "🏈"
    
    # Data Settings
    HISTORICAL_YEARS = 10  # Number of years of historical data to analyze
    MAX_RECOMMENDATIONS = 5  # Number of recommendations per category
    
    # Betting Categories
    BET_CATEGORIES = ["spread", "totals", "moneyline"]
    
    # Confidence Levels
    CONFIDENCE_LEVELS = ["High", "Medium", "Low"]
    
    # NFL Teams (for data generation and validation)
    NFL_TEAMS = [
        "Arizona Cardinals", "Atlanta Falcons", "Baltimore Ravens", "Buffalo Bills",
        "Carolina Panthers", "Chicago Bears", "Cincinnati Bengals", "Cleveland Browns",
        "Dallas Cowboys", "Denver Broncos", "Detroit Lions", "Green Bay Packers",
        "Houston Texans", "Indianapolis Colts", "Jacksonville Jaguars", "Kansas City Chiefs",
        "Las Vegas Raiders", "Los Angeles Chargers", "Los Angeles Rams", "Miami Dolphins",
        "Minnesota Vikings", "New England Patriots", "New Orleans Saints", "New York Giants",
        "New York Jets", "Philadelphia Eagles", "Pittsburgh Steelers", "San Francisco 49ers",
        "Seattle Seahawks", "Tampa Bay Buccaneers", "Tennessee Titans", "Washington Commanders"
    ]
    
    @classmethod
    def get_sports_api_key(cls) -> Optional[str]:
        """Get the SportsGameOdds API key"""
        return cls.SPORTS_API_KEY
    
    @classmethod
    def get_openai_api_key(cls) -> Optional[str]:
        """Get the OpenAI API key"""
        return cls.OPENAI_API_KEY
    
    @classmethod
    def set_api_keys(cls, sports_key: str = None, openai_key: str = None):
        """Set API keys programmatically"""
        if sports_key:
            cls.SPORTS_API_KEY = sports_key
        if openai_key:
            cls.OPENAI_API_KEY = openai_key

# Environment variable setup instructions
ENV_SETUP_INSTRUCTIONS = """
To set up environment variables for production deployment:

1. Create a .env file in your project root:
   SPORTS_GAME_ODDS_API_KEY=your_api_key_here
   OPENAI_API_KEY=your_openai_key_here

2. For Streamlit Cloud deployment, add these as secrets:
   - Go to your app settings
   - Add secrets in TOML format:
     [secrets]
     SPORTS_GAME_ODDS_API_KEY = "your_api_key_here"
     OPENAI_API_KEY = "your_openai_key_here"

3. For local development, you can also set environment variables:
   Windows: set SPORTS_GAME_ODDS_API_KEY=your_key
   Mac/Linux: export SPORTS_GAME_ODDS_API_KEY=your_key
"""
