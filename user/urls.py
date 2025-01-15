
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    # User management routes
    path('api/', include('authentication.urls')),
    path('api-auth/', include('rest_framework.urls')),
]
