from transformers import BlipProcessor, BlipForConditionalGeneration
from PIL import Image
import torch

processor = BlipProcessor.from_pretrained(
    "Salesforce/blip-image-captioning-base"
)

model = BlipForConditionalGeneration.from_pretrained(
    "Salesforce/blip-image-captioning-base"
)

images = [
    Image.open("images/bear.jpg").convert("RGB"),
    Image.open("images/mountain.jpg").convert("RGB"),
    Image.open("images/sea.jpg").convert("RGB"),
]

#image에 대응되는 text 추가
texts=[
    "the color of the bear is ",
    "snow is on the ",
    "the color of the sea is "
]

inputs = processor(
    images=images,
    text=texts, #text를 모델에 함께 넣어주기, 아래 truncation이랑 padding도 추가
    return_tensors="pt",
    truncation=True,
    padding=True
)


outputs = model.generate(**inputs)

for i, output in enumerate(outputs):
    caption = processor.decode(
        output,
        skip_special_tokens=True
    )

    print(f"Image {i}: {caption}")