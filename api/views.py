from django.shortcuts import render

# Create your views here.


from django.http import HttpResponse
from django.views import View
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

from rest_framework.views import APIView



class MyView(APIView):
    template_name="login.html"
    def get(self, request, *args, **kwargs):
        print(request)
        return render(request,template_name=self.template_name)

    def post(self,request):
        user_email = request.data['email']
        password = request.data['password']
        print(request.data)
        u = User.objects.create(email=user_email,username=user_email)
        u.set_password(password)
        u.save()

        token = Token.objects.create(user=u)
        print(token.key)
        data ={'Token':token.key}
        return Response(data=data, status=201)


myview = MyView.as_view()




class Test(APIView):
    template_name="login.html"
    def get(self, request, *args, **kwargs):
        data = {'auth': True}
        return Response(data, status=200)


some = MyView.as_view()