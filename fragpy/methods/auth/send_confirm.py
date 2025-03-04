import fragpy

class SendConfirm:
    async def send_confirm(self: "fragpy.Client",phone_number: str):
        """Send confirm message to the given phone number.
        """
        
        phone_number = phone_number.strip(" +")
        print(phone_number)