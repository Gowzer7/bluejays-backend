import requests

def get_fangraphs_bluejays_hitters():
    url = "https://www.fangraphs.com/api/projections?pos=all&stats=bat&type=steamer&lg=all"

    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)",
        "Accept": "application/json",
        "Referer": "https://www.fangraphs.com/projections.aspx"
    }

    try:
        response = requests.get(url, headers=headers)
        data = response.json()

        hitters = []
        for player in data:
            if player.get("Team") != "TOR":
                continue
            if player.get("Season") != 2024:
                continue
            if player.get("PA", 0) < 100:
                continue

            hitters.append({
                "name": player["PlayerName"],
                "AVG": float(player.get("AVG", 0)),
                "OPS": float(player.get("OPS", 0)),
                "HR": int(player.get("HR", 0)),
                "RBI": int(player.get("RBI", 0))
            })

        return hitters

    except Exception as e:
        return {"error": f"Could not load projections: {str(e)}"}