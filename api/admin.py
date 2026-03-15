from django.contrib import admin
from .models import User, Country, City, Hotel, Restaurant, Activity, Monument, TravelPlan, Recommendation, Favorite

admin.site.register(User)
admin.site.register(Country)
admin.site.register(City)
admin.site.register(Hotel)
admin.site.register(Restaurant)
admin.site.register(Activity)
admin.site.register(Monument)
admin.site.register(TravelPlan)
admin.site.register(Recommendation)
admin.site.register(Favorite)