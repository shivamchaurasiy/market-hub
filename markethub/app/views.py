from django.shortcuts import render, redirect
from django.views import View           # view the product on category based
# from .forms import Sign_Up, MyPasswordChangeForm
from django.contrib import messages   #  messages alert
from .models import Product, Cart, OrderPlaced, Customer
from .forms import CustomRegistrationForm, CustomerProfileForm
from django.db.models import Q
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


class ProductView(View):
    def get(self, request):
        bottomwears=Product.objects.filter(category='BW')
        topwears=Product.objects.filter(category='TW')
        laptops=Product.objects.filter(category='L')
        mobiles=Product.objects.filter(category='M')
        return render(request, 'app/home.html', {'bottomwears':bottomwears,'topwears':topwears, 'laptops':laptops, 'mobiles':mobiles})


class ProductDetailView(View):
    '''
    About of Q Object
    Queries ko Combine Karna: Aap Q objects ka istemal karke ek hi query mein multiple conditions ko combine kar sakte hain. Jaise agar aapko un users ko dhundhna hai jo kisi specific city se hain ya kisi specific email se hain:
    Ex. = users = User.objects.filter(Q(city='Indore') | Q(email='example@example.com'))
    
    Conditions ko Chain Karna: Aap multiple Q objects ko chain kar sakte hain complex queries ke liye. Jaise agar aapko un users ko dhundhna hai jo kisi specific city se hain aur ya toh unka email specific ho ya unki age ek certain limit se zyada ho:
    Ex = users = User.objects.filter(Q(city='Indore') & (Q(email='example@example.com') | Q(age__gt=30)))

    Conditions ko Negate Karna: Aap kisi condition ko negate karne ke liye ~ (not) operator ka istemal bhi kar sakte hain. Jaise agar aapko un users ko dhundhna hai jo kisi specific city se nahi hain:
    Ex = users = User.objects.filter(~Q(city='Indore'))
    '''
    def get(self,request, id):
        product=Product.objects.get(pk=id)
        item_already_in_cart = False
        if request.user.is_authenticated:
            item_already_in_cart = Cart.objects.filter(Q(product=product.id) & Q(user=request.user)).exists()
        return render(request, 'app/productdetail.html', {'product':product, 'item_already_in_cart':item_already_in_cart})
 
def buy_now(request):
     return render(request, 'app/buynow.html')


def mobile(request, data=None):
    if data == None:
        mobiles = Product.objects.filter(category='M')
    elif data == 'Redmi' or data == 'Samsung':
        mobiles = Product.objects.filter(category='M').filter(brand=data)
    elif data == 'below':
        mobiles = Product.objects.filter(category='M').filter(selling_price__lt=10000)
    elif data == 'above':
        mobiles = Product.objects.filter(category='M').filter(selling_price__gt=10000)
    return render(request, 'app/mobile.html', {'mobiles':mobiles})


class CustomRegistrationView(View):
    def get(self, request):
        form = CustomRegistrationForm()
        return render(request, 'app/customerregistration.html', {'form':form})
    def post(self, request):
        form = CustomRegistrationForm(request.POST)
        if form.is_valid():
            messages.success(request, 'Congratulations!! Registered Succesfully')
            form.save()
            return redirect('customerregistration')
        return render(request, 'app/customerregistration.html', {'form':form})
        

@method_decorator(login_required, name='dispatch')
class ProfileView(View):
    def get(self, request):
        form = CustomerProfileForm()
        return render(request, 'app/profile.html', {'form':form, 'active':'btn-primary'})
    
    def post(self, request):
        form = CustomerProfileForm(request.POST)
        if form.is_valid():
            usr = request.user
            name = form.cleaned_data['name']
            locality = form.cleaned_data['locality']
            city = form.cleaned_data['city']
            state = form.cleaned_data['state']
            zipcode = form.cleaned_data['zipcode'] 
            reg = Customer(user=usr, name=name, locality=locality, city=city, state=state, zipcode=zipcode)
            reg.save()
            messages.success(request, "Congratulations!! Profile Updated Successfully")
            return redirect('profile')
        return render(request, 'app/profile.html', {'form':form, 'active':'btn-primary'})
    
    
