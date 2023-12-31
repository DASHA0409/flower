from django.contrib import admin
from .models import Advertisement
from django.contrib.auth.views import LoginView


class CustomLoginView(LoginView):
    template_name = 'registration/login.html'


urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
]
class AdvertisementAdmin(admin.ModelAdmin):
    list_display = [
        'id', 'title', 'description', 'price',
        'created_date', 'auction', 'updated_date', 'get_html_image',
    ]

    list_filter = ['auction', 'created_at']
    actions = ['make_auction_as_false', 'make_auction_as_true']

    fieldsets = (
        ('Общее', {
            'fields': ('title', 'description', 'image'),
        }),
        ('Финансы', {
            'fields': ('price', 'auction'),
            'classes': ['collapse']
        })
    )

    @admin.action(description='Убрать возможность торга')
    def make_auction_as_false(self, request, queryset):
        queryset.update(auction=False)

    @admin.action(description='Добавить возможность торга')
    def make_auction_as_true(self, request, queryset):
        queryset.update(auction=True)


admin.site.register(Advertisement, AdvertisementAdmin)
