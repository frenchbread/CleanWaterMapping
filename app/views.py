from django.shortcuts import get_object_or_404, RequestContext, render_to_response
from django.core.context_processors import csrf
from app.forms import PointsForm
from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.core.urlresolvers import reverse
from app.models import Point

def home(request):

    args = {}
    args.update(csrf(request))

    template = 'main.html'
    context = RequestContext(request)

    return render_to_response(template, args, context_instance=context)


def index(request):

    args = {}
    args.update(csrf(request))

    template = 'index.html'
    context = RequestContext(request)

    return render_to_response(template, args, context_instance=context)


def newpoint(request):

    args = {}
    args.update(csrf(request))

    if request.POST:
        form = PointsForm(request.POST, request.FILES)
        if form.is_valid():
            form = form.save(commit=False)
            #form.user = request.user
            form.save()

            return HttpResponseRedirect(reverse('home'))
    else:
        form = PointsForm()

    args.update({'f': form})

    template = 'newsample.html'
    context = RequestContext(request)

    return render_to_response(template, args, context_instance=context)


def point(request, point_id):

    args = {}
    args.update(csrf(request))
    p = get_object_or_404(Point, id=point_id)

    args.update({'p': p})
    template = 'point.html'
    context = RequestContext(request)
    return render_to_response(template, args, context_instance=context)


def mapp(request):

    context_vars = {}
    context_vars.update(csrf(request))

    p = Point.objects.all()

    template = 'mapp.html'
    context = RequestContext(request)
    context_vars.update({'p': p})
    return render_to_response(template, context_vars, context_instance=context)