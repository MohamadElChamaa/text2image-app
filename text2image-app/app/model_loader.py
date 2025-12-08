# app/model_loader.py
import os
import torch
from diffusers import StableDiffusionPipeline

_pipeline = None

def get_pipeline():
    """
    Charge le pipeline une seule fois et le retourne.
    Utiliser la variable d'environnement HF_MODEL pour changer le modèle.
    """
    global _pipeline
    if _pipeline is not None:
        return _pipeline

    model_name = os.environ.get("HF_MODEL", "stabilityai/stable-diffusion-2-1-base")
    hf_token = os.environ.get("HF_TOKEN", None)

    device = "cuda" if torch.cuda.is_available() else "cpu"
    torch_dtype = torch.float16 if device == "cuda" else torch.float32

    print(f"[model_loader] Loading model {model_name} on {device} with dtype={torch_dtype}")

    # Chargement
    try:
        _pipeline = StableDiffusionPipeline.from_pretrained(
            model_name,
            use_auth_token=hf_token,
            torch_dtype=torch_dtype
        )
    except TypeError:
        # certains environnements récents n'utilisent plus use_auth_token
        _pipeline = StableDiffusionPipeline.from_pretrained(
            model_name,
            token=hf_token,
            torch_dtype=torch_dtype
        )

    # deplacer sur device
    _pipeline = _pipeline.to(device)

    # Activer xformers si dispo (plus efficace sur GPU)
    try:
        _pipeline.enable_xformers_memory_efficient_attention()
        print("[model_loader] xFormers enabled")
    except Exception as e:
        print(f"[model_loader] xFormers not available or failed to enable: {e}")

    # Optionnel : scheduler, safety checker etc. (à personnaliser)
    return _pipeline
