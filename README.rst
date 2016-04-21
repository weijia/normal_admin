=============================
normal_admin
=============================

.. image:: https://badge.fury.io/py/normal_admin.png
    :target: https://badge.fury.io/py/normal_admin

.. image:: https://travis-ci.org/weijia/normal_admin.png?branch=master
    :target: https://travis-ci.org/weijia/normal_admin

.. image:: https://coveralls.io/repos/weijia/normal_admin/badge.png?branch=master
    :target: https://coveralls.io/r/weijia/normal_admin?branch=master

Create admin site without staff role.

Documentation
-------------
The full documentation is not available yet: https://normal_admin.readthedocs.org.


Quickstart
----------

Install normal_admin::

    pip install normal_admin

admin.py::

    from django.contrib.auth.models import User

    from normal_admin.user_admin import UserAdmin

    user_admin_example_site = UserAdmin(name='user_admin_example')

    user_admin_example_site.register(User)

urls.py::

    from django.conf.urls import patterns, include, url
    from admin import user_admin_example_site


    urlpatterns = patterns('',
                           # url(r'^admin/', include(admin.site.urls)),
                           url(r'^', include(user_admin_example_site.urls)),
                           )

Features
--------

* TODO