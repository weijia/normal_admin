from django.contrib.admin.sites import AdminSite
from django.contrib.admin.forms import AdminAuthenticationForm
from django import forms
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth import authenticate

__author__ = 'weijia'

ERROR_MESSAGE = _("Please enter the correct username and password "
                  "for a staff account. Note that both fields are case-sensitive.")


class UserAdminAuthenticationForm(AdminAuthenticationForm):
    """
    Same as Django's AdminAuthenticationForm but allows to login
    any user who is not staff.
    """
    def clean(self):
        try:
            return super(UserAdminAuthenticationForm, self).clean()
        except:
            username = self.cleaned_data.get('username')
            password = self.cleaned_data.get('password')
            message = ERROR_MESSAGE

            if username and password:
                try:
                    self.user_cache = authenticate(username=username, password=password)
                except:
                    # The following is for userena as it uses different param
                    self.user_cache = authenticate(identification=username, password=password)
                if self.user_cache is None:
                    raise forms.ValidationError(message)
                elif not self.user_cache.is_active:
                    raise forms.ValidationError(message)
            self.check_for_test_cookie()
            return self.cleaned_data

    # For Django 1.8
    def confirm_login_allowed(self, user):
        if not user.is_active:
            raise forms.ValidationError(
                    self.error_messages['invalid_login'],
                    code='invalid_login',
                    params={'username': self.username_field.verbose_name}
            )


class UserAdmin(AdminSite):
    # Anything we wish to add or override
    login_form = UserAdminAuthenticationForm

    def has_permission(self, request):
        return request.user.is_active
