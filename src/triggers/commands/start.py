from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from aiogram.filters import CommandStart
from aiogram import Router, F

from backend.user import User
from backend.log import Log
from backend.templates import Templates

start_command = Router()
start_command.name = "start"
log = Log()

@start_command.message(CommandStart(), F.chat.type == "private")
async def command_start_handler(message: Message, state: FSMContext):
    await state.clear()
    
    user_id = message.from_user.id
    username = message.from_user.username

    user = User(user_id, username)

    log.message_logging(call="/start", user=user, chat_id=message.chat.id)

    await message.answer(Templates.START, parse_mode="markdown")
