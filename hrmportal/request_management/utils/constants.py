from django.utils.translation import gettext_lazy as _


class VerboseConstants:
    REQUEST_TYPE = _("Request Type")
    REQUEST_TYPES = _("Request Types")

    REQUEST_SUB_TYPE = _("Request Sub Type")
    REQUEST_SUB_TYPES = _("Request Sub Types")

    USER_REQUEST = _("User Request")
    USER_REQUESTS = _("User Requests")


class RequestTypes:
    INFRA_REQUEST = "infra_request"
    HR_REQUEST = "hr_request"
    ADMIN_REQUEST = "admin_request"

    CHOICES = (
        (INFRA_REQUEST, _("Infra Request")),
        (HR_REQUEST, _("HR Request")),
        (ADMIN_REQUEST, _("Admin Request")),
    )

    @classmethod
    def get_choices(cls):
        return cls.CHOICES


class RequestStatus:
    PENDING = "pending"
    APPROVED = "approved"
    REJECTED = "rejected"

    CHOICES = (
        (PENDING, _("Pending")),
        (APPROVED, _("Approved")),
        (REJECTED, _("Rejected")),
    )

    @classmethod
    def get_choices(cls):
        return cls.CHOICES
