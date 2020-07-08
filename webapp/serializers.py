from rest_framework import serializers
from .models import employees


class empserializer(serializers.ModelSerializer) :

    class Meta:
        model=employees
        # fields=('firstname','lastname')
        fields= '__all__'

        # class FileUploaderSerializer(serializers.ModelSerializer):
        #     # overwrite = serializers.BooleanField()
        #     class Meta:
        #         model = FileUploader
        #         fields = ('file', 'name', 'version', 'upload_date', 'size')
        #         read_only_fields = ('name', 'version', 'owner', 'upload_date', 'size')
