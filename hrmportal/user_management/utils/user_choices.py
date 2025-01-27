# User Choices Constants
from django.utils.translation import gettext_lazy as _


class GradeTypes:
    CGPA = "cgpa"
    PERCENTAGE = "percentage"

    CHOICES = (
        (CGPA, _("CGPA")),
        (PERCENTAGE, _("Percentage")),
    )

    @classmethod
    def get_choices(cls) -> tuple:
        return cls.CHOICES


class Interviewer:
    YES = 1
    NO = 0
    CHOICES = (
        (YES, _("Yes")),
        (NO, _("No")),
    )

    @classmethod
    def get_choices(cls) -> tuple:
        return cls.CHOICES


class MaritialChoices:
    SINGLE = "single"
    MARRIED = "married"

    CHOICES = (
        (SINGLE, _("Single")),
        (MARRIED, _("Married")),
    )

    @classmethod
    def get_choices(cls) -> tuple:
        return cls.CHOICES


class GenderChoices:
    MALE = "male"
    FEMALE = "female"

    CHOICES = (
        (MALE, _("Male")),
        (FEMALE, _("Female")),
    )

    @classmethod
    def get_choices(cls) -> tuple:
        return cls.CHOICES


class BloodGroupChoices:
    A_POSITIVE = "A+"
    A_NEGATIVE = "A-"
    B_POSITIVE = "B+"
    B_NEGATIVE = "B-"
    O_POSITIVE = "O+"
    O_NEGATIVE = "O-"
    AB_POSITIVE = "AB+"
    AB_NEGATIVE = "AB-"

    CHOICES = (
        (A_POSITIVE, _("A+")),
        (A_NEGATIVE, _("A-")),
        (B_POSITIVE, _("B+")),
        (B_NEGATIVE, _("B-")),
        (O_POSITIVE, _("O+")),
        (O_NEGATIVE, _("O-")),
        (AB_POSITIVE, _("AB+")),
        (AB_NEGATIVE, _("AB-")),
    )

    @classmethod
    def get_choices(cls) -> tuple:
        return cls.CHOICES


class JobStatus:
    OFFERED = "offered"
    PROBATION = "probation"
    CONFIRMED = "confirmed"
    RESIGNED = "resigned"
    TERMINATED = "terminated"
    RELIEVED = "relieved"
    F_AND_F_COMPLETE = "f_and_f_complete"

    CHOICES = (
        (OFFERED, _("Offered")),
        (PROBATION, _("Probation")),
        (CONFIRMED, _("Confirmed")),
        (RESIGNED, _("Resigned")),
        (TERMINATED, _("Terminated")),
        (RELIEVED, _("Relieved")),
        (F_AND_F_COMPLETE, _("F&F Complete")),
    )

    @classmethod
    def get_choices(cls) -> tuple:
        return cls.CHOICES


class UserType:
    PERMANENT = "permanent"
    CONTRACT = "contract"
    INTERN = "intern"
    TRAINEE = "trainee"
    CHOICES = (
        (PERMANENT, _("Permanent")),
        (CONTRACT, _("Contract")),
        (INTERN, _("Intern")),
        (TRAINEE, _("Trainee")),
    )

    @classmethod
    def get_choices(cls) -> tuple:
        return cls.CHOICES
