from django.http import HttpResponseRedirect
from google.appengine.api import users


def check_user(func):
    def _wrapper(request, *args, **kwargs):
        if not users.get_current_user():
            return HttpResponseRedirect(users.create_login_url(request.path))
        else:
            return func(request, *args, **kwargs)

    return _wrapper