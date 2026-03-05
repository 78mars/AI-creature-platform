from django.contrib.auth import authenticate
from django.db.models.expressions import result
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

from web.models.user import UserProfile


class LoginView(APIView):
    def post(self, request, *args, **kwargs):
        try:
            username = request.data['username'].strip()
            password = request.data['password'].strip()
            if not username or not password:
                return Response({
                    'result': '用户名和密码不为空'
                })
            # 验证用户名和密码
            user = authenticate(username=username, password=password)
            if user:
                user_profile = UserProfile.objects.get(user=user)
                refresh = RefreshToken.for_user(user)# 生成jwt
                response = Response({
                    'result': 'success',
                    'access': str(refresh),
                    'user_id': user.id,
                    'username': user.username,
                    'photo': user_profile.photo.url,
                    'profile': user_profile.user.username,
                })
                response.set_cookie(
                    key='refresh_token',
                    value=str(refresh),
                    httponly=True,
                    samesite='Lax',
                    secure=True,
                    max_age=86400 * 7,
                )
                return response
            # 不正确的情况
            return Response({
                'result': '用户名密码错误'
            })
        except:
            return Response({
                'result':'系统异常，请稍后'
            })