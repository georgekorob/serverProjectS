from django.utils.deprecation import MiddlewareMixin


class GetHostMiddleware(MiddlewareMixin):
    def process_request(self, request):
        print(request.get_host())
