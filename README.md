# django REST framework 과제 (for ceos 11th)



### 서비스 설명
1.학생은 자신이 듣고 싶은 과목을 검색할 수 있다.   
2.검색한 과목들을 장바구니에 담는다.   
3.요일과 시간이 겹치지 않고 본인의 학점을 초과하지 않는 한에서 수강신청을 한다.   
4.듣고 싶지 않을 경우 drop을 할 수 있다.   
5.최종적인 자신의 시간표를 확인할 수 있다.

### 모델 설명
1. **Course**   
-> 과목에 대한 정보가 담긴 DB이다   
-course_name: 과목명
-professor: 교수명   
-course_num: 학수번호   
-capacity: 총정원   
-total: 현재정원   
-credit: 학점   
-first: 첫번째 수업 시간   
-second: 두번째 수업 시간

2. **Basket**   
-> 각 학생의 장바구니 목록을 보여준다   
-student_id: 학번
-fk: Course 사용

3. **Timetable**   
-> 각 학생의 시간표를 보여준다.
-student_id: 학번   
-now: 현재 총 학점   
-total: 학생이 들을 수 있는 전체학점   
-fk: Course

4. **Student**   
->user model   
-name: 학생이름   
-student_id: 학번   
-major: 전공

Course - Basket -> 1:N   
Course - Timetable -> 1:N
### ORM 적용해보기
1. 데이터베이스에 모델 객체 3개 넣기
 ![1-1] (./image/1-1.png)   
 ![1-2] (./image/1-2.png)   
 ![1-3] (./image/1-3.png)     
2. 쿼리셋으로 조회해보기   
 ![2] (./image/2.png)    
3. filter 함수 사용해보기    
![3] (./image/3.JPG)


### 간단한 회고 
1. migrations
-모델의 변경내역을 DB Schema로 반영시키는 효율적인 방법을 제공   
-makemigrations: 마이그레이션파일 생성   
-migrate: 마이그레이션 적용
2. mysqlclient install 안될때 -> pip 버전 업그레이드   
-이거때문에 너무 고생함 ㅜㅜ
3. mysql 8.0버전은 migrate오류난다(하위 버전 쓰길 추천)   
-`ALTER USER 'yeon'@'%' IDENTIFIED WITH mysql_native_password BY '비번';`   
-use mysql로 들어가서 바꿔줘야함    
-이거 성공하고 mysql에 내가 만든 테이블 떴을때 너무 행복했다 ..   
-나는 왜.. 모든 ... 커맨드...가 ..에러가 ..날까 .
