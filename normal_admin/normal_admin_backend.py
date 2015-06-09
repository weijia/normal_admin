from django_auth_ldap.backend import LDAPBackend

__author__ = 'q19420'


class NormalAdminBackend(object):
    def has_module_perms(self, user, app_label):
        return True
