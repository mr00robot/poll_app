from rest_framework import serializers

from api.models import Poll, Question, Answer, Choices


class PollSerializer(serializers.ModelSerializer):
    class Meta:
        model = Poll
        fields = '__all__'

    def update(self, instance, validated_data):
        if 'start_date' in validated_data:
            raise serializers.ValidationError({
                'start_date': 'You must not change this field.',
            })

        return super().update(instance, validated_data)


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = '__all__'


class ChoicesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choices
        fields = '__all__'


class AnswersSerializerByID(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = '__all__'
        lookup_field = 'user_id'
