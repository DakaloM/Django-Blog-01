def progress_tracker(article,  user,category):
    
    total_count = article.objects.all().count()
    count = article.objects.all().filter(author=user, category=category).count()
    
    if total_count > 0:
        progress = (count/total_count) * 100
        
    else:
        progress = 0 
    
    return progress