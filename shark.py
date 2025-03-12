import requests
import json

base_url = "https://api.sharkbot.xyz"

class GetData:

    @staticmethod
    def auth_token(token: str):
        response = requests.post(base_url + "/auth", json={"token": token})
        return response.json()

class Auth:
    def __init__(self, token: str):
        self.data = GetData().auth_token(token)

    @property
    def guild_id(self):
        return self.data.get("Guild", None)
    
    @property
    def guild_name(self):
        return self.data.get("GuildName", None)
    
    @property
    def author_id(self):
        return self.data.get("Author", None)
    
    @property
    def author_name(self):
        return self.data.get("AuthorName", None)
    
    @property
    def token(self):
        return self.data.get("Token", None)