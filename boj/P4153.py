while True:
    user_input = input()

    if user_input == '0 0 0':
        break
        
    A, B, C = map(int, user_input.split())

    if A*A + B*B == C*C:
        print("right")
    elif A*A + C*C == B*B:
        print("right")
    elif B*B + C*C == A*A:
        print("right")
    else:
        print("wrong")
