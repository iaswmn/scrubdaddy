from .utils import get_request_info
from .conf import settings


class IPInfoMiddleware:
    @staticmethod
    def process_request(request):
        ipinfo = get_request_info(request)
        if ipinfo is not None:
            # Для тестирования региона
            overwrite_region = request.COOKIES.get('country')
            if overwrite_region:
                ipinfo.country = overwrite_region

            request.META[settings.IPINFO_META_KEY] = ipinfo
