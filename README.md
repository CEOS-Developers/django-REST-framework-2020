# django REST framework 과제 (for ceos 11th)
 
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