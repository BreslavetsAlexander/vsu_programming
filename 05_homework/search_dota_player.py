from collections import deque


def is_dota_player(s):
    return not len(s) % 2 and s[0] == 'D'


def get_dota_player(deq, people_dict):
    checked_people = []
    while deq:
        current = deq.popleft()
        if current not in checked_people:
            if is_dota_player(current):
                return current
            else:
                deq += people_dict.get(current, [])
            checked_people.append(current)
    return 'Nobody players in Dota'


people = {
    'Alice': ['Bob', 'Diman', 'Vlad', 'Diana'],
    'Vlad': ['Lula', 'Ahmad'],
    'Diana': ['Dima'],
    'Bob': ['Vlad', 'Oleg']
}

d = deque(people['Alice'])

print(get_dota_player(d, people))
