import asyncio
from fragpy.client import Client


frag = Client(
    name="aa",
    session_string="",
    in_memory=False,
    phone_number="",
    no_updates=False
)

# print(frag)
# print(f"App Version: {frag.APP_VERSION}")
# print(f"Device Model: {frag.DEVICE_MODEL}")
# print(f"System Version: {frag.SYSTEM_VERSION}")

a = asyncio.run(frag.authorize())

print(a)
