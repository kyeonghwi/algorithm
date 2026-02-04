while True:
    arr= list(input().split())
    if arr== "*":
        break
    temp = arr[0][0].lower()
    tauto = True
    for elem in arr:
        if temp == elem[0].lower():
            continue
        else:
            tauto = False
    if tauto:
        print('Y')
    else:
        print('N')