from .forms import GigCreationForm , ShowcaseForm
from django.http.response import Http404
from django.shortcuts import redirect, render
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

def create_gig(request):
    if request.method == 'POST':
        g_form = GigCreationForm(request.POST)
        img_form = ShowcaseForm(request.POST, request.FILES)
        if g_form.is_valid() and img_form.is_valid():
            g_form.save(commit=False).user = request.user
            gig = g_form.save()
            img_form.save(commit=False).gig = gig 
            img_form.save()
            return redirect('gig_index')
    else:
         g_form = GigCreationForm()
         img_form = ShowcaseForm()

    return render(request,"gigs/create_gig.html",context={'g_form':g_form, 'img_form':img_form})