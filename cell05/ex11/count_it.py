import sys
if len(sys.argv) == 1:
    print("none")
else:
    a = sys.argv[1:]
    print(f"parameters: {len(a)}")

    for i in a:
        print(f"{i}: {len(i)}")