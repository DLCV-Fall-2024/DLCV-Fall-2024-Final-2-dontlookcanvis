for i in $(seq 0 9); do
    # echo ../mask/prompt_0/ref_image_${i}.png
    CUDA_VISIBLE_DEVICES=0 python sample.py --config_file ../configs/ablation_exps/2/0_config.yaml \
    --ref_image_path ../mask/prompt_0/ref_image_${i}.png \
    --ref_mask_paths ../mask/prompt_0/ref_image_${i}_dog.png ../mask/prompt_0/ref_image_${i}_cat.png \
    --outroot outputs/2_0_$i
done
