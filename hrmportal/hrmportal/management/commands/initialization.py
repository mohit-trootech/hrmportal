from utils.base_utils import get_model
from django.core.management.base import BaseCommand
from organization_management.utils.constants import OrganizationData
from user_management.utils.constants import UserGroups
from django.db import IntegrityError
from hrmportal.utils.utils import add_permissions_to_group
from django.db import transaction

Organization = get_model(app_label="organization_management", model_name="Organization")
Group = get_model(app_label="auth", model_name="Group")
City = get_model(app_label="cities_light", model_name="City")
Permission = get_model(app_label="auth", model_name="Permission")


def create_deafult_user_groups():
    """
    Create default user groups.
    """
    groups = []
    for group_name in UserGroups.get_choices():
        groups.append(Group(name=group_name))
    Group.objects.bulk_create(groups)


def create_default_organization() -> None:
    """
    Create default organization data.
    """
    organizations = []
    for organization in OrganizationData.get_choices():
        name, full_name, geoname_id = organization
        city = City.objects.get(geoname_id=geoname_id)
        organizations.append(Organization(name=name, full_name=full_name, city=city))
    Organization.objects.bulk_create(organizations)


class Command(BaseCommand):
    help = "Initialize the database with default data."

    def handle(self, *args, **options):
        try:
            with transaction.atomic():
                create_default_organization()
                create_deafult_user_groups()
                add_permissions_to_group(
                    UserGroups.ADMIN,
                    [*Permission.objects.values_list("codename", flat=True)],
                )
            self.stdout.write(
                self.style.SUCCESS("Successfully initialized the database.")
            )
        except IntegrityError as ie:
            self.stdout.write(
                self.style.WARNING(
                    f"Failed to initialize the database. Data already exists.\n{ie}"
                )
            )
        except Exception as e:
            raise e
