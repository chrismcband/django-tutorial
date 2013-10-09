import datetime
from django.db.models import Model, CharField, DateTimeField, \
    ForeignKey, IntegerField
from django.utils import timezone

# Create your models here.
class Poll(Model):
    question = CharField(max_length=200)
    pub_date = DateTimeField('date published')
    
    def __unicode__(self):  # Python 3: def __str__(self):
        return self.question

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date < now

class Choice(Model):
    poll = ForeignKey(Poll)
    choice_text = CharField(max_length=200)
    votes = IntegerField(default=0)
