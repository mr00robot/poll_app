from django.db import models


class Poll(models.Model):
    title = models.CharField(max_length=250)
    start_date = models.DateField(null=True)
    end_date = models.DateField(null=True)
    description = models.TextField()

    def __str__(self):
        return self.title


class Question(models.Model):
    TEXT = 1
    ONE_CHOICE = 2
    MULTIPLE_CHOICE = 3
    TYPE_CHOICES = (
        (TEXT, 'Text'),
        (ONE_CHOICE, 'Choice of One'),
        (MULTIPLE_CHOICE, 'Multiple Choice')
    )
    text_question = models.TextField()
    type_of_question = models.IntegerField(choices=TYPE_CHOICES)
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE)

    def __str__(self):
        return self.text_question


class Choices(models.Model):
    description = models.TextField()

    def __int__(self):
        return self.pk


class Answer(models.Model):
    user_id = models.IntegerField(unique=True)
    text_answer = models.TextField(null=True)
    one_choice_answer = models.ForeignKey(Choices, blank=True, null=True, on_delete=models.NOT_PROVIDED,
                                          related_name='one_choice')
    multiple_choice_answer = models.ManyToManyField(Choices, blank=True, null=True, related_name='multiple_choice')
