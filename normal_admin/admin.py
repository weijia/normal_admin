# from django.contrib import admin
# from django.contrib.auth.models import User
from normal_admin.user_admin import UserAdmin

user_admin_site = UserAdmin(name='usersadmin')
# Run user_admin_site.register() for each model we wish to register
# for our admin interface for users
