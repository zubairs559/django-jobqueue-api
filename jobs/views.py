from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import uuid

from .job_worker import add_job, job_results
from .serializers import JobCreateSerializer  # ✅ serializer
from drf_yasg.utils import swagger_auto_schema  # ✅ important
from drf_yasg import openapi
from .job_queue import get_job_status


class JobCreateView(APIView):
    @swagger_auto_schema(request_body=JobCreateSerializer)
    def post(self, request):
        serializer = JobCreateSerializer(data=request.data)
        if serializer.is_valid():
            payload = serializer.validated_data['payload']
            job_id = str(uuid.uuid4())
            add_job(job_id, payload)
            return Response({"job_id": job_id}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class JobStatusView(APIView):
    def get(self, request, job_id):
        job = get_job_status(job_id)
        if not job:
            return Response({'error': 'Job not found'}, status=404)

        return Response({'job_id': job_id, 'status': job['status'], 'result': job['result']})
