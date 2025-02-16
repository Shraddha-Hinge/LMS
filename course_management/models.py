from django.db import models

class Course(models.Model):
    title = models.CharField(max_length=255)
    instructor = models.CharField(max_length=255)
    duration = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    discounted_price = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    rating = models.FloatField()
    reviews = models.IntegerField()
    category = models.CharField(
        max_length=50,
        choices=[
            ('Bestseller', 'Bestseller'),
            ('Top Author', 'Top Author'),
            ('Most Popular', 'Most Popular'),
            ("Editor's Choice", "Editor's Choice")
        ],
        blank=True,
        null=True
    )
    image = models.ImageField(upload_to='course_images/', blank=True, null=True)

    def __str__(self):
        return self.title
