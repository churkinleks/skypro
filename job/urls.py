from rest_framework.routers import DefaultRouter

from .views import ResumeViewSet

app_name = 'job'

router = DefaultRouter(trailing_slash=False)
router.register(r'resume', ResumeViewSet, basename='resume')

urlpatterns = router.urls
