from django.contrib.sitemaps import GenericSitemap
from main.models import MainPageConfig

mainpage = {
    'queryset': MainPageConfig.objects.all(),
    'date_field': 'updated',
}

about = {

}

blog = {

}

blog_detail = {

}

business_account = {

}

employment_opportunities = {

}

get_in_touch = {

}

media = {

}

products = {

}

products_detail = {

}

questions = {

}

support = {

}

retail = {

}

online_shop = {

}

international = {
    
}




site_sitemaps = {
    'main': GenericSitemap(mainpage, changefreq='daily', priority=1),
}
