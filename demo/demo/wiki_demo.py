# wiki 上的一些小示例
def fib(n):
    """斐波那契数列，写出从第0项到第n项的斐波那契数列"""
    a, b, i = 0, 1, 0
    while i <= n:
        print(a, end=' ')
        a, b, i = b, a+b, i+1
    print()

if __name__ == '__main__':
    fib(19)