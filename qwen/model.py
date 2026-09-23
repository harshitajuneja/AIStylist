import os
import torch

from transformers import (
    Qwen2_5_VLForConditionalGeneration,
    AutoProcessor
)

MODEL_NAME = os.getenv(
    "QWEN_MODEL",
    "Qwen/Qwen2.5-VL-7B-Instruct"
)


print("Loading Qwen model...")

processor = AutoProcessor.from_pretrained(
    MODEL_NAME
)

model = Qwen2_5_VLForConditionalGeneration.from_pretrained(
    MODEL_NAME,
    torch_dtype=torch.bfloat16,
    device_map="auto"
)

model.eval()

print("Qwen loaded.")