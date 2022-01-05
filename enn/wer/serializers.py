from rest_framework.serializers import ModelSerializer
from.models import items
class itemsserializers(ModelSerializer):
     class Meta:
         model=items
         fields=['name','costperitem','description','stockquantity','volume']