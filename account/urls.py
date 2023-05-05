from django.urls import path
from .views import AccountListAPIView, AccountRUDAPIView
from job.views import WishlistListAPIView


urlpatterns = [
    path('list/', AccountListAPIView.as_view()),
    path('detail/<int:pk>/', AccountRUDAPIView.as_view()),
    path('wishlist/', WishlistListAPIView.as_view()),
]