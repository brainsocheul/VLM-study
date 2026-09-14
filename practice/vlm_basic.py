from transformers import BlipProcessor, BlipForConditionalGeneration
from PIL import Image
import torch #수정1

processor = BlipProcessor.from_pretrained(
    "Salesforce/blip-image-captioning-base"
)

model = BlipForConditionalGeneration.from_pretrained(
    "Salesforce/blip-image-captioning-base"
)

image = Image.open("test.jpg").convert("RGB")

inputs = processor(images=image, return_tensors="pt")

#수정2
print("==pixel_values 결과==") 
print(inputs.keys()) 
print(inputs["pixel_values"].shape)
print(inputs["pixel_values"])

#수정3
print("==vision outputs 결과==")
vision_outputs = model.vision_model(
    pixel_values=inputs["pixel_values"]
)
print(vision_outputs.last_hidden_state.shape) 

output = model.generate(**inputs)

#수정4
print("==output 결과==")
print(output)
print(output.shape)

caption = processor.decode(output[0], skip_special_tokens=True)

print(caption)

