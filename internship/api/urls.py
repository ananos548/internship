from rest_framework.routers import SimpleRouter

from .views import InvestmentProjectViewSet, NewsViewSet

router = SimpleRouter()

router.register(r'main/news', NewsViewSet)
router.register(r'investor/investment_projects', InvestmentProjectViewSet)

urlpatterns = [

]

urlpatterns += router.urls
