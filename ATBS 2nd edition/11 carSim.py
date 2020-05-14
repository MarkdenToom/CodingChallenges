# test assert statements for debugging

market_2nd = {'ns': 'green', 'ew': 'red'}  # state of lights on the intersection market street and 2nd street
mission_16th = {'ns': 'red', 'ew': 'green'}


def switch_lights(stoplight):
    for key in stoplight.keys():
        if stoplight[key] == 'green':
            stoplight[key] = 'yellow'
        if stoplight[key] == 'yellow':
            stoplight[key] = 'red'
        if stoplight[key] == 'red':
            stoplight[key] = 'green'
    assert 'red' in stoplight.values(), 'Neither light is red! ' + str(stoplight)


try:
    switch_lights(market_2nd)  # this will make it so that there's an orange and a green light on at once. Not good.
except AssertionError as err:
    print('An exception occured: ' + str(err))  # bad practice using print for errors
