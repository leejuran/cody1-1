# 나만의 프롬프트 관리 프로그램

터미널에서 메뉴 번호를 입력해 프롬프트를 관리하는 콘솔 기반 프로그램입니다.
프롬프트를 카테고리별로 등록하고, 검색하고, 즐겨찾기로 관리할 수 있습니다.

## 실행 방법

```bash
python main.py
```

프로그램 실행 후 화면에 나오는 메뉴 번호를 입력하면 원하는 기능을 사용할 수 있습니다.

## 기능 목록

1. **프롬프트 추가** — 제목, 내용, 카테고리를 입력해 새 프롬프트를 등록합니다. 제목/내용은 빈 값으로 등록할 수 없습니다.
2. **프롬프트 목록 보기** — 등록된 모든 프롬프트를 카테고리와 즐겨찾기 표시(⭐)와 함께 보여줍니다.
3. **카테고리별 조회** — 카테고리를 선택하면 해당 카테고리의 프롬프트만 보여줍니다.
4. **프롬프트 검색** — 키워드로 제목/내용을 검색합니다.
5. **프롬프트 상세 보기** — 번호를 선택하면 해당 프롬프트의 전체 내용을 보여줍니다.
6. **즐겨찾기 관리** — 번호를 선택해 즐겨찾기를 추가하거나 해제합니다.
7. **즐겨찾기 목록** — 즐겨찾기로 등록된 프롬프트만 모아서 보여줍니다.
8. **종료** — 프로그램을 종료합니다.

## 카테고리 종류

텍스트 생성, 이미지 생성, 영상 생성, 페르소나, 자동화, 기타

## 기본 등록 프롬프트

프로그램 실행 시 아래 3개의 프롬프트가 기본으로 등록되어 있습니다.

- 블로그 글쓰기 (텍스트 생성)
- 영어 번역 (텍스트 생성)
- 이미지 프롬프트 (이미지 생성)

## 개발 환경

- Python 3.10 이상
- VSCode
- Git / GitHub

## 함수 구조 설명

기능별로 함수를 분리하여 각 함수가 하나의 책임만 담당하도록 설계했습니다.

| 함수 | 역할 |
|---|---|
| `add_prompt()` | 제목/내용/카테고리 입력받아 새 프롬프트 등록 (빈값 검증 포함) |
| `show_prompts()` | 전체 프롬프트 목록 출력 |
| `search_by_category()` | 카테고리 목록 제시 후 선택한 카테고리의 프롬프트만 출력 |
| `search_prompt()` | 키워드로 제목/내용 검색 |
| `show_detail()` | 번호로 특정 프롬프트 상세 내용 출력 |
| `toggle_favorite()` | 번호로 즐겨찾기 추가/해제 |
| `show_favorites()` | 즐겨찾기된 프롬프트만 모아서 출력 |
| `main()` | 메뉴 출력 및 사용자 입력에 따라 각 함수 호출 (전체 흐름 제어) |

## 데이터 구조 선택 이유

프롬프트 데이터는 **리스트(list) 안에 딕셔너리(dict)를 담는 구조**로 저장합니다.

```python
prompts = [
    {"제목": "...", "내용": "...", "카테고리": "...", "즐겨찾기": False},
    ...
]
```

- 리스트: 순서를 유지하며 여러 개의 프롬프트를 담기에 적합하고, 번호(인덱스)로 접근하기 쉽습니다.
- 딕셔너리: 제목/내용/카테고리/즐겨찾기처럼 이름이 있는 여러 속성을 한 항목에 묶어 표현하기 적합합니다.
- 단점: 프롬프트 수가 많아지면 검색/필터링 시 매번 전체 리스트를 순회해야 하므로 성능이 떨어질 수 있습니다. 현재 규모(과제 수준)에서는 문제가 없습니다.

## 반복문(while) 설계

`main()`의 메뉴 루프는 `while True:`로 무한 반복하다가, 사용자가 종료 번호(8)를 선택하면 `break`로 루프를 빠져나가는 구조입니다. 각 기능 실행 후 자동으로 메뉴로 돌아오는 요구사항을 만족시키기 위해, 매 기능 호출 후 별도 처리 없이 다시 루프 처음(메뉴 출력)으로 돌아가도록 설계했습니다.

## Git 작업 기록

- **커밋 단위**: 기능 하나가 완성될 때마다 커밋을 나누어 진행했습니다. 예: `프롬프트 추가`, `목록 표시`, `상세 보기`, `즐겨찾기 토글`, `즐겨찾기 목록`, `README 작성` 등 기능 단위로 총 18개의 커밋을 진행했습니다.
- **브랜치 전략**: 기존 기능에 영향을 주지 않고 독립적으로 개발/테스트가 필요한 기능은 별도 브랜치에서 작업 후 `master`로 병합했습니다.
  - `feature/detail-view`: 상세 보기 기능 개발
  - `feature/favorite-list`: 즐겨찾기 목록 기능 개발
  - `docs/readme-update`: README 문서 작업
  - 각 브랜치는 `git checkout -b`로 생성하고, 기능 완성 후 `git checkout master` → `git merge`로 병합했습니다.


## 중복/충돌 처리 규칙

동일한 제목의 프롬프트가 여러 개 등록되더라도, 프로그램은 이를 별도의 항목으로 각각 저장합니다(제목 중복을 막지 않음). 카테고리가 사용자의 직접 입력으로 새로 생겨도 별도 검증 없이 새 카테고리로 인정합니다.


깃허브 저장소 URL

https://github.com/kimjisook-1052/prompt-manager


결과물 스크린샷

python --version, git --version 결과

<img width="473" height="65" alt="image" src="https://github.com/user-attachments/assets/41261f12-940f-49be-9351-435b20d0ee2c" />

 
git config --list

<img width="455" height="305" alt="image" src="https://github.com/user-attachments/assets/50ff43f5-9c35-4311-8d07-1a8ac3cfa1d7" />


git clone 실행 로그 

<img width="510" height="155" alt="image" src="https://github.com/user-attachments/assets/222762a1-2b79-483f-a23a-15e271ab37b1" />

 
메뉴 화면

<img width="448" height="246" alt="image" src="https://github.com/user-attachments/assets/b5353daa-cab4-4ed3-9e93-2d7e2d8d5755" />

 
프롬프트 추가 과정

<img width="431" height="226" alt="image" src="https://github.com/user-attachments/assets/f4ba532c-f811-43a0-ace0-dd4b1b88f2e8" />

 
목록 보기

<img width="503" height="237" alt="image" src="https://github.com/user-attachments/assets/a817ed2a-134f-4f30-9a5b-18822898a352" />

 
카테고리별 조회
 
<img width="438" height="92" alt="image" src="https://github.com/user-attachments/assets/89a1e1dd-1622-4b46-a864-ce73208d60f6" />


검색 결과
 
<img width="499" height="137" alt="image" src="https://github.com/user-attachments/assets/17edb515-0e57-4f4f-80ec-369ede3bba9b" />

 
상세 보기

<img width="448" height="173" alt="image" src="https://github.com/user-attachments/assets/e36a674e-6b32-40c2-b837-3f5101e9f629" />


즐겨찾기 관리/목록

<img width="450" height="90" alt="image" src="https://github.com/user-attachments/assets/99d2ed0f-a432-49df-8854-1b1f8bd2862e" />


git log --oneline --graph

<img width="498" height="274" alt="image" src="https://github.com/user-attachments/assets/ca153aa5-4d28-4461-8ea2-1b6a48623ab7" />
