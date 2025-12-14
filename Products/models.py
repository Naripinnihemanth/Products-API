from django.db import models


class categoryModel(models.Model):
    categories=models.CharField(max_length=50)

    def __str__(self):
        return self.categories

    
class productModel(models.Model):
    id=models.IntegerField(primary_key=True,auto_created=True)
    title=models.CharField(max_length=50,default="New product")
    price=models.IntegerField()
    category=models.ForeignKey(categoryModel,on_delete=models.CASCADE,default="Null")
    image=models.ImageField(upload_to="product-images/",default="",null=True)

    def __str__(self):
        return self.title

class multipleImages(models.Model):
    product=models.ForeignKey(productModel,on_delete=models.CASCADE,related_name="images")
    extra_images=models.ImageField(upload_to='product-images/',default='',null=True,blank=True)