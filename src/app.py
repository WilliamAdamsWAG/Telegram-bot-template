import os

from aiogram import Dispatcher, Bot
from aiogram.types import BotCommand

from triggers.commands.start import start_command
from triggers.messages.echo_message import echo_message

from backend.log import Log
from backend.templates import Templates

class App:
    """ The base class of the bot, which describes the parameters of its launch """
    TOKEN = os.environ.get("TELEGRAM_API_TOKEN")
    
    def __init__(self):
        self.bot = Bot(token=self.TOKEN)
        self.dispatcher = Dispatcher()
        
    async def configurate(self):
        """ Configuring and connecting components """
        await self.set_commands()
        await self.connect_triggers()
    
    async def set_commands(self):
        """ Enable commands to menu """
        await self.bot.set_my_commands(commands=[
            BotCommand(command="/start", description="greeting"),
        ])
        
    async def connect_triggers(self):
        """ Connect routers for enable triggers """
        # IMPORTANT: Messages and activity in the bot goes through this list sequentially, 
        # so you need to properly arrange connections, because if 1 handler is triggered, 
        # the second one will not run
        triggers = (
            start_command,
            echo_message,
        )

        log_message: str = f"\n{' ROUTERS '.center(48, '=')}\n"

        for index, router in enumerate(triggers):
            try:
                self.dispatcher.include_router(router)
                log_message += f"{router.name:<20}[{index+1}] initialized success ✅\n"
            except ValueError:
                log_message += f"{router.name:<15}[{index+1}] failed ❌\n"

        log_message += f"{''.center(48, '=')}\n"

        Log.bot_logging(log_message)
        
    async def start(self):
        Log.bot_logging(Templates.LOG_BOT_POLLING)
        
        # When the bot is turned off all commands from users are saved and will be processed at startup, 
        # in order not to process old requests you need to delete webhooks
        await self.bot.delete_webhook(drop_pending_updates=True)
        await self.dispatcher.start_polling(self.bot) # Run bot
