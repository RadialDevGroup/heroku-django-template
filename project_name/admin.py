from django.contrib import admin


class {{ project_name|capfirst }}AdminSite(admin.AdminSite):
    site_header = '{{ project_name|capfirst }} Admin'
