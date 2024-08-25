from aiogram import Router
from aiogram.types import Message, FSInputFile
from aiogram.filters import Command

from backend.user import User
from backend.log import Log

# Registering the router for further connection
audio_command = Router()
audio_command.name = "audio"

@audio_command.message(Command("audio"))
async def command_start_trigger(message: Message) -> None:
    """ Works when the user enters /audio """
    # Info about user
    user_id = message.from_user.id
    username = message.from_user.username

    user = User(user_id, username)

    Log.message_logging(call="/audio", user=user, chat_id=message.chat.id)
    
    await message.bot.send_audio(chat_id=message.chat.id, 
                                 audio=FSInputFile("src\\storage\\sounds\\audio_sample.mp3"),
                                 caption="Example audio")