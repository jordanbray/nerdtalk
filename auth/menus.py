from django.core.urlresolvers import reverse
from menu import Menu, MenuItem

children = (MenuItem("Log In", reverse("auth.views.login")),)

Menu.add_item("main", MenuItem("Auth", reverse("auth.views.home"), children=children))

