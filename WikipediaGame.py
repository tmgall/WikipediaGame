import requests
from lxml import html
import queue

def findPath(start, destination):
    prefix = "https://en.wikipedia.org/wiki/"
    topic = getTopic(start)
    dest = getTopic(destination)
    path = []
    q = queue.Queue()
    visited = {topic : "FoundSolution"}
    q.put((topic, "FoundSolution"))
    while (not q.empty()):
        curTopic = q.get()
        cur = prefix + curTopic[0]
        req = requests.get(cur)
        if curTopic == dest: 
            path.append(curTopic)
            break
        if req.status_code == 404: continue
        webpage = html.fromstring(req.content)
        links = cleanLinks(webpage.xpath('//a/@href'))
        print(curTopic)
        for link in links:
            if link in visited: continue
            if link == dest: 
                path.append(link)
                path.append(curTopic[0])
                q.queue.clear()
                print("Path: " + str(path))
                break
            else:
                visited[link] = curTopic[0]
                q.put((link, curTopic[0]))
    if len(path) == 0: print("No path exists")
    else:
        while (path[-1] != topic):
            cur = path[-1]
            next = visited[cur]
            path.append(next)
        path.reverse()
    print(path)

def remove(links, n):
    for i in range(n):
        links.pop()

def cleanLinks(links):
    toReturn = []
    for link in links:
        if len(link) < 6: continue
        if link[:6] != "/wiki/": continue
        if len(link) >= 15 and link[6:15] == "Category:": continue
        if link[-4:] == ".jpg" or link[-4:] == ".svg" or link[-4:] == ".gif": continue
        if len(link) >= 11 and link[:11] == "/wiki/Talk:": continue
        if len(link) >= 15 and link[:15] == "/wiki/Main_Page": continue
        if len(link) >= 11 and link[:11] == "/wiki/File:": continue
        if len(link) >= 13 and link[:13] == "/wiki/Portal:": continue
        if len(link) >= 11 and link[:11] == "/wiki/Help:": continue
        if len(link) >= 14 and link[:14] == "/wiki/Special:": continue
        if len(link) >= 15 and link[:15] == "/wiki/Template:": continue
        if len(link) >= 16 and link[:16] == "/wiki/Wikipedia:": continue
        link = link[6:]
        toReturn.append(link)
    return toReturn

def getTopic(startLink):
    return startLink[30:]

start = "https://en.wikipedia.org/wiki/Chess"
destination = "https://en.wikipedia.org/wiki/Downton_Abbey"

findPath(start, destination)