import boto3
from django.http import JsonResponse
from django.conf import settings
from .models import Lecture
from rest_framework.decorators import api_view, permission_classes
from .permissions import IsEnrolledOrInstructor
from rest_framework.permissions import IsAuthenticated

@api_view(['GET'])
@permission_classes([IsAuthenticated, IsEnrolledOrInstructor])
def get_presigned_s3_url(request, lecture_id):
    lecture = Lecture.objects.get(pk=lecture_id)
    BUCKET = getattr(settings, 'AWS_STORAGE_BUCKET_NAME', None)
    if not BUCKET:
        return JsonResponse({'error': 'S3 bucket not configured'}, status=500)
    s3 = boto3.client('s3')
    url = s3.generate_presigned_url('get_object', Params={'Bucket':BUCKET,'Key':lecture.video_s3_key}, ExpiresIn=300)
    return JsonResponse({'url': url})
