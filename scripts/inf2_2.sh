i=0
for config  in ../configs/prompt2_config1/*.yaml; do
    echo $config, $i
    python3 sample.py --config_file ${config} \
    --outroot outputs/2_2_$i
    i="$(($i + 1))"
done
