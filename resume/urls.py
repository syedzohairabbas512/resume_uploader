from django.contrib import admin
from django.urls import path, include
from user_resume import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.Homeview.as_view(), name="home"),
    path('<int:pk>', views.CandidateView.as_view(), name='candidate'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
