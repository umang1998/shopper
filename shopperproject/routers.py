from rest_framework import routers
from product.viewsets import ProductDetailViewSet
router = routers.DefaultRouter()
router.register(r'product', ProductDetailViewSet)