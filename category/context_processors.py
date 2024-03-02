from .models import Category

# returns a dictionary that can be used in templates
def menu_links(request):
    links = Category.objects.all()
    return dict(links = links)
