from django.contrib import admin
from .models import Wallet

class WalletConfig(admin.ModelAdmin):
    readonly_fields=('user','amount')

    def has_add_permission(self, request, obj=None):
        return False
    
    def has_delete_permission(self, request, obj=None):
        return False

admin.site.register(Wallet,WalletConfig)