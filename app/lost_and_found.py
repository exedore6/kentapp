import sqlite3
import json

#Query the database and return everything

def post_lf(item_name, user_id, lost_or_found, location, description, lf_time, image, completed, item_type):
    post_content = ("INSERT INTO lost_and_found(item_name,user_id, lost_or_found, location, description, lf_time, post_time, image, completed, item_type) VALUES(" + 
        "'" + item_name + "'," +
        str(user_id) + "," +
        str(lost_or_found) + "," +
        "'" + location + "'," +
        "'" + description + "'," +
        "'" + lf_time + "'," +
        "current_timestamp" + "," +
        "'" + image + "'," +
        str(completed) + "," +
        "'" + item_type
         + "')" )
    print(post_content)
         
    conn = sqlite3.connect('kentapp.db')
    c = conn.cursor()   
    c.execute(post_content)
    conn.commit()
    conn.close()
    #c.execute("SELECT * FROM lost_and_found")

    return ("thank you")
 

def get_lost():
    conn = sqlite3.connect('kentapp.db')
    c = conn.cursor()
    c.execute("SELECT item_id, user_id, item_name, lost_or_found, location, description, lf_time, post_time, image, completed, item_type FROM lost_and_found where lost_or_found = 1")
    items = c.fetchall()
    row_count = 0
    row_total = len(items)
    all = []
    print(items)
    while row_count<row_total:
        obj = dict(
        item_id=items[row_count][0],
        user_id=items[row_count][1],
        item_name=items[row_count][2],
        lost_or_found=items[row_count][3],
        location=items[row_count][4],
        description=items[row_count][5],
        lf_time=items[row_count][6],
        post_time=items[row_count][7],
        image=items[row_count][8],
        completed=items[row_count][9],
        item_type=items[row_count][10])
        all.append(obj)
        row_count+= 1

    conn.close()
    return (json.dumps(all))
 

def get_found():
    conn = sqlite3.connect('kentapp.db')
    c = conn.cursor()
    c.execute("SELECT item_id, user_id, item_name, lost_or_found, location, description, lf_time, post_time, image, completed, item_type FROM lost_and_found where lost_or_found = 0")
    items = c.fetchall()
    row_count = 0
    row_total = len(items)
    all = []
    print(items)
    while row_count<row_total:
        obj = dict(
        item_id=items[row_count][0],
        user_id=items[row_count][1],
        item_name=items[row_count][2],
        lost_or_found=items[row_count][3],
        location=items[row_count][4],
        description=items[row_count][5],
        lf_time=items[row_count][6],
        post_time=items[row_count][7],
        image=items[row_count][8],
        completed=items[row_count][9],
        item_type=items[row_count][10])
        all.append(obj)
        row_count+= 1

    conn.close()
    return (json.dumps(all))


def get_lost_and_found_mine():
    conn = sqlite3.connect('kentapp.db')
    c = conn.cursor()
    c.execute("SELECT item_id, user_id, item_name, lost_or_found, location, description, lf_time, post_time, image, completed, item_type FROM lost_and_found where user_id = 1")
    items = c.fetchall()
    row_count = 0
    row_total = len(items)
    all = []
    print(items)
    while row_count<row_total:
        obj = dict(
        item_id=items[row_count][0],
        user_id=items[row_count][1],
        item_name=items[row_count][2],
        lost_or_found=items[row_count][3],
        location=items[row_count][4],
        description=items[row_count][5],
        lf_time=items[row_count][6],
        post_time=items[row_count][7],
        image=items[row_count][8],
        completed=items[row_count][9],
        item_type=items[row_count][10])
        all.append(obj)
        row_count+= 1

    conn.close()
    return (json.dumps(all))


def complete_lost_and_found(item_id):
    conn = sqlite3.connect('kentapp.db')
    c = conn.cursor()
    c.execute(" UPDATE lost_and_found SET completed = 1 WHERE item_id = " + str(item_id))
    items = c.fetchall()
    row_count = 0
    row_total = len(items)
    all = []
    print(items)
    while row_count<row_total:
        obj = dict(
        item_id=items[row_count][0],
        user_id=items[row_count][1],
        item_name=items[row_count][2],
        lost_or_found=items[row_count][3],
        location=items[row_count][4],
        description=items[row_count][5],
        lf_time=items[row_count][6],
        post_time=items[row_count][7],
        image=items[row_count][8],
        completed=items[row_count][9],
        item_type=items[row_count][10])
        all.append(obj)
        row_count+= 1

    conn.close()
    return (json.dumps(all))
