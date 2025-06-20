import sys

def main():
    params = sys.argv[1:]
    if len(params)== 0:
        print("none")

    for p in params:
        if p.endswith("ism"):
            continue
        print(p+"ism")
main()
