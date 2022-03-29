from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

    # THIS IS A TUPLE FOR OUR STATUS
STATUS = ((0, "Draft"), (1, "Published"))


class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
                   # this CASCADE attribute means thta if one record in our many to one
#                  # relationship is deleted. Then the related records will be deleted too
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="blog_posts"
    )
    featured_image = CloudinaryField('image', default='placeholder')
    excerpt = models.TextField(blank=True)
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    likes = models.ManyToManyField(
        User, related_name='blogpost_like', blank=True)

    class Meta:
             # the minus sign here means to use descending order
            # so the latest post will be listed first 
        ordering = ["-created_on"]

    # it is good practice to add the string method in our projects
    # returns a string representation of an object
    def __str__(self):
        return self.title

    def number_of_likes(self):
        return self.likes.count()

 # OUR TABLE FOR POSTS IS NOW COMPLETE!!!

 # TABLE FOR COMMENTS

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE,
                             related_name="comments")
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        # the order of the comments will be ascending
        # so the oldest comment will be listed first which make sense if we want this
        # to be a conversation
        ordering = ["created_on"]

    def __str__(self):
        return f"Comment {self.body} by {self.name}"



