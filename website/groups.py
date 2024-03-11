from django.contrib.auth.models import Group, Permission, User
from django.contrib.contenttypes.models import ContentType
from website.models import Post



# creating groups to give permissions
mods, created = Group.objects.get_or_create(name='mods')

# assigning the model we want to give permission for
ct = ContentType.objects.get_for_model(model=Post)

# taking the permissions we can do post which is crud basically
perms = Permission.objects.filter(content_type=ct)

# giving all perms to mods group
mods.permissions.add(*perms)

# filtering user
user = User.objects.filter(username='testing')
test = User.objects.filter(username='auth')

# adding those users to mods group which giving permissions to do crud operations on posts
mods.user_set(user.first())
mods.user_set(test.first())