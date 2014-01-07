from menus.base import NavigationNode
from menus.menu_pool import menu_pool
from django.utils.translation import ugettext_lazy as _
from cms.menu_bases import CMSAttachMenu
from django.core.urlresolvers import reverse


class AllauthMenu(CMSAttachMenu):

    name = _("Allauth Menu")

    def get_nodes(self, request):
        return [
            NavigationNode(_('Sign Up'), reverse('account_signup'), 1, attr={'visible_for_authenticated': False}),
            NavigationNode(_('Login'),   reverse('account_login'),  2, attr={'visible_for_authenticated': False}),
            NavigationNode(_('Logout'),  reverse('account_logout'), 3, attr={'visible_for_anonymous':     False}),
        ]

menu_pool.register_menu(AllauthMenu)
