from rest_framework import serializers

from tasks.models import Task

class TaskSerializer(serializers.ModelSerializer):
    title = serializers.CharField(min_length=2, max_length=200)

    class Meta:
        model = Task
        fields = ('id','title','complete','created',)
