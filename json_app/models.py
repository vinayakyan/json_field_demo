from django.db import models


class Employee(models.Model):
    emp_id = models.BigAutoField(primary_key=True)
    first_name = models.CharField(max_length = 20)
    last_name = models.CharField(max_length = 20)
    company = models.JSONField(null = True)
    projects = models.JSONField(null = True)
    designation = models.CharField(max_length = 30)
    salary = models.FloatField()

    def __str__(self) -> str:
        return {self.full_name}

    @property
    def full_name(self)-> str:
        return f'{self.first_name} {self.last_name}'
