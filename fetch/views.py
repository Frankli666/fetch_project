from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from fetch.bing_search import run_query

# from rango.models import Category
# from rango.models import Page
# from rango.models import UserProfile
# from rango.forms import UserForm, UserProfileForm
# from rango.forms import CategoryForm, PageForm
# from django.contrib.auth import authenticate, login, logout
# from django.http import HttpResponseRedirect
# from django.contrib.auth.decorators import login_required
# from datetime import datetime
# from rango.bing_search import run_query
# from django.contrib.auth.models import User
# from django.shortcuts import redirect

from fetch.models import Sharer, Getter, Connection
from fetch.forms import UserForm

def index(request):
    return render(request, 'fetch/index.html')
	

def register(request):
    registered =False

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
        
def search(request):

    result_list = []

    if request.method == 'POST':
        query = request.POST['query'].strip()

        if query:
            # Run our Bing function to get the results list!
            result_list = run_query(query)

    return render(request, 'fetch/search.html', {'result_list': result_list}) 

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


def track_url(request):
    context = RequestContext(request)
    page_id = None
    url = '/fetch/'
    if request.method == 'GET':
        if 'page_id' in request.GET:
            page_id = request.GET['page_id']
            try:
                page = Page.objects.get(id=page_id)
                page.views = page.views + 1
                page.save()
                url = page.url
            except:
                pass

    return redirect(url)
    
def add_category(request):
    # Get the context from the request.
    context = RequestContext(request)
    cat_list = get_category_list()
    context_dict = {}
    context_dict['cat_list'] = cat_list
    
    # A HTTP POST?
    if request.method == 'POST':
        form = CategoryForm(request.POST)

        # Have we been provided with a valid form?
        if form.is_valid():
            # Save the new category to the database.
            form.save(commit=True)

            # Now call the index() view.
            # The user will be shown the homepage.
            return index(request)
        else:
	        # The supplied form contained errors - just print them to the terminal.
            print form.errors
    else:
        # If the request was not a POST, display the form to enter details.
        form = CategoryForm()

    # Bad form (or form details), no form supplied...
    # Render the form with error messages (if any).
    context_dict['form'] = form
    return render_to_response('rango/add_category.html', context_dict, context)

@login_required
def add_page(request, category_name_url):
    context = RequestContext(request)
    cat_list = get_category_list()
    context_dict = {}
    context_dict['cat_list'] = cat_list

    category_name = decode_url(category_name_url)
    if request.method == 'POST':
        form = PageForm(request.POST)
        
        if form.is_valid():
            # This time we cannot commit straight away.
            # Not all fields are automatically populated!
            page = form.save(commit=False)

            # Retrieve the associated Category object so we can add it.
            try:
                cat = Category.objects.get(name=category_name)
                page.category = cat
            except Category.DoesNotExist:
                return render_to_response( 'rango/add_page.html',
                                          context_dict,
                                          context)

            # Also, create a default value for the number of views.
            page.views = 0

            # With this, we can then save our new model instance.
            page.save()

            # Now that the page is saved, display the category instead.
            return category(request, category_name_url)
        else:
            print form.errors
    else:
        form = PageForm()

    context_dict['category_name_url']= category_name_url
    context_dict['category_name'] =  category_name
    context_dict['form'] = form

    return render_to_response( 'rango/add_page.html',
                               context_dict,
                               context)

    
def profile(request):
    context = RequestContext(request)
    cat_list = get_category_list()
    context_dict = {'cat_list': cat_list}
    u = User.objects.get(username=request.user)
    
    try:
        up = UserProfile.objects.get(user=u)
    except:
        up = None
    
    context_dict['user'] = u
    context_dict['userprofile'] = up
    return render_to_response('rango/profile.html', context_dict, context)
	
	
	
@login_required
def restricted(request):
    return HttpResponse("Since you're logged in, you can see this text!")

@login_required
def user_logout(request):

    logout(request)
    return HttpResponseRedirect('/fetch/')
