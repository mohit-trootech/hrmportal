from django.contrib.admin import site
from organization_management.models import (
    Organization,
    Technology,
    Department,
    Designation,
)

site.register(Organization)
site.register(Technology)
site.register(Department)
site.register(Designation)
