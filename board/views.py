from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

from rest_framework import viewsets
from rest_framework.parsers import JSONParser

from board.models import Board
from board.serializers import BoardDetailsSerializer, BoardListSerializer


class BoardDetailsViewSet(viewsets.ModelViewSet):
    queryset = Board.objects.all()
    serializer_class = BoardDetailsSerializer


class BoardListViewSet(viewsets.ModelViewSet):
    queryset = Board.objects.all()
    serializer_class = BoardListSerializer


@csrf_exempt
def board_list(request):
    if request.method == 'GET':
        board = Board.objects.all()
        serializer = BoardListSerializer(board, many=True)
        return JsonResponse(serializer.data, safe=False)


@csrf_exempt
def board_write(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = BoardDetailsSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def board_detail(request, pk):
    try:
        board = Board.objects.get(pk=pk)
    except Board.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = BoardDetailsSerializer(board)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = BoardDetailsSerializer(board, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        board.delete()
        return HttpResponse(status=204)
