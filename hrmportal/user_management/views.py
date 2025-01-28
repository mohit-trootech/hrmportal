from django.views.generic import TemplateView
from user_management.utils.constants import Templates


class UsersList(TemplateView):
    template_name = Templates.USER_LIST


user_list_view = UsersList.as_view()
