FIRE_STATION = 1
def formatting_input():
    test_cases = int(input())
    all_test_cases = []
    
    fire_places = []
    for i in range(test_cases):
        open_paths = []
        fire = int(input())
        fire_places.append(fire)
        street_nos = input()
        while(street_nos != "0 0"):
            start, end = street_nos.split(" ")
            if int(start) < 21 and int(end) < 21:
                open_paths.append([int(start), int(end)])
                open_paths.append([int(end), int(start)])
                street_nos = input()
        all_test_cases.append(open_paths)
    return all_test_cases, fire_places

def mapping_routes(routes):
    mapped_routes = {}
    for start, end in routes:
        if start in mapped_routes:
            mapped_routes[start].append(end)
        else:
            mapped_routes[start] = [end]
    return mapped_routes


def generate_routes(map, start, end, path=[]):
    path = path + [start]
    if start == end:
        return [path]
    if start not in map :
        return[]
    paths = []
    for node in map[start]:
        if node not in path:
            newpaths = generate_routes(map, node, end, path)
            for p in newpaths:
                paths.append(p)
    return sorted(paths)

def format(all_routes):
    for routes in all_routes:
            print(" ".join(map(str, routes)))

test_cases, fire_places = formatting_input()
l = len(test_cases)
for i in range(l):
    print(f"CASE {i + 1}:\n")
    possible_routes = generate_routes(mapping_routes(test_cases[i]), FIRE_STATION, fire_places[i])
    format(possible_routes)
    print(f"There are {len(possible_routes)} routes from the firestation to streetcorner {fire_places[i]}.\n")


