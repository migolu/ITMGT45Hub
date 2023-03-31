'''Module 4: Individual Programming Assignment 1

Parsing Data

This assignment covers your ability to manipulate data in Python.
'''

def relationship_status(from_member, to_member, social_graph):
    '''Relationship Status.
    15 points.

    Let us pretend that you are building a new app.
    Your app supports social media functionality, which means that users can have
    relationships with other users.

    There are two guidelines for describing relationships on this social media app:
    1. Any user can follow any other user.
    2. If two users follow each other, they are considered friends.

    This function describes the relationship that two users have with each other.

    Please see "assignment-4-sample-data.py" for sample data. The social graph
    will adhere to the same pattern.

    Parameters
    ----------
    from_member: str
        the subject member
    to_member: str
        the object member
    social_graph: dict
        the relationship data    

    Returns
    -------
    str
        "follower" if fromMember follows toMember,
        "followed by" if fromMember is followed by toMember,
        "friends" if fromMember and toMember follow each other,
        "no relationship" if neither fromMember nor toMember follow each other.
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.

#SAMPLE DATA
social_graph = {
    "@bongolpoc":{"first_name":"Joselito",
                  "last_name":"Olpoc",
                  "following":[
                  ]
    },
    "@joaquin":  {"first_name":"Joaquin",
                  "last_name":"Gonzales",
                  "following":[
                      "@chums","@jobenilagan"
                  ]
    },
    "@chums" : {"first_name":"Matthew",
                "last_name":"Uy",
                "following":[
                    "@bongolpoc","@miketan","@rudyang","@joeilagan"
                ]
    },
    "@jobenilagan":{"first_name":"Joben",
                   "last_name":"Ilagan",
                   "following":[
                    "@eeebeee","@joeilagan","@chums","@joaquin"
                   ]
    },
    "@joeilagan":{"first_name":"Joe",
                  "last_name":"Ilagan",
                  "following":[
                    "@eeebeee","@jobenilagan","@chums"
                  ]
    },
    "@eeebeee":  {"first_name":"Elizabeth",
                  "last_name":"Ilagan",
                  "following":[
                    "@jobenilagan","@joeilagan"
                  ]
    },
}

# CODE CELL
#from_member = string // to_member = string // social_graph = dictionary

#for testing purposes: "@chums", "@joeilagan" should be friends // "@bongolpoc", "@chums" should be followed by
def relationship_status (from_member, to_member, social_graph):
    #follower (if from_member follows to_member)
    if to_member in social_graph[from_member]["following"] and from_member not in social_graph[to_member]["following"] :
        return ("follower")
    #followed by (if to_member follows from_member)
    elif from_member in social_graph[to_member]["following"] and to_member not in social_graph[from_member]["following"]:
        return("followed by")
    #friends (if from_member and to_member follow each other)
    elif to_member in social_graph[from_member]["following"] and from_member in social_graph[to_member]["following"]:
        return("friends")
    #none
    else:
        return None
    
relationship_status ("@eeebeee", "@chums", social_graph)




def tic_tac_toe(board):
    '''Tic Tac Toe. 
    15 points.

    Tic Tac Toe is a common paper-and-pencil game. 
    Players must attempt to successfully draw a straight line of their symbol across a grid.
    The player that does this first is considered the winner.

    This function evaluates a tic tac toe board and returns the winner.

    Please see "assignment-4-sample-data.py" for sample data. The board will adhere
    to the same pattern. The board may by 3x3, 4x4, 5x5, or 6x6. The board will never
    have more than one winner. The board will only ever have 2 unique symbols at the same time.

    Parameters
    ----------
    board: list
        the representation of the tic-tac-toe board as a square list of lists

    Returns
    -------
    str
        the symbol of the winner or "NO WINNER" if there is no winner
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.

# Tic-Tac-Toe Sample Data

board1 = [
['X','X','O'],
['O','X','O'],
['O','','X'],
]

board2 = [
['X','X','O'],
['O','X','O'],
['','O','X'],
]

board3 = [
['O','X','O'],
['','O','X'],
['X','X','O'],
]

