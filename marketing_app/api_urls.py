from rest_framework.routers import DefaultRouter
from .api import CampaignViewSet, LeadViewSet

router = DefaultRouter()
router.register(r'campaigns', CampaignViewSet)
router.register(r'leads', LeadViewSet)

urlpatterns = router.urls
