# Usage
# bash inference.sh "<Path to output image folder>"
# $1 : "<Path to output image folder>"

if [ -z "$1" ]; then
  outimg_dir="./style_mix_output"
else
  outimg_dir="$1"
fi

# <Vango> and <Watercolor> Style
python3 sample.py --config_file "./configs/stylemix/vango_watercolor.yaml" --outimg_dir "$outimg_dir" --prompt_num "independent"

# <Vango and Watercolor> Style
python3 sample.py --config_file "./configs/stylemix/vango_mix.yaml" --outimg_dir "$outimg_dir" --prompt_num "mix"