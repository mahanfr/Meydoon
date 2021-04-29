from django.http.response import Http404
from django.shortcuts import render
from .models import Gig
# Create your views here.
def gig_index(request):
    gigs = Gig.objects.all()
    context = {'gigs':gigs}
    return render(request,'gigs/index.html',context=context)

def gig_view(request, gig_id):
    try:
        gig = Gig.objects.get(id=gig_id)
    except Gig.DoesNotExist:
        raise Http404('Gig not found')

    return render(request,'gigs/gig.html',context={"gig":gig})        


