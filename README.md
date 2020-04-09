# django REST framework 과제 (for ceos 11th)

## 유의사항
* 본 레포지토리는 백엔드 스터디 2-3주차의 과제를 위한 레포입니다.
* 따라서 해당 레포를 fork 및 clone 후 local에서 본인의 깃헙 ID 브랜치로 작업한 후 커밋/푸시하고,
PR 보낼 때도 `본인의 브랜치-> 본인의 브랜치`로 해야 합니다.
 
## 2주차 과제 (기한: 4/12 일요일까지)
[과제 안내](https://www.notion.so/3-Django-ORM-c531472b37e844a6a6d484553037c243)

### 서비스 설명
본인이 선택한 서비스에 대한 설명을 적어주세요!

### 모델 설명
서비스에 대해 본인이 작성한 모델들에 대한 설명과 모델 간의 관계 등을 적어주세요!

### ORM 적용해보기
shell에서 작성한 코드와 그 결과를 보여주세요! 

### 간단한 회고 
1. migratoins
-모델의 변경내역을 DB Schema로 반영시키는 효율적인 방법을 제공   
-makemigrations: 마이그레이션파일 생성   
-migrate: 마이그레이션 적용
2. mysqlclient install 안될때 -> pip 버전 업그레이드   
-이거때문에 너무 고생함 ㅜㅜ
3. mysql 8.0버전은 migrate오류난다 ..   
-ALTER USER 'yeon'@'%' IDENTIFIED WITH mysql_native_password BY '비번';   
-use mysql로 들어가서 바꿔줘야함    
-이거 성공하고 mysql에 내가 만든 테이블 떴을때 너무 행복했다 ..
