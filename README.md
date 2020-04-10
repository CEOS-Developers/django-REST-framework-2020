
# django REST framework 과제 (for ceos 11th)

### 서비스 설명

제가 선택한 서비스는 **영화관 서비스**입니다. 

정확히는 영화관 회원 **예매** 서비스입니다.

이 서비스를 이용하는 과정은 영화관의 회원이 로그인을 하는 것부터 시작됩니다.

그 후, 회원은 보고싶은 영화를 검색하고 영화관 지점을 선택합니다.

영화관 지점에서 상영스케줄을 보고 알맞은 시간대를 선택합니다.

자신이 앉고 싶은 좌석의 번호를 고릅니다.

마지막으로, 영화 티켓 결제를 하고 예약번호가 적힌 티켓(QR 코드 등)을 받습니다.


### 모델 설명

총 7개의 서비스 관련 모델과 1개의 유저 모델로 이루어져 있습니다.

**서비스 관련 모델**에는 movie, branch, theater, seat, schedule reservation(ticket), pay 이 있습니다.

* movie 모델 :

  - pk(=primary key) : movie_id

  - fk(=foreign key) : X

  - other fields : movie_title, genre

* branch 모델:
  - pk : branch_name
  
  - fk : X
  
  - other fields : location(지점 위치), total_theater(관의 개수)

* theater 모델 : 
  - pk : theater_no

  - fk : branch_name
  
  - other fields : total_seat(좌석 총 개수)

* seat 모델 :
  - pk : seat_no
  
  - fk : theater_no, branch_name
  
  - other fields : is_reservation(예약되어있는지 여부)

* schedule 모델 : 
  - pk : schedule_id
  
  - fk : branch_name, theater_no, movie_id
  
  - other fields : schedule_time, schedule_date

* reservation(ticket) 모델 : 
  - pk : reservation_id(예약번호) 
  
  - fk : schedule_id, branch_name, theater_no, seat_no, movie_id

* pay 모델 : 
  - pk : pay_id
  
  - fk : member_id(일대일 관계), reservation_id
  
  - other fields :  payment_date, price, payment_option

**유저 모델**은 member 모델입니다.
* member 모델 : 
  - pk : member_id 
  
  - pay모델과 일대일 관계입니다.

**참고 사진**

![models](./image/modeling.jpg)



### ORM 적용해보기
1. 데이터베이스에 해당 모델 객체 3개 넣기 

![create](./image/1.JPG)

2. 삽입한 객체들을 쿼리셋으로 조회해보기 (단, 객체들이 객체의 특성을 나타내는 구분가능한 이름으로 보여야 함)

![Queryset](./image/2.JPG)

3. filter 함수 사용해보기

![filter](./image/3.JPG) 



### 간단한 회고 

	모델링을 처음해보아서 처음부터 어떻게 하는지 몰랐습니다ㅠ 
	하지만, 마침 듣는 데이터베이스 수업이 있어서 수업에서 들은 대로 처음에 그림을 그려놓고 시작하게 되었습니다. 
	모델을 다 만들어 놓고 필드를 잘못 선언하여 다 지우고 시작한 것이 한 3번 정도 있었습니다. 
	부분적으로 필드가 수정되는 경우도 있지만, 만일 그 필드가 외래키로 연결되어 있으면 다른 모델을 지우고 시작해야 하더라고요ㅠ 
	그래서 그냥 다 지우고 처음부터 시작했습니다. 
	부분적으로 수정할 수 있는 방법을 알게 되면 더 좋을 거 같습니다. 
	
	그리고 마지막에 객체 생성할 때 오류가 많이 났는데, 그 이유를 알아보려고 보니 보통 제가 필드를 선언할 때, 
	pk,fk,그냥 필드 순으로 선언을 했었는데요... 
	보통은 pk, 필드, fk 순으로 선언을 하는 것을 보고 무엇인가 잘못 되었다는 것을 깨달았습니다. 
	알고보니, python에서는 키워드 인자가 위치 인자 뒤에 와야된다는 사실을 뒤늦게 알게 되었습니다.
	이것 때문에 한 번 더 모델링을 다 지우고 시작했습니다ㅠ
	
	마지막으로, 제가 데이터 모델링을 해보았지만 단순히 저의 생각을 가지고 만든 것이기 때문에, 잘못된 부분이 많을 것 같습니다! 
	하지만, 어떤 것이 잘못된 것인지 감이 잡히지 않습니다... 많은 피드백 부탁드려요!
	
