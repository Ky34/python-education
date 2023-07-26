# 1.

def route_info(route):
    if route.get('distance') and type(route['distance']) is int:
        return f"Distance to your destination is {route['distance']}"
    elif (route.get('speed') and
          route.get('time') and
          type(route['speed']) is int and
            (type(route['time']) is int or float)):
        return f"Distance to your destination is {route['speed'] * route['time']}"
    return "No distace info is available"


print(route_info({'Brand': 'Volvo'}))
print(route_info({'distance': 100}))
print(route_info({'speed': 100, 'time': 1.5}))


def route_info(route):
    if ('distance' in route) and (type(route['distance']) == int):
        return f"Distance to your destination is {route['distance']}"
    if ('speed' in route) and ('time' in route):
        return f"Distance to your destination is {route['speed'] * route['time']}"
    return "No distace info is available"


print(route_info({'distance': 15}))
print(route_info({'speed': 20, 'time': 3}))
print(route_info({'my_speed': 30}))
