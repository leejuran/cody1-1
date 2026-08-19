prompts = []

while True:
    print("\n--- 메뉴 ---")
    print("1.등록 2.목록 3.검색 4.삭제 5.종료")
    
    menu = input("번호 선택: ")

    if menu == '1':

        t = input("등록할 제목:")
        c = input("등록할 내용: ")
        prompts.append({"title": t, "content": c})
        print("저장 완료!")

    elif menu == '2': # 'elif'
        print(f"총 {len(prompts)}개가 있습니다.")
        for p in prompts:
            print(f"- {p['title']}")

    elif menu == '3': # 'elif'
        search = input("검색할 단어를 입력하세요:")
        found = False  # <- 이 줄의 앞 간격이 21번 줄과 똑같아야 해요!
        
        for p in prompts:
            if search in p['title']:
                print(f"결과: {p['title']} / {p['content']}")
                found = True
        
        if found == False:
            print("❌ 검색 결과가 없습니다 .")
    elif menu == '4':
        print("\n--- 삭제 모드 ---")
        if not prompts:
            print("❌ 삭제할 항목이 없습니다.")
        else:
            # 리스트를 번호와 함께 보여주기
            for i, p in enumerate(prompts):
                print(f"[{i+1}] {p['title']}")
            
            try:
                select = int(input("삭제할 번호를 입력하세요: "))
                if 0 < select <= len(prompts):
                    removed = prompts.pop(select - 1)
                    print(f"✅ '{removed['title']}' 항목이 삭제되었습니다.")
                else:
                    print("❌ 잘못된 번호입니다.")
            except ValueError:
                print("❌ 숫자만 입력해주세요.")

    elif menu == '5':
        print("프로그램을 종료합니다. 안녕히 가세요! 👋")
        break
            