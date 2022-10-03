from rest_framework import serializers
from .models import Employee


class EmployeeSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(write_only=True)
    last_name = serializers.CharField(write_only=True)
    class Meta:
        model = Employee
        fields = ('emp_id','first_name','last_name','designation','projects','company','full_name', 'salary')