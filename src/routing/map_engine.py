import folium
import osmnx as ox
import networkx as nx

class MapEngine:
    """
    Engine to generate interactive HTML maps for disaster response coordination.
    """
    def __init__(self, graph):
        self.G = graph

    def create_mission_map(self, routes=None, obstacles=None):
        """
        Generates a folium map with the road network, obstacles, and one or more routes.
        """
        # Center the map at the mean of node coordinates
        nodes, data = ox.graph_to_gdfs(self.G)
        center_lat = data['y'].mean()
        center_lon = data['x'].mean()
        
        m = folium.Map(location=[center_lat, center_lon], zoom_start=14, tiles="cartodbpositron")

        # Add obstacles
        if obstacles:
            for lat, lon in obstacles:
                folium.Marker(
                    location=[lat, lon],
                    popup="ENGEL / ENKAZ",
                    icon=folium.Icon(color='red', icon='exclamation-triangle', prefix='fa')
                ).add_to(m)

        # Add routes
        if routes:
            colors = ['blue', 'green', 'purple', 'orange']
            for i, route in enumerate(routes):
                route_coords = []
                for node in route:
                    n_data = self.G.nodes[node]
                    route_coords.append((n_data['y'], n_data['x']))
                
                folium.PolyLine(
                    route_coords,
                    color=colors[i % len(colors)],
                    weight=5,
                    opacity=0.8,
                    popup=f"Ekip Rota #{i+1}"
                ).add_to(m)

        return m

    def save_map(self, m, filepath="data/mission_map.html"):
        m.save(filepath)
        print(f"[*] Interaktif Görev Haritası Kaydedildi: {filepath}")

if __name__ == "__main__":
    print("[*] MapEngine modülü hazır.")
