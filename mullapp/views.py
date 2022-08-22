from django.shortcuts import render, redirect
from .forms import ProductForm, ImageForm
from .models import Image, Product
from django.contrib import messages


# Create your views here.
def index(request):
    products = Product.objects.all()
    context = {"products": products}
    return render(request, 'index.html', context)

def detail(request, id):
    product = Product.objects.get(id=id)
    images = Image.objects.filter(product=product)
    context = {"product": product, "images": images}
    return render(request, 'detail.html', context)
    

def create_product(request):
    productform = ProductForm()
    imageform = ImageForm()
    
    if request.method == 'POST':
        
        files = request.FILES.getlist('images')
        
        productform = ProductForm(request.POST, request.FILES)
        if productform.is_valid():
            product = productform.save(commit=False)
            product.vendor = request.user
            product.save()
            messages.success(request, "Product created successfully")
            
            for file in files:
                Image.objects.create(product=product, images=file)
            
            return redirect("index")
    
    context = {"p_form": productform, "i_form": imageform}
    return render(request, "create.html", context)