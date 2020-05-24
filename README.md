# django REST framework 과제 (for ceos 11th)
## 유의사항
* 본 레포지토리는 백엔드 스터디 2주차 이후의 과제를 위한 레포입니다.
* 따라서 해당 레포를 fork 및 clone 후 local에서 본인의 깃헙 ID 브랜치로 작업한 후 커밋/푸시하고,
PR 보낼 때도 `본인의 브랜치-> 본인의 브랜치`로 해야 합니다.

## 2주차 과제 (기한: 4/12 일요일까지)
<details>
 <summary> 과제 내용 보기 </summary>
 <div markdown="1">
[과제 안내](https://www.notion.so/3-Django-ORM-c531472b37e844a6a6d484553037c243)
</div>
</details>
### 서비스 설명
* 서비스 종류 : 수강신청 시스템
* 서비스의 기능 :
(1) 수강신청 시스템에 로그인 시 학생은 자신의 정보를 확인할 수 있다. (학번, 전공, 학년, 이수 가능 학점) 
(2) 듣고자 하는 과목의 학수번호, 과목 이름, 학점, 개설 교수 등의 정보로 과목을 검색할 수 있다.
(3) 수업 시간이 겹치거나 수강 가능 학점을 넘지 않는 범위 내에서 수강신청을 할 수 있다.

### 모델 설명
1. Major => major_num : 학과 일련번호 / major_name : 학과 이름 
2. Student => std_id : 학번 / std_major : 전공 / grade : 현재 학년 / credits_available : 수강 가능 학점
3. Professor => prof_id : 교수 번호 / prof_name : 이름 / prof_major : 소속 전공
4. Course => course_num : 학수번호 / course_name : 과목 이름 / credit : 학점 / prof_name : 개설 교수 / classroom : 강의실 / timetable : 강의 시간
5. Basket => course_num / std_id
6. Registration => course_num / course_credit / std_id / current_credits : 현재 수강신청 된 학점 / max_credits : 최대 수강 가능 학점 / registration_time : 수강 신청 시간   
* 1:N 관계 => Student-Registration, Course-Registration, Professor-Course
* N:M 관계 => Student-Course

### ORM 적용해보기
```shell script
>>> from api.models import Major, Student, Professor, Course, Basket, Registration
>>> m1 = Major(major_num=71, major_name="Cyber Security")
>>> m1.save()
>>> Major.objects.all()
<QuerySet [<Major: Cyber Security>]>
>>> m = Major.objects.get(major_name='Cyber Security')
>>> s1 = Student(std_id=7147, std_major=m, grade=4, credits_available=21)
>>> s1.save()
>>> Student.objects.all()
<QuerySet [<Student: Student object (7147)>]>
>>> m = Major.objects.get(major_name='Cyber Security')
>>> p1 = Professor(prof_id=1573, prof_name="P1", prof_major=m)
>>> p1.save()
>>> Professor.objects.all()
<QuerySet [<Professor: P1>]>
>>> pname = Professor.objects.get(prof_name='P1')
>>> c1 = Course(course_num=34121, course_name="Network Security", credit=3, prof_name=pname, classroom="Engineering107", timetable="Monday5")
>>> c1.save()
>>> Course.objects.all()
<QuerySet [<Course: Course object (34121)>]>
>>> Course.objects.filter(course_name="Network Security")
<QuerySet [<Course: Course object (34121)>]>
```


### 간단한 회고 
* mysqlclient을 설치하는 과정에서 pip 버전을 1.x -> 2.x로 upgrade
* settings.py의 json.load() 함수에서, 원래 내가 쓰던 Python이 3.5 버전이라 계속 오류 발생. (json.load() 함수는 Python 3.5 이하 버전에서는 오류가 난다고 한다.) 코드 수정을 아무리 해도 안돼서 결국 원래 쓰던 버전을 지우고 아예 3.8 버전으로 새로 설치했다...
* mysql은 1~2학년때 공부한 게 끝이고 3-1 데이터베이스 수업에서 mssql 잠깐 쓴 이후로 DB쪽은 공부를 거의 안했었는데, 오랜만에 하니까 명령어도 다시 외우고 나름 재미있다.
* related_name 옵션은 처음 접해봤는데, 변수명 설정 때문에 오류가 난 덕분에 ORM 쿼리가 실제로 어떻게 작동하는지 좀더 잘 알게 된 것 같다.


---
## 3주차 과제 (기한: 4/19 일요일까지)
[과제 안내](https://www.notion.so/4-DRF1-API-View-464f612bfd9e42e5945325a4ad253cbf)

### 모델 선택 및 데이터 삽입
```python
class Major(models.Model):

    def __str__(self):
        return self.name

    num = models.IntegerField(default=0, primary_key=True)
    name = models.CharField(max_length=200)


class Student(models.Model):
    std_id = models.BigIntegerField(primary_key=True)
    std_major = models.ForeignKey(Major, on_delete=models.CASCADE, related_name="major")
    grade = models.IntegerField(default=1)
    credits_available = models.IntegerField(default=18)


class Professor(models.Model):
    def __str__(self):
        return self.prof_name

    prof_id = models.IntegerField(default=0, primary_key=True)
    prof_name = models.CharField(max_length=200)
    prof_major = models.ForeignKey(Major, on_delete=models.CASCADE)


class Course(models.Model):
    def __int__(self):
        return self.num

    num = models.IntegerField(default=0, primary_key=True)
    name = models.CharField(max_length=200)
    credit = models.IntegerField(default=0)
    prof_name = models.ForeignKey(Professor, on_delete=models.CASCADE)
    classroom = models.CharField(max_length=200)
    weekday = models.CharField(max_length=100, default='')  # 강의 요일
    start_time = models.TimeField(auto_now=False, auto_now_add=False, null=True)  # 강의시간
    finish_time = models.TimeField(auto_now=False, auto_now_add=False, null=True)
```
![data](./data.PNG)

### 모든 list를 가져오는 API
api/course/ GET
```json
[
    {
        "num": 34121,
        "name": "Network Security",
        "credit": 3,
        "prof_name": "Yun",
        "classroom": "Engineering107",
        "weekday": "Friday" ,
        "start_time": "14:00:00",
        "finish_time": "16:45:00"
    },
    {
        "num": 20497,
        "name": "Computer Algorithm",
        "credit": 3,
        "prof_name": "Lee",
        "classroom": "EngineeringB159",
        "weekday": "Tuesday" ,
        "start_time": "11:00:00",
        "finish_time": "13:45:00"
    },
    {
        "num": 10328,
        "name": "UX/UI Design",
        "credit": 3,
        "prof_name": "Nam",
        "classroom": "Campus405",
        "weekday": "Monday" ,
        "start_time": "09:30:00",
        "finish_time": "12:15:00"
    }
]
```

### 특정한 데이터를 가져오는 API
api/course/34121 GET
```json
{
    "num": 34121,
    "name": "Network Security",
    "credit": 3,
    "prof_name": "Yun",
    "classroom": "Engineering107",
    "weekday": "Friday" ,
    "start_time": "14:00:00",
    "finish_time": "16:45:00"
}
```

### 새로운 데이터를 create하도록 요청하는 API
api/course POST
```json
{
    "num": 34123,
    "name": "Digital Forensics",
    "credit": 3,
    "prof_name": "Lee",
    "classroom": "Campus507",
    "weekday": "Wednesday" ,
    "start_time": "14:00:00",
    "finish_time": "16:45:00"
}
```

### (선택) 특정 데이터를 삭제 또는 업데이트하는 API
api/course/34123 PUT
```json
{
    "num": 34123,
    "name": "Digital Forensics",
    "credit": 3,
    "prof_name": "Yun",
    "classroom": "Campus507",
    "weekday": "Wednesday" ,
    "start_time": "14:00:00",
    "finish_time": "16:45:00"
}
```

### 간단한 회고 
view를 작성하는 방법이 많고 (API view, generic view, viewset 등) 각 방법에 따라 urls.py에서의 연결 방법도 달라서 처음에 헷갈렸다. 
그리고 실제로 view를 작성하고 api 테스팅을 하다 보니 모델 자체를 조금 수정해야겠다는 생각이 들었다. 
수정해야 할 사항은 일단 크게 2개가 있는데, 
1) 처음에 모델링을 할 때는 클래스마다 primary key를 설정해 주었는데, 막상 api 테스팅 후 json 코드를 보니 임의로 정한 primary key를 아예 없애고 자동으로 생성되는 id를 primary key로 하는 것이 좋을 것 같다.
2) registration 클래스를 사용하려고 보니, start/finish time 관련 연산이나 current credit 관련 연산을 어디에 구현해야 할지 몰라서 이번 과제에서는 사용하지 못했다. 앞으로 공부하면서 수정해 나가야겠다!

