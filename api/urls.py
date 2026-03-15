from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from . import views

urlpatterns = [
    path('auth/register/',    views.RegisterView.as_view(),    name='register'),
    path('auth/login/',       views.LoginView.as_view(),       name='login'),
    path('auth/logout/',      views.LogoutView.as_view(),      name='logout'),
    path('auth/refresh/',     TokenRefreshView.as_view(),      name='token_refresh'),
    path('auth/check/',       views.CheckAuthView.as_view(),   name='check_auth'),

    path('profile/',          views.ProfileView.as_view(),     name='profile'),
    path('profile/avatar/',   views.UploadAvatarView.as_view(),name='upload_avatar'),
    path('profile/preferences/', views.SavePreferencesView.as_view(), name='save_preferences'),

    path('countries/',              views.CountryListView.as_view(),   name='country-list'),
    path('countries/<int:pk>/',     views.CountryDetailView.as_view(), name='country-detail'),
    path('cities/',                 views.CityListView.as_view(),      name='city-list'),
    path('cities/<int:pk>/',        views.CityDetailView.as_view(),    name='city-detail'),
    path('hotels/',                 views.HotelListView.as_view(),     name='hotel-list'),
    path('hotels/<int:pk>/',        views.HotelDetailView.as_view(),   name='hotel-detail'),
    path('restaurants/',            views.RestaurantListView.as_view(),name='restaurant-list'),
    path('restaurants/<int:pk>/',   views.RestaurantDetailView.as_view(), name='restaurant-detail'),
    path('activities/',             views.ActivityListView.as_view(),  name='activity-list'),
    path('activities/<int:pk>/',    views.ActivityDetailView.as_view(),name='activity-detail'),
    path('monuments/',              views.MonumentListView.as_view(),  name='monument-list'),
    path('monuments/<int:pk>/',     views.MonumentDetailView.as_view(),name='monument-detail'),

    path('search/',           views.search,                    name='search'),
    path('nearby/',           views.nearby,                    name='nearby'),
    path('recommendations/',  views.recommendations,           name='recommendations'),
    path('generate-trip/',    views.generate_trip,             name='generate-trip'),

    path('travel-plans/',         views.TravelPlanListCreateView.as_view(),  name='travel-plan-list'),
    path('travel-plans/<int:pk>/', views.TravelPlanDetailView.as_view(),     name='travel-plan-detail'),
    path('favorites/',            views.FavoriteListCreateView.as_view(),    name='favorite-list'),
    path('favorites/<int:pk>/',   views.FavoriteDeleteView.as_view(),        name='favorite-delete'),

    path('admin/users/',                      views.AdminUserListView.as_view(), name='admin-users'),
    path('admin/users/<int:pk>/toggle-block/', views.toggle_user_block,          name='toggle-block'),
    path('admin/stats/',                      views.admin_stats,                 name='admin-stats'),
]