from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from .forms import GigCreationForm, GigEditForm, ShowcaseForm, CommentForm, PlanForm, PlanEditForm
from django.http.response import Http404
from django.shortcuts import redirect, render
from .models import Comment, Gig, Plan, ShowcaseImage
from django.core.exceptions import PermissionDenied
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

# Create your views here.
def gig_index(request):
    gigs = Gig.objects.all()
    context = {"gigs": gigs}
    return render(request, "gigs/index.html", context=context)


class GigDetail(generic.DetailView):
    model = Gig
    template_name = "gigs/gig.html"
    extra_context = {}

    def get(self, *args, **kwargs):
        super().get(self, *args, **kwargs)
        gig = Gig.objects.get(id=self.kwargs["pk"])
        photo = ShowcaseImage.get_images(gig=gig)
        self.extra_context.update({"photo": photo})
        return super().get(self, *args, **kwargs)


class AddComment(generic.CreateView, LoginRequiredMixin):
    model = Comment
    form_class = CommentForm

    def form_valid(self, form):
        gig_id = self.request.GET.get("gig")
        gig = Gig.objects.get(id=gig_id)
        form.save(commit=False).user = self.request.user
        form.save(commit=False).gig = gig
        form.save()
        return redirect("gig_detail", gig_id)


class AddPlan(generic.CreateView, LoginRequiredMixin):
    model = Plan
    form_class = PlanForm

    def form_valid(self, form):
        gig_id = self.request.GET.get("gig")
        gig = Gig.objects.get(id=gig_id)
        form.save(commit=False).gig = gig
        form.save()
        return redirect("gig_detail", gig_id)


# def add_image(request, gig_id):
#     try:
#         gig = Gig.objects.get(id=gig_id)
#         img_formset = modelformset_factory(ShowcaseImage, form=ShowcaseForm, extra=5)
#         photo = ShowcaseImage.get_images(gig)
#         if request.method == "POST":
#             formset = img_formset(request.POST, request.FILES, queryset=ShowcaseImage.objects.none())
#             p_form = PlanForm(request.POST)
#             c_form = CommentForm(request.POST)
#             if c_form.is_valid():
#                 c_form.save(commit=False).user = request.user
#                 c_form.save(commit=False).gig = gig
#                 c_form.save()
#                 return redirect("gig_info", gig_id=gig.id)
#             if p_form.is_valid():
#                 p_form.save(commit=False).gig = gig
#                 p_form.save()
#                 return redirect("gig_info", gig_id=gig.id)
#             if formset.is_valid():
#                 for form in formset:
#                     form.save(commit=False).gig = gig
#                     form.save()
#                 return redirect("gig_info", gig_id=gig.id)

#         else:
#             p_form = PlanForm()
#             c_form = CommentForm()
#             formset = img_formset(queryset=ShowcaseImage.objects.none())

#     except Gig.DoesNotExist:
#         raise Http404("Gig not found")

#     return render(
#         request,
#         "gigs/gig.html",
#         context={
#             "gig": gig,
#             "c_form": c_form,
#             "p_form": p_form,
#             "formset": formset,
#             "photo": photo,
#         },
#     )


@login_required
def create_gig(request):
    if request.method == "POST":
        g_form = GigCreationForm(request.POST)
        img_form = ShowcaseForm(request.POST, request.FILES)
        if g_form.is_valid() and img_form.is_valid():
            g_form.save(commit=False).user = request.user
            gig = g_form.save()
            img_form.save(commit=False).gig = gig
            img_form.save()
            return redirect("gig_detaile", pk=gig.id)
    else:
        g_form = GigCreationForm()
        img_form = ShowcaseForm()

    return render(request, "gigs/create_gig.html", context={"g_form": g_form, "img_form": img_form})


def show_category(request, category_id):
    try:
        gigs = Gig.objects.filter(category__id=category_id)
        context = {"gigs": gigs}
        return render(request, "gigs/category.html", context=context)
    except Gig.DoesNotExist:
        raise Http404("there is no gig in this category")


@csrf_exempt
@require_POST
def comment_aprove(request):
    cid = request.POST["id"]
    comment = Comment.objects.get(id=cid)
    comment.is_approved = True
    comment.save()
    return redirect("gig_detail", pk=comment.gig.id)


@login_required
def edit_gig(request, gigid):
    gig = Gig.objects.get(id=gigid)
    if gig.user != request.user:
        raise PermissionDenied
    if request.method == "POST":
        form = GigEditForm(request.POST, instance=gig)
        if form.is_valid():
            form.save()
            return redirect("gig_detail", gig_id=gigid)
    else:
        form = GigEditForm(instance=gig)
    return render(request, "gigs/gig_edit.html", context={"form": form, "gig": gig})


@login_required
def edit_plan(request, planid):
    plan = Plan.objects.get(id=planid)
    if plan.gig.user != request.user:
        raise PermissionDenied
    if request.method == "POST":
        form = PlanEditForm(request.POST, instance=plan)
        if form.is_valid():
            form.save()
            return redirect("gig_detail", pk=plan.gig.id)
    else:
        form = PlanEditForm(instance=plan)
    return render(request, "gigs/edit_plan.html", context={"form": form, "plan": plan})
