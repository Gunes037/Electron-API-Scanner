import sys
import os
import tempfile
from scanner_engine import APIKeyScanner
from extractor_utils import AsarExtractor, cleanup_directory

def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py [TARGET_ASAR]")
        return

    asar_path = sys.argv[1]
    temp_dir = tempfile.mkdtemp()
    
    # Logic flow
    if AsarExtractor.extract(asar_path, temp_dir):
        scanner = APIKeyScanner()
        # ... tarama döngüsü buraya gelecek ...
        print("[*] Scan completed.")
    
    cleanup_directory(temp_dir)

if __name__ == '__main__':
    main()