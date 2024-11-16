from django.contrib import admin
from WebApp.models import Contact

# changing django admin text
admin.site.site_title = "Admin Dashboard"  # Title in the browser tab
admin.site.site_header = "Chinmay's Portfolio"  # Header in the admin panel
admin.site.index_title = "Admin Dashboard"  # Title on the admin index page


# Register your models here.
admin.site.register(Contact)