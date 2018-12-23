from django.shortcuts import render,get_object_or_404
from .models import Brand,Driver,Pos_data

from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login

from .serializers import PosdataSerializer

# Create your views here.


# this can be also done brand.driver_set

def driver_data(request):
	if not request.user.is_authenticated:
		return render(request, 'oda/login.html')
	else:
		brand=get_object_or_404(Brand,manager=request.user)
		driver_data=brand.driver_set.all()
		context={'driver_data':driver_data}
		return render(request,'oda/driver_data.html',context)


def login_user(request):
	if request.method=="POST":
		username=request.POST['username']
		password=request.POST['password']
		user=authenticate(username=username,password=password)
		if user is not None:
			if user.is_active:
				login(request,user)
				brand_data=get_object_or_404(Brand,manager=request.user)
				#brand_data=Brand.objects.filter(manager=request.user)
				return render(request,'oda/brand_data.html',{'brand_data':brand_data})
				
			else:
				return render(request,'oda/login.html',{'error_message':"your account has been disabled"})
		else:
			return render(request,'oda/login.html', {'error_message':"invalid login Credentials"})
	else:
		if request.user.is_anonymous:
			return render(request,'oda/login.html')
		else:
			brand_data=Brand.objects.filter(manager=request.user)
			if not brand_data:
				return render(request,'oda/login.html')
			else:
				return render(request,'oda/brand_data.html',{'brand_data':brand_data})
			

def Posdata_brand(request):
	if not request.user.is_authenticated:
		return render(request, 'oda/login.html')
	else:
		brand=get_object_or_404(Brand,manager=request.user)
		posdata=Pos_data.objects.filter(brand=brand)
		serializer=PosdataSerializer(posdata,many=True)
		data=serializer.data[:]
		return render(request,'oda/map_point.html',{'data':data})

def Posdata_driver(request,driver_id):
	if not request.user.is_authenticated:
		return render(request, 'oda/login.html')
	else:
		posdata=Pos_data.objects.filter(driver_id=driver_id)
		serializer=PosdataSerializer(posdata,many=True)
		data=serializer.data[:]
		return render(request,'oda/map_point.html',{'data':data})

def Home(request):
	return render(request,'oda/home.html',{})

'''

def brand_data(request,brand_id):
	brand_data=get_object_or_404(Brand,pk=brand_id)
	context={'brand_data':brand_data}
	return render(request,'oda/brand_data.html',context)


def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                albums = Album.objects.filter(user=request.user)
                return return redirect('oda:brand_data')
            else:
                return render(request, 'music/login.html', {'error_message': 'Your account has been disabled'})
        else:
            return render(request, 'music/login.html', {'error_message': 'Invalid login'})
	return render(request, 'music/login.html')

class UserFormView(View):
	form_class=Userform
	template_name='oda/registration_form.html'

	def get(self,request):
		form=self.form_class(None)
		return render(request,self.template_name,{'form':form})
	#process form data
	def post(self,request):
		form=self.form_class(request.POST)

		if form.is_valid():
			user=form.save(commit=False)
			username=form.cleaned_data['username']
			password=form.cleaned_data['password']
			
			#user.set_password(password)
			#user.save()
			
			#return user object if credential are corect
			user = authenticate(username=username,password=password)
			if user is not None:
				if user.is_active:
					login(request,user)
					return redirect('oda:brand_data 2')
				else:
					return render(request,self.template_name,{'form':form,'error_message':"user not active"})		
			context={'form':form,'error_message':"credential not valid1"}
			return render(request,self.template_name,context)
				#request.user.username
			
		else:
			context={'form':form,'error_message':"credential not valid2"}
			return render(request,self.template_name,context)
'''