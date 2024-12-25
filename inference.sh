# Usage
# bash inference.sh "<Path to output image folder>"
# $1 : "<Path to output image folder>"

# Folder contains prompt 1's config files
prompt1_folder="./configs/inference/prompt1"

for config_file in "$prompt1_folder"/*; do
  echo "$config_file"
  python sample.py --config_file "$config_file" --outimg_dir "./test_prompt1" --prompt_num "1"
done

# Folder contains prompt 2's config files
prompt2_folder="./configs/inference/prompt2"

for config_file in "$prompt2_folder"/*; do
  echo "$config_file" 
  python sample.py --config_file "$config_file" --outimg_dir "./test_prompt2" --prompt_num "2"
done