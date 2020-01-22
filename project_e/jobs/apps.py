from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _

class JobsConfig(AppConfig):
    name = 'project_e.jobs'
    verbose_name = _("Jobs")
