from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

# ─── User Manager ─────────────────────────────────────────────────────────────
class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('Email is required')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)

# ─── User ─────────────────────────────────────────────────────────────────────
class User(AbstractBaseUser, PermissionsMixin):
    BUDGET_CHOICES = [
        ('economique', 'Économique'),
        ('moyen',      'Moyen'),
        ('eleve',      'Élevé'),
    ]
    TRAVEL_TYPE_CHOICES = [
        ('solo',    'Solo'),
        ('couple',  'Couple'),
        ('famille', 'Famille'),
        ('amis',    'Amis'),
    ]
    DURATION_CHOICES = [
        ('court', 'Court'),
        ('moyen', 'Moyen'),
        ('long',  'Long'),
    ]

    email         = models.EmailField(unique=True)
    name          = models.CharField(max_length=100)
    phone         = models.CharField(max_length=20, blank=True)
    bio           = models.TextField(blank=True)
    location      = models.CharField(max_length=100, blank=True)
    avatar        = models.ImageField(upload_to='avatars/', null=True, blank=True)

    # Preferences
    budget        = models.CharField(max_length=20, choices=BUDGET_CHOICES, default='moyen')
    travel_type   = models.CharField(max_length=20, choices=TRAVEL_TYPE_CHOICES, default='solo')
    duration      = models.CharField(max_length=20, choices=DURATION_CHOICES, default='moyen')
    interests     = models.JSONField(default=list, blank=True)  # ['Culture', 'Nature', ...]

    is_active     = models.BooleanField(default=True)
    is_staff      = models.BooleanField(default=False)
    is_admin      = models.BooleanField(default=False)
    created_at    = models.DateTimeField(auto_now_add=True)
    updated_at    = models.DateTimeField(auto_now=True)

    objects = UserManager()

    USERNAME_FIELD  = 'email'
    REQUIRED_FIELDS = ['name']

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'User'
        ordering = ['-created_at']

# ─── Country ──────────────────────────────────────────────────────────────────
class Country(models.Model):
    name        = models.CharField(max_length=100)
    flag        = models.CharField(max_length=10)
    capital     = models.CharField(max_length=100)
    language    = models.CharField(max_length=100)
    currency    = models.CharField(max_length=50)
    climate     = models.CharField(max_length=100)
    continent   = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    best_season = models.CharField(max_length=100, blank=True)
    avg_daily   = models.CharField(max_length=50, blank=True)
    visa_type   = models.CharField(max_length=100, blank=True)
    population  = models.IntegerField(default=0)
    rating      = models.FloatField(default=0.0)
    image       = models.ImageField(upload_to='countries/', null=True, blank=True)
    is_active   = models.BooleanField(default=True)
    created_at  = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Countries'
        ordering = ['name']

# ─── City ─────────────────────────────────────────────────────────────────────
class City(models.Model):
    country     = models.ForeignKey(Country, on_delete=models.CASCADE, related_name='cities')
    name        = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    image       = models.ImageField(upload_to='cities/', null=True, blank=True)
    rating      = models.FloatField(default=0.0)
    popularity  = models.IntegerField(default=0)
    budget_level= models.CharField(max_length=20, choices=[
        ('economique','Économique'), ('moyen','Moyen'), ('eleve','Élevé')
    ], default='moyen')
    tag         = models.CharField(max_length=50, blank=True)
    is_active   = models.BooleanField(default=True)
    created_at  = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name}, {self.country.name}"

    class Meta:
        verbose_name_plural = 'Cities'
        ordering = ['-popularity']

# ─── Hotel ────────────────────────────────────────────────────────────────────
class Hotel(models.Model):
    city        = models.ForeignKey(City, on_delete=models.CASCADE, related_name='hotels')
    name        = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    image       = models.ImageField(upload_to='hotels/', null=True, blank=True)
    stars       = models.IntegerField(default=3)
    price_per_night = models.DecimalField(max_digits=10, decimal_places=2)
    rating      = models.FloatField(default=0.0)
    address     = models.CharField(max_length=255, blank=True)
    amenities   = models.JSONField(default=list, blank=True)  # ['WiFi', 'Pool', ...]
    budget_level= models.CharField(max_length=20, choices=[
        ('economique','Économique'), ('moyen','Moyen'), ('eleve','Élevé')
    ], default='moyen')
    is_active   = models.BooleanField(default=True)
    created_at  = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.city.name}"

    class Meta:
        ordering = ['-rating']

