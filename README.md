# Welbot-V2
-Welbot을 바탕으로 발전시킨 V2<br>
챗봇 주소 : https://narco.iptime.org:8081/rest/chat/ <br>
REST서버 주소 : https://narco.iptime.org:8081/ <br>

## 1. 추가구현사항
  1) 사용자 맞춤형 서비스<br>
    - 웹에서 fetch method를 통하여 사용자의 위치정보(lat, lon), 날씨정보(temp, weather) 가져옴.

  2) 사용자 id를 위한 Facebook 확장.<br>
    - Dialogflow와 Facebook의 integration을 통하여 Facebook의 암호화된 'id'값을 통해 사용자 특정 가능.

  3) 사용자의 접근성 및 편의성 향상.<br>
    - 기존의 텍스트 방식에서 버튼형 투입.<br>
    - 기존에 구현이 덜 되었던 알고리즘 추가.


## 2. 한계점
  1) fetch method에서 가져온 위치,날씨 정보와 Facebook의 사용자id값을 동시에 받아올 수 없음.<br>
    (Facebook에서 기술지원중지로 사용자의 위치, 날씨 정보 접근 불가능)

  2) 사용자정보와 데이터가 충분하지 못해 맞춤형 서비스 및 추천 알고리즘 구현 실패.
