from django.template import Library, loader
from ..models import BlogPost

register = Library()


@register.simple_tag(takes_context=True)
def blog_block(context):
    request = context.get('request')
    return loader.render_to_string('blog/block.html', {
        'posts': BlogPost.objects.filter(visible=True)[:4],
    }, request=request)