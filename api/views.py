from rest_framework import generics, status, permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from django.db.models import Q
from .models import User, Country, City, Hotel, Restaurant, Activity, Monument, TravelPlan, Recommendation, Favorite
from .serializers import (
    RegisterSerializer, UserSerializer, UpdateProfileSerializer,
    CountrySerializer, CitySerializer, CityDetailSerializer,
    HotelSerializer, RestaurantSerializer, ActivitySerializer,
    MonumentSerializer, TravelPlanSerializer, RecommendationSerializer,
    FavoriteSerializer
)
from .recommendation import get_recommendations


class RegisterView(APIView):
    permission_classes = [permissions.AllowAny]
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            refresh = RefreshToken.for_user(user)
            return Response({
                'user': UserSerializer(user).data,
                'access': str(refresh.access_token),
                'refresh': str(refresh)
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):
    permission_classes = [permissions.AllowAny]
    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')
        user = authenticate(request, username=email, password=password)
        if user:
            if not user.is_active:
                return Response({'error': 'Account is disabled'}, status=status.HTTP_403_FORBIDDEN)
            refresh = RefreshToken.for_user(user)
            return Response({
                'user': UserSerializer(user).data,
                'access': str(refresh.access_token),
                'refresh': str(refresh)
            })
        return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)


class LogoutView(APIView):
    def post(self, request):
        try:
            token = RefreshToken(request.data.get('refresh'))
            token.blacklist()
            return Response({'message': 'Logged out successfully'})
        except Exception:
            return Response({'error': 'Invalid token'}, status=status.HTTP_400_BAD_REQUEST)


class CheckAuthView(APIView):
    def get(self, request):
        return Response({
            'authenticated': True,
            'user': UserSerializer(request.user).data,
            'has_preferences': bool(request.user.interests)
        })


