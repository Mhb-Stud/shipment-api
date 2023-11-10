from core.models import Shipment, Article
from django.core.cache import cache
import asyncio
import aiohttp

def city_extractor(current_location):
        return current_location.split(', ')[1].split(' ')[1]


async def fetch_data(session, obj):
    weather_api_key = '11d711372b1ae4a52de241ce61a2a310'
    current_address = obj.current_address
    city = city_extractor(obj.current_address)

    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={weather_api_key}'
    if cache.get(obj.current_address) is  None:
        async with session.get(url) as response:
            data = await response.json()
            weather_condition = data['weather'][0]['main']
            obj.weather_condition = weather_condition
            cache.set(obj.current_address, weather_condition, 1800)
    else:
        obj.weather_condition = cache.get(obj.current_address)

async def update_objects():
    async with aiohttp.ClientSession() as session:
        tasks = []
        shipments = Shipment.objects.all()
        async for shipment in shipments:
            if shipment.current_address != 'unknown':
                task = asyncio.create_task(fetch_data(session, shipment))
                tasks.append(task)
            else:
                shipment.weather_condition = 'unknown'
        await asyncio.gather(*tasks)
        await Shipment.objects.abulk_update(shipments, ["weather_condition"])


def update_weather():
    asyncio.run(update_objects())