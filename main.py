import sys
from functions import compare_results, forward, backward, get_data


def main(data, start, end, color):
    lanes = data['lineas']
    optimum = 1000000  # Numero suficientemente grande para que se registren rutas optimas
    result = [start]
    best = False
    counter = 0
    for lane_num in range(len(lanes)):
        if start in lanes[lane_num]:
            origin_lane = lanes[lane_num]
            for station_num in range(len(origin_lane)):
                if origin_lane[station_num] == start:
                    if station_num == 0:  # partimos del inicio
                        best = forward(lane_num, station_num, origin_lane, result,
                                       data, lanes, start, end, color, counter, optimum, best)
                    elif station_num == (len(origin_lane)-1):  # partimos del medio
                        best = backward(lane_num, station_num, origin_lane, result,
                                        data, lanes, start, end, color, counter, optimum, best)
                    else:  # partimos del final
                        best = forward(lane_num, station_num, origin_lane, result,
                                       data, lanes, start, end, color, counter, optimum, best)
                        best = backward(lane_num, station_num, origin_lane, result,
                                        data, lanes, start, end, color, counter, optimum, best)
    return best


if __name__ == "__main__":
    data = get_data(sys.argv)
    if data:
        start = sys.argv[2]
        end = sys.argv[3]
        color = False
        if len(sys.argv) == 5:
            color = sys.argv[4]
        r = main(data, start, end, color)
        print("Mejor ruta: {}".format(r))
