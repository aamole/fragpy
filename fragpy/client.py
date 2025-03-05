import asyncio
import logging
import platform
from fragpy import __version__
from fragpy.methods import Methods
from fragpy.utils import ainput

logger = logging.getLogger(__name__) 

class Client(Methods):
    """Fragpy Client - The main interface for interacting with Fragment."""

    APP_VERSION = f"Fragpy {__version__}"
    DEVICE_MODEL = f"{platform.python_implementation()} {platform.python_version()}"
    SYSTEM_VERSION = f"{platform.system()} {platform.release()}"
    BASE_URL = "https://fragment.com"

    def __init__(self, name: str, session_string: str = None, in_memory: bool = None, 
                 phone_number: str = None, no_updates: bool = None, logger: bool = None):
        super().__init__() 
        self.name = name
        self.session_string = session_string
        self.in_memory = in_memory
        self.phone_number = phone_number
        self.no_updates = no_updates
        self.timeout = None
    async def get_phone_number(self):
        """Get phone number."""
        while True:
            value = (await ainput("Enter phone number: ")).strip()
            if value:
                confirm = (await ainput(f'Is "{value}" correct? (y/N): ')).strip().lower()
                if confirm == "y":
                    return value

    async def authorize(self): 
        print(f"Welcome to Fragpy (version {__version__})")
        print("Fragpy is free software and comes with ABSOLUTELY NO WARRANTY.")

        if not self.phone_number:
            self.phone_number = await self.get_phone_number()

        _, ssid, tsession = await self.send_confirm(self.phone_number)
    
        print(
            f"Confirm login via Telegram with ({self.phone_number})\n"
            "To authorize this request, use the 'Confirm' button.\n"
            "If you didn't request this, use the 'Decline' button or ignore the message."
        )

        max_attempts = 300

        for i in range(max_attempts):
            check_cl, self.stel_token = await self.check_confirm(
                phone_number=self.phone_number, 
                stel_ssid=ssid,
                stel_tsession=tsession
            )
            print(self.stel_token, check_cl)
            if check_cl:
                break
            await asyncio.sleep(1)
        print(self.stel_token)
