from loguru import logger

from backend.templates import Templates

logger.add("../logs/bot.log",
           format=Templates.LOG_FORMAT,
           level="DEBUG",
           filter=lambda record: record['extra'].get('name') == f'bot')

logger.add("../logs/messages.log",
           format=Templates.LOG_FORMAT,
           level="DEBUG",
           filter=lambda record: record['extra'].get('name') == f'message')

BOT_LOG = logger.bind(name="bot")
MESSAGE_LOG = logger.bind(name="message")

class Log:
    @staticmethod
    def bot_logging(text: str) -> None:
        """ Log bot activities """
        BOT_LOG.info(text)
    
    @staticmethod
    def message_logging(*, call: str, user, chat_id):
        """ Log messages """
        MESSAGE_LOG.info(Templates.LOG_MESSAGE.substitute(
            user_id=user.user_id,
            username=user.username,
            chat=chat_id,
            text=call
        ))
        