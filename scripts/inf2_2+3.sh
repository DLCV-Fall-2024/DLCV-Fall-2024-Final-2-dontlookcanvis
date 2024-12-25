i=0
for config  in ../configs/prompt2_config1/*.yaml; do
    # echo $config, $i
    CUDA_VISIBLE_DEVICES=6 python sample.py --config_file ${config} \
    --outroot outputs/2+3_2_$i --accum True
    i="$(($i + 1))"
done
