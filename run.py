import os
import subprocess
import sys
from pathlib import Path

def main():
    project_root = Path(__file__).parent
    scraper_dir = project_root / "scraper"
    
    if not scraper_dir.exists():
        print(f"Error: Scraper directory not found at {scraper_dir}")
        return
    os.chdir(scraper_dir)
    
    try:
        subprocess.run([sys.executable, "run_all.py"], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error al ejecutar el scraper: {e}")
    except KeyboardInterrupt:
        print("\nProceso interrumpido por el usuario.")

if __name__ == "__main__":
    main()
