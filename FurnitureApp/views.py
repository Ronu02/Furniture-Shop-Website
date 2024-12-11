from django.shortcuts import render, redirect
from FurnitureApp.models import CategoryDb, ProductDb
from django.utils.datastructures import MultiValueDictKeyError
from django.core.files.storage import FileSystemStorage

from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

from WebApp.models import ContactDb
from django.contrib import messages

def Index(request):
    x = len(CategoryDb.objects.all())
    y = len(ProductDb.objects.all())
    return render(request, "Index.html", {'x': x, 'y': y})

def Add_categories(request):
    return render(request, "Add_categories.html")

def Save_categories(request):
    if request.method == "POST":
        name = request.POST.get('CategoryName')
        desc = request.POST.get('CategoryDescription')
        img = request.FILES['CategoryImage']
        obj = CategoryDb(Category_name=name, Category_description=desc, Category_image=img)
        obj.save()
        messages.success(request, "Category Saved Successfully..!")
        return redirect(Add_categories)

def Display_categories(request):
    category = CategoryDb.objects.all()
    return render(request, "Display_categories.html", {'category': category})

def Edit_categories(request, Cate_id):
    category = CategoryDb.objects.get(id=Cate_id)
    return render(request, "Edit_categories.html", {'category': category})

def Update_categories(request, Cate_id):
    if request.method == "POST":
        name = request.POST.get('CategoryName')
        desc = request.POST.get('CategoryDescription')
        try:
            img = request.FILES['CategoryImage']
            fs = FileSystemStorage()
            file = fs.save(img.name, img)
        except MultiValueDictKeyError:
            file = CategoryDb.objects.get(id=Cate_id).Category_image
        CategoryDb.objects.filter(id=Cate_id).update(Category_name=name, Category_description=desc, Category_image=file)
        messages.info(request, "Category Updated..!")
        return redirect(Display_categories)

def Delete_categories(request, Cate_id):
    x = CategoryDb.objects.filter(id=Cate_id)
    x.delete()
    messages.error(request, "Category Deleted Successfully..!")
    return redirect(Display_categories)

def Add_products(request):
    category = CategoryDb.objects.all()
    return render(request, "Add_products.html", {'category': category})

def Save_products(request):
    if request.method == "POST":
        category = request.POST.get('ProductCategory')
        name = request.POST.get('ProductName')
        quantity = request.POST.get('ProductQuantity')
        price = request.POST.get('ProductPrice')
        description = request.POST.get('ProductDescription')
        origin = request.POST.get('ProductOrigin')
        manufactures = request.POST.get('ProductManufactures')
        img1 = request.FILES['ProductImage1']
        img2 = request.FILES['ProductImage2']
        img3 = request.FILES['ProductImage3']
        obj = ProductDb(Product_category=category, Product_name=name, Product_quantity=quantity, Product_price=price,
                        Product_description=description, Product_origin=origin, Product_manufactures=manufactures,
                        Product_image1=img1, Product_image2=img2, Product_image3=img3)
        obj.save()
        messages.success(request, "Product Added Successfully..!")
        return redirect(Add_products)

def Display_products(request):
    product = ProductDb.objects.all()
    return render(request, "Display_products.html", {'product': product})

def Edit_products(request, Pro_id):
    product = ProductDb.objects.get(id=Pro_id)
    category = CategoryDb.objects.all()
    return render(request, "Edit_products.html", {'product': product, 'category': category})

def Update_products(request, Pro_id):
    if request.method == "POST":
        category = request.POST.get('ProductCategory')
        name = request.POST.get('ProductName')
        quantity = request.POST.get('ProductQuantity')
        price = request.POST.get('ProductPrice')
        description = request.POST.get('ProductDescription')
        origin = request.POST.get('ProductOrigin')
        manufactures = request.POST.get('ProductManufactures')
        try:
            img1 = request.FILES['ProductImage1']
            fs = FileSystemStorage()
            file1 = fs.save(img1.name, img1)
        except MultiValueDictKeyError:
            file1 = ProductDb.objects.get(id=Pro_id).Product_image1
        try:
            img2 = request.FILES['ProductImage2']
            fs = FileSystemStorage()
            file2 = fs.save(img2.name, img2)
        except MultiValueDictKeyError:
            file2 = ProductDb.objects.get(id=Pro_id).Product_image2
        try:
            img3 = request.FILES['ProductImage3']
            fs = FileSystemStorage()
            file3 = fs.save(img3.name, img3)
        except MultiValueDictKeyError:
            file3 = ProductDb.objects.get(id=Pro_id).Product_image3
        ProductDb.objects.filter(id=Pro_id).update(Product_category=category, Product_name=name, Product_quantity=quantity, Product_price=price,
                        Product_description=description, Product_origin=origin, Product_manufactures=manufactures,
                        Product_image1=file1, Product_image2=file2, Product_image3=file3)
        return redirect(Display_products)

def Delete_products(request, Pro_id):
    x = ProductDb.objects.filter(id=Pro_id)
    x.delete()
    messages.error(request, "Product Deleted Successfully..!")
    return redirect(Display_products)

def Admin_login(request):
    return render(request, "Admin_login.html")

def Admin_loginCheck(request):
    if request.method == "POST":
        un = request.POST.get('Username')
        pswd = request.POST.get('Password')
        if User.objects.filter(username__contains=un).exists():
            user = authenticate(username=un, password=pswd)
            if user is not None:
                login(request, user)
                request.session['username'] = un
                request.session['password'] = pswd
                messages.success(request, "Welcome..!")
                return redirect(Index)
            else:
                messages.error(request, "Please check your Password")
                return redirect(Admin_login)
        else:
            messages.warning(request, "Invalid Username")
            return redirect(Admin_login)

def Admin_logout(request):
    del request.session['username']
    del request.session['password']
    messages.info(request, "Logout Successfully")
    return redirect(Admin_login)

def Contact_data(request):
    data = ContactDb.objects.all()
    return render(request, "Contact_data.html", {'data': data})

def Delete_contact(request, contact_id):
    x = ContactDb.objects.filter(id=contact_id)
    x.delete()
    return redirect(Contact_data)

