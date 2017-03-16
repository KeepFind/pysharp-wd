# coding:utf-8
from pvplus_model.models.user import AppUserProfile


class UserService:
    def get_user(self, userid):
        try:
            return AppUserProfile.objects.get(pk_user=userid)
        except AppUserProfile.DoesNotExist:
            return None
