while True:

    try :
        a, b= map(int, input().split())
        if a == "" or b == "" :
            break
        print(a + b)
    except :
        break