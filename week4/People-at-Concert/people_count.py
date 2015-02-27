def get_people_count(activity):

    people_count = 0
    people = []

    for person in activity:
        if person not in people:
            people = people + [person]

    people_count = len(people)

    return people_count
    
