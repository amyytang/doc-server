from django.http import HttpResponse

def index(request):
    query_param_value = request.GET.get('job')
    return HttpResponse(f"The value of param_name is: {query_param_value}")
