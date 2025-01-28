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
from leave_management.utils.constants import (
    VerboseConstants,
    LeaveStatusConstants,
    LeaveTypes,
)


class SpecialLeave(Model):
    special_reason = TextField(null=True, blank=True)
    special_type = CharField(max_length=20, choices=LeaveTypes.get_special_choices())

    def __str__(self):
        return self.leave.user


class LeaveStatus(Model):
    admin_status = CharField(
        max_length=12,
        choices=LeaveStatusConstants.get_choices(),
        default=LeaveStatusConstants.PENDING,
    )
    tl_status = CharField(
        max_length=12,
        choices=LeaveStatusConstants.get_choices(),
        default=LeaveStatusConstants.PENDING,
    )
    hr_status = CharField(
        max_length=12,
        choices=LeaveStatusConstants.get_choices(),
        default=LeaveStatusConstants.PENDING,
    )
    manager_status = CharField(
        max_length=12,
        choices=LeaveStatusConstants.get_choices(),
        default=LeaveStatusConstants.PENDING,
    )

    @property
    def current_status(self):
        """
        Leave Status True if any 2 of the above status are APPROVED otherwise REJECTED
        """
        statuses = [
            self.admin_status,
            self.tl_status,
            self.hr_status,
            self.manager_status,
        ]
        return (
            sum(
                [
                    status
                    for status in statuses
                    if status == LeaveStatusConstants.APPROVED
                ]
            )
            >= 2
        )


class Leave(TitleDescriptionModel, TimeStampedModel):
    user = ForeignKey("user_management.User", on_delete=CASCADE, related_name="leaves")
    leave_from = DateField()
    leave_to = DateField()
    leave_type = CharField(max_length=20, choices=LeaveTypes.get_choices())
    leave_period = CharField(
        max_length=20, choices=LeaveStatusConstants.get_leave_period_choices()
    )
    status = OneToOneField(
        "leave_management.LeaveStatus",
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


class LeaveCount(Model):
    user = OneToOneField(
        "user_management.User", on_delete=CASCADE, related_name="leave_count"
    )
    casual_leave = IntegerField(default=0)
    emergency_leave = IntegerField(default=0)

    @property
    def total_leave(self):
        return self.casual_leave + self.emergency_leave

    @property
    def pending_leaves(self):
        return self.user.leaves.filter(status__admin_status=LeaveStatus.PENDING).count()
