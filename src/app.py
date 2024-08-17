import os

from aiogram import Dispatcher, Bot
from aiogram.types import BotCommand

from triggers.commands.start import start_command
from triggers.messages.echo_message import echo_message
from triggers.commands.image import image_command
from triggers.commands.audio import audio_command

from backend.log import Log
from backend.templates import Templates

class App:
    """ The base class of the bot, which describes the parameters of its launch """
    TOKEN = os.environ.get("TELEGRAM_API_TOKEN")
    
    def __init__(self) -> None:
        self.bot = Bot(token=self.TOKEN)
        self.dispatcher = Dispatcher()
        
    async def configure(self) -> None:
        """ Configuring and connecting components """
        await self.set_commands()
        await self.connect_routers()
    
    async def set_commands(self) -> None:
        """ Enable commands to menu """
        await self.bot.set_my_commands(commands=[
            BotCommand(command="/start", description="greeting"),
            BotCommand(command="/image", description="image sample"),
            BotCommand(command="/audio", description="audio sample"),
        ])
        
    async def connect_routers(self) -> None:
        """ Connect routers for enable triggers """
        #! IMPORTANT: Messages and activity in the bot goes through this list sequentially, 
        #! so you need to properly arrange connections, because if 1 handler is triggered, 
        #! the second one will not run
        routers: tuple = (
            start_command,
            image_command,
            audio_command,
            echo_message,
        )
        
        routers_connection_info: dict[str, bool] = {}

        for router in routers:
            try:
                self.dispatcher.include_router(router)
                routers_connection_info[router.name] = True
            except ValueError:
                routers_connection_info[router.name] = False

        Log.bot_routers_logging(routers_connection_info)
        
    async def start(self) -> None:
        Log.bot_logging(Templates.LOG_BOT_POLLING)
        
        #! When the bot is turned off all commands from users are saved and will be processed at startup, 
        #! in order not to process old requests you need to delete webhooks
        await self.bot.delete_webhook(drop_pending_updates=True)
        await self.dispatcher.start_polling(self.bot) #* Run bot
