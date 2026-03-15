from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password
from .models import User, Country, City, Hotel, Restaurant, Activity, Monument, TravelPlan, Recommendation, Favorite

# ─── Auth ─────────────────────────────────────────────────────────────────────
class RegisterSerializer(serializers.ModelSerializer):
    password  = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model  = User
        fields = ['email', 'name', 'password', 'password2']

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({'password': 'Passwords do not match'})
        return attrs

    def create(self, validated_data):
        validated_data.pop('password2')
        user = User.objects.create_user(**validated_data)
        return user

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model  = User
        fields = ['id', 'email', 'name', 'phone', 'bio', 'location',
                  'avatar', 'budget', 'travel_type', 'duration',
                  'interests', 'is_admin', 'created_at']
        read_only_fields = ['id', 'created_at']

class UpdateProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model  = User
        fields = ['name', 'phone', 'bio', 'location', 'avatar',
                  'budget', 'travel_type', 'duration', 'interests']

# ─── Country ──────────────────────────────────────────────────────────────────
class CountrySerializer(serializers.ModelSerializer):
    cities_count = serializers.SerializerMethodField()

    class Meta:
        model  = Country
        fields = '__all__'

    def get_cities_count(self, obj):
        return obj.cities.filter(is_active=True).count()

# ─── City ─────────────────────────────────────────────────────────────────────
class CitySerializer(serializers.ModelSerializer):
    country_name = serializers.CharField(source='country.name', read_only=True)
    country_flag = serializers.CharField(source='country.flag', read_only=True)

    class Meta:
        model  = City
        fields = '__all__'

class CityDetailSerializer(serializers.ModelSerializer):
    country      = CountrySerializer(read_only=True)
    hotels       = serializers.SerializerMethodField()
    restaurants  = serializers.SerializerMethodField()
    activities   = serializers.SerializerMethodField()
    monuments    = serializers.SerializerMethodField()

    class Meta:
        model  = City
        fields = '__all__'

    def get_hotels(self, obj):
        return HotelSerializer(obj.hotels.filter(is_active=True)[:5], many=True).data

    def get_restaurants(self, obj):
        return RestaurantSerializer(obj.restaurants.filter(is_active=True)[:5], many=True).data

    def get_activities(self, obj):
        return ActivitySerializer(obj.activities.filter(is_active=True)[:5], many=True).data

    def get_monuments(self, obj):
        return MonumentSerializer(obj.monuments.filter(is_active=True)[:5], many=True).data

# ─── Hotel ────────────────────────────────────────────────────────────────────
class HotelSerializer(serializers.ModelSerializer):
    city_name = serializers.CharField(source='city.name', read_only=True)

    class Meta:
        model  = Hotel
        fields = '__all__'

# ─── Restaurant ───────────────────────────────────────────────────────────────
class RestaurantSerializer(serializers.ModelSerializer):
    city_name = serializers.CharField(source='city.name', read_only=True)

    class Meta:
        model  = Restaurant
        fields = '__all__'

# ─── Activity ─────────────────────────────────────────────────────────────────
class ActivitySerializer(serializers.ModelSerializer):
    city_name = serializers.CharField(source='city.name', read_only=True)

    class Meta:
        model  = Activity
        fields = '__all__'

# ─── Monument ─────────────────────────────────────────────────────────────────
class MonumentSerializer(serializers.ModelSerializer):
    city_name = serializers.CharField(source='city.name', read_only=True)

    class Meta:
        model  = Monument
        fields = '__all__'

# ─── TravelPlan ───────────────────────────────────────────────────────────────
class TravelPlanSerializer(serializers.ModelSerializer):
    user_name = serializers.CharField(source='user.name', read_only=True)
    cities    = CitySerializer(many=True, read_only=True)
    city_ids  = serializers.PrimaryKeyRelatedField(
        many=True, queryset=City.objects.all(), source='cities', write_only=True)

    class Meta:
        model  = TravelPlan
        fields = '__all__'
        read_only_fields = ['user', 'created_at', 'updated_at']

# ─── Recommendation ───────────────────────────────────────────────────────────
class RecommendationSerializer(serializers.ModelSerializer):
    city = CitySerializer(read_only=True)

    class Meta:
        model  = Recommendation
        fields = '__all__'

# ─── Favorite ─────────────────────────────────────────────────────────────────
class FavoriteSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Favorite
        fields = '__all__'
        read_only_fields = ['user', 'created_at']