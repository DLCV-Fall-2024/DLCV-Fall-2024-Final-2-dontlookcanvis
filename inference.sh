# Usage
# bash inference.sh "<Path to output image folder>"
# $1 : "<Path to output image folder>"

if [ -z "$1" ]; then
  outimg_dir="./test_output"
else
  outimg_dir="$1"
fi

# Folder contains prompt 0's config files
prompt1_folder="./configs/inference/prompt0"

for config_file in "$prompt1_folder"/*; do
  echo "$config_file"
  python sample.py --config_file "$config_file" --outimg_dir "$outimg_dir" --prompt_num "0"
done

# Folder contains prompt 1's config files
prompt1_folder="./configs/inference/prompt1"

for config_file in "$prompt1_folder"/*; do
  echo "$config_file"
  python sample.py --config_file "$config_file" --outimg_dir "$outimg_dir" --prompt_num "1"
done

# Folder contains prompt 2's config files
prompt2_folder="./configs/inference/prompt2"

for config_file in "$prompt2_folder"/*; do
  echo "$config_file" 
  python sample.py --config_file "$config_file" --outimg_dir "$outimg_dir" --prompt_num "2"
done