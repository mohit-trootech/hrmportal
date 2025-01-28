from django.utils.translation import gettext_lazy as _


class VerboseConstants:
    CTC = _("Cost to Cut Salary")

    ALLOWANCE = _("Allowance")
    ALLOWANCES = _("Allowances")

    DEDUCTION = _("Deduction")
    DEDUCTIONS = _("Deductions")

    SALARY = _("Salary")
    APPRAISAL = _("Appraisal")
    APPRAISALS = _("Appraisals")


class AllowanceConstants:

    BASIC = _("Basic Allowance")
    HRA = _("House Rent Allowance")
    UNIFORM_ALLOWANCE = _("Uniform Allowance")
    TRANSPORT_ALLOWANCE = _("Transport Allowance")
    MEDICAL_ALLOWANCE = _("Medical Allowance")
    CONVEYANCE = _("Conveyance Allowance")
    OTHER = _("Other Allowance")


class DeductionsConstants:
    ESIC = _("ESIC")
    GRATUITY = _("Gratuity")
    PF = _("Provident Fund")
    PT = _("Professional Tax")
    OTHER = _("Other Deduction")
    TDS = _("TDS")
