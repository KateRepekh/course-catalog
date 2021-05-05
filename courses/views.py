from rest_framework import viewsets
from rest_framework.filters import SearchFilter

from django_filters.rest_framework import DjangoFilterBackend

from courses.models import Course
from courses.serializers import CourseSerializer


class CourseViewSet(viewsets.ModelViewSet):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()
    filter_backends = [SearchFilter, DjangoFilterBackend]
    search_fields = ["name"]
    filterset_fields = ["start_date", "end_date"]
