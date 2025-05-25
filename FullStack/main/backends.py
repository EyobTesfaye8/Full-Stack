from django.contrib.auth.backends import BaseBackend
from .models import User

class UserBackend(BaseBackend):
    def authenticate(self, request, email = None, password = None, **kwargs):
        user = User.objects.get(email=email)
        try:
            if user.password == password:
                print("yes")
                return user
            else:
                print("no")
                return None
        except user.DoesNotExist:
            print("is not here")
            return None
        
    def get_user_id(self, email):
        userInfo = User.objects.get(email = email)
        return userInfo.id