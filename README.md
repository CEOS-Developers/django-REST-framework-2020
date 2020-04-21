
# django REST framework 과제 (for ceos 11th)

### 모델 선택 및 데이터 삽입
##### Schedule 모델
![admin](./image/admin.JPG)
~~~
class Branch(models.Model):
    name = models.CharField(max_length=20, unique=True)
    location = models.CharField(max_length=50)

    def __str__(self):
        return str(self.id)


class Screen(models.Model):
    name = models.CharField(max_length=10, primary_key=True)
    branch = models.ForeignKey('Branch', on_delete=models.CASCADE, related_name='screens')

    def __str__(self):
        return str(self.name)


class Movie(models.Model):
    title = models.CharField(max_length=50)
    genre = models.CharField(max_length=20)

    def __str__(self):
        return str(self.id)


class Schedule(models.Model):
    time = models.DateTimeField()
    movie = models.ForeignKey('Movie', on_delete=models.CASCADE, related_name='schedule')
    branch = models.ForeignKey('Branch', on_delete=models.CASCADE, related_name='schedule')
    screen = models.ForeignKey('Screen', on_delete=models.CASCADE, related_name='schedule')

    def __str__(self):
        return str(self.id)
~~~

### 모든 list를 가져오는 API
##### ap1/schedule/ GET
~~~
HTTP 200 OK
Allow: GET, POST, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

[
    {
        "id": 1,
        "time": "2020-04-17T14:15:00+09:00",
        "movie": 1,
        "branch": 1,
        "screen": "MX"
    },
    {
        "id": 2,
        "time": "2020-04-18T11:30:00+09:00",
        "movie": 2,
        "branch": 2,
        "screen": "COMFORT1"
    },
    {
        "id": 3,
        "time": "2020-04-19T22:45:00+09:00",
        "movie": 3,
        "branch": 1,
        "screen": "8"
    }
]
~~~

### 특정한 데이터를 가져오는 API
##### api/schedule/3 GET
~~~
HTTP 200 OK
Allow: GET, PUT, PATCH, DELETE, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

{
    "id": 3,
    "time": "2020-04-19T22:45:00+09:00",
    "movie": 3,
    "branch": 1,
    "screen": "8"
}
~~~

### 새로운 데이터를 create하도록 요청하는 API
##### api/schedule POST
~~~
HTTP 201 Created
Allow: GET, POST, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

{
    "id": 4,
    "time": "2012-05-14T08:45:00+09:00",
    "movie": 1,
    "branch": 1,
    "screen": "8"
}
~~~

### (선택) 특정 데이터를 삭제 또는 업데이트하는 API
##### api/schedule/4 PUT
~~~
HTTP 200 OK
Allow: GET, PUT, PATCH, DELETE, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

{
    "id": 4,
    "time": "1999-03-18T08:00:00+09:00",
    "movie": 1,
    "branch": 1,
    "screen": "8"
}
~~~


### 간단한 회고
    튜토리얼을 따라 하다 보니까 API를 만들 수 있는 방법이 너무 많아서 처음에는 뭘로 코드를 짜야할 지 몰랐지만, 
    결국에는 제일 짧고 쉬운 걸로 코드를 짰어요ㅎㅎ 그리고 그냥 admin에 register만 하면, pk밖에 안 보여서 전체 column을
    보이게 하기 위해서 list_display를 사용했습니다! generics.~View를 사용하니 너무 편리하게 코드를 짤 수 있어서 좋았어요! 
    하지만, 과제를 하다보니까 약간 모델링이 잘못되었다는 생각도 들더라고요.. 
    예를 들면, 제가 생각하기에는 Branch와 Screen이 붙어다니길을 원했는데 Schedule을 보고 제가 다시 선택해야한다는 것을 알게되었어요ㅠ.ㅠ
    그리고, url연결할 때도 검색해보니 사람들이 r'^~'이런 표현을 많이 써서 무턱대고 따라 썼다가 아무것도 작동을 안하더라고요
    (r'^~'이 이전버전에 쓰이고 지금은 path로 대체된다는데 맞나요?)

    처음으로 django의 drf 기능을 사용해서 과제해봤는데 너무 편리한 것 같아요!
    틀린 부분 있으면 언제든지 피드백 해주세요 ᕕ( ᐛ )ᕗ
