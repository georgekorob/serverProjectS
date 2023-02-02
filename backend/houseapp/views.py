import aiohttp
import asyncio
import re
from django.shortcuts import redirect
from django.views.generic import ListView, DetailView
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from wakeonlan import send_magic_packet
import os
from houseapp.models import Nodemcu, PartString
from houseapp.serializers import PartStringSerializer, NodemcuSerializer
from mainapp.mixins import PageTitleMixin

flag_first_run = True
sleep_string_no = "sshpass -p {} ssh -oStrictHostKeyChecking=no {}@{} \"rundll32 powrprof.dll,SetSuspendState 0,1,0\""
sleep_string = "sshpass -p {} ssh {}@{} \"rundll32 powrprof.dll,SetSuspendState 0,1,0\""


# Create your views here.
async def req_async(client, link):
    try:
        if "https://" in link or "http://" in link:
            if '/sleepnow/' in link:
                parts = link.strip('/').rsplit('/', 4)
                sleep_cmd = sleep_string_no.format(*parts[2:])
                # if flag_first_run:
                #     sleep_cmd = sleep_string_no.format(*parts[2:])
                #     flag_first_run = False
                try:
                    os.system(sleep_cmd)
                except Exception as e:
                    print(e)
                    print(sleep_cmd)
            else:
                async with client.get(link) as response:
                    await response.read()
        # else: <servwakeport>/<macpc>
        #     send_magic_packet(link)
    except Exception as e:
        print(e)


async def run_all_async(links):
    loop = asyncio.get_running_loop()
    async with aiohttp.ClientSession(loop=loop) as client:
        await asyncio.gather(*[req_async(client, url) for url in links])


class ShowNodemcusList(ListView, PageTitleMixin):
    model = Nodemcu
    template_name = 'houseapp/house.html'
    title = 'умный дом'
    context_object_name = 'Nodemcu'


class ShowNodemcu(DetailView, PageTitleMixin):
    model = Nodemcu
    # template_name = 'houseapp/node_detail.html'
    context_object_name = 'Nodemcu'

    def get(self, request, **kwargs):
        node = Nodemcu.objects.get(pk=self.kwargs['pk'])
        parts = PartString.objects.all()
        links = node.urls
        for part in parts:
            links = re.sub(f'<{part.name}>', part.body, links)
        links = links.split('\r\n')
        asyncio.run(run_all_async(links))
        return redirect('/house/')

    def get_context_data(self, **kwards):
        ctx = super(ShowNodemcu, self).get_context_data(**kwards)
        node = Nodemcu.objects.get(pk=self.kwargs['pk'])
        self.title = node
        ctx['text'] = node.urls
        return ctx


class NodemcuViewSet(ModelViewSet):
    queryset = Nodemcu.objects.all()
    serializer_class = NodemcuSerializer
    # permission_classes = [IsAuthenticated]

    def retrieve(self, request, *args, **kwargs):
        if request.query_params.get('version') == 'click':
            node = Nodemcu.objects.get(pk=self.kwargs['pk'])
            parts = PartString.objects.all()
            links = node.urls
            for part in parts:
                links = re.sub(f'<{part.name}>', part.body, links)
            links = links.split('\r\n')
            asyncio.run(run_all_async(links))
            return Response('click')
        else:
            return super().retrieve(request, *args, **kwargs)


class PartStringViewSet(ModelViewSet):
    queryset = PartString.objects.all()
    serializer_class = PartStringSerializer
