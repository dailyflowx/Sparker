from aiogram import Router, F
from aiogram.filters import Command, CommandStart
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from app import storage, texts
from app.states import HabitStates

router = Router()


@router.message(CommandStart())
async def cmd_start(message: Message) -> None:
    await message.answer(texts.START)

@router.message(Command("help"))
async def cmd_help(message: Message) -> None:
    await message.answer(texts.HELP)

@router.message(Command("habits"))
async def cmd_habits(message: Message) -> None:
    habits = storage.list_habits(message.from_user.id)
    if not habits:
        await message.answer(texts.HABITS_EMPTY)
        return
    
    lines = "\n".join(f"• {h}" for h in habits)
    await message.answer(f"<b>Твои привычки:</b>\n\n{lines}")

@router.message(Command("add"))
async def cmd_add(message: Message, state: FSMContext) -> None:
    await message.answer(texts.ASK_HABIT_NAME)
    await state.set_state(HabitStates.waiting_for_name)

@router.message(Command("cancel"))
async def cmd_cancel(message: Message, state: FSMContext) -> None:
    await state.clear()
    await message.answer(texts.CANCEL)

@router.message(HabitStates.waiting_for_name)
async def process_habit_name(message: Message, state: FSMContext) -> None:
    title = message.text.strip()
    
    if len(title) > 100:
        await message.answer("Слишком длинное название. Напиши покороче (до 100 символов).")
        return

    storage.add_habit(message.from_user.id, title)
    
    await state.clear()
    
    await message.answer(texts.HABIT_ADDED.format(title=title))

@router.message()
async def fallback(message: Message) -> None:
    await message.answer(texts.FALLBACK)