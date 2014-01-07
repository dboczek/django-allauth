from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool
from django.utils.translation import ugettext_lazy as _
from allauth.cms_menu import AllauthMenu


class AllauthApp(CMSApp):
    name = _("Allauth App")
    urls = ['allauth.urls']
    menus = [AllauthMenu]

apphook_pool.register(AllauthApp)
