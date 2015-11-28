from django.core.urlresolvers import reverse
from menu import Menu, MenuItem

Menu.add_item("main", MenuItem("NerdTalk", reverse("nerdtalk.views.home")))

