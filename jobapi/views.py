from django.http import HttpResponse
from processor import job

def index(request):
    query_param_value = request.GET.get('job')
    if query_param_value is None:
        return HttpResponse("Request parameter is missing!", status=400)
    
    kv_pair = query_param_value.split(None, 1)
    if len(kv_pair) != 2:
        return HttpResponse(f"Invalid paramater format {kv_pair}, size {len(kv_pair)}!", status=400)

    if kv_pair[0] == "INSERT" :
        rawfields = kv_pair[1].split(",")
        fields = remove_quotes_in_list(rawfields)
        if len(fields) == 3:
            return HttpResponse(job.insert(fields[0], fields[1], fields[2]))
        
        return HttpResponse(f"Invalid number of fields for {kv_pair[0]}!", status=400)

    elif kv_pair[0] == "DELETE" :
        rawfields = kv_pair[1].split(",")
        fields = remove_quotes_in_list(rawfields)
        if len(fields) == 1 :
            return HttpResponse(job.delete(fields[0], None, None))
        elif len(fields) == 2 :
            return HttpResponse(job.delete(fields[0], fields[1], None))
        elif len(fields) == 3 :
            return HttpResponse(job.delete(fields[0], fields[1], fields[2]))
        
        return HttpResponse(f"Invalid number of fields for {kv_pair[0]}!", status=400)

    elif query_param_value.startswith("UPDATE"):
        rawfields = kv_pair[1].split(",")
        fields = remove_quotes_in_list(rawfields)
        if len(fields) == 3 :
            return HttpResponse(job.update(fields[0], None, None, fields[1], fields[2]))
        elif len(fields) == 4 :
            return HttpResponse(job.update(fields[0], fields[1], None, fields[2], fields[3]))
        elif len(fields) == 5 :
            return HttpResponse(job.update(fields[0], fields[1], fields[2], fields[3], fields[4]))
        
        return HttpResponse(f"Invalid number of fields for {kv_pair[0]}!", status=400)
    
    return HttpResponse(f"Invalid operation {query_param_value}!", status=400)

def remove_quotes(input):
    if not input:
        return
    return input.strip("'").strip('"')

def remove_quotes_in_list(rawfields):
    fields = []
    for field in rawfields:
        fields.append(remove_quotes(field))
    
    return fields