
from os import name
from django.conf.urls import url
from django.shortcuts import redirect, render, get_object_or_404
from requests.compat import quote_plus
from .models import Notice_board_details
from django.http import JsonResponse

BASE_URL = ''




def home(request):
    
    return render(request, 'base.html')
    
def new_search(request, url):
    obj = get_object_or_404(Notice_board_details, url=url)
    print(obj)
    final_url = BASE_URL.format(quote_plus(url))
    return redirect(final_url, target="_blank")

def search_result(request):
    if request.is_ajax():
        res = None
        uniName = request.POST.get('uniName')
        #print(Name)
        qs =Notice_board_details.objects.filter(uni_name__icontains = uniName)         
        #print(qs)
        if len(qs) > 0 and len(uniName) > 0:
            data =[]
            for pos in qs:
                item ={
                    'pk' : pos.pk,
                    'name' : pos.uni_name,
                    'category' : pos.uni_category,
                    'url' : pos.uni_url
                } 
            data.append(item)
            res = data
        else:
            res = "No University Found"

        return JsonResponse({'data' : res})
    return JsonResponse({})



