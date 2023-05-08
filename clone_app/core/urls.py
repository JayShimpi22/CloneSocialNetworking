from django.urls import include, path
from core import views
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('follow/done/',login_required(views.FollowDoneView.as_view()),name= 'follow_done_view'),
    path('unfollow/done/',login_required(views.UnfollowDoneView.as_view()),name= 'unfollow_done_view'),
    path('post/create/',login_required(views.PostCreateView.as_view()),name= 'post_create_view'),
    path('post/delete/<int:id>/',login_required(views.PostDeleteView.as_view()),name= 'post_delete_view'),
    path('post/detail/<int:id>/',login_required(views.PostDetailView.as_view()),name= 'post_detail_view'),
    path('post/save/<int:id>/',login_required(views.PostSaveView.as_view()),name= 'post_save_view'),
    path('post/unsave/<int:id>/', login_required(views.PostUnsaveView.as_view()), name='post_unsave_view'),

    path('post/like/<int:id>/',login_required(views.PostLikeView.as_view()),name= 'post_like_view'),
    path('post/unlike/<int:id>/',login_required(views.PostUnlikeView.as_view()),name= 'post_unlike_view'),
    path('post/comment/<int:id>/',login_required(views.PostCommentView.as_view()),name= 'post_comment_view'),
    path('post/liked/',login_required(views.LikedPostView.as_view()),name= 'liked_posts_view'),
    path('post/explore/',login_required(views.ExplorePostsView.as_view()),name= 'explore_posts_view'),
    path('post/saved/', login_required(views.SavedPostsView.as_view()), name='saved_posts_view'),

]