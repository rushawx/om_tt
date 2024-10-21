import json
import uuid

import aiohttp
from bs4 import BeautifulSoup

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from app.models import Record


async def index(request):
    return HttpResponse('Hello! This is a test task for Open Media.')

@csrf_exempt
async def create_page(request):
    
    if request.method == "POST":
    
        url = json.loads(request.body).get('url')

        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                html = await response.text()

        soup = BeautifulSoup(html, 'html.parser')

        data = Record(
            uuid=uuid.uuid4(),
            h1=len(soup.find_all('h1')),
            h2=len(soup.find_all('h2')),
            h3=len(soup.find_all('h3')),
            a=[x.get('href') for x in soup.find_all('a')],
        )

        await data.asave()

        return HttpResponse(data.uuid)

async def view_page_object(request, uid):

    object = await Record.objects.aget(pk=uid)

    data = {
        'h1': object.h1,
        'h2': object.h2,
        'h3': object.h3,
        'a': object.a
    }

    return HttpResponse(json.dumps(data))

async def list_page_objects(request):

    order = request.GET.get('order', '-created_at')

    records = []

    async for object in Record.objects.all().order_by(order):

        data = {
            'h1': object.h1,
            'h2': object.h2,
            'h3': object.h3,
            'a': object.a
        }

        records.append(data)

    return HttpResponse(json.dumps(records))
