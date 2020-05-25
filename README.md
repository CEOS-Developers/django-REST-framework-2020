# django REST framework 과제 (for ceos 11th)


### 서비스 설명
영화관 데이터베이스 관리 서비스이다.    
하나의 영화관에서 상영되는 영화, 시기별 누적관객수, 영화 장르 및 국가별 통계, 영화관 직원 관리 데이터베이스입니다.      

### 모델 설명
DB : megabox 영화관       
1. Movie: 영화관에서 상영하는 영화들   
    title 타이틀   
    director : Foreign Key    
    release_date 개봉일   
    running_time 상영시간 (minutes 단위)   
    country : Foreign Key    
    genre : Foreign Key    

2. Director: 감독   
   name   
3. Country: 국가   
   name    
4. Genre: 장르    
   name : choices=GENRE_CHOICES 장르 입력할 때 중복을 피하기 위해서 choice 튜플 생성   
    GENRE_CHOICES = {   
        ('SF', 'science_fiction'),    
        ('DR', 'drama'),   
        ('RM', 'romance'),     
        ('AC', 'action'),    
        ('HR', 'horror'),       
        ('DS', 'disaster'),    
        ('DC', 'documentary'),    
        ('MS', 'mystery'),    
        ('FT', 'fantasy'),    
        ('CM', 'comedy'),    
        ('SP', 'sport'),    
        ('WR', 'war'),    
        ('EP', 'epic'),   
        ('MU', 'musical'),    
        ('AD', 'adventure'),    
        ('WS', 'western'),     
        ('TH', 'thriller')     
    }   

5. Member: User model 영화관 멤버쉽회원   
  OneToOne 링크 방식 사용     
  nickname 닉네임    
  phone_number 전화번호    
  rank 회원등급    

6. Watcher: 유저가 언제 어떤 영화를 봤는지 알 수 있다.    
   member : Foreign key    
   movie: Foreign key     
   watched_at: 날짜    
    
7. Workers : 영화관 직원들 목록    
   name 이름    
   birth 생년월일    
   join_date 입사일   
   gender 성별   
   position 포지션 :choice 튜플 사용    
   POSITION_CHOICES = {    
        ('CO', 'counter'),    
        ('CL', 'cleaning'),    
        ('FD', 'food'),    
        ('TK', 'ticket')    
    }
   
### ORM 적용해보기

 
 <모델 수정 후>

![](https://images.velog.io/images/kylie/post/1c96c125-ab24-4a2b-8b64-dfa025ba3416/1.PNG)![](https://images.velog.io/images/kylie/post/81900a7c-9e91-47fa-b14b-edfa70ffe93d/3.PNG)


### 간단한 회고 
DB를 논리적으로 설계하는 작업은 상당히 어려운 것 같다. 설계를 잘못했을 때 , 전체 서비스가 붕괴되므로 초기 설계 단계가 정말 중요하다고 느꼈다. Foreign key를 사용할 때 테이블끼리 관계가 있으므로 delete 옵션 설정할 때도 신중해야 한다.  
 
## action decorator 
ViewSet에서 기본적으로 제공하는 뷰 :
-ModelViewSet ( Retrieve, List, Create, Destroy, Update 뷰 제공)
-ReadOnlyModelViewSet ( Retrieve, List 뷰 제공)
이러한 뷰들을 action이라고 한다.
만들어진 액션들은 router에의해 자동으로 url과 매핑된다.

새로운 action은 뷰셋 내에서 새로운 메소드를 작성한 후 @action decorator를 사용해 정의할 수 있다.
만들어진 액션들은 router에의해 자동으로 url과 매핑된다.
```
     # url: /movies/long-movies 상영시간이 120분보다 긴 영화들 조회
    @action(methods=['get'], detail=False, url_path='long-movies', url_name='long-movies')
    def long_movies(self, request):
        # mv = self.get_queryset()
        # long_mv = []
        # for movie in mv:
        #     if movie.running_time > 120:
        #         long_mv.append(movie)
        # 
        # serializer = self.get_serializer(long_mv, many=True)
        mv = self.get_queryset().filter(running_time__gte=120)
        serializer = self.get_serializer(mv, many=True)
        return Response(serializer.data)
    # url : /movies/{pk}/release-today 개봉일을 오늘 날짜로 바꿔줌
    @action(methods=['post'], detail=True, url_path='release-today', url_name='release-today')
    def release_today(self, request, pk):
        today = date.today()
        instance = self.get_object()
        instance.release_date = today
        instance.save()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)
 ```

## SerializerMethodField

**user model**
```
class Member(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nickname = models.CharField(max_length=100, unique=True)
    phone_number = models.CharField(max_length=100, validators=[RegexValidator(r'^[0-9]+$',
                                                                               'Enter a valid phone number.')])  # 제약조건 010-xxxx-xxxx
    RANK_CHOICES = {
        ('V', 'vip'),
        ('G', 'gold'),
        ('S', 'silver')
    }
    rank = models.CharField(max_length=2, choices=RANK_CHOICES)
    def __str__(self):
        return self.nickname
  ```
  **serializers.py**
  ```
  class WorkersSerializer(serializers.ModelSerializer):
    days_since_joined = serializers.SerializerMethodField()
    def get_days_since_joined(self, obj):
        return (datetime.date.today() - obj.join_date).days
    class Meta:
        model = Workers
        fields = '__all__'
  ```

  ## Filtering and Permission

### 1. Filtering
request 통해 filtering 하여 필요한 인자들을 얻을 수 있다.
- self.request.user   
- self.request.GET   
- self.requset.query_params (== self.request.GET)   
- self.kwargs    

- get_queryset    
- SearchFilter    

#### filters.py
- FilterSet 
```
class WorkersFilter(FilterSet):  # workers filtered by gender
    gender = filters.CharFilter(method='filter_by_gender')
    class Meta:
        model = Workers
        fields = ['gender']
    def filter_by_gender(self, queryset, gender, value):
        return queryset.filter(**{
            gender: value,
        })
```

### 2. Permision

#### django에서 기본적으로 제공해주는 권한:
- is_superuser    
- is_staff    
- is_active    

#### DRF에서 기본적으로 제공해주는 Permission:
AllowAny : 인증여부에 상관없이 뷰 호출 허용 (default)   
IsAuthenticated : 인증된 요청에 한해서 뷰호출 허용    
IsAdminUser : Staff 인증 요청에 한해서 뷰호출 허용    
IsAuthenticatedOrReadOnly : 비인증 요청에게는 읽기 권한만 허용    
DjangoModelPermissions : 인증된 요청에 한해서만 뷰 호출 허용, 추가로 유저별 인증 권한체크를 수행    
DjangoModelPermissionsOrAnonReadOnly : DjangoModelPermissions 와 유사하나 비인증 요청에 대해서는 읽기 권한만 허용    
DjangoObjectPermissions     
비인증된 요청 거부    
인증된 레코드 접근에 대한 권한체크를 추가로 수행   

<출처 : https://ssungkang.tistory.com/entry/Django-Authentication-%EA%B3%BC-Permissions>

#### permissions.py

```
SAFE_METHODS = ('GET', 'HEAD', 'OPTIONS')
#유저가 존재하고 스태프일 경우에 허가
class IsAdminUser(permissions.BasePermission):
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_staff)
#super user only
class IsSuperUser(permissions.BasePermission):
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_superuser)
#안전한 request method 이거나 유저가 존재하고 로그인 되어 있을 경우에 허가
class IsAuthenticatedOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        return bool(
            request.method in SAFE_METHODS or
            request.user and
            request.user.is_authenticated
        )
```
