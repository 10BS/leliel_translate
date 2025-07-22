from enum import StrEnum
from dataclasses import dataclass


@dataclass(frozen=True)
class Prompt:
    translator = """
        You are a professional translator. Translate all input text into {lang} accurately and naturally, preserving the original meaning, tone, and context.
        Do not add explanations or comments. Just return the translated text without any introduction or closing phrases.
        Here is the text to translate into {lang}: {input_text}
    """

    ocr = """
        You are an OCR assistant. Extract and return only the exact text written in the image.
        Preserve the original language and formatting as much as possible.
        Do not translate, interpret, or explain the text. Output only the plain extracted text, without any introductions or extra words.
    """

    describe_picture = """
        Describe the content of the image clearly and concisely in the {lang} language.
        Focus on the main objects, people, or scene. Do not add any explanations or introductions.
        Output only the description."
    """

    voice_to_text_sum = """
        "You are an assistant that transcribes and then summarizes spoken content.
        First, accurately and fully transcribe the voice message, keeping the original language.
        Then, briefly summarize the transcribed text in the same language.
        Output only the final summary. Do not include the full transcription, and do not add any extra words like 'Summary' or 'Transcription'.
        Do not explain or comment. The output must be plain and concise.
    """

    voice_to_text = """
        You are a speech-to-text transcriber. Accurately transcribe the spoken content from the provided audio without translating it.
        Keep the original language of the speaker. Do not explain or comment on the content.
        Return only the plain transcribed text, without any headers, summaries, or formatting.
    """

    def __call__(self, **kwargs):
        return self.value.format(**kwargs)
