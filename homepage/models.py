from django.db import models
from django.contrib.auth.models import User
from datetime import date
from decimal import Decimal

class Instructor(models.Model):
    name = models.CharField(max_length=255)
    bio = models.TextField()
    rating = models.FloatField(default=4.5)
    education = models.CharField(max_length=255)
    experience = models.TextField()

    def __str__(self):
        return f"{self.name} (Rating: {self.rating})"

class Course(models.Model):
    title = models.CharField(max_length=255)
    instructor = models.ForeignKey(Instructor, on_delete=models.CASCADE, related_name='courses')
    description = models.TextField()
    image = models.ImageField(upload_to='course_images/', blank=True, null=True) 
    price = models.DecimalField(max_digits=6, decimal_places=2)
    discount = models.FloatField(default=0.0)  # Discount in percentage
    is_discount_active = models.BooleanField(default=False)
    last_updated = models.DateField(auto_now=True)
    start_date = models.DateField()
    is_certificate_included = models.BooleanField(default=False)
    assignments_count = models.PositiveIntegerField(default=0)
    lifetime_access = models.BooleanField(default=True)

    def discounted_price(self):
        if self.is_discount_active:
            discount_decimal = Decimal(str(self.discount)) / Decimal('100')
            return self.price * (Decimal('1') - discount_decimal)
        return self.price

    def time_left(self):
        """Calculates the days remaining until the course starts."""
        days_remaining = (self.start_date - date.today()).days
        return max(0, days_remaining)  

    def average_rating(self):
        """Calculates the average rating from all reviews."""
        reviews = self.reviews.all()
        if reviews.exists():
            return round(sum(review.rating for review in reviews) / reviews.count(), 2)
        return 0.0  

    def __str__(self):
        return f"{self.title} ({self.instructor.name})"

class LearningPoint(models.Model):
    course = models.ForeignKey(Course, related_name='learning_points', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return f"{self.course.title} - {self.title}"

class CourseDetail(models.Model):
    course = models.OneToOneField(Course, on_delete=models.CASCADE, related_name='course_detail')
    certificate = models.BooleanField(default=False)
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
    course = models.ForeignKey(Course, related_name='reviews', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.FloatField()
    date_posted = models.DateTimeField(auto_now_add=True)  
    comment = models.TextField()
    profile_image = models.ImageField(upload_to='profile_images/', null=True, blank=True)

    def __str__(self):
        return f"Review by {self.user.username} - {self.rating}⭐"

class Author(models.Model):
    name = models.CharField(max_length=255)
    institution = models.CharField(max_length=255)
    total_reviews = models.IntegerField(default=0)  
    bio = models.TextField()
    profile_image = models.ImageField(upload_to='author_pics/', blank=True, null=True)  
    rating = models.FloatField(default=0.0) 

    def __str__(self):
        return f"{self.name} ({self.institution})"

class Education(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='education')
    degree = models.CharField(max_length=255)
    institution = models.CharField(max_length=255)
    year_start = models.IntegerField()
    year_end = models.IntegerField(null=True, blank=True)
    icon = models.ImageField(upload_to='education_icons/', blank=True, null=True) 

    def __str__(self):
        return f"{self.degree} ({self.institution}, {self.year_start}-{self.year_end or 'Present'})"
