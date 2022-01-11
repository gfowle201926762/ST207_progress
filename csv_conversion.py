# This file manipulates the imported csv files to make them fit the constraints made in the database.
# This is so we don't get an error when inserting the data.



import pandas

Post_Reaction_data = pandas.read_csv("synthetic_data/Follower_data.csv")
#tuples = Post_Reaction_data.loc[:,['user_profile_id', 'follower_id']]



# check if the csv file violates pk constraint where the pk is a composite key of two ids
def pk_constraint():
    inefficient = []
    for row in Post_Reaction_data.itertuples():
        post_id = str(row[1])
        user_profile_id = str(row[2])
        new = post_id + user_profile_id
        inefficient.append(new)

    doubled = []
    for first in inefficient:
        checking = 0
        for check in inefficient:
            if first == check:
                checking += 1
                if checking == 2:
                    print(first)

# check if two ids are the same, for example a User_Profile cannot block themselves
def not_same():
    for row in Post_Reaction_data.itertuples():
        post_id = str(row[1])
        user_profile_id = str(row[2])
        if post_id == user_profile_id:
            print(post_id + user_profile_id)

# unique function for group_members
def group_members():
    Group_Member_data = pandas.read_csv("synthetic_data/Group_Member_data.csv")

    group_member_list = []
    for row in Group_Member_data.itertuples():
        user_profile_id = str(row[1])
        group_id = str(row[2])
        new = group_id + user_profile_id
        group_member_list.append(new)


    Group_data = pandas.read_csv("synthetic_data/Group_data.csv")
    group_list = []
    for row in Group_data.itertuples():
        user_profile_id = str(row[2])
        group_id = str(row[1])
        new = group_id + user_profile_id
        group_list.append(new)


    for row in group_member_list:
        checking = 0
        for check in group_list:
            if row == check:
                checking += 1
                if checking == 1:
                    print(row)


    

group_members()