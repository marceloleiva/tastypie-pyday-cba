from django.db import models
from django.contrib.auth.models import User


class Tweet(models.Model):
    user = models.ForeignKey(User)
    pub_date = models.DateTimeField(auto_now_add=True, auto_now=False)
    tweet = models.CharField(max_length=200)

    def __unicode__(self):
        return "[{user}] {tweet}".format(
            user=self.user,
            tweet=self.tweet
        )
