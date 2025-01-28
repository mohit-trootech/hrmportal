from request_management.utils.constants import (
    RequestTypes,
    VerboseConstants,
    RequestStatus,
)
from django.db.models import Model, CharField, ForeignKey, CASCADE, TextField
from django_extensions.db.models import TimeStampedModel


class RequestType(Model):
    name = CharField(max_length=255, choices=RequestTypes.get_choices(), unique=True)

    class Meta:
        verbose_name = VerboseConstants.REQUEST_TYPE
        verbose_name_plural = VerboseConstants.REQUEST_TYPES
        ordering = ["name"]

    def __str__(self):
        return self.name


class RequestSubType(Model):
    request_type = ForeignKey(RequestType, on_delete=CASCADE, related_name="sub_types")
    name = CharField(max_length=255)

    class Meta:
        verbose_name = VerboseConstants.REQUEST_SUB_TYPE
        verbose_name_plural = VerboseConstants.REQUEST_SUB_TYPES
        ordering = ["name"]
        unique_together = ["request_type", "name"]

    def __str__(self):
        return self.name


class UserRequest(TimeStampedModel):
    user = ForeignKey(
        "user_management.User", on_delete=CASCADE, related_name="user_request"
    )
    request_type = ForeignKey(
        RequestType, on_delete=CASCADE, related_name="user_request"
    )
    request_sub_type = ForeignKey(
        RequestSubType,
        on_delete=CASCADE,
        related_name="user_request",
        blank=True,
        null=True,
    )
    description = TextField(null=True, blank=True)
    status = CharField(
        max_length=64,
        choices=RequestStatus.get_choices(),
        default=RequestStatus.PENDING,
    )

    class Meta:
        verbose_name = VerboseConstants.USER_REQUEST
        verbose_name_plural = VerboseConstants.USER_REQUESTS
        ordering = ["-created"]

    def __str__(self):
        return "%s's %s" % (self.user, self.request_type)
