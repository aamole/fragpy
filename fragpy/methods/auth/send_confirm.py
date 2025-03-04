import logging
import fragpy
from fragpy.methods.api import send

log = logging.getLogger(__name__) 

class SendConfirm:
    async def send_confirm(self: "fragpy.Client",phone_number: str):
        """Send confirm message to the given phone number.
        """
        self.phone_number = phone_number
        print(self.phone_number)
        _, response = await send('GET', fragpy.fram(''))
        self.stel_ssid = response.cookies['stel_ssid'].value
        data, response = await send(
            'POST', 
            url=fragpy.oauth('/auth/request'), 
            cookies={"stel_ssid": self.stel_ssid}, 
            data={"phone": self.phone_number}, 
            headers=fragpy.headers,
            params=fragpy.params
        )
        if data:
            if data == 'Invalid phone number':
                log.error("Invalid phone number %s change it.", self.phone_number)
            if data == 'false':
                pass
            
            print(data)
            print(response)