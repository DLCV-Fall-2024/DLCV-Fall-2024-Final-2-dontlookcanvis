i=0
for config  in ../configs/prompt0_config1/*.yaml; do
    echo $config, $i
    CUDA_VISIBLE_DEVICES=0 python sample.py --config_file ${config} \
    --outroot outputs/2+3_0_$i  --accum True
    i="$(($i + 1))"
done
