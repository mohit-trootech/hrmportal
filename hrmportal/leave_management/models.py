from django.db.models import (
    ForeignKey,
    DateField,
    CASCADE,
    CharField,
    OneToOneField,
    BooleanField,
    FileField,
    TextField,
    Model,
    IntegerField,
)
from django_extensions.db.models import TitleDescriptionModel, TimeStampedModel
from leave_management.utils.constants import VerboseConstants, LeaveStatus, LeaveTypes


class Leave(TitleDescriptionModel, TimeStampedModel):
    user = ForeignKey("user_management.User", on_delete=CASCADE, related_name="leaves")
    leave_count = OneToOneField(
        "leave_management.LeaveCount", on_delete=CASCADE, related_name="leave"
    )
    leave_from = DateField()
    leave_to = DateField()
    leave_type = CharField(max_length=20, choices=LeaveTypes.get_choices())
    leave_period = CharField(
        max_length=20, choices=LeaveStatus.get_leave_period_choices()
    )
    status = OneToOneField(
        LeaveStatus,
        on_delete=CASCADE,
    )
    is_special_leave = BooleanField(default=False)
    special_leave = OneToOneField(
        "leave_management.SpecialLeave", on_delete=CASCADE, null=True, blank=True
    )
    attachment = FileField(null=True, blank=True)

    class Meta:
        verbose_name = VerboseConstants.LEAVE
        verbose_name_plural = VerboseConstants.LEAVES

    def __str__(self):
        return "%s's Leave - %s" % (self.user, self.title)


class SpecialLeave:
    special_reason = TextField(null=True, blank=True)
    special_type = CharField(max_length=20, choices=LeaveTypes.get_special_choices())

    def __str__(self):
        return self.leave.user


class LeaveStatus(Model):
    admin_status = CharField(
        max_length=12, choices=LeaveStatus.get_choices(), default=LeaveStatus.PENDING
    )
    tl_status = CharField(
        max_length=12, choices=LeaveStatus.get_choices(), default=LeaveStatus.PENDING
    )
    hr_status = CharField(
        max_length=12, choices=LeaveStatus.get_choices(), default=LeaveStatus.PENDING
    )
    manager_status = CharField(
        max_length=12, choices=LeaveStatus.get_choices(), default=LeaveStatus.PENDING
    )


class LeaveCount(Model):
    casual_leave = IntegerField(default=0)
    emergency_leave = IntegerField(default=0)
