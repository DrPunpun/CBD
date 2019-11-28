import random
import time

def str_time_prop(start, end, format, prop):
    """Get a time at a proportion of a range of two formatted times.

    start and end should be strings specifying times formated in the
    given format (strftime-style), giving an interval [start, end].
    prop specifies how a proportion of the interval to be taken after
    start.  The returned time will be in the specified format.
    """

    stime = time.mktime(time.strptime(start, format))
    etime = time.mktime(time.strptime(end, format))

    ptime = stime + prop * (etime - stime)

    return time.strftime(format, time.localtime(ptime))


def random_date(start="2017-1-1 1:00", end="2019-1-1 23:00"):
    return str_time_prop(start, end, '%Y-%m-%d %H:%M', random.random())

## Generic print function
def insert(table, attributes, values):
	return f"INSERT INTO {table} {attributes} VALUES {values};"

def users(num):
	list_users = []
	for i in range(num):
		username = 'admin'+str(i)
		name = username.capitalize()
		email = username + "@cassandra.com"
		regist = random_date()
		list_users.append({'username':username,'name':name,'email':email,'register_time':regist})
	return list_users

def video(num, users):
	list_vids = []
	description = "Lorem Ipsum is simply dummy text of the printing and typesetting industry."
	tags = ["comedy","aveiro","lifestyle","reaction","cooking","top10","gameplay","gamer","music"]
	for i in range(num):
		name = 'video'+str(i)
		user = random.choice(users)
		up_time = random_date(start=user["register_time"])
		vid_tags = [random.choice(tags) for i in range(4)]
		list_vids.append({'name':name, 'author':user['email'], 'upload_time':up_time, 'description':description, 'tags': vid_tags})
	return list_vids

def comments(num, users, vids):
	list_comments = []
	text = "very good :)"
	for i in range(num):
		video = random.choice(vids)
		post_time = random_date(start=video["upload_time"])
		user = random.choice(users)
		list_comments.append({'video': video["name"], "post_time":post_time,"user":user["email"], "comment":text})
	return list_comments

def followers(num, users, vids):
	list_followers = []
	for i in range(num):
		video = random.choice(vids)
		user = random.choice(users)
		list_followers.append({'video': video["name"], 'user': user["email"]})
	return list_followers

def rating(num, vids):
	list_ratings = []
	for i in range(num):
		video = random.choice(vids)
		rating = random.randint(1,5)
		list_ratings.append({'video':video["name"], "id":i,"value":rating})
	return list_ratings

def events(num, vids, users):
	list_events = []
	events = ["play","pause","stop"]
	for i in range(num):
		video = random.choice(vids)
		user = random.choice(users)
		event = random.choice(events)
		event_time = random_date(start=video["upload_time"])
		vid_time = random.randint(1,600)
		list_events.append({'event': event, 'event_time': event_time, 'vid_time':vid_time, 'user':user["email"], 'video':video["name"]})
	return list_events

def main():
	list_users = users(15)
	for u in list_users:
		print(insert('users', "(username, name, email, register_time)", tuple(u.values())))
	list_vids = video(20, list_users)
	for v in list_vids:
		print(insert('video', "(name, author, upload_time, description, tags)", tuple(v.values())))
	list_comments=comments(30, list_users, list_vids)
	for c in list_comments:
		print(insert('video_comments', "(video, post_time, comment)", (c["video"], c["post_time"], c["comment"])))
		print(insert('user_comments', "(user, post_time, comment)", (c["user"], c["post_time"], c["comment"])))
	list_followers = followers(40, list_users, list_vids)
	for f in list_followers:
		print(insert('followers', "(video, user)", tuple(f.values())))
	list_ratings = rating(60, list_vids)
	for r in list_ratings:
		print(insert('rating', "(video, id, value)", tuple(r.values())))
	list_events = events(80, list_vids, list_users)
	for e in list_events:
		print(insert('events', "(event, event_time,vid_time,user,video)", tuple(e.values())))

if __name__ == "__main__":
    main()