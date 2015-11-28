from django.core.urlresolvers import reverse
from menu import Menu, MenuItem

def logged_in(request):
    if request.user == None:
        return False
    if request.user.is_authenticated():
        return True
    return False

def logged_out(request):
    return not logged_in(request)

children = (MenuItem("Log In",
                     reverse("auth.views.login"),
                     check=lambda request: logged_out(request)),
            MenuItem("Log Out",
                     reverse("auth.views.logout"),
                     check=lambda request: logged_in(request)),
           )

Menu.add_item("main", MenuItem("Auth", reverse("auth.views.home"), children=children))

