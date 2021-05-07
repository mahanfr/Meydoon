from .forms import GigCreationForm , ShowcaseForm,CommentForm
from django.http.response import Http404
from django.shortcuts import redirect, render
from .models import Category, Comment, Gig
from django.urls import reverse
# Create your views here.
def gig_index(request):
    gigs = Gig.objects.all()
    categories = Category.objects.all()
    context = {'gigs':gigs}
    return render(request,'gigs/index.html',context=context)

def gig_view(request, gig_id):
    try:
        gig = Gig.objects.get(id=gig_id)
        comments =Comment.objects.filter(gig=gig)
        next_url = request.GET.get('next','/')
        
        if request.method == 'POST':
            c_form = CommentForm(request.POST)
            if c_form.is_valid():
                c_form.save(commit=False).user = request.user
                c_form.save(commit=False).gig = gig 
                c_form.save()
                return redirect('gig_info', gig_id=gig.id)
        else:
            c_form = CommentForm()
        
    except Gig.DoesNotExist:
        raise Http404('Gig not found')

    return render(request,'gigs/gig.html',context={"gig":gig,'c_form':c_form,'comments':comments})        

def create_gig(request):
    if request.method == 'POST':
        g_form = GigCreationForm(request.POST)
        img_form = ShowcaseForm(request.POST, request.FILES)
        if g_form.is_valid() and img_form.is_valid():
            g_form.save(commit=False).user = request.user
            gig = g_form.save()
            img_form.save(commit=False).gig = gig 
            img_form.save()
            return redirect('gig_info',gig_id=gig.id)
    else:
         g_form = GigCreationForm()
         img_form = ShowcaseForm()

    return render(request,"gigs/create_gig.html",context={'g_form':g_form, 'img_form':img_form})

def show_category(request,category_id):
    try:
        gigs = Gig.objects.filter(category__id=category_id)
        categories = Category.objects.all()
        context = {'gigs':gigs}
        return render(request,'gigs/category.html',context=context)
    except Gig.DoesNotExist:
        raise Http404('there is no gig in this category')

    
