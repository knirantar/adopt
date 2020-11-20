from django.contrib import admin
from .models import Animal,AnimalImages,Volunteer,Stories,Contact
# Register your models here.

class AnimalImageAdmin(admin.StackedInline):
    model = AnimalImages

@admin.register(Animal)
class AnimalAdmin(admin.ModelAdmin):
    inlines = [AnimalImageAdmin]

    class Meta:
       model = Animal

class AnimalImageAdmin(admin.ModelAdmin):
    pass

admin.site.register(Volunteer)
admin.site.register(Stories)
admin.site.register(Contact)