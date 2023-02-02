from django.urls import path, include
from django.contrib import admin
from houseapp.views import NodemcuViewSet, PartStringViewSet
from mainapp.views import MenuViewSet
from authapp.views import UserViewSet
from mainapp.views import IndexTemplateView, ContactsTemplateView, AboutTemplateView
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView, TokenVerifyView

router = routers.DefaultRouter()
router.register('users', UserViewSet)
router.register('menus', MenuViewSet)
router.register('nodemcus', NodemcuViewSet)
router.register('partstrings', PartStringViewSet)

# app_name = 'mainapp'
urlpatterns = [
    path('', IndexTemplateView.as_view(), name='index'),
    path('contacts/', ContactsTemplateView.as_view(), name='contacts'),
    path('about/', AboutTemplateView.as_view(), name='about'),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api-token-auth/', obtain_auth_token),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('user/', include('authapp.urls', namespace='authapp')),
    path('house/', include('houseapp.urls', namespace='houseapp')),
    path('admin/', admin.site.urls),
]  # + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
