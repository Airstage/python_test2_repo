from pprint import pprint


def dialog(text):
    pprint(text)
    answer = input()
    return answer


def friendship(person, host):
    if not host.are_friends(person):
        host.add_friend(person)
    else:
        pprint(f'{host} are already befrended this person.')



