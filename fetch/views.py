from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from fetch.bing_search import run_query
from django.contrib.auth.models import User


from fetch.models import MasterUser
from fetch.forms import UserForm


def index(request):
    return render(request, 'fetch/index.html')


def register(request):
    registered = False

    if request.method == 'POST':
        user_form = UserForm(data=request.POST)

        if user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            registered = True

        else:
            print user_form.errors

    else:
        user_form = UserForm()

    return render(request,
                  'fetch/register.html',
                  {'user_form': user_form, 'registered': registered})


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/fetch/')
            else:
                return HttpResponse("your fetch account is disabled")
        else:
            print "invalid login details: {0}, {1}".format(username, password)
            return HttpResponse("Invalid login details supplied")
    else:
        return render(request, 'fetch/login.html', {})
        
        
        
        
def masteruser(request, masteruser_username_slug):
    context_dict = {}
    context_dict['result_list'] = None
    context_dict['query'] = None
    if request.method == 'POST':
        query = request.POST['query'].strip()

        if query:
            result_list = run_query(query)

            context_dict['result_list'] = result_list
            context_dict['query'] = query
    try:
        masteruser = MasterUser.objects.get(slug=masteruser_username_slug)
        context_dict['masteruser_username'] = MasterUser.username
        context_dict['masteruser'] = masteruser
    except MasterUser.DoesNotExist:
        pass

    if not context_dict['query']:
        context_dict['query'] = masteruser.username

    return render(request, 'fetch/masteruser.html', context_dict)





def search(request):

    context_dict={}

    if request.method == 'POST':
        query = request.POST['query'].strip()

        result_list = User.objects.filter(username=query)
        context_dict['result_list'] = result_list
        print result_list

    return render(request,'fetch/search.html',context_dict)


# def search(request):
# 	UserName = MasterUser.objects.filter(username="Abin")
# 
#         # Adds our results list to the template context under name pages.
#         context_dict['username'] = Username
# 	
# 	
#     return render(request, 'fetch/login.html', context_dict) 

#         
# def search(request):
# 
#     result_list = []
# 
#     if request.method == 'POST':
#         query = request.POST['query'].strip()
# 
#         if query:
#             # Run our Bing function to get the results list!
#             result_list = run_query(query)
# 
#     return render(request, 'rango/search.html', {'result_list': result_list})

# 3.8new
def forgetPassword(request):
    # 	if request.method == 'POST':
    #     		username = request.POST.get('username')
    #     		user = authenticate(username=username)
    #
    #         if user:
    #             if username.is_active:
    #                 forgetPassword(request, username)
    #                 return HttpResponseRedirect("We would send a confirm to your email.")

    return render(request, 'registration/password_reset_email.html', {})










@login_required
def restricted(request):
    return HttpResponse("Since you're logged in, you can see this text!")


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/fetch/')
