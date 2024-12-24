for i in $(seq 0 9); do
    CUDA_VISIBLE_DEVICES=5 python sample.py --config_file ../configs/ablation_exps/2+3/1_config.yaml \
    --ref_image_path ../mask/prompt_1/ref_image_${i}.png \
    --ref_mask_paths ../mask/prompt_1/ref_image_${i}_flower.png ../mask/prompt_1/ref_image_${i}_vase.png \
    --outroot outputs/2+3_1_$i
done
