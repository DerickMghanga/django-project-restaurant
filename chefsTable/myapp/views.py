from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render


# create your views here.
def home(request):
    path = request.path
    scheme = request.scheme
    method = request.method
    address = request.META['REMOTE_ADDR']
    user_agent = request.META['HTTP_USER_AGENT']
    path_info = request.path_info

    response = HttpResponse()
    response.headers['Age'] = 20
    
    msg = f"""<br>
        <br>Path: {path}
        <br>Address: {address}
        <br>Scheme: {scheme}
        <br>Method: {method}
        <br>User agent: {user_agent}
        <br>Path Info: {path_info}
        <br>Response header: {response.headers}
    """
    return HttpResponse(msg, content_type='text/html', charset='utf-8')

def menuitems(request, dish):
    items = {
        'pasta': 'Pasta is type of noddle',
        'falafel': 'These are deep fried patties',
        'cheesecake': 'Is a type of dessert made of cream, soft cheese on top of cookie',
    }

    # Url parameter(dish) passed is matched to the below function
    description = items[dish]

    return HttpResponse(f"<h2>{dish}</h2>" + description)
