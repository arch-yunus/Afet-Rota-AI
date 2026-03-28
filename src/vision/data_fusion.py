import numpy as np

class MultispectralFusion:
    """
    Simulates the fusion of SAR (Synthetic Aperture Radar) and Optical satellite data.
    Provides higher confidence routes in adverse weather or light conditions.
    """
    def __init__(self):
        print("[*] Multispectral Fusion Engine: Init.")

    def fuse_detections(self, optical_data, sar_data):
        """
        Combines optical confidence and SAR structural integrity data.
        """
        print("[*] Veri Füzyonu Koşturuluyor: [Optik RGB] + [SAR L-Band]...")
        
        fused_score = (optical_data * 0.4) + (sar_data * 0.6)
        
        status = "YÜKSEK GÜVEN" if fused_score > 0.8 else "DÜŞÜK GÜVEN"
        print(f"[+] Füzyon Tamamlandı. Birleşik Risk Skoru: {fused_score:.2f} ({status})")
        
        return fused_score

if __name__ == "__main__":
    fusion = MultispectralFusion()
    # Example: 70% confidence from optical, 90% from SAR (better at structural detection)
    fusion.fuse_detections(0.7, 0.9)
