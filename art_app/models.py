from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator



class Category(models.Model):
    name = models.CharField(max_length=60, default="")
   

    @classmethod
    def get_categories(cls):
        categories = Category.objects.all()
        return categories
    def __str__(self):
        return self.name

    @classmethod
    def update_categories(cls, id, value):
        cls.objects.filter(id=id).update(art=value)
    def save_category(self):
        self.save()
    def delete_category(self):
        self.delete()

class Art(models.Model):
    title = models.CharField(max_length=155)
    art_image = models.ImageField(upload_to='landing_images/', null=True)
    description = models.TextField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    category = models.ForeignKey(Category,on_delete=models.CASCADE, null=True)
    date = models.DateTimeField(auto_now_add=True, null=True)
    

    

    @classmethod
    def filter_by_category(cls, category):
        image_category = Art.objects.filter(category__name=category).all()
        return image_category

    @classmethod
    def get_all_arts(cls):
        all_arts = cls.objects.all()
        return all_arts

    def save_arts(self):
        self.save()


    def delete_arts(self):
        self.delete()


    @classmethod
    def search_by_title(cls,search_term):
        certain_user = cls.objects.filter(title__icontains = search_term)
        return certain_user


    def __str__(self):
        return self.title


class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to='profile_photo/', null=True)
    bio = models.CharField(max_length=255)
    
    contact = models.TextField(max_length=255)
    arts = models.ForeignKey(Art, on_delete=models.CASCADE, null=True)

    @classmethod
    def get_profile(cls):
        all_profiles = cls.objects.all()
        return all_profiles

    def save_profles(self):
        self.save()


    def delete_profiles(self):
        self.delete()


    def __str__(self):
        return str(self.user)


class Comments(models.Model):
    comment = models.CharField(max_length=250)
    user = models.ForeignKey(User,on_delete=models.CASCADE, null=True)
    posted_by = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True)
    commented_art = models.ForeignKey(Art, on_delete=models.CASCADE, null=True)

    def save_comments(self):
        self.save()

    def delete_comments(self):
        self.delete()

    def __str__(self):
        return self.posted_by





   


