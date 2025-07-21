import asyncio
import logging

from aiogram import Bot, Dispatcher, types, F
from aiogram.filters.command import Command

from cmds import GenAI
from cfg_reader import config
from prompts import Prompt

bot = Bot(token=config.bot_token.get_secret_value())
dp = Dispatcher()
gemini = GenAI(
    api_key=config.gemini_api_key.get_secret_value(), model="gemini-2.5-flash"
)

logging.basicConfig(level=logging.INFO)

@dp.message(Command("start"))
async def cmd_start(message: types.Message) -> None:
    await message.answer("Go away.")


@dp.message(F.text)
async def cmd_translate(message: types.Message) -> None:
    lang: str = "English"
    input_text: str = message.text
    prompt = Prompt.translator(lang=lang, input_text=input_text)

    output_text = gemini.do_task("translate", lang, input_text)
    await message.reply(output_text)


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())

