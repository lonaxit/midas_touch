from django.contrib import admin
from subscription.models import *
# Register your models here.
admin.site.register(ProductCategory)
admin.site.register(Product)
admin.site.register(Loan)
admin.site.register(ConsolidatedLoan)
admin.site.register(LoanDeduction)