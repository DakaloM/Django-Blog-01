def get_article_count(artlicle):
    sport_articles_count = artlicle.objects.filter(category='Sport').count()
    travel_articles_count = artlicle.objects.filter(category='Travel').count()
    nature_articles_count = artlicle.objects.filter(category='Nature').count()
    lifestyle_articles_count = artlicle.objects.filter(category='Lifestyle').count()
    other_articles_count = artlicle.objects.filter(category='Other').count()
            
    return {
        'sport_count': sport_articles_count,
        'travel_count': travel_articles_count,
        'nature_count': nature_articles_count,
        'lifestyle_count': lifestyle_articles_count,
        'other_count': other_articles_count
    }
   
    
def get_article_count_per_user(artlicle, user):
    sport_articles_count = artlicle.objects.filter(category='Sport', author=user).count()
    travel_articles_count = artlicle.objects.filter(category='Travel', author=user).count()
    nature_articles_count = artlicle.objects.filter(category='Nature', author=user).count()
    lifestyle_articles_count = artlicle.objects.filter(category='Lifestyle', author=user).count()
    other_articles_count = artlicle.objects.filter(category='Other', author=user).count()
            
    return {
        'sport_count': sport_articles_count,
        'travel_count': travel_articles_count,
        'nature_count': nature_articles_count,
        'lifestyle_count': lifestyle_articles_count,
        'other_count': other_articles_count
    }
   
    