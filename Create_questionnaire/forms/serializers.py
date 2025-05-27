from rest_framework import serializers  
from .models import Form, Question, Option, Response, Answer

class OptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Option
        fields = ['id', 'text']

class QuestionSerializer(serializers.ModelSerializer):
    options = OptionSerializer(many=True, read_only=True)
    class Meta:
        model = Question
        fields = ['id', 'text', 'question_type', 'is_required', 'options']
        
class FormSerializer(serializers.ModelSerializer):
    form = QuestionSerializer(many=True, read_only=True)
    class Meta:
        model = Form
        fields = ['id', 'title', 'description', 'created_at', 'is_active', 'questions']
        
class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        filds = ['question', 'text_answer', 'selected_option']
        
class  ResponseSerializer(serializers.ModelSerializer):
    answers = AnswerSerializer(many=True)
    class Meta:
        model = Response
        fildes = ['form', 'answers']
    
    def create(self, validated_data):
        answers_data = validated_data.pop('answers')
        response = Response.objects.create(**validated_data)
        for answer_data in answers_data:
            Answer.objects.create(response=response, **answer_data)
        return response 
