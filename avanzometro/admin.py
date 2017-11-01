from django.contrib import admin
# Import the UserProfile model individually.
from avanzometro.models import UserProfile

# Import the UserProfile model with Category and Page.
# If you choose this option, you'll want to modify the import statement you've already got to include UserProfile.
from avanzometro.models import UserProfile

admin.site.register(UserProfile)
# Register your models here.
