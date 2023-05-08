from crum import get_current_user

def auto_save_current_user(obj):
    user = get_current_user()   # request obj
    if user and not user.pk:
        user = None
    if not obj.pk:
        obj.user = user