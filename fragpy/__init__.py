__version__ = "0.0.1"

oauth: str = "https://oauth.telegram.org/{}".format
fram: str = "https://fragment.com{}".format
params: dict[str, str] = {
    "bot_id": "5444323279", "origin": fram(''),
    "request_access": "write", "return_to": fram(''),
}
headers: dict[str, str] = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
}