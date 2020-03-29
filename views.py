from django.shortcuts import render	#Django提供你很多方便你操作的函式，而rendor可以將我們要傳達的資料一併打包，再透過 HttpResponse 回傳到瀏覽器
from .models import Vendor
from .forms import VendorForm	#day18 新增
from .forms import RawVendorForm #day19 新增

# Create your views here.
def vendor_index(request):
	vendor_list = Vendor.objects.all() #把所有Vendor的資料取出來
	context = {'vendor_list': vendor_list}	#建立Dict對應到Vendor的資料
	return render(request, 'vendors/vendor_detail.html', context)
	
#day18 新增
def vendor_create_view(request):
# 	form = VendorForm(request.POST or None) day19 修改為以下一行
	form = RawVendorForm(request.POST or None)
	if form.is_valid():
# 		form.save() # day19 修改為以下
		print(form.cleaned_data)
		form = VendorForm()
		
	context = {
		'form':form
	}
	return render(request, "vendors/vendor_create.html", context)