from django.contrib.admin.apps import AdminConfig


class {{ project_name|capfirst }}AdminConfig(AdminConfig):
    default_site = '{{ project_name }}.admin.{{ project_name|capfirst }}AdminSite'
