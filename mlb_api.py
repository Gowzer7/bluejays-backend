import requests

def get_mlb_player_id(name):
    bluejays = {
        "Bo Bichette": 666182,
        "Vladimir Guerrero Jr.": 665489,
        "George Springer": 592450,
        "Cavan Biggio": 666134,
    }
    return bluejays.get(name)

def get_game_logs(player_id, season='2024'):
    url = f"https://statsapi.mlb.com/api/v1/people/{player_id}/stats"
    params = {
        "stats": "gameLog",
        "group": "hitting",
        "season": season
    }
    r = requests.get(url, params=params)
    data = r.json()
    try:
        stats = data['stats'][0]['splits']
        return [
            {
                "date": s["date"],
                "AVG": float(s["stat"].get("avg", 0)),
                "OPS": float(s["stat"].get("ops", 0)),
                "RBI": int(s["stat"].get("rbi", 0))
            }
            for s in stats
        ]
    except (KeyError, IndexError):
        return []

def get_career_stats(player_id):
    url = f"https://statsapi.mlb.com/api/v1/people/{player_id}/stats"
    params = {
        "stats": "career",
        "group": "hitting"
    }
    r = requests.get(url, params=params)
    data = r.json()
    try:
        stat = data["stats"][0]["splits"][0]["stat"]
        return {
            "AVG": float(stat.get("avg", 0)),
            "OPS": float(stat.get("ops", 0)),
            "HR": int(stat.get("homeRuns", 0)),
            "RBI": int(stat.get("rbi", 0))
        }
    except (KeyError, IndexError):
        return {}