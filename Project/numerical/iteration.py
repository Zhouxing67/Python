import sympy as sp

x = sp.symbols("x")


def iteration(f, cur=3, tolerance=1e-8, max_t=20):
    print(f"初始值为{cur}, 迭代格式为 : next = {f}")
    for i in range(0, max_t):
        next = f.evalf(subs={x: cur})
        print(f"第{i}次迭代，此时得到的值为{next}")
        if abs(next - cur) < tolerance:
            print("精度符合要求， 退出循环")
            break
        cur = next
    return next


def main():
    f1 = sp.acos(-1 / (1 + sp.exp(-2 * x)))
    f2 = 0.5 * sp.log(-1 / (1 + 1 / sp.cos(x)))
    f3 = x - (sp.cos(x) + 1 / (1 + sp.exp(-2 * x))) / sp.diff(
        sp.cos(x) + 1 / (1 + sp.exp(-2 * x))
    )
    ftable = [f1, f2, f3]
    for f in ftable:
        val = iteration(f)
        print(f"迭代结果为{val}")


if __name__ == "__main__":
    main()
