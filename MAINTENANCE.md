# Bakım ve Güncelleme Klavuzu (MAINTENANCE.md)

**Afet-Rota-AI** sisteminin operasyonel sürekliliğini sağlamak için aşağıdaki periyodik işlemler önerilir.

## 1. Veri Kaynağı Güncellemeleri
- **Yol Ağı (OSM):** Her 3 ayda bir `GraphLoader` üzerinden güncel OpenStreetMap verisi indirilmelidir.
- **Dinamik Engeller:** Sahadan gelen `/report-damage` verileri operasyon sonunda temizlenmeli veya kalıcı veri tabanına (PostGIS) aktarılmalıdır.

## 2. AI Modeli Yenileme Döngüsü
- **Eğitim Verisi:** Her afetten elde edilen yeni SAR/Optik görüntüleri, modelin "Fine-tuning" eğitimine dahil edilmelidir.
- **Donanım Optimizasyonu:** Yeni uç cihaz sürücüleri (JetPack/OpenVINO) çıktığında `edge_inference.py` süreci tekrarlanmalıdır.

## 3. Bağımlılık Yönetimi
Sistem kritik kütüphanelere dayanır (`osmnx`, `networkx`, `fastapi`). Güvenlik yamaları için periyodik olarak:
```bash
pip list --outdated
```
komutu ile güncellemeler kontrol edilmelidir.

---
*Gelecek sürümlerde otomatik model sürümleme (MLflow) entegrasyonu planlanmaktadır.*
