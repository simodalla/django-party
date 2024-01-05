import datetime
from typing import Any

from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models.query import QuerySet
from django.views.generic import ListView

from party.models import Party


class PartyListPage(LoginRequiredMixin, ListView):
    template_name = "party/party_list/page_parties_list.html"
    context_object_name = "parties"

    def get_queryset(self) -> QuerySet[Party]:
        return Party.objects.filter(
            organizer=self.request.user, party_date__gte=datetime.date.today()
        ).order_by("party_date")
