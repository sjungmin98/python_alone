def play_game():     
    answer = []  # 정답 숫자 리스트     
    # 사용자로부터 3개의 숫자 입력 받기     
    user_input = input("0~9 숫자 3개를 입력하세요: ")  
    # 사용자로부터 게임 횟수 입력 받기
    user_trygame = int(input("도전 횟수를 입력하세요: "))  
    user_numbers = user_input.split()  # 입력 받은 숫자를 리스트로 변환      
    # 입력 받은 숫자를 answer 리스트에 저장     
    for number in user_numbers:         
        answer.append(int(number))
          
    # 게임 진행 
    for i in range(user_trygame):    
        strikes = 0  # 스트라이크 수     
        balls = 0  # 볼 수  
        # 사용자로부터 추측 숫자 입력 받기         
        guess_input = input("0~9 숫자 3개를 추측하세요: ")         
        guess_numbers = guess_input.split()  
        # 추측한 숫자를 리스트로 변환          
        # 추측한 숫자와 정답 숫자 비교         
        for i in range(3):             
            if int(guess_numbers[i]) == answer[i]:  
                # 값과 위치가 일치하는 경우                 
                strikes += 1             
            elif int(guess_numbers[i]) in answer:  
                # 값은 일치하지만 위치가 다른 경우                 
                balls += 1          
        # 결과 출력         
        print("{}S {}B".format(strikes, balls))      
        if strikes == 3:
            # 게임 종료     
            print("3S!")  
            break
    print("Game Over!")
# 게임 실행 
play_game() 