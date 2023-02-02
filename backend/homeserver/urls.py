"""homeserver URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include
# from dietapp.views import ProductViewSet, CategoryViewSet, DayPartProductViewSet
# from moneyapp.views import BankViewSet, BasketViewSet, TransferViewSet
# router.register('banks', BankViewSet)
# router.register('baskets', BasketViewSet)
# router.register('transfers', TransferViewSet)
# router.register('products', ProductViewSet)
# router.register('categories', CategoryViewSet)
# router.register('dayparts', DayPartProductViewSet)

urlpatterns = [
    path('backend/', include('mainapp.urls')),
    # path('backend/', include('mainapp.urls', namespace='mainapp')),
    # path('', include('mainapp.urls', namespace='mainapp')),
    # path('api/', include(router.urls)),
    # path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    # path('api-token-auth/', obtain_auth_token),
    # path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    # path('admin/', admin.site.urls),
    # path('user/', include('authapp.urls', namespace='authapp')),
    # path('house/', include('houseapp.urls', namespace='houseapp')),
    # path('diet/', include('dietapp.urls', namespace='dietapp')),
]

