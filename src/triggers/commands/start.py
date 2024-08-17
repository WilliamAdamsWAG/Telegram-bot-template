from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext

from backend.user import User
from backend.log import Log
from backend.templates import Templates

# Registering the router for further connection
start_command = Router()
start_command.name = "start"

@start_command.message(CommandStart(), F.chat.type == "private")
async def command_start_trigger(message: Message, state: FSMContext) -> None:
    """ Works when the user enters /start """
    await state.clear()  #  Exit from any FSM states
    
    # Info about user
    user_id = message.from_user.id
    username = message.from_user.username

    user = User(user_id, username)

    Log.message_logging(call="/start", user=user, chat_id=message.chat.id)

    await message.answer(Templates.START, parse_mode="markdown")
