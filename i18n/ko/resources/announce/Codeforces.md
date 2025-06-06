## 1.73

- 웹사이트 현지화 데이터를 외부 JSON으로 독립시켜 유지 관리가 용이합니다.
- 스크립트는 국제화를 지원하고 크라우드인 플랫폼을 사용하여 현지화를 자동화합니다.
- 일부 버튼을 아이콘 버튼으로 바꾸기
- 공식 api-free, api-pro 및 deeplx를 포함한 DeepL API에 대한 지원을 추가합니다(제안해 주신 @Vistarin에게 감사드립니다)!
- 잔액 조회를 구성하기 위해 deep 및 chatgpt에 대한 지원을 추가하려면 서비스 제공업체가 이를 지원하고 적절한 API를 제공해야 한다는 점에 유의하세요.
- 번역 전 텍스트에 대한 판단을 추가하여 코드 조각으로 의심되는 경우 자동으로 번역되지 않으며, 번역을 클릭하기 전에 팝업 창이 표시됩니다.
- 번역 서비스의 대상 언어를 선택할 수 있는 기능 추가하기
- 정보 페이지와 업데이트 채널 및 업데이트 소스 선택 항목을 추가합니다.
- 캐시 새로 고침, 데이터 지우기, 가져오기 및 내보내기를 포함한 디버깅 유지 관리 페이지를 추가합니다.
- 사용자 지정 옵션 추가： '코드 편집기 제출 버튼 위치', 기본값은 하단으로 설정, 제안해 주신 @lishufood님께 감사드립니다!
- 각 로딩 기능을 개선하고, 불필요한 대기 관계를 제거하며, 스크립트 로딩 시간을 단축합니다.
- 번역 기능 및 오류 메시지 표시가 개선되었습니다.
- 자동 번역 성능 개선 및 자동 번역이 되지 않는 문제 개선
- 온라인 실행과 관련된 코드 샘플 개선
- 실행 결과의 차이를 비교하는 코드Diff() 메서드 개선
- 대화창 배경 콘텐츠가 더 이상 마우스로 스크롤되지 않도록 개선되었습니다.
- 코드 편집기의 스타일을 오른쪽, 아래쪽, 전체 화면으로 고정할 수 있도록 개선해 주신 @lishufood 님께 감사드립니다!
- 단순 모드에서 .html2md-패널 패널 표시가 개선되었습니다.
- 설정 패널에서 구성 페이지의 스타일 개선하기
- acmsguru 제목 페이지 편집기 오류 수정
- 웹사이트의 모바일/데스크톱 버전을 전환한 후 이슈 페이지의 코드 편집기가 오류를 보고하는 문제를 수정했습니다.
- 데이터를 DOM에 직접 잘못 저장하여 페이지 성능 저하를 초래하는 getMarkdown() 메서드의 버그를 수정했습니다.
- 모유투고님의 피드백 덕분에 '접힌 블록 자동 펼치기'를 끈 후 접힌 블록 내부의 번역 버튼이 표시되지 않는 문제를 수정했습니다!
- "페이지 리소스가 완전히 로드될 때까지 기다리지 않음" 옵션은 이론적으로 의미가 없으므로 이전에 가능한 상태를 선택 취소하는 것으로 이름이 변경되었습니다.
- 수많은 코드 구조 조정
- **CSS 클래스 이름 변경이 많으므로 스타일러스 사용자 정의 스타일을 사용하는 경우 이를 조정해야 할 수 있습니다**.
- 기타 조정 및 개선 사항

## 1.72

- caoxuanming의 피드백 덕분에 ChatGPT 구성 패널이 표시되지 않는 문제를 해결했습니다!
- 제안해 주신 @liuhao6님께 감사드리며, 기본적으로 '마우스 스크롤 잠금'을 켜는 구성 스위치를 추가합니다.

## 1.71

- 제안해 주신 @wrkwrk님께 감사드리며, 클리스트 등급 API를 v4로 업데이트하고, 제목 페이지에서 데이터를 가져오는 방식을 API를 통해 가져오는 방식으로 조정했습니다!
- 기본적으로 활성화된 ChatGPT 번역 '스트리밍' 옵션 추가하기
- Google 번역 결과가 비어 있는 문제 수정 피드백을 보내주신 @shicxin님께 감사드립니다!
- "코드 커밋에 대한 이중 확인" 구성 스위치를 기본적으로 켜도록 설정하세요. 제안해 주신 @Rikkual님께 감사드립니다!
- 전체 주제 집합 페이지에 작은 영역을 추가하는 버튼
- 전체 주제 세트 페이지를 마우스 오른쪽 버튼으로 클릭하여 인쇄할 때 번역 결과가 표시되지 않는 문제 수정 피드백을 보내주신 @zfs732님께 감사드립니다!

## 1.70

- 제목 페이지 하단에 코드 편집기를 추가하여 온라인 코드 테스트, 코드 제출 등을 지원합니다. 자세한 내용은 정보 페이지를 참조하세요.
- 스크립트 버튼을 삽입하고 결과를 번역할 때 제목 설명이 변경된 것으로 간주되던 문제를 수정했습니다.
- 포트폴리오 매시업 관리 페이지 개선 사항
- 기본적으로 꺼져 있는 '짧은 텍스트 자동 번역' 기능을 추가합니다.
- 번역 대기 간격 구현이 개선되어 이제 대기 간격이 전 세계적으로 작동합니다.
- '대상 영역 범위 표시' 구현 개선 사항
- 다크 모드 개선, 샘플 요소의 호버 스타일 개선 피드백을 보내주신 @SUPERLWR에게 감사드립니다!
- 설정 패널 옵션 추가: 번역 - 텍스트의 \*\*기호 필터링 피드백을 주신 @Dog_E, CreMicro에게 감사드립니다!
- 비스타린의 피드백에 따라 '로딩 알림 표시'를 끈 후 클리스트 등급이 제대로 표시되지 않던 문제를 수정했습니다.
- 기타 개선 및 수정 사항
