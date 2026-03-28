import osmnx as ox
import networkx as nx
import os

class GraphLoader:
    """
    Utility to download and manage OpenStreetMap graph data.
    """
    def __init__(self, cache_dir="data/osm_street_networks/"):
        self.cache_dir = cache_dir
        if not os.path.exists(cache_dir):
            os.makedirs(cache_dir)

    def load_from_address(self, address, dist=2000, network_type="drive", refresh=False):
        """
        Loads a street network from an address or city name.
        """
        filename = f"{address.replace(',', '_').replace(' ', '_')}_{network_type}.graphml"
        filepath = os.path.join(self.cache_dir, filename)

        if os.path.exists(filepath) and not refresh:
            print(f"[*] Diskten Garph Verisi Yükleniyor: {filepath}")
            return ox.load_graphml(filepath)
        
        print(f"[*] OSMnx ile Canlı Veri İndiriliyor: {address}...")
        try:
            G = ox.graph_from_address(address, dist=dist, network_type=network_type)
            ox.save_graphml(G, filepath)
            return G
        except Exception as e:
            print(f"[!] Hata: Graph verisi indirilemedi. {e}")
            return None

if __name__ == "__main__":
    loader = GraphLoader()
    # Test with a known location (e.g., Besiktas, Istanbul)
    # G = loader.load_from_address("Beşiktaş, Istanbul", dist=500)
    print("[*] GraphLoader modülü hazır.")
