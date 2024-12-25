i=0
for config  in ../configs/prompt2_config1/*.yaml; do
    echo $config, $i
    CUDA_VISIBLE_DEVICES=2 python sample.py --config_file ${config} \
    --outroot outputs/2_2_$i
    i="$(($i + 1))"
done
