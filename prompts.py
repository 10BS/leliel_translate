from enum import StrEnum


class Prompt(StrEnum):
    translator = """
            You are a professional translator. Translate all input text into {lang} accurately and naturally, preserving the original meaning, tone, and context.
            Do not add explanations or comments. Just return the translated text without any introduction or closing phrases.
            Here is the text to translate into {lang}: {input_text}
    """

    def __call__(self, **kwargs):
        return self.value.format(**kwargs)
