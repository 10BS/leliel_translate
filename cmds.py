from typing import Literal, Optional
from google import genai
from google.genai import types

from prompts import Prompt


class GenAI:

    def __init__(
        self,
        api_key: str | None,
        model: str | None,
        system_instruction: Optional[str] = None,
        temperature: float | None = 0,
        max_output_tokens: int | None = 4096,
        top_k: float | None = 10,
        top_p: float | None = 0.5,
    ) -> None:
        self.api_key = api_key
        self.model = model
        self.system_instruction = system_instruction
        self.temperature = temperature
        self.max_output_tokens = max_output_tokens
        self.top_k = top_k
        self.top_p = top_p

        self.config = types.GenerateContentConfig(
        temperature=self.temperature,
        max_output_tokens=self.max_output_tokens,
        top_k=self.top_k,
        top_p=self.top_p,
    )

    def do_task(
        self,
        task: Literal[
            "translate",
            "ocr",
            "describe_picture",
            "voice_to_text",
            "voice_to_text_sum",
        ],
        lang: str,
        input_text: str,
    ) -> Optional[str]:
        client = genai.Client(api_key=self.api_key)
        prompt = None
        match task:
            case "translate":
                prompt = str(Prompt.translator.format(lang=lang, input_text=input_text))
            case "ocr":
                prompt = str(Prompt.ocr)
            case "describe_picture":
                prompt = str(Prompt.describe_picture.format(lang=lang))
            case "voice_to_text":
                prompt = str(Prompt.voice_to_text)
            case "voice_to_text_sum":
                prompt = str(Prompt.voice_to_text_sum)
        response = client.models.generate_content(
            model=self.model,
            contents=prompt,
            config=self.config,
        )
        return response.text

# TODO deprecate
def translate(self) -> str | None:
    client = genai.Client(api_key=self.api_key)
    response = client.models.generate_content(
        model=self.model,
        contents=Prompt.translator,
        config=config
    )
    return response.text

def ocr(self) -> str | None:
    client = genai.Client(api_key=self.api_key)
    response = client.models.generate_content(
        model=self.model,
        contents=Prompt.ocr,
        config=config
    )
    return response.text

def describe_picture(self) -> str | None:
    client = genai.Client(api_key=self.api_key)
    response = client.models.generate_content(
        model=self.model,
        contents=Prompt.describe_picture,
        config=config
    )
    return response.text

def voice_to_text(self) -> str | None:
    client = genai.Client(api_key=self.api_key)
    response = client.models.generate_content(
        model=self.model,
        contents=Prompt.voice_to_text,
        config=config
    )
    return response.text

def voice_to_text_sum(self) -> str | None:
    client = genai.Client(api_key=self.api_key)
    response = client.models.generate_content(
        model=self.model,
        contents=Prompt.voice_to_text_sum,
        config=config
    )
    return response.text
