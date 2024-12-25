i=0
for config  in configs/inference/prompt0/*.yaml; do
    CUDA_VISIBLE_DEVICES=0 python sample.py --config_file ${config} 
done
