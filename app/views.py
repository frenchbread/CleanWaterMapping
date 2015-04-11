from django.shortcuts import get_object_or_404, RequestContext, render_to_response
from django.core.context_processors import csrf
from app.forms import PointsForm
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse


def home(request):

    args = {}
    args.update(csrf(request))

    template = 'main.html'
    context = RequestContext(request)

    return render_to_response(template, args, context_instance=context)


def newpoint(request):

    args = {}
    args.update(csrf(request))

    if request.POST:
        form = PointsForm(request.POST, request.FILES)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user
            form.save()

            return HttpResponseRedirect(reverse('home'))
    else:
        form = PointsForm()

    args.update({'f': form})

    template = 'newsample.html'
    context = RequestContext(request)

    return render_to_response(template, args, context_instance=context)