goals = {}
def add_goal(goal):
    goals[goal] = {
        "description": "",
        "statut": "Not started"
    }
    print(goals)
add_goal("test")