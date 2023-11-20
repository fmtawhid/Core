from .models import postCatagory
def menu_links(request):
    links = postCatagory.objects.all()
    return dict(links = links)