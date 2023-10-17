"""Air traffic planning."""


def update_delayed_flight(
    schedule: dict[str, tuple[str, str]],
    delayed_flight_number: str,
    new_departure_time: str
) -> dict[str, tuple[str, str]]:
    """
    Update the departure time of a delayed flight in the flight schedule.

    Return a dictionary where the time of the specified flight is modified.
    This means that the result dictionary should not contain the old time,
    instead a new departure time points to the specified flight.
    The input schedule cannot be changed.

    :param schedule: Dictionary of flights ({time string: (destination, flight number)})
    :param delayed_flight_number: Flight number of the delayed flight
    :param new_departure_time: New departure time for the delayed flight
    :return: Updated flight schedule with the delayed flight's departure time changed
    """
    updated_flight = {}

    for time, flight in schedule.items():
        if delayed_flight_number == flight[1]:
            updated_flight[new_departure_time] = flight
        else:
            updated_flight[time] = flight

    return updated_flight


def cancel_flight(schedule: dict[str, tuple[str, str]], cancelled_flight_number: str) -> dict[str, tuple[str, str]]:
    """
    Create a new schedule where the specified flight is cancelled.

    The function cannot modify the existing schedule parameter.
    Instead, create a new dictionary where the cancelled flight is not added.

    :param schedule: Dictionary of flights ({time: (destination, flight number)})
    :param cancelled_flight_number: Flight number of the cancelled flight
    :return: New flight schedule with the cancelled flight removed
    """
    updated_schedule = {}

    for time, flight in schedule.items():
        if cancelled_flight_number == flight[1]:
            continue
        else:
            updated_schedule[time] = flight

    return updated_schedule


def busiest_time(schedule: dict[str, tuple[str, str]]) -> list[str]:
    """
    Find the busiest hour(s) at the airport based on the flight schedule.

    Finds the busiest hour(s) at the airport based on the flight schedule. The busiest hour(s)
    is/are determined by counting the number of flights departing in each hour of the day.
    All flights departing with the same hour in their departure time, are counted into the same hour.

    The function returns a list of strings of the busiest hours, sorted in ascending order, such as ["08", "21"].

    :param schedule: Dictionary containing the flight schedule, where keys are departure times
                     in the format "HH:mm" and values are tuples containing destination and flight number.
    :return: List of strings representing the busiest hour(s) in 24-hour format, such as ["08", "21"].
    """
    counted_hours = {}
    busy_time = []
    count = 0

    for time in schedule:
        hours = time.split(":")[0]
        minutes = time.split(":")[1]

        if hours in counted_hours:
            counted_hours[hours].append(minutes)
        else:
            counted_hours[hours] = [minutes]

    for hour, minute in counted_hours.items():
        if len(minute) > count:
            busy_time.clear()
            busy_time.append(hour)
            count = len(minute)
        elif len(minute) == count:
            busy_time.append(hour)

    return busy_time


def connecting_flights(schedule: dict[str, tuple[str, str]], arrival: tuple[str, str]) -> list[tuple[str, str]]:
    """
    Find connecting flights based on the provided arrival information and flight schedule.

    The function takes a flight schedule and the arrival time and location of a flight,
    and returns a list of available connecting flights. A connecting flight is considered
    available if its departure time is at least 45 minutes after the arrival time, but less
    than 4 hours after the arrival time. Additionally, a connecting flight must not go back
    to the same place the arriving flight came from.

    :param schedule: Dictionary containing the flight schedule, where keys are departure
                     times in the format "HH:mm" and values are tuples containing
                     destination and flight number. For example:
                     {
                         "14:00": ("Paris", "FL123"),
                         "15:00": ("Berlin", "FL456")
                     }

    :param arrival: Tuple containing the arrival time and the location the flight is
                    arriving from. For example:
                    ("11:05", "Tallinn")

    :return: A list of tuples containing the departure time and destination of the
             available connecting flights, sorted by departure time. For example:
             [
                 ("14:00", "Paris"),
                 ("15:00", "Berlin")
             ]
             If no connecting flights are available, the function returns an empty list.
    """
    arrival_time = arrival[0].split(":")
    arrival_time_in_minutes = int(arrival_time[0]) * 60 + int(arrival_time[1])
    first_flight = arrival_time_in_minutes + 45
    last_flight = arrival_time_in_minutes + 240
    connecting_flights = []

    for time, flight in schedule.items():
        flight_time = int(time.split(":")[0]) * 60 + int(time.split(":")[1])
        if first_flight <= flight_time < last_flight:
            if flight[0] != arrival[1]:
                connecting_flights.append((time, flight[0]))

    return connecting_flights


