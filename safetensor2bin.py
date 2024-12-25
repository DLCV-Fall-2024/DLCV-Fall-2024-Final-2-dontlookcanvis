from safetensors.torch import load_file
import torch

safetensors_path = "experiments/pretrained_models/RealVisXL_V5.0/unet/diffusion_pytorch_model.fp16.safetensors"
bin_output_path = "experiments/pretrained_models/RealVisXL_V5.0/unet/diffusion_pytorch_model.bin"

# Load the safetensors weights
weights = load_file(safetensors_path)

# Save as .bin
torch.save(weights, bin_output_path)
print(f"Saved .bin file to {bin_output_path}")
