from rest_framework.renderers import JSONRenderer
from rest_framework.views import APIView, exception_handler


class BaseJSONRenderer(JSONRenderer):
    """
    Base JSON response renderer
    """
    def render(self, data, media_type=None, renderer_context=None):
        return super().render(data, media_type, renderer_context)


class BaseApiView(APIView):
    """
    Base API View
    """
    renderer_classes = [BaseJSONRenderer]


def base_api_exception_handler(exc, context):
    response = exception_handler(exc, context)
    return response
