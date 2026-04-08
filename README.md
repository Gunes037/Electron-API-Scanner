# 🛡️ Electron API Key Scanner (Statik Analiz Otomasyonu)

<p align="center">
  <img src="https://images.seeklogo.com/logo-png/61/1/istinye-universitesi-logo-png_seeklogo-610039.png" alt="İstinye Üniversitesi Logo" width="200">
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Language-Python-blue.svg" alt="Python">
  <img src="https://img.shields.io/badge/Focus-Security-red.svg" alt="Security">
  <img src="https://img.shields.io/badge/License-MIT-green.svg" alt="License">
</p>

---

## 🎓 Akademik Bilgiler
* **Üniversite:** İstinye Üniversitesi (İSÜ)
* **Ders:** Tersine Mühendislik (Reverse Engineering)
* **Eğitmen:** Keyvan Arasteh
* **Proje Konusu:** 28. API Key Leakage in Electron
* **Öğrenci:** Güneş Bingül (2320191055)

---

## 📖 İçindekiler
1. [Proje Hakkında](#-proje-hakkında)
2. [Kullanılan Teknolojiler](#-kullanılan-teknolojiler)
3. [Yazılım Mimarisi](#-yazılım-mimarisi)
4. [Kurulum ve Kullanım](#-kurulum-ve-kullanım)
5. [Güvenlik Notu](#-güvenlik-notu)

---

## ℹ️ Proje Hakkında
Bu proje, Electron tabanlı masaüstü uygulamalarının kaynak kodlarındaki sızıntıları tespit etmek için geliştirilmiş bir güvenlik otomasyonudur. Uygulama, `.asar` paketlerini otomatik olarak açar ve **AWS/Google Cloud API** anahtarları gibi hassas verileri Regex (Düzenli İfadeler) kullanarak tarar.

## 🛠️ Kullanılan Teknolojiler
* **Python:** Dosya sistemi yönetimi ve analiz motoru.
* **Regex:** Spesifik anahtar desenlerini yakalamak için optimize edilmiş kalıplar.
* **Asar CLI:** Node.js tabanlı paket açma aracı.

## 🏗️ Yazılım Mimarisi (Architectural Separation)
Hocamızın beklentileri doğrultusunda, proje monolitik yapıdan kurtarılarak modüler hale getirilmiştir:
* **`scanner_engine.py`:** Regex kurallarını ve tarama mantığını barındıran çekirdek modül.
* **`extractor_utils.py`:** Dosya çıkarma ve temizleme işlemlerini yapan yardımcı araçlar.
* **`main.py`:** Uygulamanın giriş noktası ve iş akış yönetimi.

## 🚀 Kurulum ve Kullanım

### 1. Bağımlılıkların Kurulması
Sisteminizde Node.js kurulu olmalıdır. Ardından `asar` paketini kurun:
```bash
npm install -g asar
