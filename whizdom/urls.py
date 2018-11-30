from django.contrib import admin
from django.conf.urls import url
from django.conf.urls import include
from rest_framework.documentation import include_docs_urls

admin.site.site_header = "Whizdom : Admin"
admin.site.site_title = "Whizdom : Admin"

urlpatterns = [
    url(r'^', include_docs_urls(title='SupplyAI API')),
    url('admin/', admin.site.urls),
    url('api/v1/bouncer/', include('bouncer.urls')),
    url('api/v1/content/', include('content.urls')),
]
