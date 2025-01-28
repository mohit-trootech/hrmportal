from django.utils.translation import gettext_lazy as _


class ReviewChoices:
    POOR = 1
    BELOW_AVERAGE = 2
    AVERAGE = 3
    GOOD = 4
    EXCELLENT = 5

    CHOICES = (
        (POOR, _("Poor")),
        (BELOW_AVERAGE, _("Below Average")),
        (AVERAGE, _("Average")),
        (GOOD, _("Good")),
        (EXCELLENT, _("Excellent")),
    )

    @classmethod
    def get_choices(cls):
        return cls.CHOICES
