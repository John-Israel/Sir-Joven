from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('gender/list', views.gender_list),
    path('gender/add', views.add_gender),
    path('gender/edit/<int:genderId>', views.editGender),
    path('gender/delete/<int:genderId>', views.delete_gender),
    # Paths for CRUD users
    path('users/list', views.userList),
    path('users/add', views.add_user),
    path('users/edit/<int:userId>', views.editUser),
    path('users/delete/<int:userId>', views.delete_user,)
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)