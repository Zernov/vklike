import vk
import operator
from time import sleep

def getTop(id, count):
    session = vk.Session()
    api = vk.API(session)

    post_count = api.wall.get(owner_id = id, count = 1)[0]

    posts = {}
    step = 100
    current = 0

    response = api.wall.get(owner_id = id, count = step, offset = current)
    print("[0%] 0/" + str(post_count), end = "\r")

    while len(response) > 1:
        for i in range(1, len(response)):
            posts.update({makeLink(id, response[i]['id']) : response[i]['likes']['count']})
        current += step
        progress = int(100 * current / post_count)
        print("[" + str(progress) + "%] " + str(current) + "/" + str(post_count), end = "\r")
        sleep(0.1)
        response = api.wall.get(owner_id = id, count = step, offset = current)

    return dict(sorted(posts.items(), key = operator.itemgetter(1), reverse=True)[:count])

def makeLink(id, post):
    return "https://vk.com/wall" + str(id) + "_" + str(post)

def printDict(dict):
    for record in dict:
        print(record + " (" + str(dict[record]) + ")")

top = getTop(-58219172,10)

printDict(top)
