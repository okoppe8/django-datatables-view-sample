from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class SampleConfig(AppConfig):
    name = 'sample'
    verbose_name = _("地方自治体一覧")

