from django.shortcuts import render
from store.models.product import Product
from store.models.category import Category

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
    print('You are', request.session.get('email'))
    
    return render(request, 'index.html', data)
   
