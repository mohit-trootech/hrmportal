from django.db.models import ForeignKey, CASCADE, DecimalField, OneToOneField, TextField
from django_extensions.db.models import TimeStampedModel
from salary_management.utils.constants import (
    VerboseConstants,
    AllowanceConstants,
    DeductionsConstants,
)


class Salary(TimeStampedModel):
    user = OneToOneField(
        "user_management.User", on_delete=CASCADE, related_name="salary"
    )
    ctc = DecimalField(
        max_digits=10, decimal_places=2, verbose_name=VerboseConstants.CTC
    )

    class Meta:
        verbose_name = VerboseConstants.SALARY
        verbose_name_plural = VerboseConstants.SALARY
        ordering = ["-created"]

    def __str__(self):
        return str(self.user)


class Allowance(TimeStampedModel):
    salary = ForeignKey(
        "salary_management.Salary", on_delete=CASCADE, related_name="allowances"
    )
    basic = DecimalField(
        max_digits=10, decimal_places=2, verbose_name=AllowanceConstants.BASIC
    )
    hra = DecimalField(
        max_digits=10, decimal_places=2, verbose_name=AllowanceConstants.HRA
    )
    uniform = DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name=AllowanceConstants.UNIFORM_ALLOWANCE,
    )
    transport = DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name=AllowanceConstants.TRANSPORT_ALLOWANCE,
    )
    medical = DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name=AllowanceConstants.MEDICAL_ALLOWANCE,
    )
    conveyance = DecimalField(
        max_digits=10, decimal_places=2, verbose_name=AllowanceConstants.CONVEYANCE
    )
    other = DecimalField(
        max_digits=10, decimal_places=2, verbose_name=AllowanceConstants.OTHER
    )

    class Meta:
        verbose_name = VerboseConstants.ALLOWANCE
        verbose_name_plural = VerboseConstants.ALLOWANCES

    def __str__(self):
        return str(self.salary)


class Deduction(TimeStampedModel):
    esic = DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0.00,
        verbose_name=DeductionsConstants.ESIC,
    )

    gratuity = DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0.00,
        verbose_name=DeductionsConstants.GRATUITY,
    )
    pf = DecimalField(
        max_digits=10, decimal_places=2, verbose_name=DeductionsConstants.PF
    )
    tds = DecimalField(
        max_digits=10, decimal_places=2, verbose_name=DeductionsConstants.TDS
    )
    other = DecimalField(
        max_digits=10, decimal_places=2, verbose_name=DeductionsConstants.OTHER
    )
    salary = ForeignKey(Salary, on_delete=CASCADE, related_name="deductions")

    class Meta:
        verbose_name = VerboseConstants.DEDUCTION
        verbose_name_plural = VerboseConstants.DEDUCTIONS

    def __str__(self):
        return str(self.salary)


class Appraisal(TimeStampedModel):
    user = OneToOneField(
        "user_management.User", on_delete=CASCADE, related_name="appraisal"
    )
    feedback = TextField(blank=True, null=True)
    salary = ForeignKey(
        "salary_management.Salary", on_delete=CASCADE, related_name="appraisals"
    )

    class Meta:
        verbose_name = VerboseConstants.APPRAISAL
        verbose_name_plural = VerboseConstants.APPRAISALS

    def __str__(self):
        return str(self.user)
