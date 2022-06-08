from django.urls import path
from . import views
from django.contrib import admin

admin.site.site_header = "Vinayak Mart Administration"
admin.site.site_title = "Database"
admin.site.index_title = "Application Database"

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('customer', views.customer, name='customer'),
    path('inventory', views.inventory, name='inventory'),
    path('order', views.order, name='place_order'),
    path('purchase', views.purchase_return, name='purchase_return'),
    path('sales', views.sales_return, name='sales_return'),
    path('staff', views.staff, name='staff'),
    path('transaction', views.transaction, name='new_transaction'),
    path('loadproductdetails', views.show_added_products, name='load_products'),
    path('changeddropdown', views.chained_dropdown, name='chained_dropdown'),
    path('showsupplierinfo', views.show_supplier_info, name='show_supplier_info'),
    path('show_added_products_orders', views.show_added_products_orders, name='show_added_products_orders'),
    path('changeddropdownorders', views.chained_dropdown_orders, name='changeddropdownorders'),
    path('chaineddropdownsales', views.chained_dropdown_sales, name='chained_dropdown_sales'),
    path('show_added_products_sales', views.show_added_products_sales, name='show_added_products_sales'),
    path('chaineddropdownpurchase', views.chained_dropdown_purchase, name='chained_dropdown_purchase'),
    path('show_added_products_purchase', views.show_added_products_purchase, name='show_added_products_purchase'),
    path('generatepdf/<order_id>/', views.generatepdf, name='generatepdf'),
    path('graphs', views.generate_graphs, name='generategraphs')
]
