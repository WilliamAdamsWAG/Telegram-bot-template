from loguru import logger

from src.templates import Templates

logger.add("logs/bot.log",
           format="\n{level.icon}{time:DD.MM HH:mm:ss}\n{message}\n",
           level="DEBUG",
           filter=lambda record: record['extra'].get('name') == f'bot')

logger.add("logs/messages.log",
           format="\n{level.icon}{time:DD.MM HH:mm:ss}\n{message}\n",
           level="DEBUG",
           filter=lambda record: record['extra'].get('name') == f'message')

class Log:
    bot_log = logger.bind(name="bot")
    message_log = logger.bind(name="message")

    def bot_logging(self, text: str) -> None:
        self.bot_log.info(text)
        
    def message_logging(self, *, call: str, user, chat_id):
        self.message_log.info(Templates.LOG_MESSAGE.substitute(
            user_id=user.user_id,
            username=user.username,
            chat=chat_id,
            text=call
        ))
        