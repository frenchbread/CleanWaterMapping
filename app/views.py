from django.shortcuts import get_object_or_404, RequestContext, render_to_response
from django.core.context_processors import csrf


def home(request):

    args = {}
    args.update(csrf(request))

    template = 'main.html'
    context = RequestContext(request)

    return render_to_response(template, args, context_instance=context)
