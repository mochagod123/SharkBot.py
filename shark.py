import aiohttp
import asyncio
import json

class GetData:
    async def get_money(guild: int, user: int):
        async with aiohttp.ClientSession() as session:
            async with session.get(f"https://www.sharkbot.xyz/api/money?guild={guild}&user={user}") as response:
                return json.loads(await response.text())
            
    async def get_item(user: int):
        async with aiohttp.ClientSession() as session:
            async with session.get(f"https://www.sharkbot.xyz/api/item?user={user}") as response:
                return json.loads(await response.text())
            
    async def get_score(guild: int, user: int):
        async with aiohttp.ClientSession() as session:
            async with session.get(f"https://www.sharkbot.xyz/api/score?user={user}&guild={guild}") as response:
                return json.loads(await response.text())

class Economy:
    def __init__(self, guild: int, user: int):
        loop = asyncio.get_event_loop()
        self.data = loop.run_until_complete(GetData.get_money(guild, user))

    @property
    def coin_name(self):
        try:
            return self.data["CoinName"]
        except:
            return None
    
    @property
    def money(self):
        try:
            return self.data["Money"]
        except:
            return None
        
class EconomyItems:
    def __init__(self, user: int):
        loop = asyncio.get_event_loop()
        self.data = loop.run_until_complete(GetData.get_item(user))

    @property
    def item(self):
        try:
            return self.data["Items"]
        except:
            return None
        
class Score:
    def __init__(self, guild: int, user: int):
        loop = asyncio.get_event_loop()
        self.data = loop.run_until_complete(GetData.get_score(guild, user))

    @property
    def score(self):
        try:
            return self.data["Score"]
        except:
            return None