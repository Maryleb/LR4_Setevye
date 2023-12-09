import pandas as pd

def get_booked_rooms(conn, param_1, param_2):
    return pd.read_sql('''
              SELECT type_room_name AS Тип_номера,
              CASE 
                WHEN room_id IS NULL THEN '-'
                ELSE SUM(
                    CASE 
                        WHEN status_name == "Забронирован" THEN 1
                        ELSE 0
                    END)
              END AS Количество,
              
                CASE
                  WHEN COUNT(room_id) == 0 THEN "Не определен"
                  WHEN SUM( CASE 
                        WHEN status_name == "Забронирован" THEN 1
                        ELSE 0
                    END) > :param_2 THEN "Высокий"
                  WHEN SUM( CASE 
                        WHEN status_name == "Забронирован" THEN 1
                        ELSE 0
                    END) < :param_1 THEN "Низкий"
                  ELSE "Средний"
                END AS Спрос
              FROM type_room LEFT OUTER JOIN room USING (type_room_id)
              LEFT OUTER JOIN room_booking USING (room_id)
              LEFT OUTER JOIN status USING (status_id)
              GROUP BY type_room.type_room_id
              ORDER BY Количество DESC, type_room_name
                        ''', conn, params={"param_1": param_1, "param_2": param_2})