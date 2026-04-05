# 🛡️ Proje 28: API Key Leakage in Electron (Statik Analiz)

![Python](https://img.shields.io/badge/Language-Python-blue?style=for-the-badge&logo=python)
![Security](https://img.shields.io/badge/Focus-Security-red?style=for-the-badge&logo=dependabot)

## ℹ️ Proje Hakkında
Bu proje, Electron tabanlı masaüstü uygulamalarının (`.asar` paketleri) kaynak kodlarını otomatik olarak analiz eden ve unutulmuş, kritik API anahtarlarını tespit eden bir **siber güvenlik aracıdır.**

## 🛠️ Kullanılan Teknolojiler ve Yaklaşım
Bu projede manuel "asar" ve "grep" komutları yerine süreci tamamen otomatize eden profesyonel bir yapı kurulmuştur:
* 🐍 **Python:** os, re, subprocess kütüphaneleri ile dosya sistemi yönetimi ve analiz motoru.
* 🔍 **Regex (Düzenli İfadeler):** Kod blokları arasına gizlenmiş spesifik anahtar paternlerini (Pattern Matching) yakalamak için.

## 🧠 Algoritma Mantığı
Geliştirilen `key_hunter.py` aracı şu adımlarla çalışır:

1.  📂 **Extraction:** Hedef `.asar` dosyası `subprocess` kütüphanesi ile arkaplanda geçici bir dizine çıkartılır.
2.  🌲 **Traversal:** `os.walk()` fonksiyonu kullanılarak kaynak kod dosyaları (.js, .json, .html) recursive olarak taranır.
3.  🎯 **Pattern Matching:** Her dosyanın içeriği okunur ve sisteme tanımlanan Regex kalıpları (Örn: AWS için `AKIA[0-9A-Z]{16}`) ile eşleştirilir.
4.  🧹 **Cleanup:** İşlem bitince geçici klasör otomatik olarak silinerek bellek ve disk temizliği yapılır.

## 💻 Kullanım
Uygulamayı çalıştırmak için terminal üzerinden hedef dosyayı parametre olarak vermeniz yeterlidir:

```bash
python key_hunter.py hedef_uygulama.asar
