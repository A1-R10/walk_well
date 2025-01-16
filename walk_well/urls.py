from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('dashboard.urls')),
    path("accounts/", include("user_authentication.urls")),
    path("post/", include('blog.urls')),

    # 3rd party
    path('accounts/auth/', include('allauth.urls')),
]
