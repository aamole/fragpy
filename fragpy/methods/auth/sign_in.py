import fragpy

class SignIn:
    async def sign_in(self: "fragpy.Client",phone_number: str,phone_code_hash: str,phone_code: str):
        """Authorize a user in Telegram with a valid confirmation code.
        """
        phone_number = phone_number.strip(" +")
        print(phone_number)
