from django_extensions.db.models import TitleDescriptionModel
from django.db.models import DateField


class Holiday(TitleDescriptionModel):
    from_date = DateField()
    to_date = DateField()

    def __str__(self):
        return self.title
