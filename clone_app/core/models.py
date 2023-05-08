from django.db import models
from django.contrib.auth import get_user_model
from crum import get_current_user
from core.utlis import auto_save_current_user
# Create your models here.

User = get_user_model()
# Posts
class PostModel(models.Model):
    text = models.CharField(max_length=160,blank = True,null=True)
    image = models.ImageField(upload_to='post_images')
    user = models.ForeignKey(User,on_delete=models.PROTECT,editable=False)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-created_on',)

    def __str__(self):
        return str(self.pk)
    
    def save(self, *args, **kwargs):
        user = get_current_user()   # request obj
        if user and not user.pk:
            user = None
        if not self.pk:
            self.user = user
        super(PostModel, self).save(*args, **kwargs)


# Comments
class CommentModel(models.Model):
    text = models.CharField(max_length=250)
    post = models.ForeignKey(PostModel,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE,editable=False)
    commented_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.text

    def save(self, *args, **kwargs):
        user = get_current_user()   # request obj
        if user and not user.pk:
            user = None
        if not self.pk:
            self.user = user
        super(CommentModel, self).save(*args, **kwargs)

    @property
    def comments_count(self):
        cnt = self.commentmodel_set.count()
        return cnt
# Likes

class LikeModel(models.Model):
    post = models.ForeignKey(PostModel,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE,editable=False)
    # is_like = models.BooleanField(default=True)
    liked_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return str(self.post.id)
    
    def save(self, *args, **kwargs):
        user = get_current_user()   # request obj
        if user and not user.pk:
            user = None
        if not self.pk:
            self.user = user
        super(LikeModel, self).save(*args, **kwargs)

    @property
    def likes_count(self):
        cnt = self.likemodel_set.count()
        return cnt
    
    
# Followers  
class FollowerModel(models.Model):
    user = models.ForeignKey(User,related_name='follow_follower',on_delete=models.CASCADE,editable=False)
    followed = models.ForeignKey(User,related_name='follow_followed',on_delete=models.CASCADE)
    followed_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user} ====>>>> {self.followed}"
    
    def save(self, *args, **kwargs):
        user = get_current_user()   # request obj
        if user and not user.pk:
            user = None
        if not self.pk:
            self.user = user
        super(FollowerModel, self).save(*args, **kwargs)
    
class SavedPost(models.Model):
    post = models.ForeignKey(PostModel,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE,editable=False)
    saved_on = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.post.pk
    
    def save(self, *args, **kwargs):
        user = get_current_user()   # request obj
        if user and not user.pk:
            user = None
        if not self.pk:
            self.user = user
        super(SavedPost, self).save(*args, **kwargs)