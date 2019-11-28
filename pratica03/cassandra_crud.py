from cassandra.cluster import Cluster
import insert_info_cassandra_vidshare as helper

cluster = Cluster()
session = cluster.connect("video_share")

def update(table, attribute,new_value, *conditions):
    command = f"UPDATE {table} SET {attribute} = '{new_value}' WHERE"
    for i in range(len(conditions) - 1):
        command += f" {conditions[i]} AND"
    command += f" {conditions[-1]};"
    print(command)
    return session.execute(command)

def insert(table, attributes, values):
	return session.execute(f"INSERT INTO {table} {attributes} VALUES {values};")

def select(table, attributes, *conditions, filter=False, limit=None, group_by=None, order_by=None):
    command = f"SELECT {attributes} FROM {table}"
    if len(conditions)!=0:
        command += " WHERE"
        for i in conditions[:-1]:
            command += f" {i} AND"
        command += " " + conditions[-1]
    if filter:
        command += " ALLOW FILTER"
    if group_by is not None:
        command += " group by " + group_by
    if order_by is not None:
        command += " order by " + order_by
    if limit is not None:
        command += " limit " + str(limit)
    print(command)
    try:
        return [row for row in session.execute(command + ";")]
    except Exception as e:
        print("Command Select failed")
        raise
    return None

def mass_insert():
    list_users = helper.users(15)
    for u in list_users:
        insert('users', "(username, name, email, register_time)", tuple(u.values()))
    list_vids = helper.video(20, list_users)
    for v in list_vids:
        insert('video', "(name, author, upload_time, description, tags)", tuple(v.values()))
    list_comments= helper.comments(30, list_users, list_vids)
    for c in list_comments:
        insert('video_comments', "(video, post_time, comment)", (c["video"], c["post_time"], c["comment"]))
        insert('user_comments', "(user, post_time, comment)", (c["user"], c["post_time"], c["comment"]))
    list_followers = helper.followers(40, list_users, list_vids)
    for f in list_followers:
        insert('followers', "(video, user)", tuple(f.values()))
    list_ratings = helper.rating(60, list_vids)
    for r in list_ratings:
        insert('rating', "(video, id, value)", tuple(r.values()))
    list_events = helper.events(80, list_vids, list_users)
    for e in list_events:
        insert('events', "(event, event_time,vid_time,user,video)", tuple(e.values()))

def main(initial=False):
    if initial:
        mass_insert()
        update('users', 'username', 'admin0', 'email=\'admin0@cassandra.com\'')
    [print(e) for e in select("video", "*", "author = 'admin13@cassandra.com'")]
    [print(e) for e in select("user_comments", "*", "user = 'admin3@cassandra.com'", order_by="post_time desc")]
    print(select("rating", "avg(value)", group_by="video"))
    print(select("video_comments", "comment", "video='video0'", limit=3))
    ## select * from events where video = 'video3' and user='admin4@cassandra.com' limit 5;
    print(select("events", "*", "video='video9'", "user='admin4@cassandra.com'", limit=3));
if __name__ == "__main__":
    main()
    