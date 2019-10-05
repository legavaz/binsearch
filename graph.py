from collections import deque
import os

os.system('CLS')

graph ={}
graph["you"]    =['alice','bob','claire']
graph["bob"]    =['anuj','peggy']
graph["alice"]  =['peggy']
graph["claire"] =['tom','jonny']
graph["anuj"]   =[]
graph["peggy"]  =[]
graph["tom"]    =[]
graph["jonny"]  =[]



def person_is_seller(name):
    return name[-1]=='m'


def serch(name):
    search_queue = deque()
    search_queue+=graph[name]
    serched =   []
    while search_queue:
        # person = search_queue.popleft()
        person = search_queue.pop() #ошибка
        if not person in serched: 
            if person_is_seller(person):
                print(person,'is seller Mango')
                return True
            else:
                search_queue +=graph[person]
                # print(person,'NO seller Mango')
                serched.append(person)
    return False

serch('you')
