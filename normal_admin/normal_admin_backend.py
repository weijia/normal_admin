__author__ = 'weijia'


# noinspection PyMethodMayBeStatic
class NormalAdminBackend(object):
    def has_module_perms(self, user, app_label):
        return True

    def authenticate(self, **kwargs):
        return None
