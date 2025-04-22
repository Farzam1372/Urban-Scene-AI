import torch
from PIL import Image
from transformers import CLIPProcessor, CLIPModel

# Load CLIP model from Hugging Face
model_name = "openai/clip-vit-base-patch32"
model = CLIPModel.from_pretrained(model_name)
processor = CLIPProcessor.from_pretrained(model_name)

# Load an example image from local folder
image_path = "../data/street.jpg" #D:\Github\Urban-Scene-AI\src\data
image = Image.open(image_path)

# Text labels for scene description
labels = ["busy city street", "traffic accident", "construction site", "empty road"]

# Process inputs
inputs = processor(text=labels, images=image, return_tensors="pt", padding=True)

# Run inference
outputs = model(**inputs)
logits = outputs.logits_per_image
probs = logits.softmax(dim=1).detach().numpy()

# Print results
for label, prob in zip(labels, probs[0]):
    print(f"{label}: {prob:.4f}")