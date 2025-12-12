n = int(input())
arr = list(map(int, input().split()))

if n == 1:
    print("A")
elif n == 2:
    if arr[0] == arr[1]:
        print(arr[0])
    else:
        print("A")
else:
    if arr[0] == arr[1]:
        same = True
        for i in range(n):
            if arr[i] != arr[0]:
                same = False
                break

        if same:
            print(arr[0])
        else:
            print("B")
    else:
        diff = arr[2] - arr[1]
        prev_diff = arr[1] - arr[0]

        if diff % prev_diff != 0:
            print("B")
        else:
            a = diff // prev_diff
            b = arr[1] - arr[0] * a

            ok = True
            for i in range(n - 1):
                if arr[i] * a + b != arr[i + 1]:
                    ok = False
                    break

            if ok:
                print(arr[n - 1] * a + b)
            else:
                print("B")
