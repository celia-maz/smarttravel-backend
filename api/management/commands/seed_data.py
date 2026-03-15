from django.core.management.base import BaseCommand
from api.models import (
    Country, City, Hotel, Restaurant, Activity, Monument
)


class Command(BaseCommand):
    help = 'Seed database with rich travel data'

    def handle(self, *args, **kwargs):
        self.stdout.write('Seeding rich travel data...')
        Country.objects.all().delete()
        self._seed()
        self.stdout.write(self.style.SUCCESS('Done! Database seeded successfully.'))

    def _seed(self):
        data = [
            {
                'country': {
                    'name': 'France', 'flag': '🇫🇷', 'capital': 'Paris',
                    'language': 'French', 'currency': 'Euro (€)', 'climate': 'Temperate',
                    'continent': 'Europe', 'population': 68, 'rating': 4.8,
                    'best_season': 'Spring & Fall', 'avg_daily': '$120-160',
                    'visa_type': 'Schengen Visa',
                    'description': 'France is a nation that has profoundly shaped Western civilization.',
                    'image': 'https://picsum.photos/seed/france/800/600',
                },
                'cities': [
                    {
                        'name': 'Paris', 'tag': 'Romance', 'budget_level': 'eleve',
                        'rating': 4.9, 'popularity': 1000,
                        'description': 'The City of Light — romantic, artistic and iconic.',
                        'image': 'https://picsum.photos/seed/paris/800/600',
                        'hotels': [
                            {'name': 'Le Grand Hotel Paris', 'stars': 5, 'price_per_night': 420, 'rating': 4.9, 'budget_level': 'eleve', 'description': 'Legendary luxury on Boulevard des Capucines', 'image': 'https://picsum.photos/seed/hotel1/600/400'},
                            {'name': 'Hotel des Arts Montmartre', 'stars': 3, 'price_per_night': 95, 'rating': 4.5, 'budget_level': 'moyen', 'description': 'Charming boutique hotel in artistic Montmartre', 'image': 'https://picsum.photos/seed/hotel2/600/400'},
                            {'name': 'Generator Paris', 'stars': 2, 'price_per_night': 35, 'rating': 4.2, 'budget_level': 'budget', 'description': 'Stylish hostel near Canal Saint-Martin', 'image': 'https://picsum.photos/seed/hotel3/600/400'},
                        ],
                        'restaurants': [
                            {'name': 'Le Comptoir du Relais', 'cuisine_type': 'French Bistro', 'avg_price': 45, 'rating': 4.7, 'budget_level': 'moyen', 'description': 'Classic Saint-Germain bistro with seasonal menu', 'image': 'https://picsum.photos/seed/resto1/600/400'},
                            {'name': 'Septime', 'cuisine_type': 'Modern French', 'avg_price': 90, 'rating': 4.9, 'budget_level': 'eleve', 'description': 'Michelin-starred natural wine and seasonal cuisine', 'image': 'https://picsum.photos/seed/resto2/600/400'},
                            {'name': 'Breizh Cafe', 'cuisine_type': 'Creperie', 'avg_price': 22, 'rating': 4.6, 'budget_level': 'budget', 'description': 'Best buckwheat galettes in the Marais', 'image': 'https://picsum.photos/seed/resto3/600/400'},
                        ],
                        'activities': [
                            {'name': 'Louvre Museum Tour', 'category': 'culture', 'price': 17, 'duration': '3 hours', 'rating': 4.8, 'description': "World's largest art museum with the Mona Lisa", 'image': 'https://picsum.photos/seed/louvre/600/400'},
                            {'name': 'Seine River Cruise', 'category': 'aventure', 'price': 25, 'duration': '1.5 hours', 'rating': 4.7, 'description': 'Panoramic boat tour past Notre-Dame and the Eiffel Tower', 'image': 'https://picsum.photos/seed/seine/600/400'},
                            {'name': 'Montmartre Walking Tour', 'category': 'culture', 'price': 20, 'duration': '2 hours', 'rating': 4.6, 'description': 'Discover the bohemian hilltop village of artists', 'image': 'https://picsum.photos/seed/montmartre/600/400'},
                        ],
                        'monuments': [
                            {'name': 'Eiffel Tower', 'monument_type': 'Landmark', 'entry_price': 26, 'rating': 4.9, 'description': 'Iron lattice tower symbol of France, built 1889', 'image': 'https://picsum.photos/seed/eiffel/600/400'},
                            {'name': 'Notre-Dame Cathedral', 'monument_type': 'Cathedral', 'entry_price': 0, 'rating': 4.8, 'description': 'Gothic masterpiece under restoration after 2019 fire', 'image': 'https://picsum.photos/seed/notredame/600/400'},
                            {'name': 'Palace of Versailles', 'monument_type': 'Palace', 'entry_price': 20, 'rating': 4.7, 'description': 'Royal chateau with magnificent Hall of Mirrors', 'image': 'https://picsum.photos/seed/versailles/600/400'},
                        ],
                    },
                    {
                        'name': 'Nice', 'tag': 'Beach', 'budget_level': 'eleve',
                        'rating': 4.7, 'popularity': 750,
                        'description': 'Mediterranean gem on the French Riviera with azure waters.',
                        'image': 'https://picsum.photos/seed/nice/800/600',
                        'hotels': [
                            {'name': 'Hotel Negresco', 'stars': 5, 'price_per_night': 380, 'rating': 4.9, 'budget_level': 'eleve', 'description': 'Iconic pink dome palace on the Promenade des Anglais', 'image': 'https://picsum.photos/seed/hotel4/600/400'},
                            {'name': 'Villa Saint-Exupery', 'stars': 3, 'price_per_night': 55, 'rating': 4.6, 'budget_level': 'budget', 'description': 'Best hostel on the Riviera with stunning views', 'image': 'https://picsum.photos/seed/hotel5/600/400'},
                        ],
                        'restaurants': [
                            {'name': 'La Petite Maison', 'cuisine_type': 'Nicoise', 'avg_price': 65, 'rating': 4.8, 'budget_level': 'eleve', 'description': 'Celebrity hotspot for authentic Nicoise cuisine', 'image': 'https://picsum.photos/seed/resto4/600/400'},
                        ],
                        'activities': [
                            {'name': 'Promenade des Anglais Walk', 'category': 'nature', 'price': 0, 'duration': '2 hours', 'rating': 4.7, 'description': 'Iconic seafront promenade along the Mediterranean', 'image': 'https://picsum.photos/seed/promenade/600/400'},
                        ],
                        'monuments': [
                            {'name': 'Castle Hill', 'monument_type': 'Historic Site', 'entry_price': 0, 'rating': 4.6, 'description': 'Panoramic viewpoint over Nice and the Baie des Anges', 'image': 'https://picsum.photos/seed/castlehill/600/400'},
                        ],
                    },
                ],
            },
            {
                'country': {
                    'name': 'Japan', 'flag': '🇯🇵', 'capital': 'Tokyo',
                    'language': 'Japanese', 'currency': 'Yen (Y)', 'climate': 'Temperate',
                    'continent': 'Asia', 'population': 125, 'rating': 4.9,
                    'best_season': 'Spring (Cherry Blossom)', 'avg_daily': '$100-150',
                    'visa_type': 'Visa on Arrival',
                    'description': 'Japan is a country where ancient traditions and futuristic technology coexist in perfect harmony.',
                    'image': 'https://picsum.photos/seed/japan/800/600',
                },
                'cities': [
                    {
                        'name': 'Tokyo', 'tag': 'Urban', 'budget_level': 'moyen',
                        'rating': 4.9, 'popularity': 1200,
                        'description': "The world's most populous metropolis — electric and endlessly fascinating.",
                        'image': 'https://picsum.photos/seed/tokyo/800/600',
                        'hotels': [
                            {'name': 'Park Hyatt Tokyo', 'stars': 5, 'price_per_night': 550, 'rating': 4.9, 'budget_level': 'eleve', 'description': 'Iconic luxury hotel from Lost in Translation', 'image': 'https://picsum.photos/seed/hotel6/600/400'},
                            {'name': 'Shinjuku Granbell Hotel', 'stars': 4, 'price_per_night': 180, 'rating': 4.7, 'budget_level': 'moyen', 'description': 'Design hotel in the heart of Shinjuku', 'image': 'https://picsum.photos/seed/hotel7/600/400'},
                            {'name': 'Khaosan Tokyo Origami', 'stars': 2, 'price_per_night': 28, 'rating': 4.4, 'budget_level': 'budget', 'description': 'Friendly hostel steps from Asakusa temple', 'image': 'https://picsum.photos/seed/hotel8/600/400'},
                        ],
                        'restaurants': [
                            {'name': 'Sukiyabashi Jiro', 'cuisine_type': 'Sushi', 'avg_price': 300, 'rating': 5.0, 'budget_level': 'eleve', 'description': "World's most famous sushi restaurant, 3 Michelin stars", 'image': 'https://picsum.photos/seed/sushi/600/400'},
                            {'name': 'Ichiran Ramen', 'cuisine_type': 'Ramen', 'avg_price': 15, 'rating': 4.7, 'budget_level': 'budget', 'description': 'Solo dining ramen experience in private booths', 'image': 'https://picsum.photos/seed/ramen/600/400'},
                            {'name': 'Gonpachi Nishi-Azabu', 'cuisine_type': 'Japanese Izakaya', 'avg_price': 45, 'rating': 4.6, 'budget_level': 'moyen', 'description': "The inspiration for Kill Bill's restaurant scene", 'image': 'https://picsum.photos/seed/izakaya/600/400'},
                        ],
                        'activities': [
                            {'name': 'Shibuya Crossing Experience', 'category': 'culture', 'price': 0, 'duration': '1 hour', 'rating': 4.8, 'description': "World's busiest pedestrian crossing", 'image': 'https://picsum.photos/seed/shibuya/600/400'},
                            {'name': 'TeamLab Planets', 'category': 'culture', 'price': 32, 'duration': '2 hours', 'rating': 4.9, 'description': 'Immersive digital art museum in Toyosu', 'image': 'https://picsum.photos/seed/teamlab/600/400'},
                            {'name': 'Tsukiji Outer Market Tour', 'category': 'gastronomie', 'price': 40, 'duration': '3 hours', 'rating': 4.7, 'description': 'Morning food tour at world-famous fish market', 'image': 'https://picsum.photos/seed/tsukiji/600/400'},
                        ],
                        'monuments': [
                            {'name': 'Senso-ji Temple', 'monument_type': 'Temple', 'entry_price': 0, 'rating': 4.8, 'description': "Tokyo's oldest temple in historic Asakusa", 'image': 'https://picsum.photos/seed/sensoji/600/400'},
                            {'name': 'Tokyo Skytree', 'monument_type': 'Tower', 'entry_price': 22, 'rating': 4.7, 'description': "World's second tallest structure at 634 meters", 'image': 'https://picsum.photos/seed/skytree/600/400'},
                        ],
                    },
                    {
                        'name': 'Kyoto', 'tag': 'Culture', 'budget_level': 'moyen',
                        'rating': 4.8, 'popularity': 900,
                        'description': 'Ancient capital with 1,600 Buddhist temples and Shinto shrines.',
                        'image': 'https://picsum.photos/seed/kyoto/800/600',
                        'hotels': [
                            {'name': 'Tawaraya Ryokan', 'stars': 5, 'price_per_night': 800, 'rating': 5.0, 'budget_level': 'eleve', 'description': "Japan's finest traditional inn since 1709", 'image': 'https://picsum.photos/seed/hotel9/600/400'},
                            {'name': 'The Screen Kyoto', 'stars': 4, 'price_per_night': 220, 'rating': 4.8, 'budget_level': 'eleve', 'description': 'Contemporary boutique hotel near Nijo Castle', 'image': 'https://picsum.photos/seed/hotel10/600/400'},
                        ],
                        'restaurants': [
                            {'name': 'Kikunoi Honten', 'cuisine_type': 'Kaiseki', 'avg_price': 180, 'rating': 4.9, 'budget_level': 'eleve', 'description': 'Three Michelin star kaiseki cuisine since 1912', 'image': 'https://picsum.photos/seed/kaiseki/600/400'},
                        ],
                        'activities': [
                            {'name': 'Arashiyama Bamboo Grove', 'category': 'nature', 'price': 0, 'duration': '2 hours', 'rating': 4.8, 'description': 'Walk through ethereal towering bamboo forest', 'image': 'https://picsum.photos/seed/bamboo/600/400'},
                            {'name': 'Geisha District Walk', 'category': 'culture', 'price': 25, 'duration': '2.5 hours', 'rating': 4.7, 'description': 'Evening stroll through Gion with local guide', 'image': 'https://picsum.photos/seed/gion/600/400'},
                        ],
                        'monuments': [
                            {'name': 'Fushimi Inari Shrine', 'monument_type': 'Shrine', 'entry_price': 0, 'rating': 4.9, 'description': 'Thousands of vermilion torii gates up the mountain', 'image': 'https://picsum.photos/seed/fushimi/600/400'},
                            {'name': 'Kinkaku-ji Golden Pavilion', 'monument_type': 'Temple', 'entry_price': 5, 'rating': 4.8, 'description': 'Zen temple covered in gold leaf reflecting on a pond', 'image': 'https://picsum.photos/seed/kinkaku/600/400'},
                        ],
                    },
                ],
            },
            {
                'country': {
                    'name': 'Morocco', 'flag': '🇲🇦', 'capital': 'Rabat',
                    'language': 'Arabic / French', 'currency': 'Dirham (MAD)', 'climate': 'Arid',
                    'continent': 'Africa', 'population': 37, 'rating': 4.7,
                    'best_season': 'Oct-Apr', 'avg_daily': '$50-80',
                    'visa_type': 'Visa Free (90 days)',
                    'description': 'Morocco is a land of contrasts where the Sahara desert meets Atlantic coasts.',
                    'image': 'https://picsum.photos/seed/morocco/800/600',
                },
                'cities': [
                    {
                        'name': 'Marrakech', 'tag': 'Culture', 'budget_level': 'budget',
                        'rating': 4.7, 'popularity': 850,
                        'description': 'The Red City — a sensory feast of souks, riads and Djemaa el-Fna.',
                        'image': 'https://picsum.photos/seed/marrakech/800/600',
                        'hotels': [
                            {'name': 'Royal Mansour Marrakech', 'stars': 5, 'price_per_night': 900, 'rating': 5.0, 'budget_level': 'eleve', 'description': 'A royal city within a city', 'image': 'https://picsum.photos/seed/hotel11/600/400'},
                            {'name': 'Riad Yasmine', 'stars': 4, 'price_per_night': 120, 'rating': 4.8, 'budget_level': 'moyen', 'description': 'Instagram-famous riad with iconic pool in the medina', 'image': 'https://picsum.photos/seed/hotel12/600/400'},
                            {'name': 'Equity Point Marrakech', 'stars': 2, 'price_per_night': 18, 'rating': 4.3, 'budget_level': 'budget', 'description': 'Social hostel with rooftop terrace', 'image': 'https://picsum.photos/seed/hotel13/600/400'},
                        ],
                        'restaurants': [
                            {'name': 'Nomad', 'cuisine_type': 'Modern Moroccan', 'avg_price': 25, 'rating': 4.7, 'budget_level': 'moyen', 'description': 'Rooftop restaurant with contemporary Moroccan cuisine', 'image': 'https://picsum.photos/seed/nomad/600/400'},
                            {'name': 'Djemaa el-Fna Food Stalls', 'cuisine_type': 'Street Food', 'avg_price': 8, 'rating': 4.5, 'budget_level': 'budget', 'description': 'Legendary outdoor market with grills', 'image': 'https://picsum.photos/seed/djemaa/600/400'},
                        ],
                        'activities': [
                            {'name': 'Sahara Desert Camel Trek', 'category': 'aventure', 'price': 95, 'duration': '2 days', 'rating': 4.9, 'description': 'Overnight camel trek into Erg Chebbi dunes', 'image': 'https://picsum.photos/seed/sahara/600/400'},
                            {'name': 'Medina Souk Tour', 'category': 'culture', 'price': 20, 'duration': '3 hours', 'rating': 4.6, 'description': 'Guided maze tour through spice souks', 'image': 'https://picsum.photos/seed/souk/600/400'},
                            {'name': 'Hammam Spa Experience', 'category': 'gastronomie', 'price': 35, 'duration': '2 hours', 'rating': 4.7, 'description': 'Traditional Moroccan steam bath', 'image': 'https://picsum.photos/seed/hammam/600/400'},
                        ],
                        'monuments': [
                            {'name': 'Bahia Palace', 'monument_type': 'Palace', 'entry_price': 7, 'rating': 4.6, 'description': '19th century palace with intricate Moorish decoration', 'image': 'https://picsum.photos/seed/bahia/600/400'},
                            {'name': 'Saadian Tombs', 'monument_type': 'Historic Site', 'entry_price': 7, 'rating': 4.5, 'description': 'Royal necropolis dating from the 16th century', 'image': 'https://picsum.photos/seed/saadian/600/400'},
                        ],
                    },
                ],
            },
            {
                'country': {
                    'name': 'Italy', 'flag': '🇮🇹', 'capital': 'Rome',
                    'language': 'Italian', 'currency': 'Euro (€)', 'climate': 'Mediterranean',
                    'continent': 'Europe', 'population': 60, 'rating': 4.8,
                    'best_season': 'Apr-Jun & Sep-Oct', 'avg_daily': '$100-140',
                    'visa_type': 'Schengen Visa',
                    'description': 'Italy is an open-air museum where ancient ruins and culinary excellence combine.',
                    'image': 'https://picsum.photos/seed/italy/800/600',
                },
                'cities': [
                    {
                        'name': 'Rome', 'tag': 'History', 'budget_level': 'moyen',
                        'rating': 4.8, 'popularity': 950,
                        'description': 'The Eternal City — 2,500 years of history at every corner.',
                        'image': 'https://picsum.photos/seed/rome/800/600',
                        'hotels': [
                            {'name': 'Hotel de Russie', 'stars': 5, 'price_per_night': 480, 'rating': 4.9, 'budget_level': 'eleve', 'description': 'Legendary luxury near Piazza del Popolo', 'image': 'https://picsum.photos/seed/hotel14/600/400'},
                            {'name': 'The RomeHello Hostel', 'stars': 2, 'price_per_night': 28, 'rating': 4.5, 'budget_level': 'budget', 'description': 'Social hostel walking distance from Termini', 'image': 'https://picsum.photos/seed/hotel15/600/400'},
                        ],
                        'restaurants': [
                            {'name': 'La Pergola', 'cuisine_type': 'Fine Italian', 'avg_price': 200, 'rating': 4.9, 'budget_level': 'eleve', 'description': 'Only 3 Michelin star restaurant in Rome', 'image': 'https://picsum.photos/seed/pergola/600/400'},
                            {'name': 'Da Enzo al 29', 'cuisine_type': 'Roman Trattoria', 'avg_price': 30, 'rating': 4.8, 'budget_level': 'moyen', 'description': 'Authentic cacio e pepe in Trastevere', 'image': 'https://picsum.photos/seed/enzo/600/400'},
                        ],
                        'activities': [
                            {'name': 'Colosseum Skip-the-Line', 'category': 'culture', 'price': 22, 'duration': '2 hours', 'rating': 4.8, 'description': 'Guided tour of the iconic 80 AD amphitheatre', 'image': 'https://picsum.photos/seed/colosseum/600/400'},
                            {'name': 'Vatican Museums & Sistine Chapel', 'category': 'culture', 'price': 27, 'duration': '3 hours', 'rating': 4.9, 'description': "Michelangelo's ceiling and 7km of priceless art", 'image': 'https://picsum.photos/seed/vatican/600/400'},
                        ],
                        'monuments': [
                            {'name': 'Colosseum', 'monument_type': 'Amphitheatre', 'entry_price': 16, 'rating': 4.9, 'description': 'The greatest amphitheatre ever built, 70 AD', 'image': 'https://picsum.photos/seed/colosseum2/600/400'},
                            {'name': 'Trevi Fountain', 'monument_type': 'Fountain', 'entry_price': 0, 'rating': 4.7, 'description': 'Baroque masterpiece — toss a coin to return to Rome', 'image': 'https://picsum.photos/seed/trevi/600/400'},
                        ],
                    },
                    {
                        'name': 'Venice', 'tag': 'Romance', 'budget_level': 'eleve',
                        'rating': 4.7, 'popularity': 800,
                        'description': 'A floating city built on 118 islands — uniquely magical.',
                        'image': 'https://picsum.photos/seed/venice/800/600',
                        'hotels': [
                            {'name': 'Gritti Palace', 'stars': 5, 'price_per_night': 700, 'rating': 4.9, 'budget_level': 'eleve', 'description': '15th century palace on the Grand Canal', 'image': 'https://picsum.photos/seed/hotel16/600/400'},
                        ],
                        'restaurants': [
                            {'name': 'Osteria alle Testiere', 'cuisine_type': 'Venetian Seafood', 'avg_price': 70, 'rating': 4.8, 'budget_level': 'eleve', 'description': 'Best cicchetti and seafood pasta', 'image': 'https://picsum.photos/seed/testiere/600/400'},
                        ],
                        'activities': [
                            {'name': 'Grand Canal Gondola Ride', 'category': 'aventure', 'price': 80, 'duration': '40 minutes', 'rating': 4.7, 'description': "Classic gondola ride through Venice's waterways", 'image': 'https://picsum.photos/seed/gondola/600/400'},
                        ],
                        'monuments': [
                            {'name': "St Mark's Basilica", 'monument_type': 'Cathedral', 'entry_price': 3, 'rating': 4.8, 'description': 'Byzantine cathedral with golden mosaics', 'image': 'https://picsum.photos/seed/stmarks/600/400'},
                        ],
                    },
                ],
            },
            {
                'country': {
                    'name': 'Indonesia', 'flag': '🇮🇩', 'capital': 'Jakarta',
                    'language': 'Indonesian', 'currency': 'Rupiah (IDR)', 'climate': 'Tropical',
                    'continent': 'Asia', 'population': 270, 'rating': 4.7,
                    'best_season': 'May-Sep', 'avg_daily': '$40-70',
                    'visa_type': 'Visa on Arrival',
                    'description': 'Indonesia is an archipelago of 17,000 islands offering volcanic landscapes.',
                    'image': 'https://picsum.photos/seed/indonesia/800/600',
                },
                'cities': [
                    {
                        'name': 'Bali', 'tag': 'Beach', 'budget_level': 'budget',
                        'rating': 4.8, 'popularity': 1100,
                        'description': 'Island of the Gods — temples, rice terraces and perfect surf.',
                        'image': 'https://picsum.photos/seed/bali/800/600',
                        'hotels': [
                            {'name': 'Four Seasons Bali at Sayan', 'stars': 5, 'price_per_night': 600, 'rating': 4.9, 'budget_level': 'eleve', 'description': 'Jungle resort above Ayung River with infinity pools', 'image': 'https://picsum.photos/seed/hotel17/600/400'},
                            {'name': 'Katamama Boutique Hotel', 'stars': 4, 'price_per_night': 250, 'rating': 4.8, 'budget_level': 'eleve', 'description': 'Handcrafted Balinese luxury in Seminyak', 'image': 'https://picsum.photos/seed/hotel18/600/400'},
                            {'name': 'Puri Garden Hotel', 'stars': 2, 'price_per_night': 22, 'rating': 4.4, 'budget_level': 'budget', 'description': 'Budget-friendly oasis in the heart of Ubud', 'image': 'https://picsum.photos/seed/hotel19/600/400'},
                        ],
                        'restaurants': [
                            {'name': 'Locavore', 'cuisine_type': 'Modern Indonesian', 'avg_price': 80, 'rating': 4.9, 'budget_level': 'eleve', 'description': "Asia's 50 Best — hyperlocal Balinese ingredients", 'image': 'https://picsum.photos/seed/locavore/600/400'},
                            {'name': 'Warung Babi Guling Ibu Oka', 'cuisine_type': 'Balinese', 'avg_price': 5, 'rating': 4.7, 'budget_level': 'budget', 'description': "Anthony Bourdain's favourite suckling pig", 'image': 'https://picsum.photos/seed/warung/600/400'},
                        ],
                        'activities': [
                            {'name': 'Mount Batur Sunrise Trek', 'category': 'aventure', 'price': 65, 'duration': '6 hours', 'rating': 4.8, 'description': 'Pre-dawn hike to active volcano for spectacular sunrise', 'image': 'https://picsum.photos/seed/batur/600/400'},
                            {'name': 'Tegalalang Rice Terrace Walk', 'category': 'nature', 'price': 3, 'duration': '2 hours', 'rating': 4.7, 'description': 'Walk through UNESCO-listed emerald rice paddies', 'image': 'https://picsum.photos/seed/tegalalang/600/400'},
                            {'name': 'Seminyak Surf Lesson', 'category': 'aventure', 'price': 30, 'duration': '2 hours', 'rating': 4.6, 'description': "Learn to surf on Bali's famous beach breaks", 'image': 'https://picsum.photos/seed/surf/600/400'},
                        ],
                        'monuments': [
                            {'name': 'Tanah Lot Temple', 'monument_type': 'Temple', 'entry_price': 4, 'rating': 4.8, 'description': 'Sea temple perched dramatically on a coastal rock', 'image': 'https://picsum.photos/seed/tanahlot/600/400'},
                            {'name': 'Uluwatu Temple', 'monument_type': 'Temple', 'entry_price': 4, 'rating': 4.7, 'description': 'Clifftop temple above the Indian Ocean', 'image': 'https://picsum.photos/seed/uluwatu/600/400'},
                        ],
                    },
                ],
            },
            {
                'country': {
                    'name': 'Greece', 'flag': '🇬🇷', 'capital': 'Athens',
                    'language': 'Greek', 'currency': 'Euro (€)', 'climate': 'Mediterranean',
                    'continent': 'Europe', 'population': 11, 'rating': 4.7,
                    'best_season': 'May-Oct', 'avg_daily': '$80-120',
                    'visa_type': 'Schengen Visa',
                    'description': 'Greece is the cradle of Western civilization, offering ancient ruins and turquoise waters.',
                    'image': 'https://picsum.photos/seed/greece/800/600',
                },
                'cities': [
                    {
                        'name': 'Santorini', 'tag': 'Romance', 'budget_level': 'eleve',
                        'rating': 4.9, 'popularity': 950,
                        'description': 'Iconic blue domes, dramatic cliffs and legendary sunsets.',
                        'image': 'https://picsum.photos/seed/santorini/800/600',
                        'hotels': [
                            {'name': 'Canaves Oia Epitome', 'stars': 5, 'price_per_night': 1200, 'rating': 5.0, 'budget_level': 'eleve', 'description': 'Cliffside infinity pools with Caldera views', 'image': 'https://picsum.photos/seed/hotel20/600/400'},
                            {'name': 'Astra Suites', 'stars': 5, 'price_per_night': 450, 'rating': 4.9, 'budget_level': 'eleve', 'description': 'Cave suites carved into the volcanic cliffs', 'image': 'https://picsum.photos/seed/hotel21/600/400'},
                        ],
                        'restaurants': [
                            {'name': 'Kastro Restaurant Oia', 'cuisine_type': 'Greek Seafood', 'avg_price': 65, 'rating': 4.8, 'budget_level': 'eleve', 'description': 'Fresh octopus and sunset views from Oia castle', 'image': 'https://picsum.photos/seed/kastro/600/400'},
                        ],
                        'activities': [
                            {'name': 'Caldera Sailing Sunset Cruise', 'category': 'aventure', 'price': 85, 'duration': '5 hours', 'rating': 4.9, 'description': 'Catamaran cruise with BBQ and sunset', 'image': 'https://picsum.photos/seed/caldera/600/400'},
                            {'name': 'Akrotiri Archaeological Site', 'category': 'culture', 'price': 12, 'duration': '2 hours', 'rating': 4.6, 'description': 'Minoan Bronze Age city preserved by volcanic eruption', 'image': 'https://picsum.photos/seed/akrotiri/600/400'},
                        ],
                        'monuments': [
                            {'name': 'Oia Village Blue Domes', 'monument_type': 'Landmark', 'entry_price': 0, 'rating': 4.9, 'description': 'The most photographed view in Greece', 'image': 'https://picsum.photos/seed/oia/600/400'},
                        ],
                    },
                    {
                        'name': 'Athens', 'tag': 'History', 'budget_level': 'moyen',
                        'rating': 4.6, 'popularity': 700,
                        'description': "The world's oldest city and birthplace of democracy.",
                        'image': 'https://picsum.photos/seed/athens/800/600',
                        'hotels': [
                            {'name': 'Hotel Grande Bretagne', 'stars': 5, 'price_per_night': 350, 'rating': 4.8, 'budget_level': 'eleve', 'description': 'Historic landmark hotel facing Syntagma Square', 'image': 'https://picsum.photos/seed/hotel22/600/400'},
                        ],
                        'restaurants': [
                            {'name': 'Nolan Athens', 'cuisine_type': 'Greek-Asian Fusion', 'avg_price': 55, 'rating': 4.7, 'budget_level': 'eleve', 'description': 'Creative cuisine with Acropolis views', 'image': 'https://picsum.photos/seed/nolan/600/400'},
                        ],
                        'activities': [
                            {'name': 'Acropolis & Parthenon Tour', 'category': 'culture', 'price': 20, 'duration': '3 hours', 'rating': 4.9, 'description': 'Guided tour of the ancient citadel above Athens', 'image': 'https://picsum.photos/seed/acropolis/600/400'},
                        ],
                        'monuments': [
                            {'name': 'The Parthenon', 'monument_type': 'Temple', 'entry_price': 20, 'rating': 4.9, 'description': 'Ancient Greek temple dedicated to goddess Athena', 'image': 'https://picsum.photos/seed/parthenon/600/400'},
                        ],
                    },
                ],
            },
            {
                'country': {
                    'name': 'Algeria', 'flag': '🇩🇿', 'capital': 'Algiers',
                    'language': 'Arabic / French', 'currency': 'Dinar (DZD)', 'climate': 'Arid / Mediterranean',
                    'continent': 'Africa', 'population': 45, 'rating': 4.5,
                    'best_season': 'Oct-Apr', 'avg_daily': '$30-60',
                    'visa_type': 'Required',
                    'description': "Algeria is Africa's largest country, offering Roman ruins and Saharan dunes.",
                    'image': 'https://picsum.photos/seed/algeria/800/600',
                },
                'cities': [
                    {
                        'name': 'Algiers', 'tag': 'Culture', 'budget_level': 'budget',
                        'rating': 4.3, 'popularity': 400,
                        'description': 'La Blanche — the white city cascading over the Mediterranean.',
                        'image': 'https://picsum.photos/seed/algiers/800/600',
                        'hotels': [
                            {'name': 'Sofitel Algiers Hamma Garden', 'stars': 5, 'price_per_night': 180, 'rating': 4.6, 'budget_level': 'eleve', 'description': 'Luxury tower overlooking the Bay of Algiers', 'image': 'https://picsum.photos/seed/hotel23/600/400'},
                            {'name': 'Hotel Albert 1er', 'stars': 3, 'price_per_night': 55, 'rating': 4.2, 'budget_level': 'moyen', 'description': 'Central hotel near the Casbah and sea', 'image': 'https://picsum.photos/seed/hotel24/600/400'},
                        ],
                        'restaurants': [
                            {'name': 'Le Tantonville', 'cuisine_type': 'French-Algerian', 'avg_price': 25, 'rating': 4.5, 'budget_level': 'moyen', 'description': 'Classic brasserie in the heart of Algiers', 'image': 'https://picsum.photos/seed/tantonville/600/400'},
                        ],
                        'activities': [
                            {'name': 'Casbah of Algiers Tour', 'category': 'culture', 'price': 15, 'duration': '3 hours', 'rating': 4.6, 'description': 'UNESCO World Heritage Ottoman medina', 'image': 'https://picsum.photos/seed/casbah/600/400'},
                        ],
                        'monuments': [
                            {'name': "Notre-Dame d'Afrique", 'monument_type': 'Basilica', 'entry_price': 0, 'rating': 4.5, 'description': 'Stunning neo-Byzantine basilica overlooking the sea', 'image': 'https://picsum.photos/seed/ndafrique/600/400'},
                        ],
                    },
                ],
            },
            {
                'country': {
                    'name': 'Spain', 'flag': '🇪🇸', 'capital': 'Madrid',
                    'language': 'Spanish', 'currency': 'Euro (€)', 'climate': 'Mediterranean',
                    'continent': 'Europe', 'population': 47, 'rating': 4.8,
                    'best_season': 'Apr-Jun & Sep-Oct', 'avg_daily': '$90-130',
                    'visa_type': 'Schengen Visa',
                    'description': 'Spain captivates with flamenco rhythms, Gaudi architecture and tapas culture.',
                    'image': 'https://picsum.photos/seed/spain/800/600',
                },
                'cities': [
                    {
                        'name': 'Barcelona', 'tag': 'Architecture', 'budget_level': 'moyen',
                        'rating': 4.8, 'popularity': 1000,
                        'description': "Gaudi's city — where Gothic meets Art Nouveau on the Mediterranean.",
                        'image': 'https://picsum.photos/seed/barcelona/800/600',
                        'hotels': [
                            {'name': 'Hotel Arts Barcelona', 'stars': 5, 'price_per_night': 400, 'rating': 4.8, 'budget_level': 'eleve', 'description': 'Ritz-Carlton tower overlooking the Olympic marina', 'image': 'https://picsum.photos/seed/hotel25/600/400'},
                            {'name': 'Generator Barcelona', 'stars': 2, 'price_per_night': 30, 'rating': 4.4, 'budget_level': 'budget', 'description': 'Design hostel in Gracia with rooftop bar', 'image': 'https://picsum.photos/seed/hotel26/600/400'},
                        ],
                        'restaurants': [
                            {'name': 'Tickets', 'cuisine_type': 'Avant-garde Tapas', 'avg_price': 80, 'rating': 4.9, 'budget_level': 'eleve', 'description': "Albert Adria's playful tapas bar", 'image': 'https://picsum.photos/seed/tickets/600/400'},
                            {'name': 'Bar Mut', 'cuisine_type': 'Catalan', 'avg_price': 40, 'rating': 4.7, 'budget_level': 'moyen', 'description': 'Upscale Eixample tapas bar', 'image': 'https://picsum.photos/seed/barmut/600/400'},
                        ],
                        'activities': [
                            {'name': 'Sagrada Familia Guided Tour', 'category': 'culture', 'price': 26, 'duration': '1.5 hours', 'rating': 4.9, 'description': "Gaudi's unfinished masterpiece", 'image': 'https://picsum.photos/seed/sagrada/600/400'},
                            {'name': 'Gothic Quarter Walking Tour', 'category': 'culture', 'price': 15, 'duration': '2 hours', 'rating': 4.7, 'description': 'Medieval labyrinth with Roman ruins', 'image': 'https://picsum.photos/seed/gothic/600/400'},
                        ],
                        'monuments': [
                            {'name': 'Sagrada Familia', 'monument_type': 'Cathedral', 'entry_price': 26, 'rating': 4.9, 'description': "Gaudi's magnum opus — under construction since 1882", 'image': 'https://picsum.photos/seed/sagrada2/600/400'},
                            {'name': 'Park Guell', 'monument_type': 'Park', 'entry_price': 10, 'rating': 4.7, 'description': 'Mosaic wonderland with panoramic views', 'image': 'https://picsum.photos/seed/guell/600/400'},
                        ],
                    },
                ],
            },
            {
                'country': {
                    'name': 'Turkey', 'flag': '🇹🇷', 'capital': 'Ankara',
                    'language': 'Turkish', 'currency': 'Lira (TRY)', 'climate': 'Mediterranean/Continental',
                    'continent': 'Europe/Asia', 'population': 84, 'rating': 4.7,
                    'best_season': 'Apr-Jun & Sep-Nov', 'avg_daily': '$50-90',
                    'visa_type': 'e-Visa Required',
                    'description': 'Turkey bridges two continents — Byzantine churches, Ottoman mosques and turquoise Aegean coasts.',
                    'image': 'https://picsum.photos/seed/turkey/800/600',
                },
                'cities': [
                    {
                        'name': 'Istanbul', 'tag': 'Culture', 'budget_level': 'moyen',
                        'rating': 4.8, 'popularity': 900,
                        'description': 'Where Europe meets Asia — minarets, bazaars and Bosphorus magic.',
                        'image': 'https://picsum.photos/seed/istanbul/800/600',
                        'hotels': [
                            {'name': 'Four Seasons Sultanahmet', 'stars': 5, 'price_per_night': 500, 'rating': 4.9, 'budget_level': 'eleve', 'description': 'Former Ottoman prison converted to luxury', 'image': 'https://picsum.photos/seed/hotel27/600/400'},
                            {'name': 'Vault Karakoy', 'stars': 4, 'price_per_night': 150, 'rating': 4.7, 'budget_level': 'moyen', 'description': 'Design hotel in a converted bank vault', 'image': 'https://picsum.photos/seed/hotel28/600/400'},
                        ],
                        'restaurants': [
                            {'name': 'Mikla Restaurant', 'cuisine_type': 'New Anatolian', 'avg_price': 80, 'rating': 4.8, 'budget_level': 'eleve', 'description': 'Rooftop panoramic restaurant redefining Turkish cuisine', 'image': 'https://picsum.photos/seed/mikla/600/400'},
                            {'name': 'Karakoy Gulluoglu', 'cuisine_type': 'Turkish Bakery', 'avg_price': 8, 'rating': 4.7, 'budget_level': 'budget', 'description': "Istanbul's finest baklava since 1949", 'image': 'https://picsum.photos/seed/baklava/600/400'},
                        ],
                        'activities': [
                            {'name': 'Bosphorus Sunset Cruise', 'category': 'aventure', 'price': 30, 'duration': '2 hours', 'rating': 4.8, 'description': 'Boat cruise between Europe and Asia at golden hour', 'image': 'https://picsum.photos/seed/bosphorus/600/400'},
                            {'name': 'Grand Bazaar Shopping Tour', 'category': 'culture', 'price': 20, 'duration': '3 hours', 'rating': 4.6, 'description': "Navigate 4,000 shops in the world's oldest covered market", 'image': 'https://picsum.photos/seed/grandbazaar/600/400'},
                        ],
                        'monuments': [
                            {'name': 'Hagia Sophia', 'monument_type': 'Mosque/Museum', 'entry_price': 0, 'rating': 4.9, 'description': '1,500 year old architectural marvel', 'image': 'https://picsum.photos/seed/hagiasophia/600/400'},
                            {'name': 'Blue Mosque', 'monument_type': 'Mosque', 'entry_price': 0, 'rating': 4.8, 'description': 'Six minarets and 20,000 blue Iznik tiles', 'image': 'https://picsum.photos/seed/bluemosque/600/400'},
                        ],
                    },
                ],
            },
        ]

        for entry in data:
            cd = entry['country']
            country = Country.objects.create(
                name=cd['name'], flag=cd['flag'], capital=cd['capital'],
                language=cd['language'], currency=cd['currency'],
                climate=cd['climate'], continent=cd['continent'],
                population=cd['population'], rating=cd['rating'],
                best_season=cd['best_season'], avg_daily=cd['avg_daily'],
                visa_type=cd['visa_type'], description=cd['description'],
                image=cd['image'], is_active=True,
            )
            self.stdout.write(f'  OK {country.name}')

            for cdata in entry['cities']:
                city = City.objects.create(
                    country=country,
                    name=cdata['name'], tag=cdata['tag'],
                    budget_level=cdata['budget_level'],
                    rating=cdata['rating'], popularity=cdata['popularity'],
                    description=cdata['description'],
                    image=cdata['image'], is_active=True,
                )
                for h in cdata.get('hotels', []):
                    Hotel.objects.create(city=city, is_active=True, **h)
                for r in cdata.get('restaurants', []):
                    Restaurant.objects.create(city=city, is_active=True, **r)
                for a in cdata.get('activities', []):
                    Activity.objects.create(city=city, is_active=True, **a)
                for m in cdata.get('monuments', []):
                    Monument.objects.create(city=city, is_active=True, **m)
                self.stdout.write(f'     -> {city.name}')