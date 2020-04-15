# django REST framework 과제 (for ceos 11th)

 
## 2주차 과제 (기한: 4/12 일요일까지)
[과제 안내](https://www.notion.so/3-Django-ORM-c531472b37e844a6a6d484553037c243)

### 서비스 설명
영화관 데이터베이스 관리 서비스이다.    
하나의 영화관에서 상영되는 영화, 시기별 누적관객수, 영화 장르 및 국가별 통계, 영화관 직원 관리 데이터베이스입니다.      

### 모델 설명
DB : megabox 영화관    
1. Movie : 영화관에서 상영하는 영화들      
   title이 Movie의 primary key이다. 
2. ScreeningDates: 시기별 누적 관객수    
   foreign key로 Movie의 title를 cascade 옵션으로받는다   
   start_date: 통계 시작 날짜
   finished_date: 통계 끝 날짜 , set null = True 
3. GenreStat:영화관에서 상영하는 영화 장르별 통계   
   foreign key로 Movie의 genre를 cascade 옵션으로 받는다   
4. CountryStat:영화관에서 상영하는 영화 국가별 통계   
   foreign key로 Movie의 country를 cascade 옵션으로 받는다    
5. Workers: 영화관 직원들 목록     

### ORM 적용해보기

- 객체 생성
![](https://images.velog.io/images/kylie/post/ab5b1a0f-4908-47ab-814a-9f94fa1380ed/res1.PNG)![](https://images.velog.io/images/kylie/post/231f575b-9dd3-4fcf-a3ee-725567e2fd89/res2.PNG)![](https://images.velog.io/images/kylie/post/bf3def25-0b03-451d-85db-455945045ec4/res3.PNG)![](https://images.velog.io/images/kylie/post/4c8513c8-a342-42c2-ab0d-7892affe9263/res4.PNG)

- 삽입한 객체들을 쿼리셋으로 조회, filter 함수 사용하기 
 ![](https://images.velog.io/images/kylie/post/f6c3105d-9a25-4b30-86af-69114afa2f2c/res5.PNG)![](https://images.velog.io/images/kylie/post/84b84ade-6bd3-4796-a434-6d8fe5d54617/3%EB%B2%88%EB%8B%B52.PNG)



### 간단한 회고 
DB를 논리적으로 설계하는 작업은 상당히 어려운 것 같다. 설계를 잘못했을 때 , 전체 서비스가 붕괴되므로 초기 설계 단계가 정말 중요하다고 느꼈다. Foreign key를 사용할 때 테이블끼리 관계가 있으므로 delete 옵션 설정할 때도 신중해야 한다.  
 

