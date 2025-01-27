from django.contrib.auth.models import AbstractUser
from django.db.models import (
    Model,
    CharField,
    ForeignKey,
    CASCADE,
    ImageField,
    TextField,
    OneToOneField,
    ManyToManyField,
    DateField,
)
from user_management.utils.constants import VerboseConstants
from user_management.utils.user_choices import (
    MaritialChoices,
    GenderChoices,
    BloodGroupChoices,
    JobStatus,
    UserType,
    Interviewer,
    GradeTypes,
)
from phonenumber_field.modelfields import PhoneNumberField
from django_extensions.db.models import TimeStampedModel


def profile_upload_to(instance, filename):
    return f"images/{instance.user}/{filename}"


def user_qualification_certificate(instance, filename):
    return f"images/{instance.user}/qualification/{filename}"


def user_aggrement(instance, filename):
    return f"images/{instance.user}/agreement/{filename}"


class Skill(Model):
    name = CharField(max_length=255, unique=True)
    technology = ForeignKey("organization_management.Technology", on_delete=CASCADE)

    class Meta:
        verbose_name = VerboseConstants.SKILL
        verbose_name_plural = VerboseConstants.SKILLS
        ordering = ["name"]

    def __str__(self):
        return self.name


class Agreement(TimeStampedModel):
    user = OneToOneField("user_management.UserOrganizationDetail", on_delete=CASCADE)
    agreement = ImageField(upload_to=user_aggrement)

    class Meta:
        verbose_name = VerboseConstants.AGREEMENT
        verbose_name_plural = VerboseConstants.AGREEMENTS

    def __str__(self):
        return self.agreement.url


class Address(Model):
    address = TextField()
    landmark = TextField(blank=True, null=True)
    city = ForeignKey("cities_light.City", on_delete=CASCADE)

    class Meta:
        verbose_name = VerboseConstants.ADDRESS
        verbose_name_plural = VerboseConstants.ADDRESSES

    def __str__(self):
        return self.address


class UserIdentity(Model):
    user = OneToOneField("user_management.User", on_delete=CASCADE)
    pancard = CharField(max_length=10, blank=True, null=True)
    adharcard = CharField(max_length=12, blank=True, null=True)
    voterid = CharField(max_length=10, blank=True, null=True)
    passport = CharField(max_length=8, blank=True, null=True)
    driving_license = CharField(max_length=15, blank=True, null=True)

    class Meta:
        verbose_name = VerboseConstants.USER_IDENTITY
        verbose_name_plural = VerboseConstants.USER_IDENTITIES

    def __str__(self):
        return self.user.email


class UserMetaData(Model):
    user = OneToOneField("user_management.User", on_delete=CASCADE)
    gender = CharField(
        max_length=255, choices=GenderChoices.get_choices(), blank=True, null=True
    )
    maritial_status = CharField(
        max_length=255, choices=MaritialChoices.get_choices(), blank=True, null=True
    )
    date_of_birth = DateField(blank=True, null=True)
    phone_number = PhoneNumberField(region="IN", blank=True, null=True)
    emergency_number = PhoneNumberField(region="IN", blank=True, null=True)
    blood_group = CharField(
        max_length=3, choices=BloodGroupChoices.get_choices(), blank=True, null=True
    )

    class Meta:
        verbose_name = VerboseConstants.USER_META_DATA
        verbose_name_plural = VerboseConstants.USER_META_DATAS

    def __str__(self):
        return self.user.email


class BankDetail(Model):
    user = OneToOneField("user_management.User", on_delete=CASCADE)
    bank_name = CharField(max_length=255)
    account_number = CharField(max_length=20)
    ifsc_code = CharField(max_length=11)
    branch = CharField(max_length=255)
    account_holder_name = CharField(max_length=255)

    class Meta:
        verbose_name = VerboseConstants.BANK_DETAIL
        verbose_name_plural = VerboseConstants.BANK_DETAILS

    def __str__(self):
        return self.user.email


class UserOrganizationDetail(Model):
    user = OneToOneField("user_management.User", on_delete=CASCADE, related_name=None)
    employee_code = CharField(max_length=4, blank=True, null=True)
    organization = ForeignKey("organization_management.Organization", on_delete=CASCADE)
    department = ForeignKey("organization_management.Department", on_delete=CASCADE)
    designation = ForeignKey("organization_management.Designation", on_delete=CASCADE)
    job_status = CharField(
        max_length=255, choices=JobStatus.get_choices(), blank=True, null=True
    )
    user_type = CharField(
        max_length=255, choices=UserType.get_choices(), blank=True, null=True
    )
    joining_date = DateField(blank=True, null=True)
    is_interviewer = CharField(
        max_length=255, blank=True, null=True, default=Interviewer.NO
    )
    skills = ManyToManyField(Skill, blank=True)
    reporting_manager = ForeignKey(
        "user_management.User",
        on_delete=CASCADE,
        blank=True,
        null=True,
        related_name="reporting_manager",
    )

    class Meta:
        verbose_name = VerboseConstants.USER_ORGANIZATION_DETAIL
        verbose_name_plural = VerboseConstants.USER_ORGANIZATION_DETAILS

    def __str__(self):
        return self.user.email


class UserQualification(Model):
    user = OneToOneField("user_management.User", on_delete=CASCADE)
    degree = CharField(max_length=255)
    college = CharField(max_length=255)
    university = CharField(max_length=255)
    passing_year = DateField(blank=True, null=True)
    grade = CharField(max_length=5, blank=True, null=True)
    grade_type = CharField(
        max_length=12, blank=True, null=True, choices=GradeTypes.get_choices()
    )
    certificate = ImageField(
        upload_to=user_qualification_certificate, blank=True, null=True
    )

    class Meta:
        verbose_name = VerboseConstants.USER_QUALIFICATION
        verbose_name_plural = VerboseConstants.USER_QUALIFICATIONS

    def __str__(self):
        return self.user.email


class User(AbstractUser):
    email = CharField(max_length=255, unique=True)
    image = ImageField(upload_to=profile_upload_to, blank=True, null=True)
    present_address = OneToOneField(
        "user_management.Address",
        on_delete=CASCADE,
        related_name="present_address",
        null=True,
        blank=True,
    )
    permanent_address = OneToOneField(
        "user_management.Address",
        on_delete=CASCADE,
        related_name="permanent_address",
        null=True,
        blank=True,
    )
    skills = ManyToManyField(Skill, blank=True)
    created_by = ForeignKey(
        "self", on_delete=CASCADE, related_name="created_users", null=True, blank=True
    )

    class Meta:
        verbose_name = VerboseConstants.USER
        verbose_name_plural = VerboseConstants.USERS

    def __str__(self):
        return self.email
