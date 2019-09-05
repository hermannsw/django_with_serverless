from django.http import HttpResponse
from django.views.decorators.http import require_http_methods


@require_http_methods(["GET"])
def healthcheck(request):
    return HttpResponse('{"data":"data value"}')