# ─── Restaurant ───────────────────────────────────────────────────────────────
class Restaurant(models.Model):
    city         = models.ForeignKey(City, on_delete=models.CASCADE, related_name='restaurants')
    name         = models.CharField(max_length=200)
    description  = models.TextField(blank=True)
    image        = models.ImageField(upload_to='restaurants/', null=True, blank=True)
    cuisine_type = models.CharField(max_length=100)
    avg_price    = models.DecimalField(max_digits=10, decimal_places=2)
    rating       = models.FloatField(default=0.0)
    address      = models.CharField(max_length=255, blank=True)
    opening_hours= models.CharField(max_length=100, blank=True)
    budget_level = models.CharField(max_length=20, choices=[
        ('economique','Économique'), ('moyen','Moyen'), ('eleve','Élevé')
    ], default='moyen')
    is_active    = models.BooleanField(default=True)
    created_at   = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.city.name}"

    class Meta:
        ordering = ['-rating']

# ─── Activity ─────────────────────────────────────────────────────────────────
class Activity(models.Model):
    CATEGORY_CHOICES = [
        ('culture',     'Culture'),
        ('nature',      'Nature'),
        ('gastronomie', 'Gastronomie'),
        ('shopping',    'Shopping'),
        ('sport',       'Sport'),
        ('aventure',    'Aventure'),
    ]

    city        = models.ForeignKey(City, on_delete=models.CASCADE, related_name='activities')
    name        = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    image       = models.ImageField(upload_to='activities/', null=True, blank=True)
    category    = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    price       = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    duration    = models.CharField(max_length=50, blank=True)  # "3 heures"
    rating      = models.FloatField(default=0.0)
    max_persons = models.IntegerField(default=20)
    is_active   = models.BooleanField(default=True)
    created_at  = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.city.name}"

    class Meta:
        verbose_name_plural = 'Activities'
        ordering = ['-rating']

# ─── Monument ─────────────────────────────────────────────────────────────────
class Monument(models.Model):
    city          = models.ForeignKey(City, on_delete=models.CASCADE, related_name='monuments')
    name          = models.CharField(max_length=200)
    description   = models.TextField(blank=True)
    image         = models.ImageField(upload_to='monuments/', null=True, blank=True)
    monument_type = models.CharField(max_length=100)  # 'Landmark', 'Museum', ...
    entry_price   = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    rating        = models.FloatField(default=0.0)
    address       = models.CharField(max_length=255, blank=True)
    opening_hours = models.JSONField(default=dict, blank=True)
    built_year    = models.IntegerField(null=True, blank=True)
    is_active     = models.BooleanField(default=True)
    created_at    = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.city.name}"

    class Meta:
        ordering = ['-rating']

# ─── TravelPlan ───────────────────────────────────────────────────────────────
class TravelPlan(models.Model):
    STATUS_CHOICES = [
        ('upcoming', 'Upcoming'),
        ('ongoing',  'Ongoing'),
        ('past',     'Past'),
    ]

    user         = models.ForeignKey(User, on_delete=models.CASCADE, related_name='travel_plans')
    title        = models.CharField(max_length=200)
    destination  = models.CharField(max_length=200)
    start_date   = models.DateField()
    end_date     = models.DateField()
    total_budget = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    spent_budget = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    status       = models.CharField(max_length=20, choices=STATUS_CHOICES, default='upcoming')
    cities       = models.ManyToManyField(City, blank=True)
    notes        = models.TextField(blank=True)
    created_at   = models.DateTimeField(auto_now_add=True)
    updated_at   = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} - {self.user.name}"

    class Meta:
        ordering = ['-created_at']

# ─── Recommendation ───────────────────────────────────────────────────────────
class Recommendation(models.Model):
    user        = models.ForeignKey(User, on_delete=models.CASCADE, related_name='recommendations')
    city        = models.ForeignKey(City, on_delete=models.CASCADE)
    score       = models.FloatField(default=0.0)
    reasons     = models.JSONField(default=list, blank=True)  # ['Budget match', 'Interests match']
    created_at  = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.name} → {self.city.name} (score: {self.score})"

    class Meta:
        ordering = ['-score']

# ─── Favorite ─────────────────────────────────────────────────────────────────
class Favorite(models.Model):
    user       = models.ForeignKey(User, on_delete=models.CASCADE, related_name='favorites')
    city       = models.ForeignKey(City, on_delete=models.CASCADE, null=True, blank=True)
    hotel      = models.ForeignKey(Hotel, on_delete=models.CASCADE, null=True, blank=True)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, null=True, blank=True)
    activity   = models.ForeignKey(Activity, on_delete=models.CASCADE, null=True, blank=True)
    monument   = models.ForeignKey(Monument, on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.name} favorites"

    class Meta:
        ordering = ['-created_at']