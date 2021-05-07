import datetime
def context_procesor(request):
    return{'year':datetime.datetime.now().year}