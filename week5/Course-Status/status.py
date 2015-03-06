def status_count(students):

    students_dict = {}
    finalized = []
    not_finalized = []
    
    for student in students:

        if student["status"] == "finalized":
            finalized = finalized + [student["name"]]

        else:
            not_finalized = not_finalized + [student["name"]]

    students_dict = {"finalized" : finalized,
                     "not_finalized" : not_finalized}
    
    return  students_dict

        
