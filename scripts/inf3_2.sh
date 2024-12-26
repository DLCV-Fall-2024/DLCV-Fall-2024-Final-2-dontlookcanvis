for i in $(seq 0 9); do
    python3 sample.py --config_file ../configs/ablation_exps/2/3_config.yaml \
    --ref_image_path ../mask/prompt_3/ref_image_${i}.png \
    --ref_mask_paths ../mask/prompt_3/ref_image_${i}_cat.png ../mask/prompt_3/ref_image_${i}_glasses.png ../mask/prompt_3/all_white.png\
    --outroot outputs/2_3_$i
done
