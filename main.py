import asyncio
import logging

from aiogram import Bot, Dispatcher, types, F
from aiogram.filters.command import Command
from aiogram.types import Message
from aiogram.methods import SendMessage

from cfg_reader import config
from cmds import GeminiClient

bot = Bot(token=config.bot_token.get_secret_value())
dp = Dispatcher()
gemini = GeminiClient(
    api_key=config.gemini_api_key.get_secret_value(), model="gemini-2.5-flash"
)

logging.basicConfig(level=logging.INFO)

@dp.message(Command("start"))
async def cmd_start(message: types.Message) -> None:
    await message.answer("Go away.")


@dp.message(F.text)
async def cmd_translate(message: types.Message) -> None:
    lang: str = message.from_user.language_code
    input_text: str = message.text
    output_text = gemini.do_task(task="translate", lang=lang, input_text=input_text)
    await message.reply(output_text)


async def cmd_summarize() -> None:
    pass

@dp.message(F.photo)
async def cmd_ocr(message: Message) -> None:
    file = message.photo[-1].file_id
    lang: str = message.from_user.language_code
    output_text = gemini.do_task(task="ocr", lang=lang, file=file)
    await message.reply(output_text)

async def cmd_describe_picture() -> None:
    pass

async def cmd_speech_to_text() -> None:
    pass

async def cmd_speech_to_text_sum() -> None:
    pass

async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Exit")
