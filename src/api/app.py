from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
from src.routing.main_navigator import calculate_route

app = FastAPI(title="Afet-Rota-AI API", description="Afet Yönetimi Rota Optimizasyon Servisi")

class RouteRequest(BaseModel):
    start_coord: str
    target_coord: str
    use_satellite_data: bool = True

class RouteResponse(BaseModel):
    route: List[str]
    estimated_safety: float
    message: str

@app.get("/")
def health_check():
    return {"status": "active", "service": "Afet-Rota-AI"}

@app.post("/calculate-safe-route", response_model=RouteResponse)
def get_safe_route(request: RouteRequest):
    try:
        # Simulate route calculation integration
        route_nodes = calculate_route(request.start_coord, request.target_coord, disaster_data=request.use_satellite_data)
        return RouteResponse(
            route=route_nodes,
            estimated_safety=0.95,
            message="BKZS verisi ile optimize edilmiş güvenli rota."
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
