from string import Template
from datetime import datetime


class Templates:
    LOG_BOT_POLLING = (f"\n{' POLLING '.center(50, '=')}\n"
                   f"Bot polling started at {datetime.now()}\n"
                   f"{''.center(50, '=')}\n")
    
    START = "This is example of greeting text"
    
    LOG_MESSAGE = Template(f"\nMessage ->\n"
                           f"@$username:$user_id (chat $chat)\n"
                           f"$text\n")
