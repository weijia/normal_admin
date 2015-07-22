__author__ = 'weijia'
from django.contrib.admin.sites import AdminSite
from django.contrib.admin.forms import AdminAuthenticationForm
from django import forms
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth import authenticate

ERROR_MESSAGE = _("Please enter the correct username and password "
                  "for a staff account. Note that both fields are case-sensitive.")


class UserAdminAuthenticationForm(AdminAuthenticationForm):
    """
    Same as Django's AdminAuthenticationForm but allows to login
    any user who is not staff.
    """

    def clean(self):
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


class UserAdmin(AdminSite):
    # Anything we wish to add or override
    login_form = UserAdminAuthenticationForm

    def has_permission(self, request):
        return request.user.is_active
