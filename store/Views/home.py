from django.shortcuts import render, redirect
from store.models.product import Product
from store.models.category import Category
from django.views import View

# print(make_password('1234'))
# print(check_password('1234','pbkdf2_sha256$320000$BXfmD5ytn1Fb37zTnrcBCV$OOOtkKATefBN22pXi6m9iVnw6G236Vt17vurE2gXJqg='))

# Create your views here.
# def index(request):
#     return HttpResponse('<H1> Index Page </H1>')

class Index(View):
    
    def post(self, request):
        product = request.POST.get("product")
        remove = request.POST.get('remove')
        cart = request.session.get('cart')
        if cart:
            quantity = cart.get(product)
            if quantity:   
                if remove:   
                    if quantity <= 1:
                        cart.pop(product)
                    else:
                        cart[product] = quantity-1
                else:
                    cart[product] = quantity+1
            else:
                cart[product] = 1
        else:
            cart = {}
            cart[product] = 1
        
        request.session['cart'] = cart
        print("Cart:", request.session['cart'])
        return redirect('homepage')
    
    def get(self, request):
        cart = request.session.get('cart')
        if not cart:
            request.session['cart'] = {}
            
        
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


   
