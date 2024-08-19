from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from aiogram.filters import CommandStart
from aiogram import Router, F

from backend.user import User
from backend.log import Log
from backend.templates import Templates

echo_message = Router()
echo_message.name = "echo_message"
log = Log()

@echo_message.message(F.chat.type == "private")
async def echo(message: Message):
    user_id = message.from_user.id
    username = message.from_user.username

    user = User(user_id, username)

    log.message_logging(call=message.text, user=user, chat_id=message.chat.id)

    await message.answer(message.text, parse_mode="markdown")
