#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    tickets_departure = {}
    for i in tickets:
        tickets_departure[i.source] = i

    curr_ticket = tickets_departure["NONE"]

    route = []

    while True:
        route.append(curr_ticket.destination)

        if curr_ticket.destination is "NONE":
            break

        curr_ticket = tickets_departure[curr_ticket.destination]
        print(route)

    return route

