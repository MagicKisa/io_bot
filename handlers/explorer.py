from aiogram import F, Router, types
from aiogram.filters import Command
from aiogram.filters import StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import default_state
from aiogram.types import Message, ReplyKeyboardRemove, FSInputFile
from keyboards.simple_row import make_row_keyboard

router = Router()


explorers_row = ["Fantom", "BNB", "Core", "Arbitrum", "Base", "Polygon", "Ethereum"]
urls_row = ["https://ftmscan.com/", "https://bscscan.com/", "https://scan.coredao.org/", "https://arbiscan.io/", "https://basescan.org/", "https://polygonscan.com/", "https://etherscan.io/"]

expl_dict = dict(zip(explorers_row, urls_row))

# Клавиатура с основными кнопками
kb = make_row_keyboard(explorers_row)

# Хэндлер на команду /start
@router.message(F.text == "Посмотреть в explorer")
async def handle_explorers(message: Message):
    await message.answer(
                               "Выберите интересующую платформу из меню:",
                                reply_markup=kb
                               )
    


@router.message(F.text.in_(explorers_row))
async def handle__explorers_choice(message: Message):
    await message.answer(expl_dict[message.text])
    
