i=0
for config  in configs/inference/prompt0/*.yaml; do
    python3 sample.py --config_file ${config}
done
