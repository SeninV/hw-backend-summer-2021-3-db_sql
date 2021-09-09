# INFO
# Вывести топ 5 самых коротких по длительности перелетов
# В ответе должно быть 2 колонки [flight_no, duration]
TASK_1_QUERY = """
select flight_no,  scheduled_arrival - scheduled_departure as duration FROM flights order by duration asc limit 5
"""
#  flight_no | duration 
# -----------+----------
#  PG0235    | 00:25:00
#  PG0234    | 00:25:00
#  PG0233    | 00:25:00
#  PG0235    | 00:25:00
#  PG0234    | 00:25:00


# INFO
# Вывести топ 3 рейса по числу упоминаний в таблице flights
# количество упоминаний которых меньше 50
# В ответе должно быть 2 колонки [flight_no, count]
TASK_2_QUERY = """
select flight_no, COUNT(1) as count from flights group by flight_no having count(1) < 50 order by count(1) desc limit 3
"""
#  flight_no | count 
# -----------+-------
#  PG0260    |    27
#  PG0371    |    27
#  PG0310    |    27

# INFO
# Вывести число перелетов внутри одной таймзоны 
# Нузно вывести 1 значение в колонке count
TASK_3_QUERY = """
select count(1) from flights
left join airports_data as a1 on flights.departure_airport = a1.airport_code
left join airports_data  on flights.arrival_airport = airports_data.airport_code
where a1.timezone = airports_data.timezone
"""
#  count  
# --------
#  16824

