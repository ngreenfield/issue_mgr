from django.views.generic import ListView
from .models import Issue, Status


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