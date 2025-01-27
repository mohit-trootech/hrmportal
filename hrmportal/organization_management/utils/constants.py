from django.utils.translation import gettext_lazy as _


class VerboseConstants:
    """
    Constants for verbose names of models.
    """

    ORGANIZATION = _("Organization")
    ORGANIZATIONS = _("Organizations")

    TECHNOLOGY = _("Technology")
    TECHNOLOGIES = _("Technologies")

    DEPARTMENT = _("Department")
    DEPARTMENTS = _("Departments")

    DESIGNATION = _("Designation")
    DESIGNATIONS = _("Designations")


class OrganizationData:
    """Organization Default Data"""

    # Organization Names
    TROOTECH_AHMEDABAD = "trootech_ahmedabad"
    TROOTECH_SURAT = "trootech_surat"
    TROO_INBOUND = "troo_inbound"
    QUIXOM = "quixom"

    # Organization Full Names
    TROOTECH_BUINESS = "Trootech Business Pvt. Ltd."
    QUIXOM_BUINESS = "Quixom Business Pvt. Ltd."
    TROO_INBOUND_BUINESS = "TrooInbound Business Pvt. Ltd."

    # Organization Locations
    TROOTECH_LOCATION_SURAT_GEONAMEID = 1255364
    TROOTECH_LOCATION_AHMEDABAD_GEONAMEID = 1279233
    TROO_INBOUND_LOCATION_AHMEDABAD_GEONAMEID = 1279233
    QUIXOM_LOCATION_AHMEDABAD_GEONAMEID = 1279233

    @classmethod
    def get_choices(cls):
        return (
            (
                cls.TROOTECH_AHMEDABAD,
                cls.TROOTECH_BUINESS,
                cls.TROOTECH_LOCATION_AHMEDABAD_GEONAMEID,
            ),
            (
                cls.TROOTECH_SURAT,
                cls.TROOTECH_BUINESS,
                cls.TROOTECH_LOCATION_SURAT_GEONAMEID,
            ),
            (
                cls.TROO_INBOUND,
                cls.TROO_INBOUND_BUINESS,
                cls.TROO_INBOUND_LOCATION_AHMEDABAD_GEONAMEID,
            ),
            (cls.QUIXOM, cls.QUIXOM_BUINESS, cls.QUIXOM_LOCATION_AHMEDABAD_GEONAMEID),
        )
