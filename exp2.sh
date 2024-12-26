# Usage
# bash inference.sh "<Path to output image folder>"
# $1 : "<Path to output image folder>"

outimg_dir="./test_output"

# Folder contains prompt 0's config files
prompt1_folder="./configs/inference/prompt0"

for config_file in "$prompt1_folder"/*; do
  echo "$config_file" >> inference_config_check
  python3 sample.py --config_file "$config_file" --outimg_dir "$outimg_dir" --prompt_num "0"
done

# Folder contains prompt 1's config files
prompt1_folder="./configs/inference/prompt1"

for config_file in "$prompt1_folder"/*; do
  echo "$config_file" >> inference_config_check
  python3 sample.py --config_file "$config_file" --outimg_dir "$outimg_dir" --prompt_num "1"
done

# Folder contains prompt 2's config files
prompt2_folder="./configs/inference/prompt2"

for config_file in "$prompt2_folder"/*; do
  echo "$config_file" >> inference_config_check
  python3 sample.py --config_file "$config_file" --outimg_dir "$outimg_dir" --prompt_num "2"
done

# Folder contains prompt 3's config files
prompt3_folder="./configs/inference/prompt3"

for config_file in "$prompt3_folder"/*; do
  echo "$config_file" >> inference_config_check
  python3 sample_sdxl.py --config_file "$config_file" --outimg_dir "$outimg_dir" --prompt_num "3"
done

python3 clip_evaluation/clip_score.py --input_dir Data/concept_image \
        --json_path Data/prompts.json --output_dir test_output