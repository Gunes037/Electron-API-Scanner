# Proje 28: API Key Leakage in Electron (Statik Analiz)

## Proje Hakkında
Bu proje, Electron tabanlı masaüstü uygulamalarının (`.asar` paketleri) kaynak kodlarını otomatik olarak analiz eden ve unutulmuş API anahtarlarını tespit eden bir Python aracıdır. 

## Kullanılan Teknolojiler ve Yaklaşım
Bu projede manuel "asar" ve "grep" komutları yerine süreci tamamen otomatize eden bir yapı kurulmuştur:
* **Python (os, re, subprocess):** Dosya sistemi gezintisi ve asar komutlarının arkaplanda çalıştırılması için.
* **Regex (Düzenli İfadeler):** Kod blokları arasına gizlenmiş spesifik anahtar paternlerini yakalamak için.

## Algoritma Mantığı
1. **Extraction (Dışa Aktarım):** Hedef `.asar` dosyası `subprocess` kütüphanesi ile geçici bir klasöre çıkartılır.
2. **Traversal:** `os.walk()` fonksiyonu kullanılarak kaynak kod dosyaları (.js, .json, .html) taranır.
3. **Pattern Matching:** Her dosyanın içeriği okunur ve sisteme önceden tanımlanan Regex kalıpları (Örn: AWS için `AKIA[0-9A-Z]{16}`) ile eşleştirilir.
4. **Cleanup:** İşlem bitince geçici klasör otomatik olarak silinerek disk temizliği yapılır.

## Kullanım
Uygulamayı çalıştırmak için terminal üzerinden hedef dosyayı parametre olarak vermeniz yeterlidir:
`python key_hunter.py hedef_uygulama.asar`