board4 = [
['X','X','X'],
['O','X','O'],
['O','','O'],
]

board5 = [
['X','X','O'],
['O','X','O'],
['X','','O'],
]

board6 = [
['X','X','O'],
['O','X','O'],
['X','',''],
]

board7 = [
['X','X','O',''],
['O','X','O','O'],
['X','','','O'],
['O','X','','']
]

# CODE CELL
#board == list
#Have to check if there is winner horizontal, vertical, diagonal 
#for testing purposes: board 1,2,3 = up-down diagonal // board 4 = horizontal row // board 5 = vertical column // board 6 = no winner

def tic_tac_toe (board):
    
    for i in range(0, len(board)):
        horizontal = board[i]
        vertical = list(zip(*board))
        #check horizontal rows (Xs and Os)
        if (all([s=="X" for s in horizontal])) == True:
            return ("X")
        elif (all([s=="O" for s in horizontal])) == True:
            return ("O")

        #check vertical columns (Xs and Os) 

        elif (all([s=="X" for s in vertical[i]])) == True:
            return ("X")
        elif (all([s=="O" for s in vertical[i]])) == True:
            return ("O")

    
    #check up-down diagonal (Xs and Os)
    updown_diagonal= ([board[i][i] for i,v in enumerate(board)])
    downup_diagonal= ([board[len(board)-1-i][i] for i,v in enumerate(board)])
    #check if X wins using all()
    if (all([s=="X" for s in updown_diagonal])) == True:
        return ("X")
    #check if O wins
    elif (all([s=="O" for s in updown_diagonal])) == True:
        return ("O")
    #check down-up diagonal (Xs and Os)
    #check if Xs using all()
    elif (all([s=="X" for s in downup_diagonal])) == True:
        return ("X")
    #check if O wins
    elif (all([s=="O" for s in downup_diagonal])) == True:
        return ("O")  
    else:
        return None

    
tic_tac_toe(board6)


#ETA
def eta(first_stop, second_stop, route_map):
    '''ETA. 
    20 points.

    A shuttle van service is tasked to travel along a predefined circlar route.
    This route is divided into several legs between stops.
    The route is one-way only, and it is fully connected to itself.

    This function returns how long it will take the shuttle to arrive at a stop
    after leaving another stop.

    Please see the sample data file in this same folder for sample data. The route map will
    adhere to the same pattern. The route map may contain more legs and more stops,
    but it will always be one-way and fully enclosed.

    Parameters
    ----------
    first_stop: str
        the stop that the shuttle will leave
    second_stop: str
        the stop that the shuttle will arrive at
    route_map: dict
        the data describing the routes

    Returns
    -------
    int
        the time it will take the shuttle to travel from first_stop to second_stop
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    
    #Sample Data
    legs = {
     ("upd","admu"):{
         "travel_time_mins":10
     },
     ("admu","dlsu"):{
         "travel_time_mins":35
     },
     ("dlsu","upd"):{
         "travel_time_mins":55
     }
}

legs = {
    ('a1', 'a2'): {
        'travel_time_mins': 10
    },
    ('a2', 'b1'): {
        'travel_time_mins': 10230
    },
    ('b1', 'a1'): {
        'travel_time_mins': 1
    }
}

# CODE CELL
#legs = dictionary, source = string, destination = string
def eta (legs, source, destination):    
    order = [i for i in legs.keys()]
    k = {}
    v = {}
    
    
    t = 0
    begin = 0
    end = 0
    last = 0
    
    for a,b in legs:
        k[a] = b
        v[b] = a
        
    result = sum([i["travel_time_mins"] for i in legs.values()])
    
    begin = (order.index((source, k[source])))
    end = order.index((v[destination], destination))
    
    if(source,k[source]) == (source,destination):
        return legs[source,destination]["travel_time_mins"]
    
    else:
        if begin < end:
            for c in range(begin, end+1):
                last += (legs[order[c]]["travel_time_mins"])
        elif end < begin:
            for c in range(end + 1, begin):
                t += (legs[order[c]]["travel_time_mins"])
                last = result - t
        return last
            
eta(legs,"dlsu","admu")