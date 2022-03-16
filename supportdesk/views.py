from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import IssueTicketForm
from .models import IssueTickets
from django.db.models import Q
from django.core.paginator import Paginator


def place_holder_home(request):
    return render(request, "supportdesk/placeholder.html")


@login_required(login_url='/auth/login/')
def create_ticket(request):
    if not request.user.is_staff or request.user.is_superuser:
        if request.method == "POST":
            form = IssueTicketForm(request.POST)
            if form.is_valid():
                print(request.user)
                ticket = form.save(commit=False)
                ticket.creator = request.user
                ticket = ticket.save()
                return redirect('/supportdesk/list/tickets')

        else:
            form = IssueTicketForm()
            context = {
                "form": form,
            }
            return render(request, "supportdesk/ticket_creation_form.html", context)
    else:
        return redirect('/auth/login')


@login_required(login_url='/auth/login/')
def list_customer_tickets(request):
    if not request.user.is_staff or request.user.is_superuser:
        page = request.GET.get('page', 1)
        tickets = IssueTickets.objects.filter(Q(creator=request.user))
        page_data = Paginator(tickets, 30)
        context = {
            "tickets": page_data.page(page)}
        return render(request, "supportdesk/ticket_listing.html", context)
    else:
        return redirect('/auth/login')


@login_required(login_url='/auth/login/')
def list_agent_tickets(request):
    if request.user.is_staff or request.user.is_superuser:
        page = request.GET.get('page', 1)
        tickets = IssueTickets.objects.filter(Q(assigned_to=request.user))
        page_data = Paginator(tickets, 30)
        context = {
            "tickets": page_data.page(page)}
        return render(request, "supportdesk/agent_tickets.html", context)
    else:
        return redirect('/auth/login')


@login_required(login_url='/auth/login/')
def list_single_ticket(request):
    if request.user.is_staff or request.user.is_superuser:
        ticket_id = request.GET.get('id', 1)
        ticket = IssueTickets.objects.get(id=ticket_id)
        context = {
            "ticket": ticket}
        return render(request, "supportdesk/ticket_view.html", context)
    else:
        return redirect('/auth/login')
