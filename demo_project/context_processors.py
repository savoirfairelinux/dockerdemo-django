from redis import Redis


redis = Redis(host='cache', port=6379)


def views_counter(request):
    return {
        'views_counter': redis.incr('views_counter'),
    }
