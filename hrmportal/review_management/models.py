from django.db.models import DateField, ForeignKey, CASCADE, IntegerField, TextField
from django_extensions.db.models import TimeStampedModel
from review_management.utils.constants import ReviewChoices

# Create your models here.


class ReviewBase(TimeStampedModel):
    created = DateField()
    user = ForeignKey("user_management.User", on_delete=CASCADE, related_name="reviews")

    class Meta:
        abstract = True


class Review(ReviewBase):
    performance_rating = IntegerField(choices=ReviewChoices.get_choices)
    performance_comment = TextField(null=True, blank=True)
    delivery_rating = IntegerField(choices=ReviewChoices.get_choices)
    delivery_comment = TextField(null=True, blank=True)
    socialization_rating = IntegerField(choices=ReviewChoices.get_choices)
    socialization_comment = TextField(null=True, blank=True)

    def __str__(self):
        return "%s Review %s" % (self.user, self.created)

    @property
    def overall_review(self):
        return "{review:.2f}".format(
            review=(
                self.performance_rating
                + self.delivery_rating
                + self.socialization_rating
            )
            / 3
        )
