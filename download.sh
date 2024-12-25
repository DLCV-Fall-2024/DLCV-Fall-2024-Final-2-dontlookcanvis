# To get all models
# wget -O SDXL.zip https://www.dropbox.com/scl/fi/wr8fpypgp8nuhwvhl6jo3/SDXL.zip?rlkey=82wfvgjl5vrx5jtakvzvfrbsf&dl=1 
# unzip SDXL.zip
# mv SDXL experiments/pretrained_models
# rm SDXL.zip

# To get cat2, wearable_glasses, watercolor only
mkdir experiments/pretrained_models/SDXL
wget -O experiments/pretrained_models/SDXL/cat2_edlora_model-latest.pth \
https://www.dropbox.com/scl/fi/p4j656fxdd65162zv6zl8/cat2_edlora_model-latest.pth?rlkey=b6cromh218ifhyzxn6lolgdiy&st=42omus5x&dl=1 \

