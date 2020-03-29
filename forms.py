#day18 新增

from django import forms
from .models import Vendor, Food
from django.utils.translation import gettext_lazy as _ ##新增labels對應->內容用中文表示

class VendorForm(forms.ModelForm):
	class Meta:
		model = Vendor		#我要哪用哪一個Model
		fields = '__all__'	#使用Model的哪些攤位
		
		#新增labels對應
		labels = {
			'vendor_name': _('攤販名稱'),
			'store_name': _('店名'),
			'phone_number': _('電話'),
			'address': _('地址'),
		}

# day19 -- 創建一個 Raw Form 
class RawVendorForm(forms.Form):
	vendor_name = forms.CharField()
	store_name = forms.CharField()
	phone_number = forms.CharField()
