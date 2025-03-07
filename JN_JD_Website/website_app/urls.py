from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.sign_in, name='signin'),
    path('createaccount/', views.create_account, name='createaccount'),  # Corrected view name to match
    path('home/', views.home, name='home'),
    path('logout/', LogoutView.as_view(next_page='signin'), name='logout'),
    path('editgroups/<int:org_id>/', views.edit_groups, name='editgroups'),
    path('editevent/<int:event_id>/', views.edit_event, name='editevent'),
    path('viewevents/', views.view_events, name='viewevents'),
    path('createorg/', views.create_org, name='createorg'),
    path('creategroup/', views.create_group, name='creategroup'),
    path('createevent/', views.create_event, name='createevent'),
    path('vieworgs/', views.view_organizations, name='vieworgs'),
    path('joinorg/', views.join_org, name='joinorg'),
    path('deleteorg/<int:org_id>/', views.delete_organization, name='delete_organization'),
    path("update-user-group/", views.update_user_group, name="update_user_group"),
    path("add-user-to-group/", views.add_user_to_group, name="add_user_to_group"),
    path("remove-user-from-group/", views.remove_user_from_group, name="remove_user_from_group"),
    path("update-group-name/", views.update_group_name, name="update_group_name")
]
