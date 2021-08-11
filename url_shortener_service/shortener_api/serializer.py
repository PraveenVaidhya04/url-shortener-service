# Import python package.
from rest_framework import serializers
from rest_framework import exceptions
from .models import UrlDetail
from django.conf import settings


# Create serializer for Business Info.
class ShortenerSerializers(serializers.Serializer):
    # Create some field for User Login like email, password.
    url = serializers.CharField(style={"input_type": "text"}, write_only=True, required=False, allow_blank=True)

    # Create a validate function for Login.
    def validate(self, data):
        url = data.get("url", "")
        if url:
            if UrlDetail.objects.filter(url=url).exists():  # Check user exist or not.
                mes = "This URL already exist."  # Message if email not registered.
                raise exceptions.APIException(mes)  # Call message if email not registered.
            else:
                url_data = UrlDetail(url=url)
                url_data.save()
                return str(settings.BASE_URL + url_data.token)
        else:
            mes = "Please Enter URL."  # Message if email not registered.
            raise exceptions.APIException(mes)  # Call message if email not registered.
# ======================================================================================================================
