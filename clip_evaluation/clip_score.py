import os
os.environ["TOKENIZERS_PARALLELISM"] = "false"

import json
import argparse
import os
from clip_image_score import calculate_clip_image_scores_folder
from clip_text_score import calculate_clip_text_scores_folder

if __name__ == '__main__':
    # Set up argument parser
    parser = argparse.ArgumentParser(description='Process some JSON data.')
    parser.add_argument('--json_path', type=str, help='Path to the JSON file')
    parser.add_argument('--input_dir', type=str, default='.', help='Directory of the hw2_data/textual_inversion')
    parser.add_argument('--output_dir', type=str, default='.', help='Directory of saved output')
    
    # Parse the arguments
    args = parser.parse_args()
    json_path = args.json_path
    input_dir = args.input_dir
    output_dir = args.output_dir
    
    # Assuming the JSON is saved in a file named 'data.json'
    with open(json_path, 'r') as f:
        data = json.load(f)

    image_scores_list = []
    text_scores_list = []

    # Iterate through the data and print the prompt_4_clip_eval
    for key, value in data.items():
        output_folder_path = os.path.join(output_dir, key)

        img_score_sum = []
        txt_score_sum = []

        clip_eval = value["prompt_4_clip_eval"]
        print("\n=================={}=====================".format(clip_eval))

        text_scores = calculate_clip_text_scores_folder(output_folder_path, clip_eval)
        text_scores = sum(text_scores) / len(text_scores)
        text_scores_list.append(text_scores)

        for idx, src in enumerate(value["src_image"]):
            print("--------------------{}--------------------".format(src))
            input_folder_path = os.path.join(input_dir, src)
            image_scores = calculate_clip_image_scores_folder(output_folder_path, input_folder_path)
            image_scores = sum(image_scores) / len(image_scores)
            print(f"CLIP Image Score: {image_scores:.2f}")
            img_score_sum.append(image_scores)


        print("===================Avg.====================")
        img_score_avg = sum(img_score_sum) / len(img_score_sum) 
        print(f"CLIP Image Score: {img_score_avg:.2f}")
        print(f"CLIP Text Score: {text_scores:.2f}")
        image_scores_list.append(img_score_avg)

    print(f"\nTotal avg score: CLIP-I: {sum(image_scores_list) / len(image_scores_list):.2f}, CLIP-T: {sum(text_scores_list) / len(text_scores_list):.2f}")
    

    