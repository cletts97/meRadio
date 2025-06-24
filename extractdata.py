import urllib3, facebook, requests, urllib

import json
from datetime import datetime

def retrieveName(graph):
    name = graph.get_object(id='me', fields='name')
    return name["name"]

def retrievePosts(graph):
    feed = graph.get_connections(id='me', connection_name='feed')
    feed_data = feed['data']
    posts = []

    for post in feed_data:
        posts.append(graph.get_object(id=post["id"], fields='created_time, message, full_picture'))

    return posts

        # Sorts by oldest first
def sortByTimeStamp(post_list):
    exclude = "-T:+"
    sorted_list = []
    for post in post_list:
        timestamp = post["created_time"]
        for character in exclude:
            timestamp = timestamp.replace(character, "")
        if 'message' in post:
            if 'full_picture' in post:
                data = (timestamp, post["message"], post["full_picture"])
            else:
                data = (timestamp, post["message"], "")
        else:
            if 'full_picture' in post:
                data = (timestamp, "", post["full_picture"])
            else:
                continue
        counter = 0
        while counter < len(sorted_list):
            if sorted_list[counter][0] > data[0]:
                break
            counter += 1
        if counter == len(sorted_list):
            sorted_list.append(data)
        else:
            sorted_list.insert(counter, data)
    return sorted_list

def saveImages(data):
    counter = 0
    for post in data:
        if post[2] != "":
            urllib.request.urlretrieve(post[2], "Images/image" + str(counter) + ".jpg" )
            counter += 1

def dateToString(timestamp):
    year = timestamp[0:4]
    month = timestamp[4:6]
    day = timestamp[6:8]

    return "On the " + str(day) + " of " + str(month) + " " + str(year)

#def saveImages2():
    #urllib.request.urlretrieve("https://storage.googleapis.com/gd-wagtail-prod-assets/original_images/evolving_google_identity_2x1.jpg", "Images/local-filename.jpg" )
