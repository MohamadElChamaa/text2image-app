# app/utils.py
import os
from PIL import Image
from datetime import datetime

OUTPUT_DIR = "outputs"
os.makedirs(OUTPUT_DIR, exist_ok=True)

def sanitize_filename(name: str) -> str:
    invalid = ['<', '>', ':', '"', '/', '\\', '|', '?', '*']
    for c in invalid:
        name = name.replace(c, "_")
    return name.strip()[:80]

def save_image(image: Image.Image, prompt: str, index: int, seed=None) -> str:
    prompt_clean = sanitize_filename(prompt)
    timestamp = datetime.utcnow().strftime("%Y%m%dT%H%M%SZ")
    seed_part = f"_seed{seed}" if seed is not None else ""
    filename = f"{timestamp}_{prompt_clean}_{index}{seed_part}.png"
    path = os.path.join(OUTPUT_DIR, filename)
    image.save(path)
    return path
