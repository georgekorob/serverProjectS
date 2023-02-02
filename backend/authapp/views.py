from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LogoutView, LoginView, FormView
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404, redirect

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import UpdateView  # , FormView
from rest_framework.renderers import JSONRenderer
from rest_framework.viewsets import ModelViewSet

from authapp.forms import UserLoginForm, UserRegisterForm, UserProfileForm
from authapp.models import User
from authapp.serializers import UserSerializer, UserInfoSerializer
from mainapp.mixins import PageTitleMixin


class UserLoginView(PageTitleMixin, LoginView):
    form_class = UserLoginForm
    title = 'авторизация'
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        super().form_valid(form)
        return HttpResponseRedirect(self.success_url)


class UserLogoutView(LoginRequiredMixin, LogoutView):
    success_url = reverse_lazy('index')

    def dispatch(self, request, *args, **kwargs):
        super().dispatch(request, *args, **kwargs)
        return redirect(self.success_url)


class UserRegisterView(PageTitleMixin, FormView):
    form_class = UserRegisterForm
    template_name = 'authapp/register.html'
    title = 'регистрация'
    success_url = reverse_lazy('authapp:login')

    def form_valid(self, form):
        form.save()
        return HttpResponseRedirect(self.get_success_url())


class UserProfileView(LoginRequiredMixin, PageTitleMixin, UpdateView):
    form_class = UserProfileForm
    success_url = reverse_lazy('authapp:profile')
    # template_name = 'authapp/profile.html'
    title = 'редактирование'

    def form_valid(self, form):
        super().form_valid(form)
        return HttpResponseRedirect(self.get_success_url())

    def get_object(self, *args, **kwargs):
        return get_object_or_404(User, pk=self.request.user.pk)

    def post(self, request, *args, **kwargs):
        form = UserProfileForm(data=request.POST, files=request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
        return redirect(self.success_url)


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filterset_fields = ['username']


def get_user_by_name(request, username):
    user = User.objects.get(username=username)
    serializer = UserInfoSerializer(user)
    data = JSONRenderer().render(serializer.data)
    return HttpResponse(data, content_type='application/json')
