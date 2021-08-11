# Import Python Packages.
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .serializer import ShortenerSerializers
from .models import UrlDetail


# Create class for create short url of long url.
class index(APIView):

    def post(self, request):
        if request.method == "POST":  # Check method is post or not.
            serializer = ShortenerSerializers(data=request.data)
            if serializer.is_valid():
                url = serializer.validated_data
                data_response = {'detail': "Get Short URL.", 'status': 1, 'sort_url': url}
                return Response(data_response)


# Create class for get main url.
class GetUrl(APIView):

    def get(self, request, token):
        if UrlDetail.objects.filter(token=token).exists():  # Check token exist or not.
            url_instance = get_object_or_404(UrlDetail, token=token)
            data_response = {'detail': "Get Main URL.", 'status': 1, 'main_url': url_instance.url}
        else:
            data_response = {'detail': "Invalid URL.", 'status': 0}
        return Response(data_response)
