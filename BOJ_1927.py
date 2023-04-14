'''
최소 힙

최소 힙을 이용

배열에 자연수 x를 넣는다.
배열에서 가장 작은 값을 출력, 그 값을 배열에서 제거함

프로그램은 처음에 비어있는 배열에서 시작함

'''

import heapq

import sys

N = int(input())

x = [list(map(int,input().split())) for _ in range(N)]