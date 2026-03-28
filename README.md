# 🛰️ Afet-Rota-AI: Otonom Afet Lojistik ve Rota Optimizasyon Ekosistemi

![TUA Astrohackathon](https://img.shields.io/badge/Etkinlik-TUA_Astrohackathon-0052cc?style=for-the-badge)
![Milli Uzay Programı](https://img.shields.io/badge/Hedef-BKZS_Entegrasyonu-e60000?style=for-the-badge)
![Maturity](https://img.shields.io/badge/Sistem_Olgunluğu-Aethel--Plus-gold?style=for-the-badge)

**Afet-Rota-AI**, afet sonrası "Altın Saatler" içerisinde arama-kurtarma ekiplerinin en büyük engeli olan **"Statik Harita Bilgisizliği"** sorununu, yerli uydu verileri ve dinamik ağ optimizasyonu ile çözen uçtan uca bir Karar Destek Sistemidir.

---

## 🏗️ Sistem Mimarisi (Architectural Overview)

Aşağıdaki diyagram, uzay segmentinden başlayarak saha ekiplerine uzanan tam otonom veri akışını göstermektedir:

```mermaid
graph TD
    subgraph "Uzay Segmenti"
        S1[İMECE / GÖKTÜRK-1] -->|Yüksek Çözünürlüklü Optik/SAR| V1
    end

    subgraph "Afet-Rota-AI Çekirdek"
        V1[Damage Assessment AI] -->|Enkaz Poligonları & Koordinat| G1[Dynamic Graph Engine]
        O1[OpenStreetMap Data] -->|Yol Ağı Grafı| G1
        G1 -->|Maliyet Güncelleme| R1[Multi-Objective Router]
    end

    subgraph "Saha & Haberleşme"
        B1[BKZS Yerli Konumlandırma] -->|Anlık GPS/GNSS| R1
        R1 -->|Güvenli Rota API| F1[Rescue Fleet / Mobile App]
        F1 -->|Geri Bildirim| V1
    end

    style V1 fill:#f96,stroke:#333
    style G1 fill:#69f,stroke:#333
    style R1 fill:#9f6,stroke:#333
```

---

## 🧠 Matematiksel Model ve Optimizasyon

Sistem, yolların maliyetini sadece mesafe bazlı değil, **"Risk Katsayısı"** odaklı hesaplar. $e$ kenarı (yol parçası) için dinamik maliyet fonksiyonu:

$$Cost(e, mode) = Distance(e) \cdot \Phi(e)^{P_{mode}}$$

Burada:
- $\Phi(e)$: AI Vision modülünden gelen **Hasar/Risk İndeksi** (1.0 = Güvenli, 5000.0 = Tam Blokaj).
- $P_{mode}$: Kullanıcı seçimli optimizasyon sertliği.
    - **Safety-First ($P=10$):** En küçük riskte dahi uzun deturları tercih eder.
    - **Time-First ($P=2$):** Hız ve risk arasında denge kurar.

---

## 🛠️ Profesyonel Özellikler (Aethel-Plus)

| Özellik | Tanımlama | Teknoloji |
| :--- | :--- | :--- |
| **Dinamik Rerouting** | Yol kapandığında BKZS verisiyle 1 sn altında yeni rota üretimi. | NetworkX / Dijkstra |
| **Fleet Management** | Birden fazla ekibin dar sokaklarda çakışmasını önleyen filo koordinasyonu. | Custom Weight Penalizer |
| **Interactive GIS** | Operasyon merkezleri için Folium tabanlı interaktif görev haritaları. | Folium / Leaflet.js |
| **AI Vision Pipeline** | SAR ve Optik görüntülerden otonom enkaz tespiti (Simüle). | PyTorch / OpenCV |

---

## 🚀 Hızlı Başlangıç (Quick Start)

### 1. Kurulum
```bash
git clone https://github.com/arch-yunus/Afet-Rota-AI.git
pip install -r requirements.txt
```

### 2. Operasyonel Dashboard Başlatma
Sistemi görsel arayüzü ve API servisleri ile başlatmak için:
```bash
python -m uvicorn src.api.app:app --reload
```
Dashboard'u görüntülemek için tarayıcınızdan `http://localhost:8000` adresine gidin.

---

## 🗺️ Gelecek Vizyonu: TUA BKZS Entegrasyonu
Projenin nihai hedefi, Türkiye'nin yerli **BKZS (Bölgesel Konumlama ve Zamanlama Sistemi)** altyapısını kullanarak, GPS sinyalinin zayıf olduğu enkaz kanyonlarında dahi santimetre hassasiyetinde ve tam güvenli navigasyon sunmaktır.

---

## 👨‍💻 Geliştirici Bilgisi
**Afet-Rota-AI Team** | TUA Astrohackathon 2026 Projesi
*Systems Architecture & AI Optimization*
