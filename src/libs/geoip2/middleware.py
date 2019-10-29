from .utils import get_country_info

DEFAULT_COUNTRY = 'US'
AVAILABLE_COUNTRIES = ['US', 'CA', 'IL',]


class GeoIP2Middleware:
    @staticmethod
    def process_request(request):
        if request.COOKIES.get('country'):
            country = request.COOKIES.get('country')
        else:
            country = get_country_info(request)

        request.META['GEOIP_COUNTRY'] = country if country in AVAILABLE_COUNTRIES else DEFAULT_COUNTRY
