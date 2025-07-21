from typing import Literal, Optional

from google import genai
from google.genai import types

from prompts import Prompt


class GeminiClient:

    def __init__(
            self,
            api_key: Optional[str],
            model: Optional[str],
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

        self.client = genai.Client(api_key=self.api_key)

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
            file: Optional[bytes] = None,
    ) -> Optional[str]:
        if task == "translate":
            self.__translate(lang=lang, input_text=input_text)

    # POSSIBLE TASKS:

    def __translate(self, lang: Optional[str], input_text: Optional[str]) -> str | None:
        prompt = Prompt.translator.format(lang=lang, input_text=input_text)
        response = self.client.models.generate_content(
            model=self.model,
            contents=prompt,
            config=self.config
        )
        return print(response)
