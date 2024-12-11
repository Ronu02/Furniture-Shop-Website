from django.shortcuts import render, redirect
from FurnitureApp.models import ProductDb, CategoryDb
from WebApp.models import ContactDb, SignupDb, CartDb, OrderDb
from django.contrib import messages
import razorpay

def Home(request):
    category = CategoryDb.objects.all()
    data = CartDb.objects.filter(Username=request.session['Name'])
    c = data.count()
    return render(request, "Home.html", {'category': category, 'c': c})

def Product_page(request):
    product = ProductDb.objects.all()
    data = CartDb.objects.filter(Username=request.session['Name'])
    c = data.count()
    return render(request, "Products.html", {'product': product, 'c': c})

def About_page(request):
    data = CartDb.objects.filter(Username=request.session['Name'])
    c = data.count()
    return render(request, "About.html", {'c': c})

def Contact_page(request):
    data = CartDb.objects.filter(Username=request.session['Name'])
    c = data.count()
    return render(request, "Contact.html", {'c': c})

def Save_contact(request):
    if request.method == "POST":
        name1 = request.POST.get('Fname')
        name2 = request.POST.get('Lname')
        email = request.POST.get('Email')
        msg = request.POST.get('Message')
        obj = ContactDb(First_name=name1, Last_name=name2, Email_address=email, Message=msg)
        obj.save()
        return redirect(Contact_page)

def Products_filtered(request, cat_name):
    category = ProductDb.objects.filter(Product_category=cat_name)
    return render(request, "Products_filtered.html", {'category': category})

def Single_product(request, Pro_id):
    data = ProductDb.objects.get(id=Pro_id)
    return render(request, "Single_product.html", {'data': data})

def Sign_up(request):
    return render(request, "Sign_up.html")

def Sign_in(request):
    return render(request, "Sign_in.html")

def Save_signup(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        mobile = request.POST.get('mobile')
        pswd = request.POST.get('pass')
        re_pswd = request.POST.get('re_pass')
        obj = SignupDb(Name=name, Email=email, Mobile=mobile, Password=pswd, Repeat_password=re_pswd)
        if SignupDb.objects.filter(Name=name).exists():
            messages.warning(request, "Username already exists")
            return redirect(Sign_in)
        elif SignupDb.objects.filter(Email=email).exists():
            messages.warning(request, "Email already exists")
            return redirect(Sign_in)
        elif SignupDb.objects.filter(Mobile=mobile).exists():
            messages.warning(request, "Mobile Number already exists")
            return redirect(Sign_in)

        obj.save()
        return redirect(Sign_up)

def Signin_check(request):
    if request.method == "POST":
        un = request.POST.get('your_name')
        pswd = request.POST.get('your_pass')
        if SignupDb.objects.filter(Name=un, Password=pswd).exists():
            request.session['Name'] = un
            request.session['Password'] = pswd
            messages.success(request, "Logined Successfully..!")
            return redirect(Home)
        else:
            messages.error(request, "Please try again")
            return redirect(Sign_in)
    else:
        messages.warning(request, "Please try again")
        return redirect(Sign_in)

def Log_out(request):
    del request.session['Name']
    del request.session['Password']
    return redirect(Sign_in)

def Save_cart(request):
    if request.method == "POST":
        un = request.POST.get('User')
        qn = request.POST.get('No')
        pro = request.POST.get('Product')
        rs = request.POST.get('Total')
        obj = CartDb(Username=un, Product_name=pro, Quantity=qn, Total_price=rs)
        obj.save()
        return redirect(Home)

def Cart_page(request):
    data = CartDb.objects.filter(Username=request.session['Name'])

    Subtotal = 0
    Shipping_charge = 0
    Total = 0
    for i in data:
        Subtotal += i.Total_price

    if Subtotal > 50000:
        Shipping_charge = 300
    else:
        Shipping_charge = 150

    Total = Subtotal + Shipping_charge

    return render(request, "Cart.html", {'data': data, 'Subtotal': Subtotal,
                                         'Shipping_charge': Shipping_charge, 'Total': Total})

def Delete_cart(request, Cart_id):
    x = CartDb.objects.filter(id=Cart_id)
    x.delete()
    return redirect(Cart_page)

def Checkout(request):
    data = CartDb.objects.filter(Username=request.session['Name'])

    Subtotal = 0
    Shipping_charge = 0
    Total = 0
    for i in data:
        Subtotal += i.Total_price

    if Subtotal > 50000:
        Shipping_charge = 300
    else:
        Shipping_charge = 150

    Total = Subtotal + Shipping_charge

    return render(request, "Checkout.html", {'data': data, 'Subtotal': Subtotal,
                                             'Shipping_charge': Shipping_charge, 'Total': Total})

def Save_order(request):
    if request.method == "POST":
        country = request.POST.get('country')
        name = request.POST.get('name')
        message = request.POST.get('message')
        address = request.POST.get('address')
        place = request.POST.get('place')
        pincode = request.POST.get('pincode')
        email = request.POST.get('email')
        mobile = request.POST.get('mobile')
        total = request.POST.get('total')
        obj = OrderDb(Country=country, Name=name, Message=message, Address=address, Place=place,
                      Pincode=pincode, Email=email, Mobile=mobile, Total_price=total)
        obj.save()
        return redirect(Checkout)

def Payment(request):
    customer = OrderDb.objects.order_by('-id').first()
    payy = customer.Total_price
    amount = int(payy*100)
    payy_str = str(amount)

    for i in payy_str:
        print(i)
    if request.method == "POST":
        order_currency = 'INR'
        client = razorpay.Client(auth=('rzp_test_qWjY3EJqeA5lrt', 'NNCMneW1p9scp2blI7vFaYhv'))
        payment = client.order.create({'amount': amount, 'currency': order_currency})

    return render(request, "Payment.html", {'customer': customer, 'payy_str': payy_str})
