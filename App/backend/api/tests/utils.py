from django.test import TestCase, RequestFactory
from faker import Faker

from ..models.user import User
from ..models.artitem import ArtItem, Tag
from ..serializers.serializers import ArtItem, ArtItemSerializer
from django.contrib.auth.models import AnonymousUser, User
from ..views.artitem import post_artitem
from ..views.auth import *
from ..views.user import users_api
from ..views.follow import follow_user

# utils for unit tests
class Utils:
    def __init__(self):
        self.faker = Faker()
        self.factory = RequestFactory()
        self.BASE64 = "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVQYV2NgYAAAAAMAAWgmWQ0AAAAASUVORK5CYII="


    def register(self):
        password =  self.faker.pystr(min_chars = 10)
        email = f"{self.faker.first_name()}.{self.faker.last_name()}@{self.faker.domain_name()}"
        username = self.faker.pystr(min_chars = 10)
        data = {
            "email": email,
            "username": username,
            "password":password,
            "password_confirm": password
            }
        request = self.factory.post('/auth/register/', data, content_type='application/json')
        response = RegisterView().as_view()(request)

        req = self.factory.get('/users/profile/users/', content_type='application/json')
        users = users_api(req)
        
        for user in users.data:
            if(user['username'] == username):
                id = user['id']
                break

        data = response.data
        data['user']['id'] = id

        return data
    
    # user["user"] = user information
    # user["token"] = token
    def upload_an_image(self, user):
        tag = Tag.objects.create(tagname=self.faker.pystr(min_chars = 10), description=self.faker.paragraph(nb_sentences=3))

        title = self.faker.pystr(min_chars = 10)
        description  = self.faker.paragraph(nb_sentences=3)
        category = ArtItem.Category.DRAWING.value
        artitem_image = self.BASE64

        data = {
            "title": title,
            "description": description,
            "category": category,
            "artitem_image": artitem_image,
            "tags": [tag.id]
        }

        header = {"HTTP_AUTHORIZATION": "Token " + user["token"]}
        request = self.factory.post('/artitems/me/upload/', data, **header, content_type='application/json')
        response = post_artitem(request)
        return response.data
    
    def create_follow(self, user1, user2):
        header = {"HTTP_AUTHORIZATION": "Token " + user1["token"]}
        request = self.factory.post('/users/follow/', **header, content_type='application/json')
        follow_user(request, user2['user']['id']) # user1 follows user2


utils = Utils()