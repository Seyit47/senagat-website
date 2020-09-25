from django.conf import settings

def get_pagination(page, count, limit = 5):
    try:
        page = int(page)
    except:
        page = 1
        
    lastpage = count // limit + (1 if count % limit > 0 else 0)

    page = 1 if page > lastpage or page < 1 else page
    prv = page - 1 if page - 1 > 0    else page
    nxt = page + 1 if page < lastpage else page
    l = min(page - 1, max(2, 4 - lastpage + page))
    r = min(max(2, 5 - page), lastpage - page)
    pages = [i for i in range(page - l , page + r + 1)]
    return {
        'page': page,
        'prv': prv,
        'nxt': nxt,
        'lastpage': lastpage,
        'pages': pages    
    }

def get_day_time(date):
    h = date.hour
    if h >= 5 and h < 8:
        return 'morning'
    elif h >= 8 and h < 11:
        return 'noon'
    elif h >= 11 and h < 17:
        return 'afternoon'
    elif h >= 17 and h < 20:
        return 'evening'
    elif h >= 20 and h < 22:
        return 'night'
    elif h >= 22 and h < 5:
        return 'midnight'
    return 'afternoon'

