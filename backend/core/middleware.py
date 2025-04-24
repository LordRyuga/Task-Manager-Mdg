from rest_framework_simplejwt.authentication import JWTAuthentication
from django.utils.deprecation import MiddlewareMixin

class CookieToHeaderMiddleware(MiddlewareMixin):
    def process_request(self, request):
        if 'access' in request.COOKIES:
            request.META['HTTP_AUTHORIZATION'] = f"Bearer {request.COOKIES['access']}"