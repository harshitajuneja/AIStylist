import json
import torch

from qwen_vl_utils import process_vision_info

from .model import model, processor
from .prompts import PRODUCT_ANALYSIS_PROMPT


def analyze_image(image_path: str):

    messages = [
        {
            "role": "user",
            "content": [
                {
                    "type": "image",
                    "image": image_path
                },
                {
                    "type": "text",
                    "text": PRODUCT_ANALYSIS_PROMPT
                }
            ]
        }
    ]

    text = processor.apply_chat_template(
        messages,
        tokenize=False,
        add_generation_prompt=True
    )

    image_inputs, video_inputs = process_vision_info(
        messages
    )

    inputs = processor(
        text=[text],
        images=image_inputs,
        videos=video_inputs,
        padding=True,
        return_tensors="pt"
    )

    inputs = inputs.to(model.device)

    with torch.inference_mode():

        generated_ids = model.generate(
            **inputs,
            max_new_tokens=700,
            do_sample=False
        )

    generated_ids_trimmed = [
        out_ids[len(in_ids):]
        for in_ids, out_ids
        in zip(
            inputs.input_ids,
            generated_ids
        )
    ]

    output = processor.batch_decode(
        generated_ids_trimmed,
        skip_special_tokens=True,
        clean_up_tokenization_spaces=False
    )[0]

    return parse_json(output)


def parse_json(text):

    text = text.strip()

    # Remove accidental markdown
    if text.startswith("```"):
        text = text.replace(
            "```json",
            ""
        ).replace(
            "```",
            ""
        ).strip()

    try:

        return json.loads(text)

    except json.JSONDecodeError:

        start = text.find("{")
        end = text.rfind("}")

        if start != -1 and end != -1:

            return json.loads(
                text[start:end + 1]
            )

        raise ValueError(
            f"Qwen did not return valid JSON:\n{text}"
        )