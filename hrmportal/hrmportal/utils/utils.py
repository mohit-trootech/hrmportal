from utils.base_utils import get_model

Group = get_model(app_label="auth", model_name="Group")
Permission = get_model(app_label="auth", model_name="Permission")


def add_permissions_to_group(group_name: str, permissions: list) -> None:
    """
    Add permissions to a group.
    """
    group = Group.objects.get(name=group_name)
    permissions = Permission.objects.filter(codename__in=permissions)
    group.permissions.add(*permissions)
