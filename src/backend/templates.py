from string import Template
from datetime import datetime


class Templates:
    LOG_FORMAT: str = "\n{level.icon}{time:DD.MM HH:mm:ss}\n{message}\n"
    
    LOG_BOT_POLLING: str = (f"\n{' POLLING '.center(50, '=')}\n"
                       f"Bot polling started at {datetime.now()}\n"
                       f"{''.center(50, '=')}\n")
    
    LOG_MESSAGE = Template(f"\nMessage ->\n"
                           f"@$user_info (chat $chat)\n"
                           f"$text\n")
    
    LOG_ROUTERS_REGISTER = Template(f"\n{' ROUTERS '.center(48, '=')}\n"
                                   f"$routers"
                                   f"{''.center(48, '=')}\n")
     
    LOG_ROUTER_TRUE = Template(f"$router[$index] initialized success ✅\n")
    LOG_ROUTER_FALSE = Template(f"$router[$index] failed ❌\n")
    
    START: str = "This is example of greeting text"
