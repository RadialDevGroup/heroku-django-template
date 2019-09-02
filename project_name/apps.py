from django.contrib.admin.apps import AdminConfig


class {{ project_name|capfirst }}AdminConfig(AdminConfig):
    default_site = 'ohai.admin.{{ project_name|capfirst }}AdminSite'
    