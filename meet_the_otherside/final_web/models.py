from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Organization(models.Model):
    id = models.AutoField(primary_key=True, unique=True, null=False)
    name = models.CharField(max_length=300, blank=False, null=False, unique=True)
    description = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=300, blank=True)
    def __str__(self):
        return self.name

class Position(models.Model):
    id = models.AutoField(primary_key=True, unique=True, null=False)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    name = models.CharField(max_length=300, blank=False, null=False, unique=True)
    description = models.TextField(max_length=500, blank=True)
    def __str__(self):
        return self.name

class Profile(models.Model):
    id = models.AutoField(primary_key=True, unique=True, null=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField(default='default.png', upload_to='profile_pics')
    bio = models.TextField(max_length=500, blank=True)
    credibility = models.IntegerField(default=50, blank=False, null=False)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE, blank=True, null=True)
    position = models.ForeignKey(Position, on_delete=models.CASCADE, blank=True, null=True)
    location = models.CharField(max_length=300, blank=True)
    def __str__(self):
        return self.user.username

class Post(models.Model):
    id = models.AutoField(primary_key=True, unique=True, null=False)
    title = models.CharField(max_length=200)
    body = models.TextField(max_length=1000)
    date_posted = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    reliability = models.IntegerField(default=50, blank=False, null=False)

    def __str__(self):
        return self.user.username + ' - ' + self.title + ' - ' + str(id)

class Comments(models.Model):
    CHOICES = [
        ('None', 'Blank'),
        ('Fact', 'Fact'),
        ('MisInfo', 'Misinformation'),
        ('MisConst', 'Misconstrued')
    ]
     
    id = models.AutoField(primary_key=True, unique=True, null=False)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    type = models.CharField(max_length=300, choices = CHOICES, default='None')
    comment_date = models.DateTimeField(auto_now_add=True, blank=False, null=False)

    text = models.TextField()
    previous_comment = models.ForeignKey('self', null=True, blank=True, on_delete=models.DO_NOTHING)

class Votes(models.Model):
    CHOICES = [
        ('Up', 'Upvote'),
        ('Down', 'Downvote'),
        ('None', 'Not voted')
    ]
    type = [('Post', 'Post'), ('Comment', 'Comment')]
    id = models.AutoField(primary_key=True, unique=True, null=False)
    select_type = models.CharField(max_length=300, choices = type, blank=False, null=False)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, blank=True, null=True)
    comments = models.ForeignKey(Comments, on_delete=models.CASCADE, blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    vote = models.CharField(max_length=300, choices = CHOICES, default='None')

    def __str__(self):
        return self.user.username + ' - ' + self.post.title + ' - ' + str(id)

class PostImages(models.Model):
    post_image_id = models.AutoField(primary_key=True, blank=False, null=False)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='post_pictures')

class CommentImages(models.Model):
    post_image_id = models.AutoField(primary_key=True, blank=False, null=False)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='post_pictures')

class PostVideos(models.Model):
    post_video_id = models.AutoField(primary_key=True, blank=False, null=False)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    video = models.FileField(upload_to='post_videos')

class PostUrls(models.Model):
    post_url_id = models.AutoField(primary_key=True, blank=False, null=False)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    url = models.URLField()