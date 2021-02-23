from django.contrib import admin
from django.urls    import include, path

urlpatterns = [
    path('',            include('peer.urls')),
    path('signup',      include('peer.urls')),
    path('signup_done', include('peer.urls')),
    path('signin',      include('peer.urls')),
    path('admin/',      admin.site.urls),
]
