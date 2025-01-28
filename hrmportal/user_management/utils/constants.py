from django.utils.translation import gettext_lazy as _


class UserGroups:
    ADMIN = "admin"
    ADMIN_EXCEUTIVE = "admin_executive"
    HR_MANAGER = "hr_manager"
    NETWORK_ADMIN = "network_admin"
    HR_EXECUTIVE = "hr_executive"
    HR = "hr"
    TEAM_LEADER = "team_leader"
    PROJECT_MANGER = "project_manager"
    EMPLOYEE = "employee"
    CLIENT = "client"

    @classmethod
    def get_choices(cls) -> tuple:
        return (
            cls.ADMIN,
            cls.ADMIN_EXCEUTIVE,
            cls.HR_MANAGER,
            cls.NETWORK_ADMIN,
            cls.HR_EXECUTIVE,
            cls.HR,
            cls.TEAM_LEADER,
            cls.PROJECT_MANGER,
            cls.EMPLOYEE,
            cls.CLIENT,
        )


class VerboseConstants:
    """
    Constants for verbose names of models.
    """

    USER = _("User")
    USERS = _("Users")
    SKILL = _("Skill")
    SKILLS = _("Skills")

    USER_IDENTITY = _("User Identity")
    USER_IDENTITIES = _("User Identities")
    USER_META_DATA = _("User Meta Data")
    USER_META_DATAS = _("User Meta Datas")
    USER_QUALIFICATION = _("User Qualification")
    USER_QUALIFICATIONS = _("User Qualifications")
    AGREEMENT = _("Agreement")
    AGREEMENTS = _("Agreements")
    ADDRESS = _("Address")
    ADDRESSES = _("Addresses")
    BANK_DETAIL = _("Bank Detail")
    BANK_DETAILS = _("Bank Details")
    USER_ORGANIZATION_DETAIL = _("User Organization Detail")
    USER_ORGANIZATION_DETAILS = _("User Organization Details")
    USER_REPORTING = _("User Reporting")
