from aiogram import Dispatcher, Bot
from aiogram.types import BotCommand

from handlers.start import start_command

from src.core import Core
from src.log import Log
from src.templates import Templates

class App:
    dispatcher = Dispatcher()
    core = Core()
    log = Log()
    
    def __init__(self):
        self.bot = Bot(token=self.core.token)
        
    async def configurate(self):
        await self.set_commands()
        await self.register_handlers()
    
    async def set_commands(self):
        await self.bot.set_my_commands(commands=[
            BotCommand(command="/start", description="Начать работу"),
        ])
        
    async def register_handlers(self):
        handlers = (
            start_command,
        )

        log_message: str = f"\n{' ROUTERS '.center(48, '=')}\n"

        for index, router in enumerate(handlers):
            try:
                self.dispatcher.include_router(router)
                log_message += f"{router.name:<20}[{index+1}] initialized success ✅\n"
            except ValueError:
                log_message += f"{router.name:<15}[{index+1}] failed ❌\n"

        log_message += f"{''.center(48, '=')}\n"

        self.log.bot_logging(log_message)
        
    async def start(self):
        self.log.bot_logging(Templates.BOT_POLLING)
        await self.bot.delete_webhook(drop_pending_updates=True)
        await self.dispatcher.start_polling(self.bot)
