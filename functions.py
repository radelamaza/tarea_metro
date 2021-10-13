import json


def get_data(argv):
    if len(argv) < 4:
        print("No se reciben los suficientes parámetros")
    else:
        try:
            f = open(argv[1])
            return json.load(f)
        except:
            print("El archivo no existe o no es formato JSON")
            exit()


def compare_results(current, best):
    if best:
        if len(best) > len(current):
            best = current

    else:
        best = current
    return best


def forward(lane_num, station, lane, current, data, lanes, start, end, color, counter, optimum, best):
    if color and [x for x in data[color] if x in lane]:
        if lane[station+1] not in data[color] and lane[station+1] != lane[-1]:
            return forward(lane_num, station+1, lane, current, data, lanes, start, end, color, counter, optimum, best)

    current = current.copy()
    counter += 1
    if counter < optimum:

        if lane[station+1] == end:
            current.append(lane[station+1])
            best = compare_results(current, best)
            optimum = len(best)
        elif (lane[station+1] == start or (lane[station+1] in current)):
            pass
        else:
            current.append(lane[station+1])
            if len(lane) == (station+2):
                for x in range(len(lanes)):
                    if lane[station+1] in lanes[x]:
                        if lane[station+1] == lanes[x][0]:
                            best = forward(
                                x, 0, lanes[x], current, data, lanes, start, end, color, counter, optimum, best)
                        else:
                            best = backward(x, len(
                                lanes[x])-1, lanes[x], current, data, lanes, start, end, color, counter, optimum, best)
            else:
                best = forward(lane_num, station+1, lane, current, data,
                               lanes, start, end, color, counter, optimum, best)
    return best


def backward(lane_num, station, lane, current, data, lanes, start, end, color, counter, optimum, best):
    if color and [x for x in data[color] if x in lane]:
        if lane[station-1] not in data[color] and lane[station-1] != lane[0]:
            return backward(lane_num, station-1, lane, current, data, lanes, start, end, color, counter, optimum, best)
    current = current.copy()
    counter += 1
    if counter < optimum:
        if lane[station-1] == end:
            current.append(lane[station-1])
            best = compare_results(current, best)
            optimum = len(best)
        elif (lane[station-1] == start or (lane[station-1] in current)):
            pass
        else:
            current.append(lane[station-1])
            if (station-2) < 0:
                for x in range(len(lanes)):
                    if lane[station-1] in lanes[x]:
                        if lane[station-1] == lanes[x][0]:
                            best = forward(
                                x, 0, lanes[x], current, data, lanes, start, end, color, counter, optimum, best)
                        else:
                            best = backward(x, len(
                                lanes[x])-1, lanes[x], current, data, lanes, start, end, color, counter, optimum, best)

            else:
                best = backward(lane_num, station-1, lane, current, data,
                                lanes, start, end, color, counter, optimum, best)
    return best
