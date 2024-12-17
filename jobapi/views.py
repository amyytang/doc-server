from django.http import HttpResponse
from processor.query import query

def index(request):
    query_param_value = request.GET.get('job')
    if query_param_value is None:
        return HttpResponse("Request parameter is missing!", status=400)
    
    #result = job(query_param_value)
    result = query(query_param_value)
    return HttpResponse(result)
