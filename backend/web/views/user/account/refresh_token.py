from django.conf import settings

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

class RefreshTokenView(APIView):
    def post(self, request):
        try:
            # 从cookie中获取refresh token
            refresh_token = request.COOKIES.get('refresh_token')
            if not refresh_token:
                return Response({
                    'result':'Refresh Token不存在'}, status = 401)
            # 判断refreshtoken是否过期
            refresh = RefreshToken(refresh_token) # 如果过期会返回异常，被后面捕获返回401
            if settings.SIMPLE_JWT['ROTATE_REFRESH_TOKENS']:
                refresh.set_jti() # 刷新refresh
                response = Response({
                    'result': 'success',
                    'access': str(refresh.access_token)  # 刷新access
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
            # 如果ROTATE_REFRESH_TOKENS不为true则不需要刷新refresh
            return Response({
                'result': 'success',
                'access': str(refresh.access_token)
            })
        except:
            return Response({
                'result': 'resfresh_token过期了'
            }, status = 401)