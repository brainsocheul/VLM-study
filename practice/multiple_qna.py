from transformers import BlipProcessor, BlipForQuestionAnswering
from PIL import Image

processor = BlipProcessor.from_pretrained(
    "Salesforce/blip-vqa-base"
)

model = BlipForQuestionAnswering.from_pretrained(
    "Salesforce/blip-vqa-base"
)

images = [
    Image.open("images/bear.jpg").convert("RGB"),
    Image.open("images/mountain.jpg").convert("RGB"),
    Image.open("images/sea.jpg").convert("RGB"),
]

texts=[ #질문을 해보자
    "what kind of bear is this?",
    "what is on the mountains?",
    "how the weather is there?"
]

inputs = processor(
    images=images,
    text=texts,
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