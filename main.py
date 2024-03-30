import logging
import asyncio
from aiogram import Router, F
from aiogram import Bot, Dispatcher, types
from aiogram.enums import ParseMode
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.filters import Command, StateFilter
from aiogram.utils.keyboard import InlineKeyboardBuilder
from predictor import predict_cluster_and_target_distribution

from handlers import checking_code, common, scam_stats, explorer

# Устанавливаем уровень логгирования
logging.basicConfig(level=logging.INFO)

# Замените 'YOUR_BOT_TOKEN' на токен вашего бота
TOKEN = '6422865949:AAHROAkmBm_rLzVv-3TnlgkWdZf9aV9LrJA'
bot = Bot(token=TOKEN)
dp = Dispatcher()


async def main():
    dp.include_routers(common.router, checking_code.router, scam_stats.router, explorer.router)
    await dp.start_polling(bot)
    
if __name__ == '__main__':
    asyncio.run(main())


