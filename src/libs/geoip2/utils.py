from ipware.utils import is_valid_ipv4
import geoip2.database


def get_country_info(request):
    if not request:
        return None
    country = request.META.get('GEOIP_COUNTRY')

    if country is not None:
        return country

    ip_addresses = [
        request.META.get('HTTP_CF_CONNECTING_IP'),
        request.META.get('REMOTE_ADDR')
    ]

    country = None
    for ip in ip_addresses:
        if isinstance(ip, str) and is_valid_ipv4(ip):
            reader = geoip2.database.Reader('libs/geoip2/GeoLite2-Country.mmdb')
            try:
                response = reader.country(ip)
                country = response.country.iso_code
            except geoip2.errors.AddressNotFoundError as e:
                pass
                # print(e)
    return country
