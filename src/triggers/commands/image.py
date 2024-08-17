from aiogram import Router
from aiogram.types import Message, FSInputFile
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext

from backend.user import User
from backend.log import Log

# Registering the router for further connection
image_command = Router()
image_command.name = "image"

@image_command.message(Command("image"))
async def command_start_trigger(message: Message, state: FSMContext) -> None:
    """ Works when the user enters /image """
    await state.clear()  #  Exit from any FSM states
    
    # Info about user
    user_id = message.from_user.id
    username = message.from_user.username

    user = User(user_id, username)

    Log.message_logging(call="/image", user=user, chat_id=message.chat.id)
    
    await message.bot.send_photo(chat_id=message.chat.id, 
                                 photo=FSInputFile("src\\storage\\img\\rep_banner.png"),
                                 caption="Example photo")
