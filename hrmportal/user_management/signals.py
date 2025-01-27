from django.dispatch import receiver
from hrmportal.utils.utils import get_model
from django.db.models.signals import post_save


UserMetaData = get_model(app_label="user_management", model_name="UserMetaData")
UserIdentity = get_model(app_label="user_management", model_name="UserIdentity")
User = get_model(app_label="user_management", model_name="User")
Group = get_model(app_label="auth", model_name="Group")


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    """
    create_user_profile This function creates a user profile when a new user is created.
    """
    if created:
        UserMetaData.objects.create(user=instance)
        UserIdentity.objects.create(user=instance)
        instance.groups.add(Group.objects.get(name="employee"))
