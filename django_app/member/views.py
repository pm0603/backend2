import requests
from django.contrib.auth import authenticate, logout
from django.core.exceptions import ObjectDoesNotExist
from django.db import IntegrityError
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from config import settings
from member.forms import UserForm, UserSignupForm
from member.models import MyUser, UserHash


class Login(APIView):
    def post(self, request, *args, **kwargs):
        form = UserForm(data=request.POST)
        if form.is_valid():
            user = authenticate(
                email=form.cleaned_data["email"],
                password=form.cleaned_data["password"],
            )

            if user:
                token = Token.objects.get_or_create(user=user)[0]
                ret = {"token": token.key}
                return Response(ret, status=status.HTTP_200_OK)

            else:
                return Response({"error": "이메일 혹은 비밀번호가 올바르지 않습니다."}, status=status.HTTP_400_BAD_REQUEST)


class Logout(APIView):
    permission_classes = (AllowAny,)

    def post(self, request):
        try:
            request.user.auth_token.delete()
        except:
            pass
        logout(request)
        return Response({"success": "Successfully logged out."},
                        status=status.HTTP_200_OK)


class SignUp(APIView):
    def post(self, request, *args, **kwargs):
        form = UserSignupForm(data=request.POST)
        if form.is_valid():
            try:
                MyUser.objects.create_user(
                    email=form.cleaned_data["email"],
                    password=form.cleaned_data["password"],
                )
            except IntegrityError as e:
                if "email" in str(e):
                    return Response({"error": "이미 존재하는 email 입니다."}, status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response({"success": "인증 이메일이 발송되었습니다."}, status=status.HTTP_200_OK)


class FacebookLogin(APIView):
    def post(self, request, *args, **kwargs):
        access_token = request.POST.get("access_token")
        url_debug_token = 'https://graph.facebook.com/debug_token?' \
                          'input_token={it}&' \
                          'access_token={at}'.format(
            it=access_token,
            at=settings.FB_APP_ACCESS_TOKEN
        )
        r = requests.get(url_debug_token)
        debug_token = r.json()
        if debug_token['data']['is_valid']:
            user_id = debug_token['data']['user_id']
            try:
                facebook_user = MyUser.objects.get(facebook_id=user_id)
            except MyUser.DoesNotExist:
                user_info = self.get_user_info(user_id, access_token)
                facebook_user = MyUser.objects.create_facebook_user(facebook_id=user_id,
                                                                    email=user_info['email'])
            token = Token.objects.get_or_create(user=facebook_user)[0]
            ret = {"token": token.key}
            return Response(ret, status=status.HTTP_200_OK)
        else:
            return Response({'error': debug_token['data']['error']['message']})

    def get_user_info(self, user_id, access_token):
        url_request_user_info = 'https://graph.facebook.com/' \
                                '{user_id}?' \
                                'fields=email&' \
                                'access_token={access_token}'.format(
            user_id=user_id,
            access_token=access_token
        )
        r = requests.get(url_request_user_info)
        user_info = r.json()
        return user_info


class UserActivate(APIView):
    def get(self, request, *args, **kwargs):

        hashed_email = "$pbkdf2-sha512$8000$" + kwargs.get("hash") + settings.SECRET_KEY
        try:
            active_ready_user = UserHash.objects.get(hashed_email=hashed_email)
        except ObjectDoesNotExist:
            return Response({"error": "인증요청 url이 잘못되었습니다."}, status=status.HTTP_400_BAD_REQUEST)
        active_ready_user.user.is_active = True
        active_ready_user.user.save()
        return Response({"info": "계정이 활성화 되었습니다."}, status=status.HTTP_200_OK)
