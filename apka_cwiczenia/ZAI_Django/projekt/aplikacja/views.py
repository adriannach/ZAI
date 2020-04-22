from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from .models import Questions
from .serializers import QuestionsSerializer

@api_view(['GET','POST'])
def question_list(request, serialized_question=None):
    if request.method == 'GET':
        questions = Questions.object.all()
        serialized_questions = QuestionsSerializer(questions,many=True)
        return Response(serialized_questions.data)
    elif request.method == 'POST':
        dane = JSONParser.parse(request)
        serialized_request = QuestionsSerializer(data=dane)
        if serialized_question.is_valid():
            serialized_question.save()
            return Response(serialized_question.data, status=201)
        return Response(serialized_question.errors, status=400)


@api_view(['GET','PUT','DELETE'])
def quesion_detail(request, pk):
    try:
        question = Questions.objects.get(pk=pk)
    except Questions.DoesNotExist:
        return Response(status=404)

    if request.method == 'GET':
        serialized_question = QuestionsSerializer(question)
        return Response(serialized_question.data)

    elif request.method == 'PUT':
        dane = JSONParser().parse(request)
        serialized_question = QuestionsSerializer(question,data=dane)
        if serialized_question.is_valid():
            serialized_question.save()
            return Response(serialized_question.data)
        return Response(serialized_question.errors, status=400)

    elif request.method == 'DELETE':
        question.delete()
        return Response(status=204)