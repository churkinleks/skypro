from django.shortcuts import get_object_or_404

from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .models import Resume
from .serializers import ResumeSerializer


class ResumeViewSet(viewsets.ViewSet):
    """
    Endpoints for processing methods GET(all) and PATCH(is_staff)
    """
    permission_classes = [IsAuthenticatedOrReadOnly]

    def list(self, request):
        queryset = Resume.objects.all()
        serializer = ResumeSerializer(queryset, many=True)
        return Response(serializer.data)

    def partial_update(self, request, pk):
        data = request.data
        resume = get_object_or_404(Resume, pk=pk)

        serializer = ResumeSerializer(resume, data=data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({'status': 'OK'})
