from rest_framework import serializers
from .models import *

class multipuleImageSerializer(serializers.ModelSerializer):
    class Meta:
        model=multipleImages
        fieldes=["id","product","extra_images"]


class productSerializer(serializers.ModelSerializer):
    extra_images=multipuleImageSerializer(many=True,read_only=True)
    upload_images=serializers.ListField(
        child=serializers.ImageField(max_length=100,allow_empty_file=False,use_url=False),
        write_only=True
    )

    class Meta:
        model=productModel
        fields=["id","title","price","image","category","extra_images","upload_images"]
    
    def create(self,validate):
        upload_images = validate.pop("upload_images")
        product=productModel.objects.create(**validate)
        for img in upload_images:
            newProduct=multipleImages.objects.create(product=product,extra_images=img)
        return product
    
