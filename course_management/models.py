from django.db import models
from django.contrib.auth.models import User
from datetime import date
from decimal import Decimal

class AboutAuthor(models.Model):
    name = models.CharField(max_length=255)
    institution = models.CharField(max_length=255)
    total_reviews = models.IntegerField(default=0)  
    bio = models.TextField()
    profile_image = models.ImageField(upload_to='author_pics/', blank=True, null=True)  
    rating = models.FloatField(default=0.0)
    
    # Author's Education
    degree = models.CharField(max_length=255)
    education_institution = models.CharField(max_length=255)
    year_start = models.IntegerField()
    year_end = models.IntegerField(null=True, blank=True)
    icon = models.ImageField(upload_to='education_icons/', blank=True, null=True)  

    def __str__(self):
        return f"{self.name} ({self.institution}) - {self.degree} ({self.education_institution}, {self.year_start}-{self.year_end or 'Present'})"

class Instructor(models.Model):
    name = models.CharField(max_length=255)
    bio = models.TextField()
    rating = models.FloatField(default=4.5)
    education = models.CharField(max_length=255)
    experience = models.TextField()
    author = models.ForeignKey(AboutAuthor, on_delete=models.SET_NULL, null=True, blank=True, related_name='instructors')

    def __str__(self):
        return f"{self.name} (Rating: {self.rating})"

class Course(models.Model):
    CATEGORY_CHOICES = [
        ('Bestseller', 'Bestseller'),
        ('Top Author', 'Top Author'),
        ('Most Popular', 'Most Popular'),
        ("Editor's Choice", "Editor's Choice")
    ]

    title = models.CharField(max_length=255)
    about_author = models.ForeignKey(AboutAuthor, on_delete=models.SET_NULL, null=True, blank=True, related_name='courses')
    instructor = models.ForeignKey(Instructor, on_delete=models.SET_NULL, null=True, blank=True, related_name='courses')
    description = models.TextField()
    image = models.ImageField(upload_to='course_images/', blank=True, null=True) 
    original_price = models.DecimalField(max_digits=6, decimal_places=2)
    discount_percent = models.FloatField(default=0.0)   
    is_discount_active = models.BooleanField(default=False)
    last_updated = models.DateField(auto_now=True)
    start_date = models.DateField()
    is_certificate_included = models.BooleanField(default=False)
    assignments_count = models.PositiveIntegerField(default=0)
    lifetime_access = models.BooleanField(default=True)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, blank=True, null=True)
    rating = models.FloatField(default=0.0)
    reviews_count = models.IntegerField(default=0)

    def discounted_price(self):
        if self.is_discount_active and self.discount_percent > 0:
            original_price = Decimal(self.original_price)
            discount_decimal = Decimal(self.discount_percent) / Decimal(100) 
            discounted_price = original_price * (Decimal('1') - discount_decimal)  
            return discounted_price.quantize(Decimal('0.01'))  

        return Decimal(self.original_price).quantize(Decimal('0.01')) 

    def time_left(self):
        days_remaining = (self.start_date - date.today()).days
        return max(0, days_remaining)  

    def average_rating(self):
        reviews = self.reviews.all()
        if reviews.exists():
            return round(sum(review.rating for review in reviews) / reviews.count(), 2)
        return 0.0  

    def __str__(self):
        return f"{self.title} ({self.about_author.name})"

class LearningPoint(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='learning_points')
    title = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return f"{self.course.title} - {self.title}"

class CourseDetail(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='course_details')
    batch_start_date = models.DateField()
    batch_code = models.CharField(max_length=50)
    meeting_id = models.CharField(max_length=50)
    quiz_topic = models.CharField(max_length=255)
    mini_project = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.course.title} - Batch {self.batch_code}"

class CourseMaterial(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='materials')
    title = models.CharField(max_length=255)
    category = models.CharField(max_length=100)  
    content = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.course.title} - {self.title} ({self.category})"

class Review(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.FloatField()
    date_posted = models.DateTimeField(auto_now_add=True)  
    comment = models.TextField()
    profile_image = models.ImageField(upload_to='profile_images/', null=True, blank=True)

    def __str__(self):
        return f"Review by {self.user.username} - ⭐{self.rating}"
