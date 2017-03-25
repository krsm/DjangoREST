from django.db import models

# Create your models here.


class ToDoList(models.Model):

    """ Class to represent the ToDoList Model """

    name = models.CharField(max_length=150, blank=False)
    description = models.TextField()
    deadline = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):

        """ Human readable representation of model instance """
        return "{}".format(self.name)

