# coding: utf-8
import aiohttp
from lib.logging import get_logger


class SMSC(object):
    __slots__ = ("logger", "login", "password", "phones")

    def __init__(self, login, password, phones):
        self.login = login
        self.logger = get_logger("smsc")
        self.phones = phones
        self.password = password

    async def send_messages(self, messages):
        """ Send messages for all phones
        """
        self.logger.debug(f"Sending SMS to: {self.phones}")

        async with aiohttp.ClientSession() as http:
            response = await http.post("https://smsc.ru/sys/send.php",
                                       data=dict(
                                           login=self.login,
                                           psw=self.password,
                                           phones=",".join(self.phones),
                                           mes="\n".join(messages)
                                       ))
            text = await response.text()

            self.logger.debug(f"Response from SMSC: {text}")
