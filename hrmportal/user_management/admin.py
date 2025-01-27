from django.contrib.admin import site
from user_management.models import (
    User,
    UserOrganizationDetail,
    UserMetaData,
    UserQualification,
    UserIdentity,
    BankDetail,
    Address,
    Skill,
    Agreement,
)

site.register(User)
site.register(UserOrganizationDetail)
site.register(UserMetaData)
site.register(UserQualification)
site.register(UserIdentity)
site.register(BankDetail)
site.register(Address)
site.register(Skill)
site.register(Agreement)
