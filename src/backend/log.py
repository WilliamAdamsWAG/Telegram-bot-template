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
from loguru import logger

from backend.templates import Templates

logger.add("../logs/bot.log",
           format=Templates.LOG_FORMAT.value,
           level="DEBUG",
           filter=lambda record: record['extra'].get('name') == 'bot')

logger.add("../logs/messages.log",
           format=Templates.LOG_FORMAT.value,
           level="DEBUG",
           filter=lambda record: record['extra'].get('name') == 'message')

BOT_LOG = logger.bind(name="bot")
MESSAGE_LOG = logger.bind(name="message")

class Log:
    """ Logger """
    @staticmethod
    def bot_logging(text: str) -> None:
        """ Log bot activities """
        BOT_LOG.info(text)

    @staticmethod
    def message_logging(*, call: str, user, chat_id) -> None:
        """ Log messages """
        MESSAGE_LOG.info(Templates.LOG_MESSAGE.value.substitute(
            user_info=user.user_info,
            chat=chat_id,
            text=call
        ))

    @staticmethod
    def bot_routers_logging(routers: dict[str, bool]) -> None:
        """ Log routers initiazilization """
        routers_status: str = ""

        for index, values in enumerate(list(routers.items())):
            if values[1]:
                routers_status += Templates.LOG_ROUTER_TRUE.value.substitute(
                    router=f"{values[0]:<20}",
                    index=index+1
                )
            else:
                routers_status += Templates.LOG_ROUTER_FALSE.value.substitute(
                    router=f"{values[0]:<15}",
                    index=index+1
                )

        BOT_LOG.info(Templates.LOG_ROUTERS_REGISTER.value.substitute(
            routers=routers_status
        ))
