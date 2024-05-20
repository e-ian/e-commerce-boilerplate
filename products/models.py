from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)
    #parent = models.ForeignKey('self', ...), the self argument indicates that the field is related to the same model
    #it's defined within. This is often used in hierarchical or recursive relationships, such as when a model can have a relationship with other instances of itself.
    parent = models.ForeignKey('self', related_name='subcategories', on_delete=models.CASCADE, blank=True, null=True)
    #related_name='subcategories': This is the name used to access related objects in reverse relationships. 
    #In this case, it means that each instance of the model can have subcategories, and you can access them using the attribute subcategories.

    def __str__(self) -> str:
        return self.name
    
    
class Product(models.Model):
    name = models.CharField(max_length=255
                            )
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name