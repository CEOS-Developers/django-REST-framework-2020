
# django REST framework 과제 (for ceos 11th)

## 모델 선택 및 데이터 삽입
##### Schedule 모델
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

## 모든 list를 가져오는 API
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

## 특정한 데이터를 가져오는 API
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

## 새로운 데이터를 create하도록 요청하는 API
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

## (선택) 특정 데이터를 삭제 또는 업데이트하는 API
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


## 간단한 회고
과제 시 어려웠던 점이나 느낀 점, 좋았던 점 등을 간단히 적어주세요!
	
