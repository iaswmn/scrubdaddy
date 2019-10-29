from django.conf import settings
from appconf import AppConf


class IpInfoAppConf(AppConf):
    META_KEY = 'IP_INFO'
    CACHE_TIMEOUT = 0
    DB_TIMEOUT = 0
    # IPSTACK_KEY = '676204c4614b9aa1b3bf954fa9fc5e7a' #  ipstack@ya.ru | 123456zz
    IPSTACK_KEY = 'e75a1d7dff60e0f1a4aa085b5930a139'
