
from django.contrib.sessions.models import Session  

from django.contrib.auth.models import User
from django.contrib.auth import get_user_model 
User = get_user_model() 
user = User.objects.get(username='admin')       

[s.delete() for s in Session.objects.all() if s.get_decoded().get('_auth_user_id') == user.id]

