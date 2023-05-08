import os.path
import platform
from pathlib import Path

import pytesseract

if platform.system() == "Windows":
    # We may need to do some additional downloading and setup...
    # Windows needs a PyTesseract Download
    # https://github.com/UB-Mannheim/tesseract/wiki/Downloading-Tesseract-OCR-Engine

    pytesseract.pytesseract.tesseract_cmd = (
        # r"<tesseract_exe_path>"  # e.g. r"C:\Program Files\Tesseract-OCR\tesseract.exe"
        r"C:\Program Files\Tesseract-OCR\tesseract.exe")

    # Windows also needs poppler_exe
    # POPPLER_PATH = Path(r"<poppler_path>")  # e.g. r"C:\Software\poppler-0.68.0\bin"
    POPPLER_PATH = Path(r"C:\Software\poppler-0.68.0\bin")
else:
    POPPLER_PATH = None

PATH = os.path.join(Path.cwd(), "input")
