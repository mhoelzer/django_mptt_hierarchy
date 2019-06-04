from django.db import models
from mptt.models import MPTTModel, TreeForeignKey


class File(MPTTModel):
    name = models.CharField(max_length=75, unique=True)
    parent = TreeForeignKey("self", on_delete=models.CASCADE,
                            null=True, blank=True, related_name="children")

    class MPTTMeta:
        order_insertion_by = ["name"]

    def __str__(self):
        if self.parent is None:
            return f"{self.name} (big parent)"
        return f"{self.name} is part of {self.parent}"
