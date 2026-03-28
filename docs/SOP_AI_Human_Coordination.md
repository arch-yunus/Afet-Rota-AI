# Standart Operasyon Prosedürü: Yapay Zeka ve İnsan Koordinasyonu (SOP v1.0)

**Afet-Rota-AI** sisteminin saha operasyonlarında kullanımı için belirlenen protokoller aşağıdadır.

## 1. AI Rota Onay Mekanizması
- **Düşük Riskli Rotalar (Yeşil):** Saha ekipleri tarafından doğrudan uygulanabilir.
- **Yüksek Riskli Rotalar (Kırmızı/Turuncu):** Operasyon merkezi tarafından manuel onay gerektirir. AI'nın "Time-First" modunda önerdiği rotalar her zaman görsel olarak (Drone veya Saha Keşfi) doğrulanmalıdır.

## 2. Beklenmedik Engel Karşılaşması
Saha ekibi, AI tarafından tespit edilemeyen (örneğin hareketli bir engel) bir durumla karşılaştığında:
1. Anlık konumu `/report-damage` endpoint'i üzerinden sisteme iletir.
2. `BKZS` senkronizasyonunu kontrol eder.
3. Sistemin ürettiği **yeni güvenli rotayı** takip eder.

## 3. Veri Füzyonu ve Güvenilirlik
- **Gece Operasyonları:** SAR verisi baskınlığı artırılır. Ekipler bu durumda "Yavaş İlerleme" protokolüne geçer.
- **Yağmurlu/Bulutlu Hava:** Optik verinin %50'den fazla güven kaybettiği durumlarda, operasyon merkezi sadece SAR tabanlı rotaları onaylar.

## 4. İletişim Protokolü
Tüm rota güncellemeleri, sahadaki kurtarma birimlerine şifreli **Yerli BKZS Haberleşme Kanalı** üzerinden iletilir. AI önerileri "Tavsiye" niteliğindedir; son karar her zaman saha liderine aittir.

---
*Afet-Rota-AI Stratejik Operasyonlar Masası tarafından hazırlanmıştır.*
