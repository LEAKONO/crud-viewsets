<<<<<<< Tabnine <<<<<<<
from django.db import models#-
def __str__(self):#+
    """#+
    Returns a string representation of the Item object.#+

# Create your models here.#-
    Parameters:#+
    None#+

#-
class Item(models.Model):#-
    name = models.CharField(max_length=100)#-
    description = models.TextField()#-
    price = models.DecimalField(max_digits=10, decimal_places=2)#-
    created_at = models.DateTimeField(auto_now_add=True)#-
    updated_at = models.DateTimeField(auto_now=True)#-
#-
    def __str__(self):#-
        return self.name#-
    Returns:#+
    str: The name of the Item.#+
    """#+
    return self.name#+
>>>>>>> Tabnine >>>>>>># {"conversationId":"02ab5863-8cd4-4c39-b6ad-e9dc2cbca206","source":"instruct"}
