from django.shortcuts import render_to_response, get_object_or_404
from polls.models import Poll

def index(request):
  polls = Poll.objects.all()
  return render_to_response("polls.html", {"polls": polls})

def detail(request, poll_id):
  poll = get_object_or_404(Poll, pk=poll_id)
  return render_to_response("poll-detail.html", {"poll" : poll})