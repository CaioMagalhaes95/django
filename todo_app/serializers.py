from rest_framework import serializers
from .models import Task

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'
        
        extra_kwargs = {
            'title': {'help_text': 'Título da tarefa'},
            'description': {'help_text': 'Descrição da tarefa'},
            'completed': {'help_text': 'Status de conclusão da tarefa'},
            'category': {'help_text': 'Categoria da tarefa'},
            'test_count': {'help_text': 'Quantidade de testes'},
            'requested_test_count': {'help_text': 'Quantidade de testes solicitados pelo cliente'},
            'particulate': {'help_text': 'Indica se a tarefa é particulada'},
            'base_value': {'help_text': 'Valor base para cálculo'},
            'calculated_value': {'help_text': 'Valor calculado com base em base_value'},
        }