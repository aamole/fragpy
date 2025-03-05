import logging
import fragpy
from fragpy.methods.api import send

log = logging.getLogger(__name__)

class CheckConfirm:
    async def check_confirm(self: "fragpy.Client", stel_ssid: str, stel_tsession: str, phone_number: str):
        """Check for confirmation status."""
 
        phone = phone_number.replace("+", "").replace(" ", "")

        log.info(f"Checking confirmation for: {phone}")
        
        cookies = {
            "stel_ssid": stel_ssid,
            f"stel_tsession_{phone}": stel_tsession,
            "stel_tsession": stel_tsession
        }

        data, response = await send(
            "POST",
            url=fragpy.oauth("/auth/login"),
            cookies=cookies,
            headers=fragpy.headers,
            params=fragpy.params
        )
        cookies = response.cookies
        
        stel_token = cookies.get("stel_token").value if "stel_token" in cookies else None
        log.debug(f"Response Data: {data}")

        if isinstance(data, bool) and not data:
            log.warning(f"Login confirmation failed for: {phone}")
            return False, None

        
        return True, stel_token
