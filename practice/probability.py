from transformers import BlipProcessor, BlipForConditionalGeneration
from PIL import Image
import torch

processor = BlipProcessor.from_pretrained(
    "Salesforce/blip-image-captioning-base"
)

model = BlipForConditionalGeneration.from_pretrained(
    "Salesforce/blip-image-captioning-base"
)

image = Image.open("test.jpg").convert("RGB")
text = "a"

inputs = processor(
    images=image,
    text=text,
    return_tensors="pt"
)

output = model.generate(
    **inputs,
    return_dict_in_generate=True,
    output_scores=True
)

print(output.sequences)

for step, scores in enumerate(output.scores):
    probs = torch.softmax(scores[0], dim=-1)
    top_probs, top_ids = torch.topk(probs, 5)

    print(f"\n=== step {step} ===")

    for prob, token_id in zip(top_probs, top_ids):
        token = processor.tokenizer.decode([token_id])
        print(token, prob.item())