---

## 6주차 과제
### Filter 기능 구현
filter.py
```python
class WeekdayFilter(FilterSet):  # 요일별로 강의를 필터링 할 수 있는 WeekdayFilter
    weekday = filters.CharFilter(method='course_day_filter')

    class Meta:
        model = Course
        fields = ['weekday']

    def course_day_filter(self):
        queryset = Course.objects.all()
        weekday = self.request.query_params.get('weekday', None)

        if weekday is not None:
            queryset = queryset.filter(weekday=weekday)
        return queryset


class CreditFilter(FilterSet):  # 이수학점으로 강의를 필터링 할 수 있는 CreditFilter
    credit = filters.NumberFilter(method='course_credit_filter')

    class Meta:
        model = Course
        fields = ['credit']

    def course_credit_filter(self):
        queryset = Course.objects.all()
        credit = self.request.query_params.get('credit', None)

        if credit is not None:
            queryset = queryset.filter(credit=credit)
        return queryset
```

### Permission 기능 구현 
views.py
```python
SAFE_METHODS = {'GET', 'OPTIONS', 'HEAD'}


class IsSuperUserOrReadOnly(permissions.BasePermission):  #superuser (관리자) 만 수정 및 삭제 권한을 갖고, 다른 사용자들은 get, options, head request에 대해서만 접근 가능
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user.is_superuser


class IsAuthenticated(permissions.BasePermission):  # 로그인 한 사용자만 접근 가능
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated
```

### 간단한 회고
1. Filter 기능을 구현할 때 파라미터를 넘겨 필터링 하는 부분에서 아직 관련 python 문법이 익숙하지 않아 조금 어려웠다. 또 예시 코드를 좀더 찾아보려고 구글링하던 중 method로 구현하지 않고 search filter으로 구현한 경우를 봤는데, 그 방법으로도 리팩토링 해볼 계획이다.
2. Permission을 구현하면서 HTTP method에 대한 내용이 조금 헷갈렸었는데, SAFE_METHOD에서 사용한 OPTIONS와 HEAD method에 대해 좀더 공부해 봐야겠다.
