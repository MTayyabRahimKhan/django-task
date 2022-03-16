from django.urls import path
from . import views

urlpatterns = [
    path("placeholder/", views.place_holder_home, name="supportdesk_placeholder"),
    path("create/ticket/", views.create_ticket, name="create_ticket"),
    path("list/tickets/", views.list_customer_tickets, name="list_ticket"),
    path("agent/list/tickets/", views.list_agent_tickets, name="list_agent_ticket"),
    path("view/ticket/", views.list_single_ticket, name="view_ticket"),
]
