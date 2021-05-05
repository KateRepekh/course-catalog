from rest_framework.routers import DefaultRouter

from courses.views import CourseViewSet

class OptionalSlashRouter(DefaultRouter):      
    def __init__(self, *args, **kwargs):         
        super(DefaultRouter, self).__init__(*args, **kwargs)         
        self.trailing_slash = '/?' 

router = OptionalSlashRouter()
router.register("courses", CourseViewSet)
urlpatterns = router.urls
