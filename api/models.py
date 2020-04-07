from django.db import models

# 모델링 과제를 이곳에서 해주시면 됩니다! (주석은 나중에 지우셔도 돼요!)


class Member(models.Model):
    email = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    name = models.CharField(max_length=20)
    tel = models.CharField(max_length=20)

    def __str__(self):
        return self.id
