# DLCV Final Project ( Multiple Concept Personalization )

# How to run your code?
* TODO: Please provide the scripts for TAs to reproduce your results, including training and inference. For example, 

```shell script=
bash train.sh <path/to/config>
bash inference.sh <path/to/config>
```
Eg. <path/to/config> = configs/train/stable-diffusion-v1-5/cat2.yml

# Usage
To start working on this final project, you should clone this repository into your local machine by the following command:

    git clone https://github.com/DLCV-Fall-2024/DLCV-Fall-2024-Final-2-dontlookcanvis.git
  
Note that you should replace `<team_name>` with your own team name.

For more details, please click [this link](https://docs.google.com/presentation/d/1eeXx_dL0OgkDn9_lhXnimTHrE6OYvAiiVOBwo2CTVOQ/edit?usp=sharing) to view the slides of Final Project - Multiple Concept Personalization. **The introduction video for final project can be accessed in the slides.**


### Mix of Show
Composed ED-LoRAs checkpoints: https://drive.google.com/drive/folders/1hsmbVbIrMK4EtPFHwlGLz1jd17ajbukv?usp=sharing

For reproduction of mix-of-show results, please download this repository with ```--recursive```, set up environment in ```Mix-of-Show```, download the composed ED-LoRAs from the above link and add soft links as
```
ln -s <path/of/composed_edlora> experiments/
```
Then do
```
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
  --n_samples=20

```

# Submission Rules
### Deadline
113/12/26 (Thur.) 23:59 (GMT+8)
    
# Q&A
If you have any problems related to Final Project, you may
- Use TA hours
- Contact TAs by e-mail ([ntudlcv@gmail.com](mailto:ntudlcv@gmail.com))
- Post your question under `[Final challenge 2] Discussion` section in NTU Cool Discussion
