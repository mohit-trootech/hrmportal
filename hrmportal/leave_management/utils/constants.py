from django.utils.translation import gettext_lazy as _


class VerboseConstants:
    LEAVE = _("Leave")
    LEAVES = _("Leaves")


class LeaveStatus:
    PENDING = "pending"
    REJECTED = "rejected"
    APPROVED = "approved"

    CHOICES = (
        (PENDING, _("Pending")),
        (REJECTED, _("Rejected")),
        (APPROVED, _("Approved")),
    )

    @classmethod
    def get_choices(cls) -> tuple:
        return cls.CHOICES

    FIRST_HALF = "first_half"
    SECOND_HALF = "second_half"
    FULL_DAY = "full_day"

    LEAVE_PERIOD = (
        (FIRST_HALF, _("First Half")),
        (SECOND_HALF, _("Second Half")),
        (FULL_DAY, _("Full Day")),
    )

    @classmethod
    def get_leave_period_choices(cls) -> tuple:
        return cls.LEAVE_PERIOD


class LeaveTypes:
    CASUAL = "casual_leave"
    EMERGENCY = "emergency_leave"

    CHOICES = (
        (CASUAL, _("Casual Leave")),
        (EMERGENCY, _("Emergency Leave")),
    )

    MATERNITY = "maternity_leave"
    MARRIAGE = "marriage_leave"

    SPECIAL_CHOICES = (
        (MATERNITY, _("Maternity Leave")),
        (MARRIAGE, _("Marriage Leave")),
    )

    @classmethod
    def get_special_choices(cls) -> tuple:
        return cls.SPECIAL_CHOICES

    @classmethod
    def get_choices(cls) -> tuple:
        return cls.CHOICES
