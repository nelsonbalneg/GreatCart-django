from .models import Category

#register this to settings
#this function will make each items into links
def menu_links(request):
    links = Category.objects.all()
    return dict(links=links)