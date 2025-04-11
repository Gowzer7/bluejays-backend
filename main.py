from fangraphs import get_fangraphs_bluejays_hitters
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from mlb_api import get_mlb_player_id, get_game_logs, get_career_stats

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"message": "Blue Jays API is live!"}

@app.get("/api/mlb/player/{name}/gamelogs")
def api_game_logs(name: str):
    player_id = get_mlb_player_id(name)
    if not player_id:
        return {"error": "Player not found"}
    return get_game_logs(player_id)

@app.get("/api/mlb/player/{name}/career")
def api_career(name: str):
    player_id = get_mlb_player_id(name)
    if not player_id:
        return {"error": "Player not found"}
    return get_career_stats(player_id)

@app.get("/api/projections")
def get_bluejays_projections():
    return get_fangraphs_bluejays_hitters()