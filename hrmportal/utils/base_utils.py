from django.apps.registry import apps
from django.db.models import Model


def get_model(app_label: str, model_name: str) -> Model:
    """
    Get model from app registry.

    :param app_label: The label of the application.
    :param model_name: The name of the model.
    :return: The model class.
    """
    return apps.get_model(app_label=app_label, model_name=model_name)
