from django.urls import include, path
from rest_framework import routers
from charts import views
from django.contrib import admin


router = routers.DefaultRouter()
# URL for Stock Restful API
router.register(r'stock', views.StockViewSet)


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    # URL for calculating best portfolio
    path('portfolio/', views.portfolio),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
