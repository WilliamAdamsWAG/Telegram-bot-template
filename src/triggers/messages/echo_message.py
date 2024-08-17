from aiogram import Router, F
from aiogram.types import Message

from backend.user import User
from backend.log import Log

# Registering the router for further connection
echo_message = Router()
echo_message.name = "echo_message"

@echo_message.message(F.chat.type == "private")
async def any_message_trigger(message: Message) -> None:
    """ Works when the user enters any message """
    # Info about user
    user_id = message.from_user.id
    username = message.from_user.username

    user = User(user_id, username)

    Log.message_logging(call=message.text, user=user, chat_id=message.chat.id)

    await message.answer(message.text, parse_mode="markdown")
