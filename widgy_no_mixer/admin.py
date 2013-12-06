from django.contrib import admin

from widgy.admin import WidgyAdmin

from widgy_no_mixer.models import TestModel


admin.site.register(TestModel, WidgyAdmin)
