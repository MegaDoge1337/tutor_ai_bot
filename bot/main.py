import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from config_reader import config
from llm import LLM

logging.basicConfig(level=logging.INFO)

bot = Bot(token=config.bot_token.get_secret_value())

dp = Dispatcher()

@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer("Добро пожаловать!")

@dp.message(Command("c"))
async def cmd_c(message: types.Message):
    if message.entities and message.entities[0].type == "bot_command":
        command_length = message.entities[0].length
        text_without_command = message.text[command_length:].strip()

        llm = LLM(base_url=config.llm_base_url, 
                  api_key=config.llm_api_key.get_secret_value(), 
                  model=config.llm_model)
        
        completion = llm.make_completion(user_prompt=text_without_command)

        await message.reply(f"{completion}")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        logging.info("Application closed manualy")
        exit()
