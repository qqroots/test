from django.db import models

#新增一類別來管理某欄位需要import admin
from django.contrib import admin


from django.utils.translation import gettext_lazy as _

# Create your models here.

class Vendor(models.Model):
    vendor_name = models.CharField(max_length = 20) #攤販的名稱
    store_name = models.CharField(max_length = 10)  #攤販店家的名稱
    phone_number = models.CharField(max_length = 20)#攤販店家的電話號碼
    address = models.CharField(max_length = 100)     #攤販的地址
    
    #覆寫 __str__
    def __str__(self):
        return self.vendor_name

class Food(models.Model):
    food_name = models.CharField(max_length = 30)   #食物名稱
    price_name = models.DecimalField(max_digits =3, decimal_places =0) #食物價錢
    food_vendor = models.ForeignKey(Vendor, on_delete = models.CASCADE) #代表這食物是由哪一個攤販所做的

    #覆寫 __str__
    def __str__(self):
        return self.food_name


# 自行宣告 類別
class Morethanfifty(admin.SimpleListFilter):

	title = _('price')
	parameter_name = 'compareprice' # url最先要接的參數

	def lookups(self, request, model_admin):
		return (
			('>50',_('>50')), # 前方對應下方'>50'(也就是url的request)，第二個對應到admin顯示的文字
			('<=50',_('<=50')),
		)
    # 定義查詢時的過濾條件
	def queryset(self, request, queryset):
		if self.value() == '>50':
			return queryset.filter(price_name__gt=50)
		if self.value() == '<=50':
			return queryset.filter(price_name__lte=50)



'''
顯示primary_key (pk)
https://ithelp.ithome.com.tw/articles/10200799
'''
@admin.register(Vendor)
class VendorAdmin(admin.ModelAdmin):
    # list_display = ('id','vendor_name', 'store_name', 'phone_number', 'address') #可tuple可list #新寫法請往下看
    # #提醒:千萬不要取list_display以外的名稱，因為這是Django制式寫法，而且 Django看不懂也不會跟你報錯，這對於未來debug而言是一個很大的坑

    list_display = [field.name for field in Vendor._meta.fields]
    
@admin.register(Food)
class FoodAdmin(admin.ModelAdmin):
	list_display = [field.name for field in Food._meta.fields]
	list_filter = (Morethanfifty,)
	fields = ['price_name']		#顯示欄位 or 其他寫法: field =  exclude=['food_name', 'food_vendor']
	search_fields = ('food_name','price_name') #搜尋欄位 SQL寫法:WHERE ( food_name ILIKE '麵包' OR price_name ILIKE '麵包')
	ordering = ('price_name',) #價格由小到大排序
