from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from typing import List, Optional, Tuple, Dict
from src.routing.main_navigator import RouteEngine
from src.routing.graph_utils import GraphLoader
from src.routing.map_engine import MapEngine
from src.routing.fleet_manager import FleetManager
from src.api.mission_reports import ReportGenerator

app = FastAPI(title="Afet-Rota-AI Professional API", description="Afet Yönetimi ve Koordinasyon Servisi")

# Mount Static Files for CSS
app.mount("/static", StaticFiles(directory="src/api/static"), name="static")

# Global State
loader = GraphLoader()
G = loader.load_from_address("Besiktas, Istanbul", dist=2000)
engine = RouteEngine(G)
fleet = FleetManager(engine)
mapper = MapEngine(G)
reported_damages = []

class DamageReport(BaseModel):
    coords: Tuple[float, float]
    severity: float
    type: str

class RouteRequest(BaseModel):
    unit_id: str
    start_coord: Tuple[float, float]
    target_coord: Tuple[float, float]
    optimization_mode: str = "safety_first"

@app.get("/", response_class=HTMLResponse)
def dashboard():
    return f"""
    <!DOCTYPE html>
    <html lang="tr">
    <head>
        <meta charset="UTF-8">
        <title>Afet-Rota-AI Dashboard</title>
        <link rel="stylesheet" href="/static/style.css">
    </head>
    <body>
        <div class="dashboard-container">
            <h1>🛰️ Afet-Rota-AI <span class="mission-badge">Operasyon Merkezi</span></h1>
            <p>TUA Astrohackathon 2026 - Aethel-Plus Sistemi</p>
            
            <div class="stats-grid">
                <div class="stat-card">
                    <span class="stat-value">{len(fleet.active_units)}</span>
                    <span class="stat-label">Aktif Kurtarma Birimi</span>
                </div>
                <div class="stat-card">
                    <span class="stat-value">{len(reported_damages)}</span>
                    <span class="stat-label">Tespit Edilen Engel</span>
                </div>
                <div class="stat-card">
                    <span class="stat-value">{len(G.nodes)}</span>
                    <span class="stat-label">Yol Ağı Graf Düğümü</span>
                </div>
            </div>

            <div style="display: flex; gap: 10px;">
                <a href="/get-map" class="btn">🗺️ İnteraktif Görev Haritası</a>
                <a href="/mission-briefing" class="btn" style="background: #30363d;">📄 Görev Brifingi Al</a>
            </div>
        </div>
    </body>
    </html>
    """

@app.get("/get-map", response_class=HTMLResponse)
def get_map():
    all_routes = [d['route'] for d in fleet.active_units.values()]
    m = mapper.create_mission_map(routes=all_routes, obstacles=[d.coords for d in reported_damages])
    return m._repr_html_()

@app.post("/report-damage")
def report_damage(report: DamageReport):
    reported_damages.append(report)
    engine.apply_disaster_risk([report.coords])
    return {"status": "success", "message": f"Hasar raporu kaydedildi: {report.type}"}

@app.post("/assign-mission")
def assign_mission(request: RouteRequest):
    route = fleet.assign_mission(request.unit_id, request.start_coord, request.target_coord)
    if not route:
        raise HTTPException(status_code=404, detail="Birim için güvenli rota bulunamadı.")
    return {"unit_id": request.unit_id, "route_nodes": route}

@app.get("/mission-briefing")
def get_briefing():
    obstacles = [d.coords for d in reported_damages]
    briefing_text = ReportGenerator.create_briefing("OP_HACKATHON_BEŞİKTAŞ", fleet.active_units, obstacles)
    return {"briefing": briefing_text}
