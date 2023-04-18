from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Stats
from .serializers import StatsSerializer
from rest_framework import status
# Create your views here.
@api_view(['Get'])
def getRoutes(request):
    return Response({'/stats':"You will get all the numbers of followers for each artist in the list bellow each day.",
                     '/stats/usernames_of_the_artist':'You will get all the enfo of the artist',
                     'The list':['rutshelle','darlinedesca','vanessa_desireofficiel','fatiful','aniealerte','tafaayiti','bedjineofficiel','blondedyferdinandshop'
    ]
                     })  

@api_view(['Get','Post'])
def getStats(request):
    if request.method == 'GET':
        stats = Stats.objects.all()
        serializer = StatsSerializer(stats, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = StatsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['Get','Delete','Put'])
def getStat(request,stat_id):
    if request.method == 'GET':
        stats = Stats.objects.get(id=stat_id)
        serializer = StatsSerializer(stats)
        return Response(serializer.data)
    elif request.method == 'DELETE':
        stats = Stats.objects.get(id=stat_id)
        stats.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    elif request.method == 'PUT':
        stats = Stats.objects.get(id=stat_id)
        serializer = StatsSerializer(stats, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)