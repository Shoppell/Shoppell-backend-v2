from ast import Return
from rest_framework import permissions
from shop.models import Shop, Product, SavedProduct, ShopComment, ProductComment

class ProductCommentOwnerOnly(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.user.is_authenticated:
            if ProductComment.objects.filter(user=request.user).count()==0:
                return False
            else:
                return True

    def has_object_permission(self, request, view, obj):
        if obj.user==request.user:
            return True
        else:
            return False

class ShopCommentOwnerOnly(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.user.is_authenticated:
            if ShopComment.objects.filter(user=request.user).count()==0:
                return False
            else:
                return True

    def has_object_permission(self, request, view, obj):
        if obj.user==request.user:
            return True
        else:
            return False

class SavedProductOwnerOnly(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.user.is_authenticated:
            if SavedProduct.objects.filter(user=request.user).count()==0:
                return False
            else:
                return True

    def has_object_permission(self, request, view, obj):
        if obj.user==request.user:
            return True
        else:
            return False

class ProductOwnerOnly(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.user.is_authenticated:
            if Product.objects.filter(shop=Shop.objects.filter(user=request.user).first()).count()==0:
                return False
            else:
                return True

    def has_object_permission(self, request, view, obj):
        if obj.shop==Shop.objects.filter(user=request.user).first():
            return True
        else:
            return False

class ShopOwnerOnly(permissions.BasePermission):
  
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            if Shop.objects.filter(user=request.user).count() ==0:
                return False
            else:
                return True

    def has_object_permission(self, request, view, obj):
        if obj==Shop.objects.filter(user=request.user).first():
            return True
        else:
            return False
