for i in $(seq 0 9); do
    CUDA_VISIBLE_DEVICES=6 python sample.py --config_file ../configs/ablation_exps/2+3/2_config.yaml \
    --ref_image_path ../mask/prompt_2/ref_image_${i}.png \
    --ref_mask_paths ../mask/prompt_2/ref_image_${i}_dog_1.png ../mask/prompt_2/ref_image_${i}_cat.png ../mask/prompt_2/ref_image_${i}_dog_2.png\
    --outroot outputs/2+3_2_$i
done
