"""
NFL Team Data - Colors, Logos, and Information
"""

# NFL Team Colors (Primary, Secondary)
NFL_TEAM_COLORS = {
    "Arizona Cardinals": {"primary": "#97233F", "secondary": "#000000", "accent": "#FFB612"},
    "Atlanta Falcons": {"primary": "#A71930", "secondary": "#000000", "accent": "#A5ACAF"},
    "Baltimore Ravens": {"primary": "#241773", "secondary": "#000000", "accent": "#9E7C0C"},
    "Buffalo Bills": {"primary": "#00338D", "secondary": "#C60C30", "accent": "#FFFFFF"},
    "Carolina Panthers": {"primary": "#0085CA", "secondary": "#101820", "accent": "#BFC0BF"},
    "Chicago Bears": {"primary": "#0B162A", "secondary": "#C83803", "accent": "#FFFFFF"},
    "Cincinnati Bengals": {"primary": "#FB4F14", "secondary": "#000000", "accent": "#FFFFFF"},
    "Cleveland Browns": {"primary": "#311D00", "secondary": "#FF3C00", "accent": "#FFFFFF"},
    "Dallas Cowboys": {"primary": "#003594", "secondary": "#041E42", "accent": "#869397"},
    "Denver Broncos": {"primary": "#FB4F14", "secondary": "#002244", "accent": "#FFFFFF"},
    "Detroit Lions": {"primary": "#0076B6", "secondary": "#B0B7BC", "accent": "#000000"},
    "Green Bay Packers": {"primary": "#203731", "secondary": "#FFB612", "accent": "#FFFFFF"},
    "Houston Texans": {"primary": "#03202F", "secondary": "#A71930", "accent": "#FFFFFF"},
    "Indianapolis Colts": {"primary": "#002C5F", "secondary": "#A2AAAD", "accent": "#FFFFFF"},
    "Jacksonville Jaguars": {"primary": "#006778", "secondary": "#9F792C", "accent": "#000000"},
    "Kansas City Chiefs": {"primary": "#E31837", "secondary": "#FFB81C", "accent": "#FFFFFF"},
    "Las Vegas Raiders": {"primary": "#000000", "secondary": "#A5ACAF", "accent": "#FFFFFF"},
    "Los Angeles Chargers": {"primary": "#0080C6", "secondary": "#FFC20E", "accent": "#FFFFFF"},
    "Los Angeles Rams": {"primary": "#003594", "secondary": "#FFA300", "accent": "#FF8200"},
    "Miami Dolphins": {"primary": "#008E97", "secondary": "#FC4C02", "accent": "#005778"},
    "Minnesota Vikings": {"primary": "#4F2683", "secondary": "#FFC62F", "accent": "#FFFFFF"},
    "New England Patriots": {"primary": "#002244", "secondary": "#C60C30", "accent": "#B0B7BC"},
    "New Orleans Saints": {"primary": "#D3BC8D", "secondary": "#101820", "accent": "#FFFFFF"},
    "New York Giants": {"primary": "#0B2265", "secondary": "#A71930", "accent": "#A5ACAF"},
    "New York Jets": {"primary": "#125740", "secondary": "#000000", "accent": "#FFFFFF"},
    "Philadelphia Eagles": {"primary": "#004C54", "secondary": "#A5ACAF", "accent": "#ACC0C6"},
    "Pittsburgh Steelers": {"primary": "#FFB612", "secondary": "#101820", "accent": "#FFFFFF"},
    "San Francisco 49ers": {"primary": "#AA0000", "secondary": "#B3995D", "accent": "#FFFFFF"},
    "Seattle Seahawks": {"primary": "#002244", "secondary": "#69BE28", "accent": "#A5ACAF"},
    "Tampa Bay Buccaneers": {"primary": "#D50A0A", "secondary": "#FF7900", "accent": "#0A0A08"},
    "Tennessee Titans": {"primary": "#0C2340", "secondary": "#4B92DB", "accent": "#C8102E"},
    "Washington Commanders": {"primary": "#5A1414", "secondary": "#FFB612", "accent": "#FFFFFF"}
}

