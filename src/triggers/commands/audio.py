""" MIT License

Copyright (c) 2024 WilliamAdamsWAG

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

"""
from aiogram import Router
from aiogram.types import Message, FSInputFile
from aiogram.filters import Command

from backend.user import User
from backend.database import Database
from backend.log import Log

# Registering the router for further connection
audio_command = Router()
audio_command.name = "audio"

@audio_command.message(Command("audio"))
async def command_start_trigger(message: Message) -> None:
    """ Works when the user enters /audio """
    # Info about user
    user_id: int = message.from_user.id
    username: str = message.from_user.username

    user: User = Database.get_user(user_id, username)

    Log.message_logging(call="/audio", user=user, chat_id=message.chat.id)

    await message.bot.send_audio(chat_id=message.chat.id,
                                 audio=FSInputFile("src\\storage\\sounds\\audio_sample.mp3"),
                                 caption="Example audio")
