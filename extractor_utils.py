import subprocess
import shutil

class AsarExtractor:
    @staticmethod
    def extract(asar_path, output_dir):
        try:
            subprocess.run(['asar', 'extract', asar_path, output_dir], check=True, capture_output=True)
            return True
        except:
            return False

def cleanup_directory(path):
    shutil.rmtree(path)