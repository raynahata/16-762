import requests
from PIL import Image
import torch
from transformers import Owlv2Processor, Owlv2ForObjectDetection
from transformers import OwlViTProcessor, OwlViTForObjectDetection
import numpy as np
from transformers.utils.constants import OPENAI_CLIP_MEAN, OPENAI_CLIP_STD
from PIL import ImageDraw
import time

# https://github.com/NielsRogge/Transformers-Tutorials/blob/master/OWLv2/Zero_and_one_shot_object_detection_with_OWLv2.ipynb
processor =  OwlViTProcessor.from_pretrained("google/owlvit-base-patch32")#Owlv2Processor.from_pretrained("google/owlv2-base-patch16-ensemble")
# model = Owlv2ForObjectDetection.from_pretrained("google/owlv2-base-patch16-ensemble")
model=OwlViTForObjectDetection.from_pretrained("google/owlvit-base-patch32")


# python3 save_image_ros.py to get a new rgb image
image = Image.open("captured_image.jpg")# read image from current folder--> need to subscribe to /camera/color/image_raw
image = image.rotate(-90, expand=True)
# image.show()
texts = [['water bottle', 'spray bottle']]
inputs = processor(text=texts, images=image, return_tensors="pt")
start_time = time.time()
outputs = model(**inputs)
end_time = time.time()
predition_time = end_time-start_time
print("Time take for inference",predition_time)

target_sizes = torch.Tensor([image.size[::-1]])
# Convert outputs (bounding boxes and class logits) to Pascal VOC format (xmin, ymin, xmax, ymax)
results = processor.post_process_object_detection(outputs=outputs, target_sizes=target_sizes, threshold=0.1)
i = 0  # Retrieve predictions for the first image for the corresponding text queries
text = texts[i]
boxes, scores, labels = results[i]["boxes"], results[i]["scores"], results[i]["labels"]
for box, score, label in zip(boxes, scores, labels):
    box = [round(i) for i in box.tolist()]
    print(f"Detected {text[label]} with confidence {round(score.item(), 3)} at location {box}")

# correct visualzation code
# def get_preprocessed_image(pixel_values):
#     pixel_values = pixel_values.squeeze().numpy()
#     unnormalized_image = (pixel_values * np.array(OPENAI_CLIP_STD)[:, None, None]) + np.array(OPENAI_CLIP_MEAN)[:, None, None]
#     unnormalized_image = (unnormalized_image * 255).astype(np.uint8)
#     unnormalized_image = np.moveaxis(unnormalized_image, 0, -1)
#     unnormalized_image = Image.fromarray(unnormalized_image)
#     return unnormalized_image

# unnormalized_image = get_preprocessed_image(inputs.pixel_values)
# # unnormalized_image.show()


# # Target image sizes (height, width) to rescale box predictions [batch_size, 2]
# target_sizes = torch.Tensor([unnormalized_image.size[::-1]])
# # Convert outputs (bounding boxes and class logits) to Pascal VOC Format (xmin, ymin, xmax, ymax)
# results = processor.post_process_object_detection(outputs=outputs, target_sizes=target_sizes, threshold=0.1)
# i = 0  # Retrieve predictions for the first image for the corresponding text queries
# text = texts[i]
# boxes, scores, labels = results[i]["boxes"], results[i]["scores"], results[i]["labels"]
# for box, score, label in zip(boxes, scores, labels):
#     box = [round(i, 2) for i in box.tolist()]
#     print(f"Detected {text[label]} with confidence {round(score.item(), 3)} at location {box}")



# visualized_image = unnormalized_image.copy()

# draw = ImageDraw.Draw(visualized_image)

# for box, score, label in zip(boxes, scores, labels):
#     box = [round(i, 2) for i in box.tolist()]
#     x1, y1, x2, y2 = tuple(box)
#     draw.rectangle(xy=((x1, y1), (x2, y2)), outline="red")
#     draw.text(xy=(x1, y1), text=text[label])

# visualized_image.show()

