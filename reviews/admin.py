from django.contrib import admin
from .models import Review


class WordFilter(admin.SimpleListFilter):
    title = "Filter by words!"

    parameter_name = "word"

    def lookups(self, request, model_admin):
        return [
            ("good", "Good"),
            ("great", "Great"),
            ("awesome", "Awesome"),
        ]

    def queryset(self, request, reviews):
        word = self.value()
        if word:
            return reviews.filter(payload__contains=word)
        else:
            reviews


class RatingFilter(admin.SimpleListFilter):
    title = "Filter by rating!"

    parameter_name = "rating"

    def lookups(self, request, model_admin):
        return [
            ("good", "Good Reviews"),
            ("bad", "Bad Reviews"),
        ]

    def queryset(self, request, reviews):
        rating = self.value()
        good_reviews = reviews.filter(rating__gte=3)
        bad_reviews = reviews.filter(rating__lt=3)
        if rating == "good":
            return good_reviews
        elif rating == "bad":
            return bad_reviews
        else:
            reviews


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = (
        "__str__",
        "payload",
    )

    list_filter = (
        WordFilter,
        RatingFilter,
        "rating",
        "user__is_host",
        "room__category",
        "room__pet_friendly",
    )
