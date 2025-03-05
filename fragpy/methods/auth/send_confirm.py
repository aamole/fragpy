import logging
import fragpy
from fragpy.methods.api import send

log = logging.getLogger(__name__)

class SendConfirm:
    async def send_confirm(self: "fragpy.Client", phone_number: str):
        """Send confirmation message to the given phone number."""
        
        self.phone_number = phone_number
        print(f"Sending confirmation to: {self.phone_number}")

        _, response = await send('GET', fragpy.fram(''))
        self.stel_ssid = response.cookies.get('stel_ssid', None)

        if not self.stel_ssid:
            log.error("Failed to retrieve stel_ssid.")
            raise ConnectionError('Failed to retrieve stel_ssid.')
        

        data, response = await send(
            'POST', 
            url=fragpy.oauth('/auth/request'), 
            cookies={"stel_ssid": self.stel_ssid}, 
            data={"phone": self.phone_number}, 
            headers=fragpy.headers,
            params=fragpy.params
        )
        cookies = response.cookies
        stel_ssid = cookies.get("stel_ssid").value if "stel_ssid" in cookies else None
        stel_tsession = cookies.get("stel_tsession").value if "stel_tsession" in cookies else None
    
        if isinstance(data, str):
            if data == 'Invalid phone number':
                log.error("Invalid phone number: %s. Change it.", self.phone_number)
                return False

        elif isinstance(data, bool):
            if not data:
                log.warning("Received a False response for phone: %s", self.phone_number)
                return False

        return True, stel_ssid, stel_tsession