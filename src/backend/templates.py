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
from string import Template
from datetime import datetime
from enum import Enum

class Templates(Enum):
    """ Templates
    templates for logs and messages

    """
    LOG_FORMAT: str = "\n{level.icon}{time:DD.MM HH:mm:ss}\n{message}\n"

    LOG_BOT_POLLING: str = (f"\n{' POLLING '.center(50, '=')}\n"
                       f"Bot polling started at {datetime.now()}\n"
                       f"{''.center(50, '=')}\n")

    LOG_MESSAGE = Template("\nMessage ->\n"
                           "@$user_info (chat $chat)\n"
                           "$text\n")

    LOG_ROUTERS_REGISTER = Template(f"\n{' ROUTERS '.center(48, '=')}\n"
                                   "$routers"
                                   f"{''.center(48, '=')}\n")

    LOG_ROUTER_TRUE = Template("$router[$index] initialized success ✅\n")
    LOG_ROUTER_FALSE = Template("$router[$index] failed ❌\n")

    START: str = "This is example of greeting text"
    TYPING: str = "This example use typing bot status"
