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
    def message_logging(*, call: str, user, chat_id) -> None:
        """ Log messages """
        MESSAGE_LOG.info(Templates.LOG_MESSAGE.substitute(
            user_info=user.user_info,
            chat=chat_id,
            text=call
        ))
        
    @staticmethod
    def bot_routers_logging(routers: dict[str, bool]) -> None:
        routers_status: str = ""
        
        for index, values in enumerate(list(routers.items())):
            if values[1]:
                routers_status += Templates.LOG_ROUTER_TRUE.substitute(
                    router=f"{values[0]:<20}",
                    index=index+1
                )
            else:
                routers_status += Templates.LOG_ROUTER_FALSE.substitute(
                    router=f"{values[0]:<15}",
                    index=index+1
                )
        
        BOT_LOG.info(Templates.LOG_ROUTERS_REGISTER.substitute(
            routers=routers_status
        ))
        