from django.shortcuts import render
from django.http import HttpResponse
from companywebsite.models import Category
from companywebsite.models import Page
from companywebsite.forms import CategoryForm, PageForm
from django.shortcuts import redirect
from django.urls import reverse

def index(request):
    # Query the database for all categories
    category_list = Category.objects.all()  

    # Create a context dictionary
    context_dict = {
        'boldmessage': 'Welcome to UENO INTERNATIONAL CORPORATION',
        'categories': category_list,  # Pass categories to the template
    }
    request.session.set_test_cookie()

    # Render the response and send it back!
    return render(request, 'companywebsite/index.html', context=context_dict)

def about(request):
    context_dict = {'message': "More about UENO."}
    
    if request.session.test_cookie_worked(): 
        print("TEST COOKIE WORKED!") 
        request.session.delete_test_cookie()

    return render(request, 'companywebsite/about.html', context=context_dict)


def show_category(request, category_name_slug):
    context_dict = {}
    try:
        category = Category.objects.get(slug=category_name_slug)
        pages = Page.objects.filter(category=category)

        context_dict['pages'] = pages
        context_dict['category'] = category
    except Category.DoesNotExist:

        context_dict['category'] = None
        context_dict['pages'] = None
    return render(request, 'companywebsite/category.html', context=context_dict)

def add_category(request): 
    form = CategoryForm()
    
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        
        if form.is_valid():
            form.save(commit=True)  
            return redirect('companywebsite:index')
        else:
            print(form.errors)
    return render(request, 'companywebsite/add_category.html', {'form': form})


def add_page(request, category_name_slug):
    try:
        category = Category.objects.get(slug=category_name_slug)
    except Category.DoesNotExist:
        category = None

    # If the category doesn't exist, redirect to the index page
    if category is None:
        return redirect('companywebsite:index')

    form = PageForm()

    if request.method == 'POST':
        form = PageForm(request.POST)
        if form.is_valid():
            if category:
                page = form.save(commit=False)
                page.category = category
                page.views = 0
                page.save()
                return redirect(reverse('companywebsite:show_category', kwargs={'category_name_slug': category_name_slug}))
        else:
            print(form.errors)  # Debugging: Show form errors in the console

    context_dict = {'form': form, 'category': category}
    return render(request, 'companywebsite/add_page.html', context=context_dict)