import logging
import fragpy
from fragpy.methods.api import send

log = logging.getLogger(__name__)

class CheckConfirm:
    async def check_confirm(self: "fragpy.Client", stel_ssid: str, stel_tsession: str, phone_number: str):
        """Check for confirmation status."""
        data, response = await send(
            'POST',
            url=fragpy.oauth('/auth/login'), 
            cookies={"stel_ssid": stel_ssid,f"stel_tsession_{phone_number}": stel_tsession,"stel_tsession": stel_tsession}, 
            headers=fragpy.headers,
            params=fragpy.params
        )

        if isinstance(data, bool):
            if not data:
                log.warning("Received a False response for phone: %s", phone_number)
                return False

        return True, response.cookies.get('stel_token', None)
