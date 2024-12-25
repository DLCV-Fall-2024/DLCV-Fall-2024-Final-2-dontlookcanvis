import argparse
from diffusers import StableDiffusionPipeline
import torch

def generate_image(prompt):
    # Load ChilloutMix pipeline
    model_path = "experiments/pretrained_models/chilloutmix"
    pipe = StableDiffusionPipeline.from_pretrained(
        model_path,
        torch_dtype=torch.float16,
        safety_checker=None
    ).to("cuda")

    # Generate image
    image = pipe(
        prompt=prompt,
        num_inference_steps=30,
        guidance_scale=7.5,
    ).images[0]

    # Save output with prompt as filename
    image.save(f"examples/{prompt}.png")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--prompt", type=str, default="A flower in a vase",
                       help="Prompt for image generation")
    args = parser.parse_args()

    generate_image(args.prompt)