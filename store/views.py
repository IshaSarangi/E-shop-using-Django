from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password, check_password
from .models.product import Product
from .models.category import Category
from .models.customer import Customer

# print(make_password('1234'))
# print(check_password('1234','pbkdf2_sha256$320000$BXfmD5ytn1Fb37zTnrcBCV$OOOtkKATefBN22pXi6m9iVnw6G236Vt17vurE2gXJqg='))

# Create your views here.
# def index(request):
#     return HttpResponse('<H1> Index Page </H1>')

def index(request):
    products = None
    categories = Category.get_all_categories();
    # print(products)
    # return render(request, 'orders/order.html')
    categoryID = (request.GET.get('category'))
    if categoryID:
        products = Product.get_all_products_by_categoryid(categoryID)
    else:
        products = Product.get_all_products();
    data = {}
    data['products'] = products
    data['categories'] = categories
    return render(request, 'index.html', data)

def validateCustomer(customer):
    error_message = None;
    if not customer.first_name:
        error_message = "First Name Required!"
    elif len(customer.first_name) < 4:
        error_message = "First Name must be 4 characters long" 
    elif not customer.last_name:
        error_message = "Last Name Required!"
    elif len(customer.last_name) < 4:
        error_message = "Last Name must be 4 characters long"
    elif not customer.phone:
        error_message = "Phone Number required!"
    elif len(customer.phone) < 10:
        error_message = "Phone Number must be 10 characters long"
    elif len(customer.password) < 6:
        error_message = "Password must be 6 characters long"
    elif not customer.email:
        error_message = "Email required!"
    elif len(customer.email) < 5:
        error_message = "Email must be 5 characters long" 
    elif Customer.objects.filter(email=customer.email).exists():
        error_message = "Email Address already registered!" 
    
    return error_message

def registerUser(request):
    postData = request.POST
    
    first_name = postData.get('firstname')
    last_name = postData.get('lastname')
    phone = postData.get('phone')
    email = postData.get('email')
    password = postData.get('password')
        
    # validation

    value = {
        'first_name': first_name,
        'last_name': last_name,
        'phone': phone,
        'email': email
    }
    error_message = None
        
    customer = Customer(first_name = first_name, 
                        last_name = last_name, 
                        phone = phone, 
                        email = email, 
                        password = password)
           
    error_message = validateCustomer(customer)      
                    
    # saving
    if not error_message:
        print(first_name, last_name, phone, email, password)
        customer.password = make_password(customer.password)
        customer.register()
        return redirect('homepage')
    else:
        data = {
            'error': error_message,
            'values': value
        }
    return render(request, "signup.html", data)

def signup(request):
    if (request.method == 'GET'):
        return render(request, 'signup.html')
    else:
        return registerUser(request)
       
