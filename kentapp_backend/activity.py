#11+1=12 variables
import sqlite3
import json
from flask import request

#Query the database and return everything

def post_activity(user_id, title, image, description, deadline, activity_time, location, activity_type,space_used, space_limit):
    user_id = str(user_id)
    title = title
    image = image
    description = description
    deadline = deadline
    activity_time = activity_time
    location = location
    activity_type = activity_type
    space_used = str(space_used)
    space_limit = str(space_limit)

    conn = sqlite3.connect('kentapp.db')

    c = conn.cursor()
    c.execute(
        "INSERT INTO activity (user_id, title, image, description, post_time, deadline, activity_time, location, activity_type,space_used, space_limit) VALUES(" + 
        "'" + user_id + "'," +
        "'" + title + "'," +
        "'" + image + "'," +
        "'" + description + "'," +
        "current_timestamp" + "," +
        "'" + deadline + "'," +
        "'" + activity_time + "'," +
        "'" + location + "'," +
        "'" + activity_type + "'," +
        "'" + space_used + "'," +
        "'" + space_limit
         + "')" )
    conn.commit()
    conn.close()
    
    # c.execute("SELECT * FROM activity")

    return ("finished")
 

    conn.close()

def get_activity():
    conn = sqlite3.connect('kentapp.db')
    c = conn.cursor()
    c.execute("SELECT act_id, user_id, title, image, description, post_time, deadline, activity_time, location, activity_type, space_used, space_limit FROM activity")
    items = c.fetchall()
    row_count = 0
    row_total = len(items)
    all = []
    while row_count<row_total:
        obj = dict(
        act_id=items[row_count][0],
        user_id=items[row_count][1],
        title=items[row_count][2],
        image=items[row_count][3],
        description=items[row_count][4],
        post_time=items[row_count][5],
        deadline=items[row_count][6],
        activity_time=items[row_count][7],
        location=items[row_count][8],
        activity_type=items[row_count][9],
        space_used=items[row_count][10],
        space_limit=items[row_count][11])
        all.append(obj)
        row_count+= 1

    conn.close()
    return (json.dumps(all))

def get_activity_mine():
    conn = sqlite3.connect('kentapp.db')
    c = conn.cursor()
    c.execute("SELECT act_id, user_id, title, image, description, post_time, deadline, activity_time, location, activity_type, space_used, space_limit FROM activity WHERE user_id = 1")
    items = c.fetchall()
    row_count = 0
    row_total = len(items)
    all = []
    while row_count<row_total:
        obj = dict(
        act_id=items[row_count][0],
        user_id=items[row_count][1],
        title=items[row_count][2],
        image=items[row_count][3],
        description=items[row_count][4],
        post_time=items[row_count][5],
        deadline=items[row_count][6],
        activity_time=items[row_count][7],
        location=items[row_count][8],
        activity_type=items[row_count][9],
        space_used=items[row_count][10],
        space_limit=items[row_count][11])
        all.append(obj)
        row_count+= 1

    conn.close()
    return (json.dumps(all))