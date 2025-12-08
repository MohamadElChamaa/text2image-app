# app/main.py
import os
import gradio as gr
import torch
from model_loader import get_pipeline
from utils import save_image

def generate(
    prompt: str,
    num_images: int = 1,
    guidance_scale: float = 7.5,
    steps: int = 30,
    height: int = 512,
    width: int = 512,
    seed: int | None = None,
    negative_prompt: str = "low quality, blurry, bad anatomy, deformed, watermark, text"
):
    """
    Génère des images et renvoie une liste de PIL.Image (utilisable par gr.Gallery).
    """
    pipe = get_pipeline()

    results = []
    device = "cuda" if torch.cuda.is_available() else "cpu"

    for i in range(max(1, num_images)):
        # configure generator for reproducibility (works sur CPU et CUDA)
        generator = None
        if seed is not None:
            try:
                generator = torch.Generator(device=device).manual_seed(int(seed) + i)
            except Exception:
                # fallback si le device string n'est pas supporté pour Generator()
                generator = torch.Generator().manual_seed(int(seed) + i)

        out = pipe(
            prompt=prompt,
            negative_prompt=negative_prompt,
            num_inference_steps=int(steps),
            guidance_scale=float(guidance_scale),
            height=int(height),
            width=int(width),
            generator=generator
        )
        image = out.images[0]
        save_image(image, prompt, i, seed)
        results.append(image)

    return results


def main():
    title = "Text → Image — Générateur (Stable Diffusion)"
    description = (
        "Entrez un prompt en français ou anglais et générez des images. "
        "Nécessite un token Hugging Face via la variable d'environnement HF_TOKEN."
    )

    with gr.Blocks(title=title) as demo:
        gr.Markdown(f"# {title}\n{description}")

        with gr.Row():
            with gr.Column(scale=2):
                prompt_input = gr.Textbox(
                    label="Prompt",
                    lines=4,
                    value="Une photographie réaliste d'un renard roux dans une forêt brumeuse",
                    placeholder="Une photographie réaliste d'un renard dans une forêt brumeuse..."
                )
                negative_prompt_input = gr.Textbox(
                    label="Negative prompt (optionnel)",
                    lines=2,
                    value="low quality, blurry, bad anatomy, deformed, watermark, text"
                )
                num_images = gr.Slider(1, 4, value=1, step=1, label="Nombre d'images")
                guidance = gr.Slider(1.0, 20.0, value=8.0, step=0.1, label="Guidance (CFG)")
                steps = gr.Slider(5, 60, value=30, step=1, label="Steps")
                width = gr.Radio([512, 640, 768], value=512, label="Width")
                height = gr.Radio([512, 640, 768], value=512, label="Height")
                seed = gr.Number(label="Seed (laisser vide pour aléatoire)", value=None)
                run_btn = gr.Button("Générer", variant="primary")

            with gr.Column(scale=3):
                gallery = gr.Gallery(label="Résultats", columns=2, height="auto")

        run_btn.click(
            generate,
            [prompt_input, num_images, guidance, steps, height, width, seed, negative_prompt_input],
            gallery
        )

    demo.launch(
        server_name=os.environ.get("GRADIO_SERVER_NAME", "0.0.0.0"),
        server_port=int(os.environ.get("GRADIO_SERVER_PORT", 7860)),
        share=False
    )


if __name__ == "__main__":
    main()
