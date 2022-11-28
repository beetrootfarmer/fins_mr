# Final pjt   |   🐋 FINS 김유민 김혜지

#### [📓 작업 노션 링크](https://hyejisfarm.notion.site/Final-Project-6ab346c128714892bb550b7593b7c2b0)

---
### 🧑‍💻 팀원정보 및 업무분담내역
<center class="half">   
    <img width="500" alt="main" src="https://user-images.githubusercontent.com/87971876/204215118-099a714a-7888-419b-bd9f-2a711e7a1ada.png">
    <img width="500" alt="team" src="https://user-images.githubusercontent.com/87971876/204215122-4c70e9e9-12bc-4ad3-a2b6-600ae41aaee7.png">
</center>

---

### 2. 목표서비스구현 및 실제구현정도
- 선호하는 영화를 기반으로 SNS 스타일의 마이페이지를 가지는 영화 SNS 서비스(Film + SNS)
- 영화 리스트와 좋아하는 영화를 마이페이지 표출
- 마이페이지 영화 사진 커스텀
- 선호 영화 기반 영화 추천 서비스
- 영화 검색과 장르, 키워드별 영화 목록 조회

- (미구현) 다른 사람의 마이페이지에 방문 시 영화 취향 확인 및 팔로우 
---
### 3. 데이터베이스 모델링 (ERD)
<center class="half">
    <img width="500" alt="erd" src="https://user-images.githubusercontent.com/87971876/204215098-49823c59-3ee6-4cac-bc48-d6eb366aa186.png">
    <img width="500" alt="database" src="https://user-images.githubusercontent.com/87971876/204215095-7bd1e8b7-e9af-4621-a943-d7c747827e8c.png">
</center>

#### 컴포넌트 구성

![compo](https://user-images.githubusercontent.com/87971876/204217249-755977ae-c0e5-4e17-8a43-c8019250f187.png)

#### 프로토타입
<center class="third">
    <img width="333" alt="figma1" src="https://user-images.githubusercontent.com/87971876/204215101-7c9b52f2-3fee-4581-ab7c-be0dec4e42ab.png">
    <img width="333" alt="figma2" src="https://user-images.githubusercontent.com/87971876/204215105-a2cdb49d-6c4a-4178-b20f-909a78102d9f.png">
    <img width="333" alt="figma3" src="https://user-images.githubusercontent.com/87971876/204215108-d2befb6f-07b7-4a15-acea-b481a867d163.png">
</center>

---
### 4. 영화 추천 알고리즘에 대한 기술적 설명
<center class="half">
    <img width="500" alt="algorithmn" src="https://user-images.githubusercontent.com/87971876/204215092-2943b00d-70f3-4e35-9fc3-28e6b6882f07.png">
    <img width="500" alt="recomment movies" src="https://user-images.githubusercontent.com/87971876/204210124-831f3c38-c1a0-4bcf-a2d3-45bc5093e457.png">
</center>

---
### 5. 서비스 대표 기능에 대한 설명
#### - 메인페이지 영화목록
- 영화의 스틸컷 사진이 랜덤하게 표출된 영화목록과 infinite loading을 사용해서 대용량 데이터 로딩의 딜레이를 막음
    ![main gif](https://user-images.githubusercontent.com/87971876/204210099-161a8225-f836-483a-8af7-949c0ed1fcc2.gif)
#### - 영화 좋아요
- 영화 상세 페이지에서 영화 좋아요
- 혹은 FINDER 기능을 통해 좋아요를 누르지 않은 영화 중 랜덤한 영화 목록에서 영화 포스터 카드를 움직여 좋아요 기능 구현
    <center class="half">
    <img width="500" alt="finder" src="https://user-images.githubusercontent.com/87971876/204220431-33b7db68-2c91-4fb5-a33c-dd4c46e05a00.png">
    <img width="500" alt="finder" src="https://user-images.githubusercontent.com/87971876/204210090-203f92ef-fd34-483e-b2f2-75f0003bf213.gif">
</center>

#### - 마이페이지
- 좋아요한 영화는 마이페이지 모델에 자동으로 추가되어 마이페이지에 글이 생성된다
- 다른 사람 혹은 본인이 마이페이지 게시글에 좋아요 가능
- 피드 게시글수정 시 원하는 영화의 스틸컷으로 이미지 수정 혹은 한줄 평 추가가능
<center class="half">
    <img width="
    500" alt="my page modal edit" src="https://user-images.githubusercontent.com/87971876/204210117-28f66946-7a60-4eb1-a7ce-0092e8dd19f0.png"/>
    <img width="500" alt="my page modal" src="https://user-images.githubusercontent.com/87971876/204210121-292e184a-26e5-4d43-9ea4-40e5a12282c8.png"/>
</center>
- 리스트형 카드형 두가지로 확인가능
![my page gif](https://user-images.githubusercontent.com/87971876/204210110-edd7b541-0be8-4dba-a7a5-14120fb8c6db.gif)

#### - 영화 검색
- keyup 메소드를 활용해서 입력값이 바뀔때마다 검색결과를 새롭게 받아와서 표출
- 장르별 영화목록을 토글형태로 표현해서 확인가능
![discovery gif](https://user-images.githubusercontent.com/87971876/204210055-44d39da7-3302-44e9-9c8d-c27eb4816409.gif)

#### - 키워드 영화
- 영화 상세페이지에서 영화별 키워드 확인
- 키워드 클릭 시 해당 키워드에 연관된 영화목록 표출
<center class="half">
    <img width="500" alt="keyword movie" src="https://user-images.githubusercontent.com/87971876/204210097-06af76bc-d0ee-4223-994f-fadb53f42483.png">
    <img width="500" alt="movie keyword" src="https://user-images.githubusercontent.com/87971876/204210107-bd4571fb-9d72-42dd-a062-e7a8763589f8.png">
</center>

#### - 회원가입, 로그인 페이지 유효성 검사 UI
- 가입시 필요한 회원정보의 유효성 검사를 진행 후 통화시 글자에 선을 표현해서 직관적으로 사용할 수 있게함
![join gif](https://user-images.githubusercontent.com/87971876/204210093-3edbcaf9-50fc-4c3e-baa2-c7553973a6bb.gif)

### 6. 기타 (느낀 점, 후기 등)
#### 혜지
 10일정도도 되는 시간동안 기획과 데이터 생성에 3~4일을 사용했을 때 과연 이 프로젝트를 끝낼 수 있을까 걱정이 많았습니다. 마지막 날까지 크롤링 데이터를 다루는 일은 순탄하지 않았지만 팀원 유민이와 함께 상상했던 것들을 구현해내는 일이 즐거워서 열심히 할 수 있었던 것 같습니다. 서로 모르는 부분을 알려주고 같이 찾아보며 프로젝트를 진행했고 한 학기동안 배운것을 확실하게 정리하고 적용해보는 시간이 된것 같습니다. 회원정보를 암호화해서 쿠키에 저장하거나 회원 간 채팅기능, 팔로우와 취향 매칭기능 등 여러가지 시도하고 실패한 기능들도 있어서 아쉬움이 있지만 팀원과 함꼐 했기때문에 이정도 완성도를 이끌어낼 수 있었던 것 같습니다. 처음 계획했던 것보다 서비스가 작아지고 프로젝트 컴포넌트가 복잡해진 것 그리고 구현하지 못한 기능들은 리팩토링을 통해 보완하고싶고 다음 프로젝트에서 더 완성도 있는 기획을 만들어 내고싶습니다. 
