import aiohttp

class Corona:
    def __init__(self, serviceKey: str):
        self.serviceKey = serviceKey
        self.domesticcounterurl = 'https://api.corona-19.kr/korea'
        self.cityoccurrenceurl = 'https://api.corona-19.kr/korea/country/new'

    async def DomesticCounter(self):
        async with aiohttp.ClientSession() as session:
            async with session.get(f'{self.domesticcounterurl}/?serviceKey={self.serviceKey}') as response:
                res = await response.json()
                return res

    async def CityOccurrence(self):
        async with aiohttp.ClientSession() as sessions:
            async with sessions.get(f'{self.cityoccurrenceurl}/serviceKey={self.serviceKey}') as response:
                res = await response.json()
                return res