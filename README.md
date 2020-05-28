# django REST framework 과제 (for ceos 11th)

## 유의사항
* 본 레포지토리는 백엔드 스터디 2-3주차의 과제를 위한 레포입니다.
* 따라서 해당 레포를 fork 및 clone 후 local에서 본인의 깃헙 ID 브랜치로 작업한 후 커밋/푸시하고,
PR 보낼 때도 `본인의 브랜치-> 본인의 브랜치`로 해야 합니다.
 
## 2주차 과제 + 리뷰 반영
[과제 안내](https://www.notion.so/3-Django-ORM-c531472b37e844a6a6d484553037c243)

### 서비스 설명

영화관 선택은 배제하고, 영화 예매, 리뷰 서비스를 모델링 해보았습니다.

- 회원가입 -> 영화를 예매하기 위해서 영화를 선택 -> 다른 사람들의 리뷰를 확인  
  -> 영화 선택후 관란 시간표에서 시간을 선택 -> 영화 관람한 회원만 (권한을 주어) 리뷰 작성 가능
- 보고싶은 영화를 WishList 를 만들어 관리

### 모델 설명 

가장 기본이 되는 모델로는 User, Movie, Booking 3가지로 잡았고,
하위 모델로는 TimeTable, Review, WishList 가 있습니다.

1. User : AbstractUser 사용하여 필드 변경
   - email: EmailField
   - username: CharField
   - gender: SmallIntegerField(choices=GENDER_CHOICES)
   - phone: PhoneNumberField - `pip install django-phonenumber-field[phonenumbers]`
   - wish_list: (Movie : user) (M : N) - 하나의 유저가 여러 영화에 대해, 하나의 영화를 여러 유저가 사용

   -> 로그인을 이메일로

2. Movie
   - title: CharField
   - Movie - Country (N : 1)
   - rel_day: DateTimeField
   - is_on_now: BooleanField
   - poster: ImageField

3. Country
    - name: CharField

3. Genre
   - Genre - Movie (N : 1)
   - name: CharField(choices=GENRE_CHOICES) - 표준화된 장르 19개 + indeterminate 1개

4. Director
    - Director - Movie (M : N) - 영화에 감독이 여러명일 수도 있고, 감독이 여러 영화를 만들 수 도 있음
    - name: CharField

5. TimeTable
    - TimeTable - Movie (N : 1)
    - start_time: DateTimeField
    - end_time: DateTimeField

6. Review
    - Review - User (N : 1)
    - Review - movie (N : 1)
    - rate: SmallIntegerField - 별점 1~5개중 choice
    - comment: CharField : 너무 길지않은 코멘트

7. Booking
    - Booking - user (N : 1)
    - Booking - movie (N : 1)
    - movie_time: (Booking - TimeTable) (N : 1) - 예약한 영화 시간
    - booking_time: DateTimeField - 예약을 행한 그 시간
    - num_people: IntegerField


### ORM 적용해보기
1. Movie 객체 생성
![cap1](./img/cap1.JPG)

2. Movie 객체 save
![cap1](./img/cap2.JPG)
여기서 DateTimeField 에 대한 RuntimeWarning 이 발생하는데 어떻게 해결해야하는지 모르겠습니다.  
settings.py 에서 **USE_TZ = True : 장고 내부적으로 시간대를 인식, USE_TZ = False: TIME_ZONE 을 참고하여 local time 사용** 이라고 찾아서 False 로 해봤지만 여전히 warning 은 뜨네요.
그래도 저장은 잘 됩니다.  
[해결] USE_TZ = False 로 변경 하니 TIME_ZONE 을 참고하여 local time 을 사용해서 해결됨 (이전에 적용이 안되었었듯) 
![cap1](./img/cap3.JPG)

3. TimeTable 객체 생성 및 save
TimeTable 의 객체도 동일하게 생성해주고, Movie 를 ForeignKey 로 받아오므로 Movie 객체를 넣어줍니다.
![cap1](./img/cap4.JPG)
  
4. Timetable 객체를 ForeignKey 로 연결된 Movie 의 rel_day 필드 순으로 정렬해 보았습니다.
![cap1](./img/cap6.JPG)

### 간단한 회고
MySQL 을 설치하는 것에만 하루를 꼬박 썼습니다. HDD 에 설치하고 싶은 마음에 건방지게(?) installer 를 쓰지 않고 ZIP archiving 으로 
깔려고 시도했습니다. 분명 설치는 되었다고 뜨는데 서비스 시작이 도저히 안되었고 수시간에 걸쳐 구글링으로 나온 방법들을 해보았으나 결국 실패하였네요..
마음을 바꿔 installer 로 설치를 하니 몇분만에 설치가 끝났습니다. 새로운 개발환경을 사용할 때는 항상 사전 세팅과 설치하는데 긴 시간을 쓰며 시작을 하는 것 같습니다.

모델링을 시작하면서 욕심이 생겨, 많이 써보지 못했던 필드나 방법들을 사용해보고 싶었습니다.  
처음 User 모델링을 하면서도 처음부터 다 짜보고 싶은 마음에 AbstractBaseUser 을 사용하여 처음부터 다 구현을 해보고자 했습니다.
공부를 계속 하다보니 유저 모델링을 처음부터 다 구현을 하는 경우는 유저의 형태가 여러가지가 있어서 새로 구현할 수 밖에 없을 때
하는것이 좋다는 것을 알게되어 수정하는 것으로 방향을 바꾸게 되었습니다.
  
모델링이라는 것이 필요한 모델들, 어떤 필드들을 사용할 것인지, 모델간의 관계 등을 먼저 정리를 해두고 시작해야 한다는 것을 깨달았습니다.
모델링을 하면서 생각해봐야할 부분들, 쓸 수 있는 것들을 최대한 많이 써보고 찾아보면서 이해하려고 노력했던 것이 큰 도움이 될 것 같습니다.
이전에 데이터베이스에 대해는 생각도 안해봤고, 전혀 몰랐다면, ORM 을 공부하고 백엔드에서의 모델링이 어떻게 데이터베이스에 저장되고 사용할 수있는지를
조금이나마 느끼게 되서 정말 도움이 많이 되었던 시간이었습니다.
  
아직 많이 부족해서 찾아보고, 공부하는데 남들보다 많은 시간을 쏟고 있는것 같지만, 그만큼 배우는게 많은 것 같아 잠도 줄이고 공부하게 되는것 같습니다.  
과제를 통해 공부를 해야할 단계와 좋은 방향을 제시해주셔서 감사합니다!!

ps. bash 에서는 가상환경이 계속 켜지지 않아서, 그냥 PowerShell 터미널에서 python shell 을 진행했습니다. bash에서 가상환경이 켜지지않는 경우를 검색해서 계속 해결중인데 아직 원인을 못찾았습니다..ㅠㅠ

---
---

## 3주차 과제 (기한: 4/19 일요일까지)
[과제 안내](https://www.notion.so/4-DRF1-API-View-464f612bfd9e42e5945325a4ad253cbf)

### 모델 선택 및 데이터 삽입
- Movie 모델
```python
class Movie(models.Model):
    title = models.CharField(max_length=64)
    country = models.ForeignKey('Country', on_delete=models.CASCADE, related_name='movies')
    rel_day = models.DateField(verbose_name='release_day')
    is_on_now = models.BooleanField(default=False)
    poster = models.ImageField(blank=True, null=True, upload_to='')

    def __str__(self):
        return self.title

class Country(models.Model):        # Movie 제작 국가는 하나, 한 국가에는 여러 영화가 있음
    name = models.CharField(max_length=32)

    def __str__(self):
        return self.name
```

![model](./img/api1.JPG)

### 모든 list를 가져오는 API
- URL: /api/movie/
- Method: GET

```json
[
    {
        "id": 1,
        "title": "어벤져스: 엔드게임",
        "rel_day": "2019-04-24",
        "is_on_now": false,
        "poster": null,
        "country": 2
    },
    {
        "id": 2,
        "title": "겨울왕국 2",
        "rel_day": "2019-11-21",
        "is_on_now": false,
        "poster": null,
        "country": 2
    },
    {
        "id": 3,
        "title": "극한직업",
        "rel_day": "2019-01-23",
        "is_on_now": false,
        "poster": null,
        "country": 1
    },
    {
        "id": 4,
        "title": "신과함께 -  죄와벌",
        "rel_day": "2017-12-20",
        "is_on_now": false,
        "poster": null,
        "country": 1
    },
    {
        "id": 5,
        "title": "기생충",
        "rel_day": "2019-05-30",
        "is_on_now": false,
        "poster": null,
        "country": 1
    },
    {
        "id": 6,
        "title": "1917",
        "rel_day": "2020-02-19",
        "is_on_now": true,
        "poster": null,
        "country": 2
    }
]
```

### 특정한 데이터를 가져오는 API
- URL: /api/movie/1/
- Method: GET

```json
{
    "id": 1,
    "title": "어벤져스: 엔드게임",
    "rel_day": "2019-04-24",
    "is_on_now": false,
    "poster": null,
    "country": 2
}
```

### 새로운 데이터를 create하도록 요청하는 API
- URL: /api/movie/
- Method: POST

```json
{
    "title": "명량",
    "rel_day": "2014-07-30",
    "is_on_now": false,
    "poster": null,
    "country": 1
}
```


### 간단한 회고 
'api를 만드는 방법은 뭐가 있을까?'하고 시작하는데, api, serializer, DRF, RESTful 등의 용어들이 머릿속에 뒤섞여 처음에 혼란이 왔었다. 
하나씩 풀어보는 느낌으로 블로그를 수십개를 뒤져가며 공부를 하고나니, 이제는 머릿속에 어느정도 정리가 되어있는 느낌이다. 
개념만 잘 정리하고 나면 view의 구현 자체는 크게 어렵지 않은 듯 하다.  

이전에 처음 장고를 접하고 공부할 때 templates의 html과 form 을 통해서 request를 받고 처리하는 것을 알았을 때 느꼈던 것이
'웹을 만드려면 결국 프론트엔드부터 백엔드까지 풀스택으로 개발할줄 알아야 제대로 짤 수 있겠구나'라고 생각 했었던 것이 떠올랐다.
물론 전반적으로 이해해야한다는 것에는 아직도 그렇게 생각하지만, 분업의 관점에서 볼 때, 백엔드와 프론트엔드의 연결점의 변동이 심하다고 느껴졌었다. 
이번에 DRF를 좀더 공부하면서 DRF를 사용함으로서 그 경계선도 좀더 명확해져 분업시 더 편하겠구나 느꼈다.
게다가 요즘은 웹 뿐만이 아니라 대부분의 데이터를 Json으로 주고 받으니, 다른 기술 혹은 서비스의 적용도 더 쉬울 것으로 예상된다.    

사실 DRF를 공부하고 사용하는 것 보다 admin site 를 customizing 하는 것이 좀 더 오래 걸렸다. 
admin 을 수정하다보니 model의 관계에서 1:N 의 관계중 1의 화면에서 N을 보고싶은 경우가 대부분이라는 것을 느꼈다.
예를 들어 Genre를 Movie의 설명에서 볼 수 있는 것이 상식적으로 맞는 것처럼 말이다.
Genre 모델을 만들었으니 Genre 페이지를 따로 두는 것은 거의 쓸데가 없다... 
근데 이걸 처리하려면 inlines을 알아야 했다. 이를 공부하다보니 ModelAdmin에 대해 조금 더 이해하게 되었다.

아직도 해결하지 못한 부분이 바로 M:N의 Many-To-Many 관계의 admin 작성인데, User 모델의 wish_lists 도 Movie와 Many-To-Many 관계인데 admin사이트에 잘 적용 되는 반면,
Director 의 경우는 Movie와 M:N인데 아직도 admin 사이트에 적용이 잘 안되고 있다.
검색해보니 through를 쓰라고 나와 있지만, 그 경우는 M:N 사이에 애초에 through가 될 model을 끼고 있는 경우에 해당이 되는 것 같다. 

추가) migrations에 대한 것은 이론적으로 뭔가 db에 대한 tracking의 느낌, 혹은 version 처럼 사용하면 된다는 것은
알겠으나 이미 데이터가 들어있는 경우 처리하는 방법은 아직도 어렵네요... Genre model을 m:n으로 바꾸거나 Movie 안의 field로 choices로 두려고 했는데 migrations가 계속 오류가 나서
해결이 잘 안되었습니다...ㅠㅠ db drop 하고 migrations 를 다시 만들면 되겠지만 규주님이 말씀해주신대로 migration 수정을 하는 쪽으로 연습을 해보고 싶었는데.. 아직 감을 못잡겠네요.


### 이해 내용 정리
우선 DRF는 Serializer를 통해 **html**이 아닌, **JSON** 파일 형태로 데이터를 교환한다. 이제와서 느낀거지만, 
Serializer라는 이름에서부터 이미 문자열로 뽑아내겠다는 것을 알 수 있다.
Serializer를 구현하는데는 (저수준 -> 고수준) 순서대로 4가지정도로 나눌 수 있다.

1. @api_view 데코레이터로 감싸기
    - FBV
2. APIView 클래스 상속
    - CBV
    - 필요한 method 선언, 구현하기
    - request method 마다 직접 serializer 처리
    - serializer 에 대해서 중복이 발생
3. generics 클래스 상속
    - CBV
    - APIView를 상속받아 만들어진 클래스
    - rest_framework 에서 이미 구현해 둠
    - Serializer에 request 데이터를 넣고 리턴
    - ex) generics.ListCreateAPIView : 목록/생성
    - ex) generics.RetrieveUpdateDestroyAPIView : 조회/수정/삭제
