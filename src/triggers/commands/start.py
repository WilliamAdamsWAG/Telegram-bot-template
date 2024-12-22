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
from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext

from backend.database import Database
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

    user = Database.get_user(user_id, username)

    Log.message_logging(call="/start", user=user, chat_id=message.chat.id)

    await message.answer(Templates.START.value, parse_mode="markdown")
