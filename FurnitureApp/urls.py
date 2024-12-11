from django.urls import path
from FurnitureApp import views

urlpatterns = [
    path('Index/', views.Index, name="Index"),

    path('Add_categories/', views.Add_categories, name="Add_categories"),
    path('Save_categories/', views.Save_categories, name="Save_categories"),
    path('Display_categories/', views.Display_categories, name="Display_categories"),
    path('Edit_categories/<int:Cate_id>/', views.Edit_categories, name="Edit_categories"),
    path('Update_categories/<int:Cate_id>/', views.Update_categories, name="Update_categories"),
    path('Delete_categories/<int:Cate_id>/', views.Delete_categories, name="Delete_categories"),

    path('Add_Products/', views.Add_products, name="Add_products"),
    path('Save_products/', views.Save_products, name="Save_products"),
    path('Display_products/', views.Display_products, name="Display_products"),
    path('Edit_products/<int:Pro_id>/', views.Edit_products, name="Edit_products"),
    path('Update_products/<int:Pro_id>/', views.Update_products, name="Update_products"),
    path('Delete_products/<int:Pro_id>/', views.Delete_products, name="Delete_products"),

    path('Admin_login/', views.Admin_login, name="Admin_login"),
    path('Admin_loginCheck', views.Admin_loginCheck, name="Admin_loginCheck"),
    path('Admin_logout/', views.Admin_logout, name="Admin_logout"),

    path('Contact_data/', views.Contact_data, name="Contact_data"),
    path('Delete_contact/<int:contact_id>/', views.Delete_contact, name="Delete_contact")
]