4. viewsets
    - 헬퍼클래스
    - queryset, serializer_class 가 공통이므로 한번에 처리
    - 단 몇 줄로 CRUD (Create, Read, Update, Delete)
    - viewsets.ReadOnlyModelViewSet : 목록 조회, 특정 레코드 조회
    - viewsets.ModelViewSet : 목록 조회, 특정 레코드 생성/조회/수정/삭제
    - Router 를 통해서 하나의 url 로 처리가 가능



### offline study
- property method 사용해서
- query param을 이용 하여 ex) api/item/?~~


## 6주차 과제 (기한: 5/24 일요일까지)

[과제안내](https://www.notion.so/eveningminusdot/6-DRF3-filter-and-permission-73251e36d84d42af878574c13a0949b1)

### filter 기능 구현하기

```python
class UserFilter(FilterSet):
    class Meta:
        model = User
        fields = ['gender']

    # users /?gender = 0,1,2
    def gender_filter(self, queryset, name, value):
        gender_queryset = queryset.filter(gender=value)
        return gender_queryset
```
![filter](./img/filter_gender0.JPG)
![filter](./img/filter_gender1.JPG)
```python
class ReviewFilter(FilterSet):
    # reviews/?comment=value
    comment = filters.CharFilter(method='comments_filter')

    class Meta:
        model = Review
        fields = ['comment']

    # 'value'가 들어간 comment 필터링
    def comments_filter(self, queryset, comment, value):
        comment = self.request.query_params.get(comment, None)
        if comment is not None:
            queryset = queryset.filter(comment__icontains=value)
        return queryset
```
![filter](./img/filter_comment.JPG)
```python
class MovieFilter(FilterSet):
    # movies/?title=value
    title = filters.CharFilter(method='movie_title_filter')

    class Meta:
        model = Movie
        fields = ['title']

    def movie_title_filter(self, queryset, title, value):
        title = self.request.query_params.get(title, None)
        if title is not None:
            queryset = queryset.filter(title__icontains=value)
        return queryset
```
![filter](./img/filter_movie1.JPG)
### permission 기능 구현하기
이전 과제할 때 permission 을 적용을 해뒀습니다.  

#### 이해사항
- FilterView()
Generic View 를 사용할 경우 사용/  

- Generating filters with Meta.fields
FilterSet의 메타 클래스는 중요한 코드 중복 없이 쉽게 여러 개 필터를 지정할 수 있는 fields 속성을 제공한다  

- Customize filtering with Filter.method
사용자는 필터링을 수행하는 method를 지정하여 필터의 동작을 제어할 수 있다

#### 6주차 회고
filter 을 사용할 때 datetimefield를 다루는 부분이 많이 미숙하다는 것을 느꼈습니다. 원래 vip_filter를 구현하여 
가입 날짜와 현재 날짜를 뺀 날수로 filter를 구성해 보자 하였는데, 마음처럼 쉽게 안되었습니다. 다시 시도해 보겠지만, 많이 부족함을 느끼고 있습니다.
후에 든생각은 vip의 경우 filter보다는 @action으로 구현하는 것이 더 알맞겠다는 생각이 들었는데, 다른분들은 어떻게 생각하실지 모르겠습니다.

개인적으로 너무 많이 늦어서 정말 정말 죄송합니다... 스스로 부족함을 정말 많이 느끼고 정신없었던 2주였습니다.  
늦은 전공 시험이 있었고, 폭탄같은 학교 과제들이 쏟아지는 와중에 욕심이 많아, 현재 진행하는 진행하는 아이템의 제안자로서 기획까지 어느정도 해야하다보니 잠시 개발자로서의 본업에 소홀했던 것 같습니다.
본업에 집중하지 못한 점 깊이 반성하겠습니다...ㅠㅠ

##### ps.그냥 헷갈려서 기억해두기 위한 것.
```python
def post(self, request, *args, **kwargs):
           # POST have request.data 
           return self.process_request(request, request.data)

def get(self, request, format=None):
   # GET have request.query_params
   return self.process_request(request, request.query_params)
```

