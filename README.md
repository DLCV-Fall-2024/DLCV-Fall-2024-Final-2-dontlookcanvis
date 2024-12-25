# DLCV Final Project ( Multiple Concept Personalization )

## Checkpoints download
Please download all the checkpoints from: https://drive.google.com/drive/folders/1u2un5sqWEY7yj-U-1wgyN41BICqQ3wWm?usp=sharing
You can also use ED-LoRA directly from this repository; only merged LoRAs need downloads.

## Clone this repo

    git clone https://github.com/DLCV-Fall-2024/DLCV-Fall-2024-Final-2-dontlookcanvis.git
    cd Concept-Conductor
    pip install -r requirements.txt

## General Training and Inference
```shell script=
bash train.sh <path/to/config>
bash inference.sh <path/to/config>
```
```<path/to/config>``` example: ```configs/train/stable-diffusion-v1-5/cat2.yml```

## Reproduce experimental results
### Peer review

    cd Concept-Conductor
    bash ../scripts/inf0_2.sh
    bash ../scripts/inf2_2.sh


### Final CodaLab uploads
0.

1.

2.

3.


### Poster results

#### Attention Clustering Post-processing

    cd Concept-Conductor
    bash ../scripts/attn_clustering.sh


#### Mix of Show
For reproduction of mix-of-show results, please clone this repository with ```--recursive``` to download the Mix-of-Show submodule.
Please follow the environment setup in Mix of Show repository.

    cd Mix-of-Show
    python setup.py install
    
    # Clone diffusers==0.14.0 with T2I-Adapter support
    git clone https://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p@github.com/guyuchao/diffusers-t2i-adapter.git

    # switch to T2IAdapter-for-mixofshow
    %cd diffusers-t2i-adapter
    git switch T2IAdapter-for-mixofshow

    # install from source
    pip install .

... etc.

To download checkpoints, execute:

    cd experiments/pretrained_models
    gdown 16P7v_WQ46csK_KfXhmkt1iO9ulpkUjq8
    unzip composed_edlora.zip
    rm composed_edlora.zip

Please also download the stable-diffusion v1.4 model, and create soft link:

    ln -s <path/to/sd-v1-4> experiments/pretrained_models/stable-diffusion-v1-4


For inference, here we take the prompt-0 for example:

    combined_model_root="experiments/composed_edlora/stable-diffusion-v1-4/"
    expdir="cat2+dog6"

    context_prompt="A <cat2> on the right and a <dog6> on the left."
    python Mix-of-Show/inference/mix_of_show_sample.py \
    --pretrained_model="experiments/pretrained_models/stable-diffusion-v1-4" \
    --combined_model="${combined_model_root}/${expdir}/combined_model_.pth" \
    --save_dir="results/multi-concept/${expdir}" \
    --pipeline_type="sd_pplus" \
    --prompt="${context_prompt}" \
    --suffix="" \
    --n_samples=<n_sample_you_want>