class ProfileView(APIView):
    def get(self, request):
        return Response(UserSerializer(request.user).data)

    def put(self, request):
        serializer = UpdateProfileSerializer(request.user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(UserSerializer(request.user).data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UploadAvatarView(APIView):
    """Upload avatar as base64 URL or direct URL string"""
    def post(self, request):
        user = request.user
        # Accept URL string directly
        avatar_url = request.data.get('avatar_url')
        if avatar_url:
            user.avatar = avatar_url
            user.save()
            return Response({'avatar': user.avatar, 'user': UserSerializer(user).data})

        # Accept file upload — convert to base64 and store as data URL
        if 'avatar' in request.FILES:
            import base64
            image_file = request.FILES['avatar']
            image_data = image_file.read()
            base64_data = base64.b64encode(image_data).decode('utf-8')
            content_type = image_file.content_type or 'image/jpeg'
            data_url = f'data:{content_type};base64,{base64_data}'
            user.avatar = data_url
            user.save()
            return Response({'avatar': user.avatar, 'user': UserSerializer(user).data})

        return Response({'error': 'No image provided'}, status=status.HTTP_400_BAD_REQUEST)


class SavePreferencesView(APIView):
    def post(self, request):
        user = request.user
        user.interests   = request.data.get('interests',   user.interests)
        user.budget      = request.data.get('budget',      user.budget)
        user.travel_type = request.data.get('travel_type', user.travel_type)
        user.duration    = request.data.get('duration',    user.duration)
        user.location    = request.data.get('location',    user.location)
        user.save()
        get_recommendations(user)
        return Response({'message': 'Preferences saved', 'user': UserSerializer(user).data})


class CountryListView(generics.ListAPIView):
    serializer_class = CountrySerializer
    permission_classes = [permissions.AllowAny]
    def get_queryset(self):
        qs = Country.objects.filter(is_active=True)
        q = self.request.query_params.get('q')
        if q:
            qs = qs.filter(Q(name__icontains=q) | Q(continent__icontains=q))
        continent = self.request.query_params.get('continent')
        if continent:
            qs = qs.filter(continent__icontains=continent)
        return qs


class CountryDetailView(generics.RetrieveAPIView):
    queryset = Country.objects.filter(is_active=True)
    serializer_class = CountrySerializer
    permission_classes = [permissions.AllowAny]


class CityListView(generics.ListAPIView):
    serializer_class = CitySerializer
    permission_classes = [permissions.AllowAny]
    def get_queryset(self):
        qs = City.objects.filter(is_active=True)
        q = self.request.query_params.get('q')
        if q:
            qs = qs.filter(
                Q(name__icontains=q) |
                Q(tag__icontains=q) |
                Q(country__name__icontains=q) |
                Q(description__icontains=q)
            )
        country = self.request.query_params.get('country')
        if country:
            qs = qs.filter(country__id=country)
        budget = self.request.query_params.get('budget')
        if budget:
            qs = qs.filter(budget_level=budget)
        continent = self.request.query_params.get('continent')
        if continent:
            qs = qs.filter(country__continent__icontains=continent)
        return qs.order_by('-popularity')


class CityDetailView(generics.RetrieveAPIView):
    queryset = City.objects.filter(is_active=True)
    serializer_class = CityDetailSerializer
    permission_classes = [permissions.AllowAny]


class HotelListView(generics.ListAPIView):
    serializer_class = HotelSerializer
    permission_classes = [permissions.AllowAny]
    def get_queryset(self):
        qs = Hotel.objects.filter(is_active=True)
        city = self.request.query_params.get('city')
        if city:
            qs = qs.filter(city__id=city)
        budget = self.request.query_params.get('budget')
        if budget:
            qs = qs.filter(budget_level=budget)
        return qs


class HotelDetailView(generics.RetrieveAPIView):
    queryset = Hotel.objects.filter(is_active=True)
    serializer_class = HotelSerializer
    permission_classes = [permissions.AllowAny]


class RestaurantListView(generics.ListAPIView):
    serializer_class = RestaurantSerializer
    permission_classes = [permissions.AllowAny]
    def get_queryset(self):
        qs = Restaurant.objects.filter(is_active=True)
        city = self.request.query_params.get('city')
        if city:
            qs = qs.filter(city__id=city)
        return qs


class RestaurantDetailView(generics.RetrieveAPIView):
    queryset = Restaurant.objects.filter(is_active=True)
    serializer_class = RestaurantSerializer
    permission_classes = [permissions.AllowAny]


class ActivityListView(generics.ListAPIView):
    serializer_class = ActivitySerializer
    permission_classes = [permissions.AllowAny]
    def get_queryset(self):
        qs = Activity.objects.filter(is_active=True)
        city = self.request.query_params.get('city')
        if city:
            qs = qs.filter(city__id=city)
        category = self.request.query_params.get('category')
        if category:
            qs = qs.filter(category=category)
        return qs


class ActivityDetailView(generics.RetrieveAPIView):
    queryset = Activity.objects.filter(is_active=True)
    serializer_class = ActivitySerializer
    permission_classes = [permissions.AllowAny]


class MonumentListView(generics.ListAPIView):
    serializer_class = MonumentSerializer
    permission_classes = [permissions.AllowAny]
    def get_queryset(self):
        qs = Monument.objects.filter(is_active=True)
        city = self.request.query_params.get('city')
        if city:
            qs = qs.filter(city__id=city)
        return qs


class MonumentDetailView(generics.RetrieveAPIView):
    queryset = Monument.objects.filter(is_active=True)
    serializer_class = MonumentSerializer
    permission_classes = [permissions.AllowAny]


@api_view(['GET'])
@permission_classes([permissions.AllowAny])
def search(request):
    q = request.query_params.get('q', '')
    if not q:
        return Response({'cities': [], 'countries': [], 'hotels': [],
                         'restaurants': [], 'activities': [], 'monuments': []})

    cities = CitySerializer(
        City.objects.filter(
            Q(name__icontains=q) |
            Q(tag__icontains=q) |
            Q(country__name__icontains=q) |
            Q(description__icontains=q),
            is_active=True
        ).order_by('-popularity')[:8],
        many=True
    ).data

    countries = CountrySerializer(
        Country.objects.filter(
            Q(name__icontains=q) |
            Q(capital__icontains=q) |
            Q(continent__icontains=q),
            is_active=True
        )[:5],
        many=True
    ).data

    hotels = HotelSerializer(
        Hotel.objects.filter(
            Q(name__icontains=q) |
            Q(city__name__icontains=q) |
            Q(city__country__name__icontains=q),
            is_active=True
        )[:5],
        many=True
    ).data

    restaurants = RestaurantSerializer(
        Restaurant.objects.filter(
            Q(name__icontains=q) |
            Q(cuisine_type__icontains=q) |
            Q(city__name__icontains=q),
            is_active=True
        )[:5],
        many=True
    ).data

    activities = ActivitySerializer(
        Activity.objects.filter(
            Q(name__icontains=q) |
            Q(category__icontains=q) |
            Q(city__name__icontains=q),
            is_active=True
        )[:5],
        many=True
    ).data

    monuments = MonumentSerializer(
        Monument.objects.filter(
            Q(name__icontains=q) |
            Q(city__name__icontains=q),
            is_active=True
        )[:5],
        many=True
    ).data

    return Response({
        'cities': cities, 'countries': countries, 'hotels': hotels,
        'restaurants': restaurants, 'activities': activities, 'monuments': monuments
    })


@api_view(['GET'])
@permission_classes([permissions.AllowAny])
def nearby(request):
    user_location = request.query_params.get('location', '')
    cities = City.objects.filter(is_active=True).order_by('-popularity')[:6]
    if user_location:
        nearby_first = City.objects.filter(
            Q(country__name__icontains=user_location) |
            Q(country__continent__icontains=user_location),
            is_active=True
        ).order_by('-popularity')[:6]
        if nearby_first.exists():
            cities = nearby_first
    return Response(CitySerializer(cities, many=True).data)


@api_view(['GET'])
def recommendations(request):
    results = get_recommendations(request.user)
    return Response(RecommendationSerializer(results, many=True).data)


@api_view(['POST'])
def generate_trip(request):
    destination = request.data.get('destination')
    budget      = request.data.get('budget', request.user.budget)
    travel_type = request.data.get('travel_type', request.user.travel_type)
    duration    = request.data.get('duration', 7)
    interests   = request.data.get('interests', request.user.interests)
    pace        = request.data.get('pace', 'balanced')
    accommodation = request.data.get('accommodation', 'hotel')
    season      = request.data.get('season', 'any')

    try:
        country = Country.objects.get(name__icontains=destination, is_active=True)
        cities  = City.objects.filter(country=country, is_active=True)
        scored  = []
        for city in cities:
            score = city.popularity * 0.3 + city.rating * 10
            if city.budget_level == budget:
                score += 20
            # Boost cities matching interests
            for interest in interests:
                if interest.lower() in city.tag.lower():
                    score += 15
            scored.append({
                'city': CitySerializer(city).data,
                'score': round(score, 2),
                'activities': ActivitySerializer(
                    city.activities.filter(is_active=True)[:4], many=True).data,
                'hotels': HotelSerializer(
                    city.hotels.filter(is_active=True)[:3], many=True).data,
                'restaurants': RestaurantSerializer(
                    city.restaurants.filter(is_active=True)[:3], many=True).data,
                'monuments': MonumentSerializer(
                    city.monuments.filter(is_active=True)[:3], many=True).data,
            })
        scored.sort(key=lambda x: x['score'], reverse=True)
        return Response({
            'destination': destination,
            'flag': country.flag,
            'budget': budget,
            'duration': duration,
            'travel_type': travel_type,
            'interests': interests,
            'pace': pace,
            'accommodation': accommodation,
            'season': season,
            'cities': scored[:3]
        })
    except Country.DoesNotExist:
        city_results = City.objects.filter(
            Q(name__icontains=destination) |
            Q(country__name__icontains=destination),
            is_active=True
        )[:3]
        if city_results.exists():
            scored = []
            for city in city_results:
                scored.append({
                    'city': CitySerializer(city).data,
                    'score': 100,
                    'activities': ActivitySerializer(
                        city.activities.filter(is_active=True)[:4], many=True).data,
                    'hotels': HotelSerializer(
                        city.hotels.filter(is_active=True)[:3], many=True).data,
                    'restaurants': RestaurantSerializer(
                        city.restaurants.filter(is_active=True)[:3], many=True).data,
                    'monuments': MonumentSerializer(
                        city.monuments.filter(is_active=True)[:3], many=True).data,
                })
            return Response({
                'destination': destination,
                'flag': '',
                'budget': budget,
                'duration': duration,
                'travel_type': travel_type,
                'interests': interests,
                'cities': scored
            })
        return Response({'error': 'Destination not found'}, status=status.HTTP_404_NOT_FOUND)


class TravelPlanListCreateView(generics.ListCreateAPIView):
    serializer_class = TravelPlanSerializer
    def get_queryset(self):
        return TravelPlan.objects.filter(user=self.request.user)
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class TravelPlanDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TravelPlanSerializer
    def get_queryset(self):
        return TravelPlan.objects.filter(user=self.request.user)


class FavoriteListCreateView(generics.ListCreateAPIView):
    serializer_class = FavoriteSerializer
    def get_queryset(self):
        return Favorite.objects.filter(user=self.request.user)
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class FavoriteDeleteView(generics.DestroyAPIView):
    serializer_class = FavoriteSerializer
    def get_queryset(self):
        return Favorite.objects.filter(user=self.request.user)


class AdminUserListView(generics.ListAPIView):
    serializer_class = UserSerializer
    def get_permissions(self):
        return [permissions.IsAdminUser()]
    def get_queryset(self):
        return User.objects.all()


@api_view(['POST'])
@permission_classes([permissions.IsAdminUser])
def toggle_user_block(request, pk):
    try:
        user = User.objects.get(pk=pk)
        user.is_active = not user.is_active
        user.save()
        return Response({'is_active': user.is_active})
    except User.DoesNotExist:
        return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
@permission_classes([permissions.IsAdminUser])
def admin_stats(request):
    return Response({
        'total_users': User.objects.count(),
        'total_countries': Country.objects.count(),
        'total_cities': City.objects.count(),
        'total_plans': TravelPlan.objects.count(),
        'active_users': User.objects.filter(is_active=True).count(),
        'total_favorites': Favorite.objects.count()
    })