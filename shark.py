import requests
import json

class GetData:
    @staticmethod
    def get_money(guild: int, user: int):
        response = requests.get(f"https://www.sharkbot.xyz/api/money?guild={guild}&user={user}")
        return response.json()
    
    @staticmethod
    def get_item(user: int):
        response = requests.get(f"https://www.sharkbot.xyz/api/item?user={user}")
        return response.json()
    
    @staticmethod
    def get_score(guild: int, user: int):
        response = requests.get(f"https://www.sharkbot.xyz/api/score?user={user}&guild={guild}")
        return response.json()
    
    @staticmethod
    def auth_token(token: str):
        response = requests.get(f"https://www.sharkbot.xyz/api/auth?token={token}")
        return response.json()
    
    @staticmethod
    def add_money(token: str, user: int, money: int):
        response = requests.get(f"https://www.sharkbot.xyz/api/money_add?token={token}&user={user}&money={money}")
        return response.json()

class Economy:
    def __init__(self, guild: int, user: int):
        self.data = GetData.get_money(guild, user)

    @property
    def coin_name(self):
        return self.data.get("CoinName", None)
    
    @property
    def money(self):
        return self.data.get("Money", None)
        
class AddEconomyMoney:
    def __init__(self, token: str, user: int, money: int):
        self.data = GetData.add_money(token, user, money)

class EconomyItems:
    def __init__(self, user: int):
        self.data = GetData.get_item(user)

    @property
    def item(self):
        return self.data.get("Items", None)
        
class Score:
    def __init__(self, guild: int, user: int):
        self.data = GetData.get_score(guild, user)

    @property
    def score(self):
        return self.data.get("Score", None)
        
class Auth:
    def __init__(self, token: str):
        self.data = GetData.auth_token(token)

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