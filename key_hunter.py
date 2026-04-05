import os
import sys
import subprocess
import re
import shutil
import tempfile

def extract_asar(asar_yolu, hedef_klasor):
    try:
        subprocess.run(['asar', 'extract', asar_yolu, hedef_klasor], check=True)
    except FileNotFoundError:
        print("\n[HATA] 'asar' aracı bulunamadı. Lütfen Node.js ve asar paketinin kurulu olduğundan emin olun.")
        sys.exit(1)

AWS_KEY_PATTERN = re.compile(r'AKIA[0-9A-Z]{16}')
GOOGLE_KEY_PATTERN = re.compile(r'AIza[0-9A-Za-z-_]{35}')

def scan_files(baslangic_dizini):
    bulunan_anahtarlar = []
    for root, dirs, files in os.walk(baslangic_dizini):
        for file in files:
            if file.endswith(('.js', '.json', '.html')):
                dosya_yolu = os.path.join(root, file)
                try:
                    with open(dosya_yolu, 'r', encoding='utf-8') as f:
                        icerik = f.read()
                        for regex in [AWS_KEY_PATTERN, GOOGLE_KEY_PATTERN]:
                            for match in regex.finditer(icerik):
                                bulunan_anahtarlar.append({
                                    'tip': 'AWS' if regex == AWS_KEY_PATTERN else 'Google',
                                    'anahtar': match.group(),
                                    'dosya': dosya_yolu
                                })
                except Exception:
                    pass
    return bulunan_anahtarlar

def main():
    if len(sys.argv) < 2:
        print("\nKullanım: python key_hunter.py [HEDEF_ASAR_DOSYASI]")
        sys.exit(1)

    asar_yolu = sys.argv[1]
    
    if not os.path.exists(asar_yolu):
        print(f"\n[HATA] Belirtilen dosya bulunamadı: {asar_yolu}")
        sys.exit(1)

    print(f"\n[*] {asar_yolu} analiz ediliyor...")
    gecici_klasor = tempfile.mkdtemp()

    try:
        extract_asar(asar_yolu, gecici_klasor)
        print("[*] Paket başarıyla çıkartıldı. Kaynak kodlar taranıyor...")
        
        sonuclar = scan_files(gecici_klasor)

        print("\n[TARAMA SONUÇLARI]")
        print("-" * 50)
        
        if sonuclar:
            for sonuc in sonuclar:
                print(f"[DİKKAT] {sonuc['tip']} API Anahtarı Sızıntısı Tespit Edildi!")
                print(f"  -> Bulunan Anahtar: {sonuc['anahtar']}")
                temiz_dosya_yolu = sonuc['dosya'].replace(gecici_klasor, "")
                print(f"  -> Dosya Konumu: {temiz_dosya_yolu}\n")
        else:
            print("[TEMİZ] Hiçbir AWS veya Google API anahtarı sızıntısı bulunamadı.")
            
    finally:
        shutil.rmtree(gecici_klasor)
        print("-" * 50)
        print("[*] Analiz tamamlandı. Geçici dosyalar temizlendi.")

if __name__ == '__main__':
    main()