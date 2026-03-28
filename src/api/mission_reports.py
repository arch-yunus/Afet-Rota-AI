import json
from datetime import datetime

class ReportGenerator:
    """
    Generates formal mission briefings and operational summaries.
    """
    @staticmethod
    def create_briefing(operation_id, active_units, detected_obstacles):
        briefing = [
            f"# Görev Brifingi: {operation_id}",
            f"**Tarih:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
            "---",
            "## 🆘 Operasyon Durumu",
            f"- **Aktif Kurtarma Birimi:** {len(active_units)}",
            f"- **Tespit Edilen Engel/Enkaz:** {len(detected_obstacles)}",
            "",
            "## 🛰️ Sensör ve BKZS Verisi",
            "- Uydu Görüntü Analizi: **Aktif**",
            "- BKZS Konumlama Hassasiyeti: **< 1m (Yerli Ağ)**",
            "",
            "## 📑 Birim Detayları"
        ]

        for uid, data in active_units.items():
            briefing.append(f"- **Birim {uid}:** Rota Uzunluğu: {len(data['route'])} düğüm | Durum: {data['status']}")

        return "\n".join(briefing)

    @staticmethod
    def export_json(filepath, data):
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
