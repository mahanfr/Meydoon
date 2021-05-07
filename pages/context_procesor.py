import datetime
from gigs.models import Category

def context_procesor(request):
    return{'year':datetime.datetime.now().year,'categories':Category.objects.all()}