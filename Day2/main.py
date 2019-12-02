def run(prog,ip):
    op = prog[ip]
    if op == 1:
        ptr1 = prog[ip+1]
        ptr2 = prog[ip+2]
        ptr3 = prog[ip+3]
        prog[ptr3] = prog[ptr1]+prog[ptr2]
        return run(prog,ip+4)
    elif op == 2:
        ptr1 = prog[ip+1]
        ptr2 = prog[ip+2]
        ptr3 = prog[ip+3]
        prog[ptr3] = prog[ptr1]*prog[ptr2]
        return run(prog,ip+4)
    elif op == 99:
        return prog


if __name__ == "__main__":
    with open("input.txt") as f:
        text = f.read()
        prog = [int(i) for i in text.split(",")]
        #part 1
        prog[1] = 12
        prog[2] = 2
        print(prog)
        base = prog.copy()
        print(run(prog,0))
        #part 2
        for x in range(99):
            for y in range(99):
                prog = base.copy()
                prog[1] = x
                prog[2] = y
                out = run(prog,0)
                if out is not None and out[0] == 19690720:
                    print(x)
                    print(y)
        print("done")

