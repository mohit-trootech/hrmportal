from django.apps import AppConfig


class UserManagementConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "user_management"

    def ready(self):
        super().ready()
        import user_management.signals  # noqa
