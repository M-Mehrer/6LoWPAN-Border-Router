import matplotlib.pyplot as pp
import re

#Min/Max/Average Times of all ping tests
distance = [0.1, 2, 5, 8, 13]
minimum_ble = [52.441, 52.680, 52.416, 52.390, 52.698]
minimum_wlan = [4, 4, 4, 4, 0]
average_ble = [78.959, 90.150, 85.816, 90.128, 137.682]
average_wlan = [10, 10, 10, 11, 0]
maximum_ble = [148.171, 217.012, 198.096, 221.656, 382.838]
maximum_wlan = [102, 71, 108, 165, 0]

# plot comparison of different distances
pp.plot(distance, minimum_ble, label='Minimum BLE', color='b', linestyle='', marker='o')
pp.plot(distance, minimum_wlan, label='Minimum WLAN', color='b', linestyle='', marker='x')
pp.plot(distance, average_ble, label='Durchschnitt BLE', color='g', linestyle='', marker='o')
pp.plot(distance, average_wlan, label='Durchschnitt WLAN', color='g', linestyle='', marker='x')
pp.plot(distance, maximum_ble, label='Maximum BLE', color='r', linestyle='', marker='o')
pp.plot(distance, maximum_wlan, label='Maximum WLAN', color='r', linestyle='', marker='x')

pp.xlabel("Distanz (Meter)")
pp.ylabel("Zeit (ms)")
pp.legend()
pp.title("Latenzen im Vergleich")

pp.show()

# filenames of ping test to extract all times
filenames_ble = ["pingBLE10cm", "pingBLE2m", "pingBLE5m", "pingBLE8m", "pingBLE13m"]
filenames_wlan = ["pingWLAN10cm", "pingWLAN2m", "pingWLAN5m", "pingWLAN8m"]

for i in range(filenames_ble.__len__()):
    f = open("testdata/" + str(filenames_ble[i]) + ".txt", "r")
    file_content = f.read()
    f.close()

    # extract time of individual ping
    times = re.findall("time=\d+\.*\d* ms", file_content)
    times_float = []
    peaks = 0

    for time in times:
        # parse 'time=x.y ms' to x.y float
        time_float = float(re.findall("\d+\.*\d*", time)[0])
        if time_float > average_ble[i] * 1.2:
            peaks += 1
        times_float.append(time_float)

    # plot all times
    pp.plot(range(times_float.__len__()), times_float, linestyle='', marker='o')
    pp.axhline(y=average_ble[i] * 1.2, label='Durchschnitt + 20%', color='r', linestyle='-')
    pp.xlabel("Ping #")
    pp.ylabel("Zeit (ms)")
    pp.title('Latenzverteilung BLE ' + str(distance[i]) + 'm')
    pp.legend()
    pp.show()

    print("Anzahl Ausreißer BLE " + str(distance[i]) + "m (>20% über Durchschnitt): " + str(peaks))

for i in range(filenames_wlan.__len__()):
    f = open("testdata/" + str(filenames_wlan[i]) + ".txt", "r", encoding = "utf-16")
    file_content = f.read()
    f.close()

    # extract time of individual ping
    times = re.findall("Zeit=\d+ms", file_content)
    times_float = []
    peaks = 0

    for time in times:
        # parse 'Zeit=x.yms' to x.y float
        time_float = float(re.findall("\d+", time)[0])
        if time_float > average_wlan[i] * 1.2:
            peaks += 1
        times_float.append(time_float)

    # plot all times
    pp.plot(range(times_float.__len__()), times_float, linestyle='', marker='o')
    pp.axhline(y=average_wlan[i] * 1.2, label='Durchschnitt + 20%', color='r', linestyle='-')
    pp.xlabel("Ping #")
    pp.ylabel("Zeit (ms)")
    pp.title('Latenzverteilung WLAN ' + str(distance[i]) + 'm')
    pp.legend()
    pp.show()

    print("Anzahl Ausreißer WLAN " + str(distance[i]) + "m (>20% über Durchschnitt): " + str(peaks))