# NFL Team Abbreviations
NFL_TEAM_ABBR = {
    "Arizona Cardinals": "ARI",
    "Atlanta Falcons": "ATL",
    "Baltimore Ravens": "BAL",
    "Buffalo Bills": "BUF",
    "Carolina Panthers": "CAR",
    "Chicago Bears": "CHI",
    "Cincinnati Bengals": "CIN",
    "Cleveland Browns": "CLE",
    "Dallas Cowboys": "DAL",
    "Denver Broncos": "DEN",
    "Detroit Lions": "DET",
    "Green Bay Packers": "GB",
    "Houston Texans": "HOU",
    "Indianapolis Colts": "IND",
    "Jacksonville Jaguars": "JAX",
    "Kansas City Chiefs": "KC",
    "Las Vegas Raiders": "LV",
    "Los Angeles Chargers": "LAC",
    "Los Angeles Rams": "LAR",
    "Miami Dolphins": "MIA",
    "Minnesota Vikings": "MIN",
    "New England Patriots": "NE",
    "New Orleans Saints": "NO",
    "New York Giants": "NYG",
    "New York Jets": "NYJ",
    "Philadelphia Eagles": "PHI",
    "Pittsburgh Steelers": "PIT",
    "San Francisco 49ers": "SF",
    "Seattle Seahawks": "SEA",
    "Tampa Bay Buccaneers": "TB",
    "Tennessee Titans": "TEN",
    "Washington Commanders": "WAS"
}

# NFL Divisions
NFL_DIVISIONS = {
    "AFC East": ["Buffalo Bills", "Miami Dolphins", "New England Patriots", "New York Jets"],
    "AFC North": ["Baltimore Ravens", "Cincinnati Bengals", "Cleveland Browns", "Pittsburgh Steelers"],
    "AFC South": ["Houston Texans", "Indianapolis Colts", "Jacksonville Jaguars", "Tennessee Titans"],
    "AFC West": ["Denver Broncos", "Kansas City Chiefs", "Las Vegas Raiders", "Los Angeles Chargers"],
    "NFC East": ["Dallas Cowboys", "New York Giants", "Philadelphia Eagles", "Washington Commanders"],
    "NFC North": ["Chicago Bears", "Detroit Lions", "Green Bay Packers", "Minnesota Vikings"],
    "NFC South": ["Atlanta Falcons", "Carolina Panthers", "New Orleans Saints", "Tampa Bay Buccaneers"],
    "NFC West": ["Arizona Cardinals", "Los Angeles Rams", "San Francisco 49ers", "Seattle Seahawks"]
}

def get_team_color(team_name: str, color_type: str = "primary") -> str:
    """Get team color by name and type"""
    return NFL_TEAM_COLORS.get(team_name, {}).get(color_type, "#000000")

def get_team_abbr(team_name: str) -> str:
    """Get team abbreviation"""
    return NFL_TEAM_ABBR.get(team_name, "UNK")

def get_division_teams(division: str) -> list:
    """Get teams in a division"""
    return NFL_DIVISIONS.get(division, [])

# Mock injury data generator
def generate_injury_report(team_name: str) -> list:
    """Generate mock injury report for a team"""
    import random
    
    positions = ["QB", "RB", "WR", "TE", "OL", "DL", "LB", "CB", "S", "K"]
    injury_types = ["Knee", "Ankle", "Shoulder", "Hamstring", "Concussion", "Back", "Wrist"]
    statuses = ["Questionable", "Doubtful", "Out", "Probable"]
    
    # Generate 0-5 injuries per team
    num_injuries = random.randint(0, 5)
    injuries = []
    
    for i in range(num_injuries):
        player_names = [
            f"Player {chr(65+i)}", f"J. Smith", f"M. Johnson", f"D. Williams", 
            f"K. Brown", f"T. Davis", f"R. Miller", f"C. Wilson"
        ]
        
        injury = {
            "player": random.choice(player_names),
            "position": random.choice(positions),
            "injury": random.choice(injury_types),
            "status": random.choice(statuses)
        }
        injuries.append(injury)
    
    return injuries