def address(request):
    add = Customer.objects.filter(user=request.user)
    return render(request, 'app/address.html', {'add':add, 'active':'btn-primary'})  


@login_required
def add_to_cart(request):
    user = request.user
    product_id= request.GET.get('prod_id')
    product = Product.objects.get(id=product_id)
    Cart(user=user, product=product).save()
    return redirect('/cart')


@login_required
def show_cart(request):
    if request.user.is_authenticated:
        user = request.user
        cart = Cart.objects.filter(user=user)
        print(cart)
        amount = 0.0
        shipping_amount = 70.0
        total_amount = 0.0
        cart_product = [p for p in Cart.objects.all() if p.user == user]
        print(cart_product)
        
        if cart_product:
            for p in cart_product:
                tempamount = (p.quantity * p.product.selling_price)
                amount += tempamount
                totalamount = amount + shipping_amount
            return render(request, 'app/addtocart.html', {'carts':cart, 'totalamount':totalamount, 'amount':amount})
        else:
            return render(request, 'app/emptycart.html')
        
   
# Plus Cart     
def plus_cart(request):
    if request.method == 'GET':
        prod_id = request.GET['prod_id']    # get prod_id form ajax of myscript.js file
        c = Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
        c.quantity+=1
        c.save()
        amount = 0.0
        shipping_amount = 70.0
        cart_product = [p for p in Cart.objects.all() if p.user == request.user]
        for p in cart_product:
            tempamount = (p.quantity * p.product.selling_price)
            amount += tempamount
            
        data = {
            'quantity':c.quantity,
            'amount':amount,
            'totalamount':amount + shipping_amount
        }
        print('data', data)
        return JsonResponse(data)
    
    
# Minus Cart
def minus_cart(request):
    if request.method == 'GET':
        prod_id = request.GET['prod_id']    # get prod_id form ajax of myscript.js file
        c = Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
        c.quantity-=1
        c.save()
        amount = 0.0
        shipping_amount = 70.0
        cart_product = [p for p in Cart.objects.all() if p.user == request.user]
        for p in cart_product:
            tempamount = (p.quantity * p.product.selling_price)
            amount += tempamount
            
        data = {
            'quantity':c.quantity,
            'amount':amount,
            'totalamount':amount + shipping_amount
        }
        print('data', data)
        return JsonResponse(data)
    
    
# Remove Cart
@login_required
def remove_cart(request):
    if request.method == 'GET':
        prod_id = request.GET['prod_id']    # get prod_id form ajax of myscript.js file
        c = Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
        c.delete()
        amount = 0.0
        shipping_amount = 70.0
        cart_product = [p for p in Cart.objects.all() if p.user == request.user]
        for p in cart_product:
            tempamount = (p.quantity * p.product.selling_price)
            amount += tempamount
            
        data = {
            'amount':amount,
            'totalamount':amount + shipping_amount
        }
        return JsonResponse(data)
    
    
@login_required 
def checkout(request):
    user = request.user
    add = Customer.objects.filter(user=user)
    cart_items = Cart.objects.filter(user=user)
    amount = 0.0
    shipping_amount = 70.0
    totalamount = 0.0
    cart_product = [p for p in Cart.objects.all() if p.user == request.user]
    
    if cart_product:
        for p in cart_product:
            tempamount = (p.quantity * p.product.selling_price)
            amount += tempamount
        totalamount = amount + shipping_amount
    
    return render(request, 'app/checkout.html', {'add':add, 'totalamount':totalamount, 'cart_items':cart_items}) 

@login_required
def payment_done(request):
    user = request.user
    custid = request.GET.get('custid') 
    customer = Customer.objects.get(id=custid)
    cart = Cart.objects.filter(user=user)
    for c in cart:
        OrderPlaced(user=user, customer=customer, product=c.product, quantity=c.quantity).save()
        c.delete()
    return redirect("orders")


@login_required
def orders(request):
    op = OrderPlaced.objects.filter(user=request.user)
    return render(request, 'app/orders.html', {'order_placed':op})