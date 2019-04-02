# from django.contrib.auth.models import User
# from rest_framework import authentication
# from rest_framework import exceptions
#
# class ExampleAuthentication(authentication.BaseAuthentication):
#     def authenticate(self, request):
#         username = request.META.get('X_USERNAME')
#         if not username:
#             return None
#
#         try:
#             user = User.objects.get(username=username)
#         except User.DoesNotExist:
#             raise exceptions.AuthenticationFailed('No such user')
#
#         return (user, None)
from django.contrib.auth.models import User
from rest_framework import exceptions
from rest_framework.authtoken.models import Token



# def simple_middleware(get_response):
#     # One-time configuration and initialization.
#
#     def middleware(request):
#         # Code to be executed for each request before
#         # the view (and later middleware) are called.
#         print(request.META)
#
#         username = request.META.get('X_USERNAME')
#         if not username:
#             return None
#
#         try:
#             user = Token.objects.get(key=username)
#             if user.created:
#                 pass
#         except User.DoesNotExist:
#             raise exceptions.AuthenticationFailed('No such user')
#
#         response = get_response(request)
#
#         # Code to be executed for each request/response after
#         # the view is called.
#
#         return response
#
#     return middleware
import datetime
def get_time_diff(par):
    now = datetime.datetime.now()
    timediff = now - par
    return timediff.total_seconds()


class StrideMIddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        return self.get_response(request)

    def process_exception(self, request, exception):
        print(request.META)
        username = request.META.get('HTTP_AUTHORIZATION')
        if not username:
            raise exceptions.AuthenticationFailed('No token')
        try:
            user = Token.objects.get(key=username)
            if user.created and  get_time_diff(user.created) > 18000:
                return None
            else:
                raise exceptions.AuthenticationFailed('token invalid')

        except User.DoesNotExist:
            raise exceptions.AuthenticationFailed('No such user')
