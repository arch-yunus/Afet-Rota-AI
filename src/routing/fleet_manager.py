import networkx as nx

class FleetManager:
    """
    Coordinates multiple rescue units to prevent congestion and optimize coverage.
    """
    def __init__(self, route_engine):
        self.engine = route_engine
        self.active_units = {}

    def assign_mission(self, unit_id, start_coords, end_coords, priority="high"):
        """
        Assigns a route to a unit and updates global network occupancy.
        """
        print(f"[*] Görev Atanıyor: Ünite {unit_id} -> Öncelik: {priority}")
        route = self.engine.find_safe_route(start_coords, end_coords)
        
        if route:
            self.active_units[unit_id] = {
                "route": route,
                "status": "en_route",
                "priority": priority
            }
            # Simulate network occupancy by slightly increasing weights of the chosen route
            # to encourage other units to take parallel paths if possible
            self._apply_congestion_penalty(route)
            return route
        return None

    def _apply_congestion_penalty(self, route, penalty_factor=1.2):
        for i in range(len(route) - 1):
            u, v = route[i], route[i+1]
            # Handle multigraph edges
            for k in self.engine.G[u][v]:
                self.engine.G[u][v][k]['weight'] *= penalty_factor

    def get_fleet_status(self):
        return {uid: data['status'] for uid, data in self.active_units.items()}

if __name__ == "__main__":
    print("[*] FleetManager modülü hazır.")
