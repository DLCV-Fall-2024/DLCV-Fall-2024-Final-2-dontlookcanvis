import os
import json
import random
import argparse

prompts = [
	"a photo of <TOK>"
]

semantics = {
	"cat2": "cat",
	"pet_cat1": "cat",
	"dog": "dog",
	"dog6": "dog",
	"flower_1": "flower",
	"wearable_glasses": "glasses",
	"watercolor": "watercolor",
	"vase": "vase"
}

all_region_prompts = {
	"0": [
		("A <cat2_1> <cat2_2> on the right.", '[84,263,446,512]'), 
		("A <dog6_1> <dog6_2> on the left.", '[113,15,410,245]')
		],
	"1": [
		("A <flower_1_1> <flower_1_2>.", "[77,152,383,287]"), 
		("A <vase_1> <vase_2>", "[212,152,482,331]")
		],
	"2": [
		("A <dog_1> <dog_2> near a forest.", "[213,6,493,276]"), 
		("A <pet_cat1_1> <pet_cat1_2> near a forest.", "[0,161,257,362]"),
		("A <dog6_1> <dog6_2> near a forest.","[263,298,512,512]")
		],
	"3": [
		("A <cat2_1> <cat2_2> in a <watercolor_1> <watercolor_2> style.","[107,96,512,406]"), 
		("A <wearable_glasses_1> <wearable_glasses_2> in a <watercolor_1> <watercolor_2> style.","[169,85,230,391]")
		]
}

sketches = {
	"0": "cat_dog.png",
	"1": "flower_vase.png",
	"2": "dog_cat_dog.png",
	"3": "cat_glasses.png"
}

new_concepts_tokens = {}

def check_path(_path):
	if not os.path.exists(_path):
		os.mkdir(_path)

def convert(args):
	print(args)
	check_path(args.out_captions_path)
	check_path(args.out_jsons_path)

	f = open(args.prompts_path, "w")
	for prompt in prompts:
		f.write(prompt+"\n")
	f.close()

	for token_name in os.listdir(args.input_images_path):
		print(token_name)
		caption_dir = os.path.join(args.out_captions_path, token_name)
		check_path(caption_dir)

		image_dir = os.path.join(args.input_images_path, token_name)
		for img_fn in os.listdir(image_dir):
			txt_file = open(os.path.join(caption_dir, img_fn.split(".")[0]+".txt"), "w")
			txt_file.write(random.choice(prompts))
			txt_file.close()

		output_json_file = [{
			"instance_prompt": "<TOK>",
			"instance_data_dir": image_dir,
			"caption_dir": caption_dir
		}]
		out_json_path = os.path.join(args.out_jsons_path, token_name+".json")
		json.dump(output_json_file, open(out_json_path, "w"))

		for prefix, template_fn in [("", args.template_yaml)]:#, ("test_",args.test_template_yaml)]:
			template_yaml_file = open(template_fn, "r")
			token_yaml_file = open(prefix+token_name+".yml", "w")

			yaml_content = ''.join(template_yaml_file.readlines())

			new_concepts = ["<{}_1>".format(token_name), "<{}_2>".format(token_name)]
			new_concepts_tokens[token_name] = new_concepts

			yaml_content = yaml_content.replace("<name>", token_name)
			yaml_content = yaml_content.replace("<replace_mapping>", " ".join(new_concepts))
			yaml_content = yaml_content.replace("<new_concept_token>", "+".join(new_concepts))
			yaml_content = yaml_content.replace("<concept_list>", out_json_path)
			yaml_content = yaml_content.replace("<prompts_path>", args.prompts_path)
			yaml_content = yaml_content.replace("<pretrained_path>", args.pretrained_path)

			yaml_content = yaml_content.replace("<semantic>", semantics[token_name])

			yaml_content = yaml_content.replace("<embedding_enable_tuning>", args.embedding_enable_tuning)
			yaml_content = yaml_content.replace("<text_encoder_enable_tuning>", args.text_encoder_enable_tuning)
			yaml_content = yaml_content.replace("<unet_enable_tuning>", args.unet_enable_tuning)
			yaml_content = yaml_content.replace("<embedding_lr>", str(args.embedding_lr))
			yaml_content = yaml_content.replace("<text_encoder_lr>", str(args.text_encoder_lr))
			yaml_content = yaml_content.replace("<unet_lr>", str(args.unet_lr))
			yaml_content = yaml_content.replace("<n_iterations>", str(args.n_iterations))
			yaml_content = yaml_content.replace("<lora_rank>", str(args.lora_rank))
			yaml_content = yaml_content.replace("<lora_alpha>", str(args.lora_alpha))
			yaml_content = yaml_content.replace("<latent_size>", str(args.latent_size))

			yaml_content = yaml_content.replace("<num_inference_steps>", str(args.num_inference_steps))
			yaml_content = yaml_content.replace("<guidance_scale>", str(args.guidance_scale))

			yaml_content = yaml_content.replace("<save_checkpoint_freq>", str(args.save_checkpoint_freq))
			
			token_yaml_file.write(yaml_content)
			token_yaml_file.close()
			template_yaml_file.close()


if __name__=="__main__":
	parser = argparse.ArgumentParser()
	parser.add_argument("--input_images_path", required=True)
	parser.add_argument("--input_json_path", required=True)
	parser.add_argument("--out_captions_path", required=True)
	parser.add_argument("--out_jsons_path", required=True)
	parser.add_argument("--template_yaml", required=True)
	parser.add_argument("--prompts_path", required=True)
	parser.add_argument("--pretrained_path", required=True)

	parser.add_argument("--neg_prompt", default="")

	parser.add_argument("--embedding_enable_tuning", default="true")
	parser.add_argument("--text_encoder_enable_tuning", default="true")
	parser.add_argument("--unet_enable_tuning", default="true")
	parser.add_argument("--embedding_lr", default=1e-3)
	parser.add_argument("--text_encoder_lr", default=1e-5)
	parser.add_argument("--unet_lr", default=1e-4)
	parser.add_argument("--n_iterations", default=1000)
	parser.add_argument("--lora_rank", default=4)
	parser.add_argument("--lora_alpha", default=1)
	parser.add_argument("--latent_size", default=[4,64,64])

	parser.add_argument("--num_inference_steps", default=50)
	parser.add_argument("--guidance_scale", default=7.5)

	parser.add_argument("--save_checkpoint_freq", default=10000)

	args = parser.parse_args()

	convert(args)
