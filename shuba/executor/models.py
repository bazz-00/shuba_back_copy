from user.models import User
from django.db import models
from order.models import phoneNumberRegex



class Speciality(models.Model):
    title = models.CharField(max_length=30)

    class Meta:
        db_table = 'speciality'

    def __str__(self):
        return self.title


class Executor(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone_number = models.CharField(validators=[phoneNumberRegex], max_length=16)
    city = models.CharField(max_length=50)
    photo = models.URLField(blank=True)
    is_active = models.BooleanField(default=True)
    user_id = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    speciality = models.ManyToManyField(Speciality)

    class Meta:
        db_table = 'executor'

    def __str__(self):
        return self.last_name



class ExecutorComments(models.Model):
    executor = models.ForeignKey(Executor, on_delete=models.CASCADE, related_name='comments_executor')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments_executor')
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ('created',)
        db_table = 'executor_comments'


    def __str__(self):
        return 'Comment by {} on {}'.format(self.user, self.executor)



