from aiogram import Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message

from app import texts

router = Router()


@router.message(CommandStart())
async def cmd_start(message: Message) -> None:
    await message.answer(texts.START)

@router.message(Command("help"))
async def cmd_help(message: Message) -> None:
    await message.answer(texts.HELP)

@router.message(Command("habits"))
async def cmd_habits(message: Message) -> None:
    await message.answer(texts.HABITS)