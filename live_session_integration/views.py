from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Batch, LiveSession
from .serializers import BatchSerializer, LiveSessionSerializer


class BatchViewSet(viewsets.ModelViewSet):
    queryset = Batch.objects.all()
    serializer_class = BatchSerializer
    permission_classes = [permissions.IsAuthenticated]


class LiveSessionViewSet(viewsets.ModelViewSet):
    queryset = LiveSession.objects.all()
    serializer_class = LiveSessionSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(tutor=self.request.user)

    @action(detail=True, methods=['patch'], permission_classes=[permissions.IsAdminUser])
    def upload_recording(self, request, pk=None):
        session = self.get_object()
        recording_link = request.data.get('recording_link')
        if recording_link:
            session.recording_link = recording_link
            session.save()
            return Response({'status': 'Recording uploaded successfully'})
        return Response({'error': 'Recording link is required'}, status=400)
