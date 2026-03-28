from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional, Tuple
from src.routing.main_navigator import RouteEngine
from src.routing.graph_utils import GraphLoader

app = FastAPI(title="Afet-Rota-AI API", description="Afet Yönetimi Rota Optimizasyon Servisi")

# Global State for Simulation
loader = GraphLoader()
G = loader.load_from_address("Besiktas, Istanbul", dist=2000)
engine = RouteEngine(G)
reported_damages = []

class DamageReport(BaseModel):
    coords: Tuple[float, float]
    severity: float
    type: str

class RouteRequest(BaseModel):
    start_coord: Tuple[float, float]
    target_coord: Tuple[float, float]
    use_satellite_data: bool = True

class RouteResponse(BaseModel):
    route_nodes: List[int]
    message: str

@app.get("/")
def health_check():
    return {"status": "active", "service": "Afet-Rota-AI", "graph_nodes": len(G.nodes)}

@app.post("/report-damage")
def report_damage(report: DamageReport):
    reported_damages.append(report)
    engine.apply_disaster_risk([report.coords])
    return {"status": "success", "message": f"Hasar raporu işlendi: {report.type}"}

@app.post("/calculate-safe-route", response_model=RouteResponse)
def get_safe_route(request: RouteRequest):
    try:
        route = engine.find_safe_route(request.start_coord, request.target_coord)
        if not route:
            raise HTTPException(status_code=404, detail="Güvenli rota bulunamadı.")
        
        return RouteResponse(
            route_nodes=route,
            message="BKZS verisi ve güncel hasar durumu ile optimize edilmiş rota."
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
