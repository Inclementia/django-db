from django.contrib import admin

from mainapp.models import CategorySight, Sight, RenovatedSight, Reviews

admin.site.register(CategorySight)
admin.site.register(Sight)
admin.site.register(RenovatedSight)
admin.site.register(Reviews)