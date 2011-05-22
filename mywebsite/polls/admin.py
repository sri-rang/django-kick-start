from django.contrib import admin
from polls.models import Poll, Choice

#admin.site.register(Poll)
#admin.site.register(Choice)

class ChoiceInline(admin.StackedInline):
  model = Choice
  extra = 3
  pass

class PollAdmin(admin.ModelAdmin):
  fields = ['question']
  inlines = [ChoiceInline]
  pass

admin.site.register(Poll, PollAdmin)