def busiest_hour(schedule: dict[str, tuple[str, str]]) -> list[str]:
    """
    Find the busiest hour-long slot(s) in the schedule.

    One hour slot duration is 60 minutes (or the diff of two times is less than 60).
    So, 15:00 and 16:00 are not in the same slot.

    :param schedule: Dictionary containing the flight schedule, where keys are departure
                     times in the format "HH:mm" and values are tuples containing
                     destination and flight number. For example:
                     {
                         "14:00": ("Paris", "FL123"),
                         "15:00": ("Berlin", "FL456")
                     }

    :return: A list of strings representing the starting time(s) of the busiest hour-long
             slot(s) in ascending order. For example:
             ["08:00", "15:20"]
             If the schedule is empty, returns an empty list.
    """
    schedule_times = {}
    returning_list = []

    for time1, flight1 in schedule.items():
        flight_time1 = int(time1.split(":")[0]) * 60 + int(time1.split(":")[1])
        for time2, flight2 in schedule.items():
            if flight1[1] != flight2[1]:
                time2_in_minutes = int(time2.split(":")[0]) * 60 + int(time2.split(":")[1])
                if flight_time1 < time2_in_minutes < flight_time1 + 60:
                    if time1 not in schedule_times:
                        schedule_times[time1] = 1
                    else:
                        schedule_times[time1] += 1

    sorted_schedule_times = dict(sorted(schedule_times.items(), key=lambda x: x[1], reverse=True))

    for time in sorted_schedule_times:
        returning_list.append(time)

    return returning_list


def most_popular_destination(schedule: dict[str, tuple[str, str]], passenger_count: dict[str, int]) -> str:
    """
    Find the destination where the most passengers are going.

    :param schedule: A dictionary representing the flight schedule.
                     The keys are departure times and the values are tuples
                     containing destination and flight number.
    :param passenger_count: A dictionary with flight numbers as keys and
                            the number of passengers as values.
    :return: A string representing the most popular destination.
    """
    counted_passenger_dict = {}

    for plane, passenger in passenger_count.items():
        for flight in schedule.values():
            if plane == flight[1]:
                if flight[0] in counted_passenger_dict:
                    counted_passenger_dict[flight[0]] += passenger
                else:
                    counted_passenger_dict[flight[0]] = passenger

    sorted_destination = list(sorted(counted_passenger_dict.items(), key=lambda x: x[1], reverse=True))
    popular_destination = sorted_destination[0][0]

    return popular_destination


def least_popular_destination(schedule: dict[str, tuple[str, str]], passenger_count: dict[str, int]) -> str:
    """
    Find the destination where the fewest passengers are going.

    :param schedule: A dictionary representing the flight schedule.
                     The keys are departure times and the values are tuples
                     containing destination and flight number.
    :param passenger_count: A dictionary with flight numbers as keys and
                            the number of passengers as values.
    :return: A string representing the least popular destination.
    """
    counted_passenger_dict = {}

    for plane, passenger in passenger_count.items():
        for flight in schedule.values():
            if plane == flight[1]:
                if flight[0] in counted_passenger_dict:
                    counted_passenger_dict[flight[0]] += passenger
                else:
                    counted_passenger_dict[flight[0]] = passenger

    sorted_destination = list(sorted(counted_passenger_dict.items(), key=lambda x: x[1]))
    least_popular_destination = sorted_destination[0][0]

    return least_popular_destination


if __name__ == '__main__':
    schedule = {
        "06:15": ("Tallinn", "OWL6754"),
        "11:35": ("Helsinki", "BHM2345")
    }
    new_schedule = update_delayed_flight(schedule, "OWL6754", "09:00")
    print(schedule)
    # {'06:15': ('Tallinn', 'OWL6754'), '11:35': ('Helsinki', 'BHM2345')}
    print(new_schedule)
    # {'09:00': ('Tallinn', 'OWL6754'), '11:35': ('Helsinki', 'BHM2345')}

    new_schedule = cancel_flight(schedule, "OWL6754")
    print(schedule)
    # {'06:15': ('Tallinn', 'OWL6754'), '11:35': ('Helsinki', 'BHM2345')}
    print(new_schedule)
    # {'11:35': ('Helsinki', 'BHM2345')}

    schedule = {
        "04:35": ("Maardu", "MWL6754"),
        "06:15": ("Tallinn", "OWL6754"),
        "06:30": ("Paris", "OWL6751"),
        "07:29": ("London", "OWL6756"),
        "08:00": ("New York", "OWL6759"),
        "11:30": ("Tokyo", "OWL6752"),
        "11:35": ("Helsinki", "BHM2345"),
        "19:35": ("Paris", "BHM2346"),
        "20:35": ("Helsinki", "BHM2347"),
        "22:35": ("Tallinn", "TLN1001"),
    }
    print(busiest_time(schedule))
    # ['06', '11']

    print(connecting_flights(schedule, ("04:00", "Tallinn")))
    # [('06:30', 'Paris'), ('07:29', 'London')]

    print(busiest_hour(schedule))
    # ['06:15', '06:30', '07:29', '11:30']
    # 19:35 does not match because 20:35 is not in the same slot

    # flight number: number of passengers
    passengers = {
        "MWL6754": 100,
        "OWL6754": 85,
        "OWL6751": 103,
        "OWL6756": 87,
        "OWL6759": 118,
        "OWL6752": 90,
        "BHM2345": 111,
        "BHM2346": 102,
        "BHM2347": 94,
        "TLN1001": 1
    }
    print(most_popular_destination(schedule, passengers))
    # Paris

    print(least_popular_destination(schedule, passengers))
    # Tallinn
