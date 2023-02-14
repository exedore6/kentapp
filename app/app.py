from flask import Flask
from flask import request, jsonify
import lost_and_found
import activity
import user
import sqlite3

app = Flask(__name__)

@app.route("/lost_and_found/lost", methods=['GET'])
def get_lost():
    return lost_and_found.get_lost()

@app.route("/lost_and_found/found", methods=['GET'])
def get_found():
    return lost_and_found.get_found()

@app.route("/lost_and_found/mine", methods=['GET'])
def get_lost_and_found_mine():
    return lost_and_found.get_lost_and_found_mine()

@app.route("/lost_and_found/post", methods=['POST'])
def post_lf():
    json_data = request.form
    files = request.files
    item_name = json_data['item_name']
    user_id = json_data['user_id']
    lost_or_found = json_data['lost_or_found']
    location = json_data['location']
    description = json_data['description']
    lf_time = json_data['lf_time']

    conn = sqlite3.connect('kentapp.db')
    c = conn.cursor()   
    c.execute("insert into resource(resource_type) values(1)")
    resource_id = c.lastrowid
    conn.commit()
    conn.close()
    image = "/static/image/" + str(resource_id) + ".jpg"
    file = files['file']
    file.save("static/image/" + str(resource_id) + ".jpg")
    
    completed = json_data['completed']
    item_type = json_data['item_type']
    return lost_and_found.post_lf(item_name, user_id, lost_or_found, location, description, lf_time, image, completed, item_type)


@app.route("/lost_and_found/complete", methods=['PUT'])
def complete_lost_and_found():
    # return item_id from interface?
    item_id = 2
    return lost_and_found.complete_lost_and_found(item_id)

@app.route("/activity", methods=['GET'])
def get_activity():
    return activity.get_activity()

@app.route("/activity/mine", methods=['GET'])
def get_activity_mine():
    return activity.get_activity_mine()

@app.route("/activity/post", methods=['POST'])
def post_activity():
    json_data = request.form
    files = request.files
    user_id = json_data['user_id']
    title = json_data['title']

    conn = sqlite3.connect('kentapp.db')
    c = conn.cursor()   
    c.execute("insert into resource(resource_type) values(1)")
    resource_id = c.lastrowid
    conn.commit()
    image = "/static/image/" + str(resource_id) + ".jpg"
    file = files['file']
    file.save("static/image/" + str(resource_id) + ".jpg")
    conn.close()

    description = json_data['description']
    deadline = json_data['deadline']
    activity_time = json_data['activity_time']
    location = json_data['location']
    activity_type = json_data['activity_type']
    space_used = json_data['space_used']
    space_limit = json_data['space_limit']

    return activity.post_activity(user_id, title, image, description, deadline, activity_time, location, activity_type,space_used, space_limit)

@app.route("/user", methods=['GET'])
def get_user():
    return user.get_user()

@app.route("/user/post", methods=['POST'])
def post_user():
    json_data = request.json
    print(json_data)
    user_id = json_data['user_id']
    name = json_data['name']
    email = json_data['email']
    profile_pic = json_data['profile_pic']
    teacher = json_data['teacher']
    admin = json_data['admin']
    banned = json_data['banned']
    return user.post_user(user_id,name,email,profile_pic,teacher,admin,banned)

if __name__ == "__main__":
    app.run()


#=======================================================================

#dummy lost and found item list
lost_list = [
    {'id':1, 'name':'Bible','location':'Chapel','lost_or_found':True},
    {'id':2, 'name':'Wallet','location':'dining hall','lost_or_found':True},
    {'id':3, 'name':'Bag','location':"",'lost_or_found':True}
]
found_list = [
    {'id':1, 'name':'book','location':'library','lost_or_found':False},
    {'id':2, 'name':'pencil','location':'dickenson','lost_or_found':False},
    {'id':3, 'name':'phone','location':'town','lost_or_found':False}
]

#fake activity list
act_list = [
    {'id':1, 'name':'Math club','location':'S519'},
    {'id':2, 'name':'squash game','location':'squash court'},
    {'id':3, 'name':'Weekend Mall trip','location':'behind HC'}
]

#fake user list
user_list = [
    {'id':1, 'name':'Niki','gender':'F','email':'huj23'},
    {'id':2, 'name':'Jiayi','gender':'F','email':'jiayi24'},
    {'id':3, 'name':'NH','gender':'hidden','email':'niki.hu04'}
]
