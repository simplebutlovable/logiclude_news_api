from django.db import models
from django.db.models.signals import post_delete, post_save, pre_save
from django.dispatch import receiver
from django.conf import settings
from django.core.files.storage import default_storage

from ckeditor.fields import RichTextField

from datetime import datetime
import random
import os, shutil


# Store the images in directory "temp" before moving to its specific directory
def upload_cdn(instance, filename):
    # Renaming the File before saving
    extension = "." + filename.split(".")[-1]
    filename = "Content Delievery Network/_" + str(random.randint(1000000, 9999999)) + extension
    return filename


# Dummy Model for testing purpose ONLY!
class TestBlog(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title


# Model for Storing all the News content
class News(models.Model):
    NEWS_CATEGORIES = (
        ("science", "Science"),
        ("gadgets", "Gadgets"),
        ("games", "Games"),
        ("stream", "Stream"),
    )
    top_of_the_week = models.BooleanField(default=False,
                                          blank=True,
                                          verbose_name="Top")
    editors_pick = models.BooleanField(default=False,
                                          blank=True,
                                          verbose_name="Pick")
    title = models.TextField(null=False, blank=False)
    author = models.CharField(max_length=30, null=False, blank=False)
    date_posted = models.DateTimeField(auto_now_add=True)
    category = models.CharField(choices=NEWS_CATEGORIES , max_length= 10)
    description = RichTextField(null=True, blank=True)
    display_image = models.ImageField(upload_to=upload_cdn,
                                      null=False,
                                      blank=False)

    class Meta:
        verbose_name_plural = "News"

    def __str__(self):
        return self.title


# # Move the image from the "temp" directory to its own directory
# @receiver(post_save, sender=News)
# def move_to_cdn(sender, instance, *args, **kwargs):
#     # declaring the target directory to save
#     today = datetime.now()
#     today_path = today.strftime("%Y/%m/%d")
#     target_dir = "{cdn_dir}/{date_dir}/{id}/".format(
#         cdn_dir=settings.MEDIA_ROOT, id=instance.id, date_dir=today_path)
#     # declaring the file to transfer
#     source_dir = "{cdn_dir}/temp/".format(cdn_dir=settings.MEDIA_ROOT)
#     # creating the directory if it doesn't exist
#     if not os.path.exists(target_dir):
#         os.makedirs(target_dir)
#     # getting all the files inside the "source_dir"
#     file_names = os.listdir(source_dir)
#     # looping all the filenames in the "file_name" variable and move to "target_dir" directory
#     for file_name in file_names:
#         shutil.move(os.path.join(source_dir, file_name), target_dir)
#         instance.display_image = today_path + "/" + str(instance.id) + "/" + file_name
#         instance.save()


# # Delete the old image if the object in database is deleted
# @receiver(post_delete, sender=News)
# def delete_cdn(sender, instance, *args, **kwargs):
#     path = instance.display_image.name
#     parent_path = os.path.relpath(os.path.join(path, os.pardir))
#     print("Parent Path", parent_path)
#     print("Main File", path)
#     # delete path and the file
#     if path:
#         default_storage.delete(path)
#         default_storage.delete(parent_path)


# # Delete the old image if it is changed by a new Image
# @receiver(pre_save, sender=News)
# def delete_old_image_on_update(sender, instance, *args, **kwargs):
#     if instance.pk:
#         try:
#             old_display_image = News.objects.get(pk=instance.pk).display_image

#         except News.DoesNotExist:
#             return

#         else:
#             new_display_image = instance.display_image
#             print("Old Image: ", old_display_image)
#             print("New Image: ", new_display_image)
#             if old_display_image != new_display_image:
#                 old_display_image.delete(save=False)



class Emails(models.Model):
    email = models.CharField(max_length=300, blank=False, unique=True)
    date_registered = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Emails"

    def __str__(self):
        return self.email