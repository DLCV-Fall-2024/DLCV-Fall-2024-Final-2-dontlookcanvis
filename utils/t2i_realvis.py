import argparse
import torch
from diffusers import StableDiffusionXLPipeline
from PIL import Image

def generate_image(prompt):
    # Load RealVisXL pipeline
    model_path = "experiments/pretrained_models/RealVisXL_V5.0"
    pipe = StableDiffusionXLPipeline.from_pretrained(
        model_path,
        torch_dtype=torch.float16,
        use_safetensors=True,
        variant="fp16"
    ).to("cuda")


    # Generate image
    image = pipe(
        prompt=prompt,
        num_inference_steps=30,
        guidance_scale=7.5,
    ).images[0]

    # Save output
    clean_prompt = prompt.replace(" ", "_")[:50]
    image.save(f"examples/cat_dog.png")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--prompt", type=str, default="A cat wearing wearable glasses in a watercolor style.",
                       help="Text prompt for image generation")
    args = parser.parse_args()

    generate_image(args.prompt)