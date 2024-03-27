for _ in range(4):
    si1, sj1, ei1, ej1, si2, sj2, ei2, ej2 = map(int, input().split())

    code = 'a'

    # d: 안 겹침
    if si1 > ei2 or ei1 < si2 or sj1 > ej2 or ej1 < sj2:
        code = 'd'

    elif ej1 == sj2 or sj1 == ej2:  # 세로 일치
        if ei1 == si2 or si1 == ei2:  # 가로 일치
            code = 'c'  # 점
        else:
            code = 'b'  # 면 (세로일치, 가로 불일치)
    elif ei1 == si2 or si1 == ei2:  # (세로 불일치) 가로 일치
        code = 'b'

    # 나머지 -> a: 직사각형
    else:
        code = 'a'

    print(code)
