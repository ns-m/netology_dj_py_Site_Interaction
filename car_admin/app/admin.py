from django.contrib import admin

from .models import Car, Review
from .forms import ReviewAdminForm


class CarAdmin(admin.ModelAdmin):
    fields = [('brand', 'model')]  # поля для формы редактирования
    exclude = ['']  # скрываемые поля
    list_display = ['brand', 'model', 'review_count']  # отображаемые колонки
    list_filter = ['brand']  # колонки для фильтра
    search_fields = ['model']  # поля для поиска
    ordering = ['-id']  # сортировка по-умолчанию

    def review_count(self, data):
        review = Review.objects.filter(car=data.id).count()
        return review



class ReviewAdmin(admin.ModelAdmin):
    form = ReviewAdminForm
    list_display = ['title', 'car']


admin.site.register(Car, CarAdmin)
admin.site.register(Review, ReviewAdmin)
