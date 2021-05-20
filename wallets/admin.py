from django.contrib import admin
from .models import Wallet ,Transaction
from core.settings import DEBUG

class WalletConfig(admin.ModelAdmin):
    readonly_fields=('user','amount')

    def has_add_permission(self, request, obj=None):
        if(DEBUG == True):
            return True
        return False
    
    def has_delete_permission(self, request, obj=None):
        if(DEBUG == True):
            return True
        return False

admin.site.register(Wallet,WalletConfig)
# admin.site.register(Transaction)