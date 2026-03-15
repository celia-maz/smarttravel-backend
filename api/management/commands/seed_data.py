from django.core.management.base import BaseCommand
from api.models import Country, City, Hotel, Restaurant, Activity, Monument

class Command(BaseCommand):
    help = 'Seed database with sample data'

    def handle(self, *args, **kwargs):
        self.stdout.write('🌍 Seeding data...')
        self._seed_countries()
        self.stdout.write(self.style.SUCCESS('✅ Done! Database seeded successfully.'))

    def _seed_countries(self):
        # ── FRANCE ────────────────────────────────────────────────────────────
        france, _ = Country.objects.get_or_create(name='France', defaults={
            'flag': '🇫🇷', 'capital': 'Paris', 'language': 'French',
            'currency': 'Euro (€)', 'climate': 'Temperate', 'continent': 'Europe',
            'description': 'France is a nation that has profoundly shaped Western civilization. From the grandeur of Versailles to the bohemian streets of Montmartre, its history unfolds like a living museum.',
            'best_season': 'Spring & Fall', 'avg_daily': '$120-160',
            'visa_type': 'Schengen Visa', 'population': 68, 'rating': 4.8,
        })
        paris, _ = City.objects.get_or_create(name='Paris', country=france, defaults={
            'description': 'Romantic capital of art, fashion & culture',
            'rating': 4.9, 'popularity': 1000, 'budget_level': 'eleve', 'tag': 'Romance',
        })
        nice, _ = City.objects.get_or_create(name='Nice', country=france, defaults={
            'description': 'Mediterranean coastal escape on the Riviera',
            'rating': 4.7, 'popularity': 700, 'budget_level': 'eleve', 'tag': 'Beach',
        })
        lyon, _ = City.objects.get_or_create(name='Lyon', country=france, defaults={
            'description': 'Gastronomic capital & UNESCO heritage',
            'rating': 4.6, 'popularity': 600, 'budget_level': 'moyen', 'tag': 'Cuisine',
        })
        self._seed_paris(paris)
        self._seed_nice(nice)
        self.stdout.write('  ✅ France done')

        # ── JAPAN ─────────────────────────────────────────────────────────────
        japan, _ = Country.objects.get_or_create(name='Japan', defaults={
            'flag': '🇯🇵', 'capital': 'Tokyo', 'language': 'Japanese',
            'currency': 'Yen (¥)', 'climate': 'Varied', 'continent': 'Asia',
            'description': 'Japan is a land where ancient temples stand beside neon-lit skyscrapers. A unique blend of tradition and hyper-modernity, offering unforgettable experiences.',
            'best_season': 'Spring (Sakura) & Fall', 'avg_daily': '$100-180',
            'visa_type': 'Visa on arrival', 'population': 125, 'rating': 4.9,
        })
        tokyo, _ = City.objects.get_or_create(name='Tokyo', country=japan, defaults={
            'description': 'Neon, culture & cuisine in the world\'s largest city',
            'rating': 4.8, 'popularity': 950, 'budget_level': 'moyen', 'tag': 'Culture',
        })
        kyoto, _ = City.objects.get_or_create(name='Kyoto', country=japan, defaults={
            'description': 'Ancient temples, geishas & cherry blossoms',
            'rating': 4.9, 'popularity': 900, 'budget_level': 'moyen', 'tag': 'History',
        })
        osaka, _ = City.objects.get_or_create(name='Osaka', country=japan, defaults={
            'description': 'Street food paradise and vibrant nightlife',
            'rating': 4.7, 'popularity': 800, 'budget_level': 'moyen', 'tag': 'Gastronomie',
        })
        self._seed_tokyo(tokyo)
        self._seed_kyoto(kyoto)
        self.stdout.write('  ✅ Japan done')

        # ── MOROCCO ───────────────────────────────────────────────────────────
        morocco, _ = Country.objects.get_or_create(name='Morocco', defaults={
            'flag': '🇲🇦', 'capital': 'Rabat', 'language': 'Arabic & French',
            'currency': 'Dirham (MAD)', 'climate': 'Semi-arid', 'continent': 'Africa',
            'description': 'Morocco is a country of dramatic contrasts — from the Sahara dunes to Atlantic beaches, bustling medinas to snow-capped Atlas mountains.',
            'best_season': 'Spring & Fall', 'avg_daily': '$50-90',
            'visa_type': 'Visa free (90 days)', 'population': 37, 'rating': 4.7,
        })
        marrakech, _ = City.objects.get_or_create(name='Marrakech', country=morocco, defaults={
            'description': 'Spices, souks & vibrant medina life',
            'rating': 4.7, 'popularity': 850, 'budget_level': 'economique', 'tag': 'Aventure',
        })
        fes, _ = City.objects.get_or_create(name='Fès', country=morocco, defaults={
            'description': 'Medieval medina, tanneries & history',
            'rating': 4.6, 'popularity': 600, 'budget_level': 'economique', 'tag': 'Culture',
        })
        self._seed_marrakech(marrakech)
        self.stdout.write('  ✅ Morocco done')

        # ── GREECE ────────────────────────────────────────────────────────────
        greece, _ = Country.objects.get_or_create(name='Greece', defaults={
            'flag': '🇬🇷', 'capital': 'Athens', 'language': 'Greek',
            'currency': 'Euro (€)', 'climate': 'Mediterranean', 'continent': 'Europe',
            'description': 'Greece, the cradle of Western civilization, offers a stunning combination of ancient ruins, crystal-clear waters, and idyllic island life.',
            'best_season': 'May to October', 'avg_daily': '$80-150',
            'visa_type': 'Schengen Visa', 'population': 11, 'rating': 4.9,
        })
        santorini, _ = City.objects.get_or_create(name='Santorini', country=greece, defaults={
            'description': 'Iconic white cliffs, sunsets & blue domes',
            'rating': 4.9, 'popularity': 900, 'budget_level': 'eleve', 'tag': 'Nature',
        })
        athens, _ = City.objects.get_or_create(name='Athens', country=greece, defaults={
            'description': 'Ancient history meets modern city life',
            'rating': 4.6, 'popularity': 750, 'budget_level': 'moyen', 'tag': 'History',
        })
        self._seed_santorini(santorini)
        self.stdout.write('  ✅ Greece done')

        # ── INDONESIA ─────────────────────────────────────────────────────────
        indonesia, _ = Country.objects.get_or_create(name='Indonesia', defaults={
            'flag': '🇮🇩', 'capital': 'Jakarta', 'language': 'Indonesian',
            'currency': 'Rupiah (IDR)', 'climate': 'Tropical', 'continent': 'Asia',
            'description': 'Indonesia, the world\'s largest archipelago, offers an extraordinary diversity of cultures, landscapes, and wildlife across 17,000 islands.',
            'best_season': 'May to September', 'avg_daily': '$40-80',
            'visa_type': 'Visa on arrival', 'population': 273, 'rating': 4.8,
        })
        bali, _ = City.objects.get_or_create(name='Bali', country=indonesia, defaults={
            'description': 'Temples, rice fields, surf & spiritual energy',
            'rating': 4.8, 'popularity': 980, 'budget_level': 'moyen', 'tag': 'Nature',
        })
        self._seed_bali(bali)
        self.stdout.write('  ✅ Indonesia done')

        # ── ALGERIA ───────────────────────────────────────────────────────────
        algeria, _ = Country.objects.get_or_create(name='Algeria', defaults={
            'flag': '🇩🇿', 'capital': 'Algiers', 'language': 'Arabic & French',
            'currency': 'Dinar (DZD)', 'climate': 'Semi-arid', 'continent': 'Africa',
            'description': 'Algeria, Africa\'s largest country, offers the majestic Sahara desert, ancient Roman ruins, turquoise Mediterranean beaches and rich Berber culture.',
            'best_season': 'Spring & Fall', 'avg_daily': '$30-60',
            'visa_type': 'Visa required', 'population': 44, 'rating': 4.5,
        })
        algiers, _ = City.objects.get_or_create(name='Algiers', country=algeria, defaults={
            'description': 'White city on the Mediterranean coast',
            'rating': 4.4, 'popularity': 500, 'budget_level': 'economique', 'tag': 'Culture',
        })
        djanet, _ = City.objects.get_or_create(name='Djanet', country=algeria, defaults={
            'description': 'Gateway to the Sahara — dunes, stars & silence',
            'rating': 4.7, 'popularity': 400, 'budget_level': 'economique', 'tag': 'Aventure',
        })
        self.stdout.write('  ✅ Algeria done')

    # ── PARIS DATA ─────────────────────────────────────────────────────────────
    def _seed_paris(self, city):
        Hotel.objects.get_or_create(name='Le Grand Hôtel Paris', city=city, defaults={
            'description': 'Luxury 5-star hotel in the heart of Paris',
            'stars': 5, 'price_per_night': 280, 'rating': 4.8,
            'budget_level': 'eleve', 'address': '12 Rue de Rivoli, Paris',
            'amenities': ['WiFi', 'Pool', 'Spa', 'Restaurant', 'Gym'],
        })
        Hotel.objects.get_or_create(name='Hôtel Beauté Montmartre', city=city, defaults={
            'description': 'Charming boutique hotel in Montmartre',
            'stars': 4, 'price_per_night': 140, 'rating': 4.6,
            'budget_level': 'moyen', 'address': '5 Rue Lepic, Montmartre',
            'amenities': ['WiFi', 'Breakfast', 'Bar'],
        })
        Hotel.objects.get_or_create(name='Paris City Hostel', city=city, defaults={
            'description': 'Budget-friendly hostel near the Marais',
            'stars': 2, 'price_per_night': 45, 'rating': 4.2,
            'budget_level': 'economique', 'address': '20 Rue du Temple',
            'amenities': ['WiFi', 'Lockers', 'Common kitchen'],
        })
        Restaurant.objects.get_or_create(name='Le Comptoir du Marché', city=city, defaults={
            'description': 'Classic French bistro with seasonal menu',
            'cuisine_type': 'French Bistro', 'avg_price': 35,
            'rating': 4.7, 'budget_level': 'moyen',
            'address': '8 Place du Marché', 'opening_hours': '12:00-22:30',
        })
        Restaurant.objects.get_or_create(name='Café de Flore', city=city, defaults={
            'description': 'Iconic Parisian café in Saint-Germain',
            'cuisine_type': 'French Café', 'avg_price': 25,
            'rating': 4.5, 'budget_level': 'moyen',
            'address': '172 Bd Saint-Germain', 'opening_hours': '07:30-01:30',
        })
        Activity.objects.get_or_create(name='Paris City Walking Tour', city=city, defaults={
            'description': 'Explore Paris on foot with an expert local guide',
            'category': 'culture', 'price': 25, 'duration': '3 hours',
            'rating': 4.9, 'max_persons': 12,
        })
        Activity.objects.get_or_create(name='French Cooking Class', city=city, defaults={
            'description': 'Learn to cook classic French dishes with a chef',
            'category': 'gastronomie', 'price': 80, 'duration': '4 hours',
            'rating': 4.8, 'max_persons': 8,
        })
        Monument.objects.get_or_create(name='Eiffel Tower', city=city, defaults={
            'description': 'Iconic 330m iron lattice tower, symbol of Paris',
            'monument_type': 'Landmark', 'entry_price': 26,
            'rating': 4.9, 'address': 'Champ de Mars, Paris',
            'built_year': 1889,
            'opening_hours': {'Mon-Sun': '09:00-00:00'},
        })
        Monument.objects.get_or_create(name='Louvre Museum', city=city, defaults={
            'description': 'World\'s largest art museum — home of the Mona Lisa',
            'monument_type': 'Museum', 'entry_price': 17,
            'rating': 4.8, 'address': 'Rue de Rivoli, Paris',
            'built_year': 1793,
            'opening_hours': {'Mon,Wed-Sun': '09:00-18:00', 'Tue': 'Closed'},
        })
        Monument.objects.get_or_create(name='Notre-Dame Cathedral', city=city, defaults={
            'description': 'Medieval Gothic cathedral on the Île de la Cité',
            'monument_type': 'Cathedral', 'entry_price': 0,
            'rating': 4.8, 'address': '6 Parvis Notre-Dame',
            'built_year': 1163,
            'opening_hours': {'Mon-Sun': '08:00-18:45'},
        })

    # ── NICE DATA ──────────────────────────────────────────────────────────────
    def _seed_nice(self, city):
        Hotel.objects.get_or_create(name='Hôtel Negresco', city=city, defaults={
            'description': 'Legendary belle époque palace on the Promenade',
            'stars': 5, 'price_per_night': 350, 'rating': 4.9,
            'budget_level': 'eleve', 'amenities': ['Pool', 'Spa', 'Restaurant', 'WiFi'],
        })
        Restaurant.objects.get_or_create(name='La Merenda', city=city, defaults={
            'description': 'Authentic Niçois cuisine in old town',
            'cuisine_type': 'Niçois', 'avg_price': 30,
            'rating': 4.8, 'budget_level': 'moyen',
        })
        Activity.objects.get_or_create(name='Promenade des Anglais Bike Tour', city=city, defaults={
            'description': 'Cycle along the famous beachfront promenade',
            'category': 'sport', 'price': 15, 'duration': '2 hours',
            'rating': 4.7, 'max_persons': 20,
        })
        Monument.objects.get_or_create(name='Castle Hill (Colline du Château)', city=city, defaults={
            'description': 'Panoramic views over Nice and the Baie des Anges',
            'monument_type': 'Park', 'entry_price': 0, 'rating': 4.7,
        })

    # ── TOKYO DATA ─────────────────────────────────────────────────────────────
    def _seed_tokyo(self, city):
        Hotel.objects.get_or_create(name='Hotel Shinjuku Granbell', city=city, defaults={
            'description': 'Modern design hotel in the heart of Shinjuku',
            'stars': 4, 'price_per_night': 180, 'rating': 4.7,
            'budget_level': 'moyen', 'address': 'Shinjuku, Tokyo',
            'amenities': ['WiFi', 'Restaurant', 'Bar', 'Gym'],
        })
        Hotel.objects.get_or_create(name='Capsule Hotel Anshin Oyado', city=city, defaults={
            'description': 'Classic Japanese capsule hotel experience',
            'stars': 2, 'price_per_night': 40, 'rating': 4.3,
            'budget_level': 'economique', 'amenities': ['WiFi', 'Onsen', 'Locker'],
        })
        Restaurant.objects.get_or_create(name='Ramen Ichiran Shibuya', city=city, defaults={
            'description': 'Famous solo-booth tonkotsu ramen experience',
            'cuisine_type': 'Japanese Ramen', 'avg_price': 15,
            'rating': 4.8, 'budget_level': 'economique',
        })
        Restaurant.objects.get_or_create(name='Sushi Dai Tsukiji', city=city, defaults={
            'description': 'Legendary omakase sushi at Tsukiji market',
            'cuisine_type': 'Japanese Sushi', 'avg_price': 50,
            'rating': 4.9, 'budget_level': 'moyen',
        })
        Activity.objects.get_or_create(name='Tokyo Skytree Visit', city=city, defaults={
            'description': 'Visit Tokyo from 450m — stunning panoramic views',
            'category': 'culture', 'price': 25, 'duration': '2 hours',
            'rating': 4.7, 'max_persons': 100,
        })
        Activity.objects.get_or_create(name='Teamlab Planets', city=city, defaults={
            'description': 'Immersive digital art museum in Toyosu',
            'category': 'culture', 'price': 32, 'duration': '1.5 hours',
            'rating': 4.9, 'max_persons': 50,
        })
        Monument.objects.get_or_create(name='Senso-ji Temple', city=city, defaults={
            'description': 'Tokyo\'s oldest temple in Asakusa',
            'monument_type': 'Temple', 'entry_price': 0,
            'rating': 4.8, 'built_year': 645,
        })
        Monument.objects.get_or_create(name='Shibuya Crossing', city=city, defaults={
            'description': 'World\'s busiest pedestrian crossing',
            'monument_type': 'Landmark', 'entry_price': 0, 'rating': 4.7,
        })

    # ── KYOTO DATA ─────────────────────────────────────────────────────────────
    def _seed_kyoto(self, city):
        Hotel.objects.get_or_create(name='Ryokan Yoshida Sanso', city=city, defaults={
            'description': 'Traditional Japanese ryokan with tatami rooms',
            'stars': 4, 'price_per_night': 220, 'rating': 4.9,
            'budget_level': 'eleve', 'amenities': ['Onsen', 'Breakfast', 'Yukata', 'WiFi'],
        })
        Activity.objects.get_or_create(name='Fushimi Inari Hike', city=city, defaults={
            'description': 'Walk through thousands of vermilion torii gates',
            'category': 'nature', 'price': 0, 'duration': '2-4 hours',
            'rating': 4.9, 'max_persons': 999,
        })
        Activity.objects.get_or_create(name='Tea Ceremony Experience', city=city, defaults={
            'description': 'Authentic Japanese tea ceremony in a historic house',
            'category': 'culture', 'price': 40, 'duration': '1 hour',
            'rating': 4.8, 'max_persons': 10,
        })
        Monument.objects.get_or_create(name='Kinkaku-ji (Golden Pavilion)', city=city, defaults={
            'description': 'Stunning gold-leaf covered Zen Buddhist temple',
            'monument_type': 'Temple', 'entry_price': 5,
            'rating': 4.9, 'built_year': 1397,
        })
        Monument.objects.get_or_create(name='Arashiyama Bamboo Grove', city=city, defaults={
            'description': 'Magical pathway through towering bamboo forests',
            'monument_type': 'Nature', 'entry_price': 0, 'rating': 4.8,
        })

    # ── MARRAKECH DATA ─────────────────────────────────────────────────────────
    def _seed_marrakech(self, city):
        Hotel.objects.get_or_create(name='Riad Yasmine', city=city, defaults={
            'description': 'Stunning riad with pool and rooftop terrace',
            'stars': 4, 'price_per_night': 120, 'rating': 4.8,
            'budget_level': 'moyen', 'amenities': ['Pool', 'WiFi', 'Breakfast', 'Rooftop'],
        })
        Hotel.objects.get_or_create(name='Hostel Medina Chill', city=city, defaults={
            'description': 'Budget hostel in the heart of the medina',
            'stars': 2, 'price_per_night': 20, 'rating': 4.3,
            'budget_level': 'economique', 'amenities': ['WiFi', 'Common room'],
        })
        Restaurant.objects.get_or_create(name='Le Jardin', city=city, defaults={
            'description': 'Beautiful garden restaurant in the medina',
            'cuisine_type': 'Moroccan', 'avg_price': 20,
            'rating': 4.7, 'budget_level': 'moyen',
        })
        Activity.objects.get_or_create(name='Sahara Desert Day Trip', city=city, defaults={
            'description': 'Camel ride and sunset in the Sahara dunes',
            'category': 'aventure', 'price': 60, 'duration': 'Full day',
            'rating': 4.9, 'max_persons': 15,
        })
        Activity.objects.get_or_create(name='Medina Souk Tour', city=city, defaults={
            'description': 'Navigate the labyrinthine souks with a local guide',
            'category': 'culture', 'price': 20, 'duration': '3 hours',
            'rating': 4.7, 'max_persons': 8,
        })
        Monument.objects.get_or_create(name='Jemaa el-Fna Square', city=city, defaults={
            'description': 'UNESCO-listed main square full of life and entertainment',
            'monument_type': 'Square', 'entry_price': 0, 'rating': 4.8,
        })
        Monument.objects.get_or_create(name='Bahia Palace', city=city, defaults={
            'description': '19th century palace with stunning Moroccan architecture',
            'monument_type': 'Palace', 'entry_price': 7, 'rating': 4.7,
            'built_year': 1894,
        })

    # ── SANTORINI DATA ─────────────────────────────────────────────────────────
    def _seed_santorini(self, city):
        Hotel.objects.get_or_create(name='Canaves Oia Suites', city=city, defaults={
            'description': 'Luxury cave suites with infinity pool & caldera view',
            'stars': 5, 'price_per_night': 450, 'rating': 4.9,
            'budget_level': 'eleve', 'amenities': ['Pool', 'Spa', 'Breakfast', 'WiFi'],
        })
        Restaurant.objects.get_or_create(name='Metaxi Mas', city=city, defaults={
            'description': 'Authentic Greek taverna with mezze & local wine',
            'cuisine_type': 'Greek', 'avg_price': 35,
            'rating': 4.8, 'budget_level': 'moyen',
        })
        Activity.objects.get_or_create(name='Caldera Sunset Cruise', city=city, defaults={
            'description': 'Sail around the volcano at sunset with dinner',
            'category': 'nature', 'price': 95, 'duration': '5 hours',
            'rating': 4.9, 'max_persons': 20,
        })
        Monument.objects.get_or_create(name='Oia Village', city=city, defaults={
            'description': 'Iconic white & blue architecture with the best sunset views',
            'monument_type': 'Village', 'entry_price': 0, 'rating': 4.9,
        })

    # ── BALI DATA ──────────────────────────────────────────────────────────────
    def _seed_bali(self, city):
        Hotel.objects.get_or_create(name='Four Seasons Bali at Sayan', city=city, defaults={
            'description': 'Luxury resort nestled in the Ayung River valley',
            'stars': 5, 'price_per_night': 380, 'rating': 4.9,
            'budget_level': 'eleve', 'amenities': ['Pool', 'Spa', 'Restaurant', 'Yoga'],
        })
        Hotel.objects.get_or_create(name='Canggu Beach Hostel', city=city, defaults={
            'description': 'Surf & chill hostel steps from the beach',
            'stars': 2, 'price_per_night': 18, 'rating': 4.5,
            'budget_level': 'economique', 'amenities': ['WiFi', 'Pool', 'Surf lessons'],
        })
        Restaurant.objects.get_or_create(name='Locavore', city=city, defaults={
            'description': 'Award-winning farm-to-table Indonesian cuisine',
            'cuisine_type': 'Modern Indonesian', 'avg_price': 60,
            'rating': 4.9, 'budget_level': 'eleve',
        })
        Activity.objects.get_or_create(name='Surf Lessons Kuta Beach', city=city, defaults={
            'description': 'Learn to surf on Bali\'s famous waves',
            'category': 'sport', 'price': 30, 'duration': '2 hours',
            'rating': 4.8, 'max_persons': 6,
        })
        Activity.objects.get_or_create(name='Ubud Rice Terrace Trek', city=city, defaults={
            'description': 'Hike through stunning emerald rice terraces',
            'category': 'nature', 'price': 20, 'duration': '4 hours',
            'rating': 4.8, 'max_persons': 10,
        })
        Monument.objects.get_or_create(name='Tanah Lot Temple', city=city, defaults={
            'description': 'Sacred sea temple perched on a dramatic rock formation',
            'monument_type': 'Temple', 'entry_price': 5, 'rating': 4.8,
        })
        Monument.objects.get_or_create(name='Ubud Monkey Forest', city=city, defaults={
            'description': 'Sacred forest sanctuary with hundreds of Balinese macaques',
            'monument_type': 'Nature', 'entry_price': 5, 'rating': 4.7,
        })