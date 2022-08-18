from django.contrib.auth.models import User
from rest_framework.authentication import BasicAuthentication
from rest_framework.exceptions import AuthenticationFailed



class MyAuthentication(BasicAuthentication):
    def authenticate(self, request):
        username = request.GET.get('username')
        if username is None:
            return None
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            raise AuthenticationFailed('No such user!')
        return user, None
