from django.contrib.auth.models import Group
from rest_framework.permissions import IsAdminUser, DjangoObjectPermissions


class IsAdminOrFamilyGroupOrHostHome(IsAdminUser):
    def has_permission(self, request, view):
        request_host = request.get_host()
        is_hosthome = any([host in request_host for host in ['127.0.0.1', 'localhost']])
        is_family = any([g.name == 'Family' for g in request.user.groups.all()])
        is_admin = super().has_permission(request, view)
        # print(f'Admin: {is_admin}, HostHome: {is_hosthome}, Family: {is_family}.')
        return is_hosthome or is_family or is_admin
