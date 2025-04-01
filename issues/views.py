from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView,
    DetailView
)
from .models import Issue, Status
from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    UserPassesTestMixin
)
from django.urls import reverse_lazy
from django.contrib import messages
from django.shortcuts import redirect

class BoardView(ListView):
    template_name = "issues/board.html"
    model = Issue

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        to_do = Status.objects.get(name="to do")
        in_progress = Status.objects.get(name="in progress")
        done = Status.objects.get(name="done")
        context["to_do_list"] = (
            Issue.objects
            .filter(status=to_do)
            .order_by("created_on").reverse()
        )
        context["in_progress_list"] = (
            Issue.objects
            .filter(status=in_progress)
            .order_by("created_on").reverse()
        )
        context["done_list"] = (
            Issue.objects
            .filter(status=done)
            .order_by("created_on").reverse()
        )
        return context
    
class IssueUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    template_name = "issues/edit.html"
    model = Issue
    fields = [
        "title", "summary", "status", "assignee"
    ]
    success_url = reverse_lazy("board")

    def test_func(self):
        issue = self.get_object()
        return issue.reporter == self.request.user
    
    
class IssueCreateView(LoginRequiredMixin, CreateView):
    template_name = "issues/new.html"
    model = Issue
    fields = ["title", "summary", "assignee", "status",]
    success_url = reverse_lazy("board")

    def form_valid(self, form):
        form.instance.reporter = self.request.user
        return super().form_valid(form)
    
class IssueDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    template_name = "issues/delete.html"
    model = Issue
    success_url = reverse_lazy("board")

    def test_func(self):
        issue = self.get_object()
        return issue.reporter == self.request.user
    
