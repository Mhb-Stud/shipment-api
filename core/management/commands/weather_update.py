from typing import Any
from django.core.management.base import BaseCommand
from core.models import Shipment, Article
from django.core.cache import cache
import asyncio
import aiohttp
from core.services import update_weather


class Command(BaseCommand):
    name = 'weather_update'
    def handle(self, *args: Any, **options: Any) -> str | None:
        update_weather()
    
