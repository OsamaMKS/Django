from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from .forms import SigninForm , SignupForm, ListForm , ItemForm
from .models import List, ListItems





def wish_list(request):
    if request.user.is_anonymous:
        wishlist = List.objects.all()
    else:
        wishlist=List.objects.filter(owner=request.user)
    context = {
        "wishlists": wishlist
    }
    return render(request,'wishlist.html',context)

def list_detail(request, list_id):
    list = List.objects.get(id=list_id)
    items = ListItems.objects.filter(list=list)
    context = {
        "list": list,
        "items": items,
    }
    return render(request, 'detail.html', context)

def items_wish(request, item_id):
    list = List.objects.get(id=item_id)
    items = ListItems.objects.filter(list=list)
    context = {
        "list": list,
        "items": items,
    }
    return render(request, 'itemsWish.html', context)

def list_create(request):
    if request.user.is_anonymous:
        return redirect("signin")

    form = ListForm()
    if request.method == "POST":
        form = ListForm(request.POST, request.FILES)
        if form.is_valid():
            list = form.save(commit=False)
            list.owner = request.user
            list.save()
            return redirect('wishlist')
    context = {
        "form":form,
    }
    return render(request, 'createlist.html', context)

def item_create(request, list_id):
	form = ItemForm()
	list = List.objects.get(id=list_id)
	if request.user == list.owner:
		if request.method == "POST":
			form = ItemForm(request.POST,request.FILES)
			if form.is_valid():
				item = form.save(commit=False)
				item.list = list
				item.save()
				return redirect('wishlist')
	context = {
	"form": form,
	"list": list,
	}
	return render(request, 'item_create.html', context)

def list_delete(request, list_id):
    if not request.user.is_staff:
        return redirect("whislist")

    list_obj = ListItems.objects.get(id=list_id)
    list_obj.delete()
    return redirect('wishlist')

def list_update(request, list_id):

    list_obj = List.objects.get(id=list_id)
    form = ListForm(instance=list_obj)

    if not request.user.is_staff and request.user != list_obj.owner:
        return redirect("home")

    if request.method == "POST":
        form = ListForm(request.POST, request.FILES, instance=list_obj)
        if form.is_valid():
            form.save()
            return redirect('wishlist')
    context = {
        "list_obj": list_obj,
        "form":form,
    }
    return render(request, 'update.html', context)

def home(request):
    return render(request,"home.html")

def signup(request):
    form = SignupForm()
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)

            user.set_password(user.password)
            user.save()

            login(request, user)
            return redirect("wishlist")
    context = {
        "form":form,
    }
    return render(request, 'signup.html', context)

def signin(request):
    form = SigninForm()
    if request.method == 'POST':
        form = SigninForm(request.POST)
        if form.is_valid():

            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            auth_user = authenticate(username=username, password=password)
            if auth_user is not None:
                login(request, auth_user)
                return redirect('wishlist')
    context = {
        "form":form
    }
    return render(request, 'signin.html', context)

def signout(request):
    logout(request)
    return redirect("home")
