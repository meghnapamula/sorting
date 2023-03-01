#!/bin/python3

#test

def cmp_standard(a, b):
    if a < b:
        return -1
    if b < a:
        return 1
    return 0


def cmp_reverse(a, b):
    if a < b:
        return 1
    if b < a:
        return -1
    return 0


def cmp_last_digit(a, b):
    return cmp_standard(a % 10, b % 10)


def _merged(xs, ys, cmp=cmp_standard):
    x = 0
    y = 0
    a = []
    while x < len(xs) and y < len(ys):
        if cmp(xs[x], ys[y]) == -1:
            a.append(xs[x])
            x += 1
        else:
            a.append(ys[y])
            y += 1
    while x < len(xs):
        a.append(xs[x])
        x += 1
    while y < len(ys):
        a.append(ys[y])
        y += 1
    return a


def merge_sorted(xs, cmp=cmp_standard):

    if len(xs) <= 1:
        return xs
    else:
        mid = len(xs) // 2
        left = xs[mid:]
        ll = merge_sorted(left, cmp=cmp)
        right = xs[:mid]
        rr = merge_sorted(right, cmp=cmp)
        return _merged(ll, rr, cmp=cmp)


def quick_sorted(xs, cmp=cmp_standard):

    if len(xs) <= 1:
        return xs
    mid = len(xs) // 2
    pivot = xs[mid]
    xs_smaller = [x for x in xs if cmp(x, pivot) == -1]
    xs_smaller = quick_sorted(xs_smaller, cmp=cmp)
    xs_bigger = [x for x in xs if cmp(x, pivot) == 1]
    xs_bigger = quick_sorted(xs_bigger, cmp=cmp)
    xs_equal = [x for x in xs if cmp(x, pivot) == 0]
    return xs_smaller + xs_equal + xs_bigger
