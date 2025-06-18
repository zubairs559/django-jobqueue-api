from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from rest_framework import permissions
from rest_framework_simplejwt.authentication import JWTAuthentication

from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from books.swagger import CustomSchemaGenerator  # adjust path if needed


# schema_view = get_schema_view(
#     openapi.Info(
#         title="Book API",
#         default_version='v1',
#         description="API documentation with JWT authentication",
#     ),
#     public=True,
#     permission_classes=(permissions.AllowAny,),
#     authentication_classes=[],
# )


schema_view = get_schema_view(
    openapi.Info(
        title="Book API",
        default_version='v1',
        description="API documentation with JWT authentication",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
    generator_class=CustomSchemaGenerator,  # ✅ Use custom class
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('books.urls')),

    # ✅ Swagger and ReDoc endpoints
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('api/', include('jobs.urls')),  # add this line along with books


]

# Static files (only needed in development)
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)