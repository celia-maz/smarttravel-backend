from .models import City, Recommendation

# ─── Interest → Tag mapping ───────────────────────────────────────────────────
INTEREST_TAGS = {
    'Culture':      ['culture', 'histoire', 'art', 'museum'],
    'Nature':       ['nature', 'plage', 'montagne', 'parc'],
    'Gastronomie':  ['gastronomie', 'cuisine', 'food'],
    'Shopping':     ['shopping', 'marché', 'bazaar'],
    'Sport':        ['sport', 'aventure', 'outdoor'],
    'Aventure':     ['aventure', 'trek', 'safari'],
    'History':      ['histoire', 'culture', 'monument'],
    'Art':          ['art', 'culture', 'musée'],
    'Photography':  ['nature', 'architecture', 'paysage'],
    'Beach':        ['plage', 'mer', 'nature'],
    'Nightlife':    ['nightlife', 'animation'],
    'Traditions':   ['culture', 'tradition'],
}

BUDGET_MAP = {
    'economique': 'economique',
    'moyen':      'moyen',
    'eleve':      'eleve',
}

def score_city(city, user):
    """
    Score a city for a user based on multiple criteria.
    Returns a float score between 0 and 100.
    """
    score = 0.0
    reasons = []

    # 1. Popularity score (0-20 pts)
    popularity_score = min(city.popularity / 100 * 20, 20)
    score += popularity_score

    # 2. Rating score (0-20 pts)
    rating_score = (city.rating / 5) * 20
    score += rating_score

    # 3. Budget match (0-25 pts)
    user_budget = user.budget
    if city.budget_level == user_budget:
        score += 25
        reasons.append('Budget match')
    elif (user_budget == 'eleve' and city.budget_level == 'moyen') or \
         (user_budget == 'moyen' and city.budget_level == 'economique'):
        score += 10
        reasons.append('Budget close match')

    # 4. Interest match (0-35 pts)
    user_interests = user.interests or []
    city_tag = (city.tag or '').lower()
    matched_interests = 0

    for interest in user_interests:
        tags = INTEREST_TAGS.get(interest, [])
        if any(tag in city_tag for tag in tags):
            matched_interests += 1

    if user_interests:
        interest_score = (matched_interests / len(user_interests)) * 35
        score += interest_score
        if matched_interests > 0:
            reasons.append(f'Matches {matched_interests} of your interests')

    return round(score, 2), reasons


def get_recommendations(user, limit=10):
    """
    Get top recommended cities for a user.
    Saves recommendations to DB and returns them.
    """
    cities = City.objects.filter(is_active=True).select_related('country')

    scored = []
    for city in cities:
        score, reasons = score_city(city, user)
        scored.append((city, score, reasons))

    # Sort by score descending
    scored.sort(key=lambda x: x[1], reverse=True)
    top = scored[:limit]

    # Save to DB
    recommendations = []
    for city, score, reasons in top:
        rec, _ = Recommendation.objects.update_or_create(
            user=user, city=city,
            defaults={'score': score, 'reasons': reasons}
        )
        recommendations.append(rec)

    return recommendations