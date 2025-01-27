from django_extensions.db.models import ActivatorModel
from django.db.models import CharField, ForeignKey, CASCADE
from cities_light.models import City
from organization_management.utils.constants import VerboseConstants


class Organization(ActivatorModel):
    name = CharField(max_length=255)
    full_name = CharField(max_length=1024, blank=True, null=True)
    city = ForeignKey(City, on_delete=CASCADE)

    class Meta:
        verbose_name = VerboseConstants.ORGANIZATION
        verbose_name_plural = VerboseConstants.ORGANIZATIONS
        ordering = ["name"]
        unique_together = ("name", "city")

    def __str__(self):
        return self.name

    @property
    def is_active(self):
        return self.status == ActivatorModel.ACTIVE_STATUS


class Technology(ActivatorModel):
    name = CharField(max_length=255, unique=True)
    organization = ForeignKey(Organization, on_delete=CASCADE)

    class Meta:
        verbose_name = VerboseConstants.TECHNOLOGY
        verbose_name_plural = VerboseConstants.TECHNOLOGIES
        ordering = ["name"]
        unique_together = ("name", "organization")

    def __str__(self):
        return self.name


class Department(ActivatorModel):
    name = CharField(max_length=255, unique=True)

    class Meta:
        verbose_name = VerboseConstants.DEPARTMENT
        verbose_name_plural = VerboseConstants.DEPARTMENTS
        ordering = ["name"]

    def __str__(self):
        return self.name


class Designation(ActivatorModel):
    name = CharField(max_length=255, unique=True)
    department = ForeignKey(Department, on_delete=CASCADE)

    class Meta:
        verbose_name = VerboseConstants.DESIGNATION
        verbose_name_plural = VerboseConstants.DESIGNATIONS

    def __str__(self):
        return self.name
