from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .forms import CustomPhoto, CustomUserCreationForm,VerifyForm
from django.contrib.auth.decorators import login_required
from . import verify
from .models import Category,Photo
import os

# Create your views here.

@login_required
def gallery(request):
    user = request.user
    category = request.GET.get('category')
    # print(category)
    if category == None:
        # photos = Photo.objects.all()
        photos = Photo.objects.filter(category__user=user)
    else:
        # photos = Photo.objects.filter(category__name=category)
        photos = Photo.objects.filter(category__name=category,category__user=user)



    # categories = Category.objects.all()
    categories = Category.objects.filter(user=user)

    context = {'categories':categories,'photos':photos}
    return render(request,'scrap_album/gallery.html', context)

@login_required(login_url='login')
def viewPhoto(request, pk):
    photo = Photo.objects.get(id=pk)
    return render(request,'scrap_album/photo.html',{'photo':photo})

login_required(login_url='login')
def photoDelete(request,photo_id):
    photo_delete = Photo.objects.get(pk=photo_id)
    photo_delete.delete()
    return redirect('gallery')
    

@login_required(login_url='login')
def categoryDelete(request,cat_id):
    cat_delete = Category.objects.get(pk=cat_id)
    cat_delete.delete()
    return redirect('gallery')


@login_required(login_url='login')
def update_view(request,des_id):
    update_des = Photo.objects.get(pk = des_id)
    # form1 = CustomPhoto(request.POST or None, instance=update_des)
    # if form1.is_valid():
    #     if len(request.FILES) != 0:
    #         if len(update_des.image) > 0:
    #             os.remove(update_des.image.path)
    #         update_des.image = request.FILES['image']

    #     form1.save()
    #     return redirect('gallery')

    if request.method == "POST":
        if len(request.FILES) != 0:
            if len(update_des.image) > 0:
                os.remove(update_des.image.path)
            update_des.image = request.FILES['image']
        update_des.description = request.POST.get('description')
        update_des.save()
        return redirect('gallery')

    return render(request,'scrap_album/update_description.html',{'update_des':update_des}) 




@login_required(login_url='login')
def addPhoto(request):
    # categories = Category.objects.all()
    user = request.user

    categories = user.category_set.all()

    if request.method == 'POST':
        data = request.POST
        images = request.FILES.getlist('images')

        if data['category'] != 'none':
            category = Category.objects.get(id=data['category'])
        elif data['category_new'] != '':
            category, created = Category.objects.get_or_create(user=user,name=data['category_new'])
        else:
            category = None

        for image in images:
            photo = Photo.objects.create(
                category = category,
                description = data['description'],
                image = image,
            )

        return redirect('gallery')

    context = {'categories':categories}
    return render(request,'scrap_album/add.html',context)



# def loginUser(request):
    page = 'login'
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request,user)
            
            return redirect('gallery')
        else:
            messages.info(request,'Username or Password is incorrect')
        

    return render(request,'scrap_album/login_register.html',{'page':page})

def logoutUser(request):
    logout(request)
    return redirect('login')

# def registerUser(request):
    # page = 'register'
    form  = CustomUserCreationForm()

    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            # this ccommented code is directly redirects to homepage after registration
            # stroring data in user object
            # user = form.save(commit=False)
            # user.save()

            # user = authenticate(request, username=user.username, password=request.POST['password1'])

            # if user is not None:
            #     login(request,user)
            #     return redirect('gallery')

            form.save()
            verify.send(form.cleaned_data.get('phone'))
            user = form.cleaned_data.get('username')
            messages.success(request,'Account created Successfully for ' + user)
            return redirect('verify')
        

    context = {'form':form}
    return render(request, 'scrap_album/register.html',context)

def registerUser(request):
    form  = CustomUserCreationForm()
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            verify.send(form.cleaned_data.get('phone'))
            user = form.cleaned_data.get('username')
            messages.success(request,'Account created Successfully for ' + user)
            return redirect('verify')
    
    context = {'form':form}
    return render(request, 'scrap_album/register.html',context)

@login_required(login_url='login')
def verify_code(request):
    if request.method == 'POST':
        form = VerifyForm(request.POST)
        if form.is_valid():
            code = form.cleaned_data.get('code')
            if verify.check(request.user.phone, code):
                request.user.is_verified = True
                request.user.save()
                return redirect('gallery')
    else:
        form = VerifyForm()
    return render(request, 'scrap_album/verify.html', {'form': form})