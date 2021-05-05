from rest_framework import serializers

from courses.models import Course


class CourseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Course
        fields = '__all__'

    def validate(self, data):

        def patch_field(key):
            value = data.get(key)
            return value if value else self.instance.__dict__[key]

        start_date = patch_field('start_date')
        end_date = patch_field('end_date')
            
        if start_date > end_date:
            raise serializers.ValidationError(
                "A course can't end before it starts"
            )
        return data
