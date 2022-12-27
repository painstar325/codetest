# https://www.acmicpc.net/problem/1308

import sys
input = sys.stdin.readline

def check_leap_year(year):
    if year % 4 == 0:
        if year % 400 == 0:
            return True
        elif year % 100 == 0:
            return False
        return True
    return False

def sol(start_year, start_month, start_day, end_year, end_month, end_day):
    # 천년이상 차이
    if f"{start_year + 1000}{start_month}{start_day}" <= f"{end_year}{end_month}{end_day}":
        return "gg"
    
    d_day = 0
    # 1년 이상 차이날때 한꺼번에 구하기
    for year in range(start_year, end_year):
        #윤년체크
        if check_leap_year(year):
            d_day += 366
        else:
            d_day += 365
    
    for month in range(1, start_month + 1):
        if month == start_month:
            d_day -= start_day
            break
        if month == 2:
            if check_leap_year(start_year):
                d_day -= 29 
            else:
                d_day -= 28
        elif month in [1, 3, 5, 7, 8, 10, 12]:
            d_day -= 31
        else:
            d_day -= 30
    # d_day += start_day
    for month in range(1, end_month):
        if month == 2:
            if check_leap_year(end_year):
                d_day += 29
            else:
                d_day += 28
        elif month in [1, 3, 5, 7, 8, 10, 12]:
            d_day += 31
        else:
            d_day += 30
    d_day += end_day

    return f"D-{d_day}"

if __name__ == "__main__":
    today = list(map(int, "2100 02 28".split()))
    dday = list(map(int, "2111 02 27".split()))
    # today = list(map(int, input().split()))
    # dday = list(map(int, input().split()))
    print(sol(today[0], today[1], today[2], dday[0], dday[1], dday[2]))

