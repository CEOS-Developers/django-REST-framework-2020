# django REST framework 과제 (for ceos 11th)

 
## 2주차 과제 (기한: 4/12 일요일까지)
[과제 안내](https://www.notion.so/3-Django-ORM-c531472b37e844a6a6d484553037c243)

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
 

