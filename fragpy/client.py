import asyncio
import logging
import platform
from fragpy import __version__
from fragpy.methods import Methods
from fragpy.utils import ainput

logger = logging.getLogger(__name__) 

class Client(Methods):
    """Fragpy Client, the main means for interacting with Fragment.

    Parameters:
        name (``str``):
            A name for the client, e.g.: "my_account".
        phone_number (``str``, *optional*):
            Pass the phone number as string (with the Country Code).
            Only applicable for new sessions.
    """
    APP_VERSION = f"Fragpy {__version__}"
    DEVICE_MODEL = f"{platform.python_implementation()} {platform.python_version()}"
    SYSTEM_VERSION = f"{platform.system()} {platform.release()}"

    BASE_URL = "https://fragment.com"

    def __init__(self,name: str,session_string: str = None,in_memory: bool = None,phone_number: str = None,no_updates: bool = None,):
        super().__init__() 
        self.name = name
        self.session_string = session_string
        self.in_memory = in_memory
        self.phone_number = phone_number
        self.no_updates = no_updates
        self.timeout: int = None

    async def authorize(self): 
        print(f"Welcome to Fragpy (version {__version__})")
        print("Fragpy is free software and comes with ABSOLUTELY NO WARRANTY.")
        
        while True:
            if not self.phone_number:
                while True:
                    value = await ainput("Enter phone number: ")

                    if not value:
                        continue

                    confirm = (await ainput(f'Is "{value}" correct? (y/N): ')).lower()

                    if confirm == "y":
                        break

                if value:
                    self.phone_number = value
            else:
                break
        
        await self.send_confirm(self.phone_number)

        print(
            f"Confirm login via Telegram with ({self.phone_number})\n"
            "To authorize this request, use the 'Confirm' button.\n"
            "If you didn't request this, use the 'Decline' button or ignore the message."
        )

        # trys_check = 300
        # while True:
        #     self.check_cl = await self.check_click(self.phone_number)
        #     if not self.check_cl and trys_check > 0:
        #         trys_check -= 1
        #         await asyncio.sleep(1)
        #     else:
        #         break
