import random as rand

activities_list = ["Sleeping", "Cooking", "Working on CompSci", "Procrastinating on Homework"]


def rate_my_activity(activities):
    for activity in activities:
        rating = rand.randint(0, 10)
        if rating <= 3:
            print(f"Man! {activity} sucks! I rate it a {rating} out of 10!")
        elif 3 < rating <= 7:
            print(f"Man! {activity} is alright! I rate it a {rating} out of 10!")
        else:
            print(f"Wow! What a great activity, I love {activity}, and rate it {rating} out of 10")


rate_my_activity(activities_list)
