import subprocess
import tempfile
import os
from pathlib import Path


def run(cmd, env=None):
    result = subprocess.run(cmd, shell=True, env=env)
    if result.returncode != 0:
        raise SystemExit(result.returncode)


if __name__ == "__main__":
    with tempfile.TemporaryDirectory() as tmp:
        tmp_path = Path(tmp)

        run(f"python playwright_fetch.py", env={
            **os.environ,
            "HTML_TEMP_DIR": str(tmp_path)
        })

        run("scrapy crawl liverpool", env={
            **os.environ,
            "HTML_TEMP_DIR": str(tmp_path)
        })

        print("Archivo: Laptops.txt creado correctamente.")