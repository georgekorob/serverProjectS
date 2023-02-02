import datetime
from django.http import HttpResponseRedirect, HttpResponse
from django.views.generic import TemplateView
from rest_framework.renderers import JSONRenderer
from rest_framework.viewsets import ModelViewSet
from mainapp.mixins import PageTitleMixin
from mainapp.models import MenuItem
from mainapp.serializers import MenuSerializer


# Create your views here.
class IndexTemplateView(PageTitleMixin, TemplateView):
    template_name = 'mainapp/index.html'
    title = 'главная'


class ContactsTemplateView(PageTitleMixin, TemplateView):
    template_name = 'mainapp/contacts.html'
    title = 'контакты'


class AboutTemplateView(PageTitleMixin, TemplateView):
    template_name = 'mainapp/about.html'
    title = 'о нас'


# def create_day(request):
#     Day.objects.create(date=datetime.datetime.today(), user=request.user)
#     return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def get_menu_list(request):
    if request.user.is_authenticated:
        menu = MenuItem.objects.filter(isAuthNeed=False)
    else:
        menu = MenuItem.objects.all()
    serializer = MenuSerializer(menu)
    data = JSONRenderer().render(serializer.data)
    return HttpResponse(data, content_type='application/json')


class MenuViewSet(ModelViewSet):
    queryset = MenuItem.objects.all()
    serializer_class = MenuSerializer

    # def get_queryset(self):
    #     return self.request.user.menu_access.all()
