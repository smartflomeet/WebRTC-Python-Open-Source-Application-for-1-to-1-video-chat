from django.conf import settings

def video_settings(request):
    # return any necessary values
    return {
        'API_URL': settings.API_URL,
        'APP_ID': settings.APP_ID,
        'APP_KEY': settings.APP_KEY,
    }