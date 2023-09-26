from datetime import datetime, timedelta
import pytz


def calculate_times(hours, minutes, timezone):
    try:
        now = datetime.now()
        selected_time = now.replace(
            hour=int(hours), minute=int(minutes), second=0, microsecond=0)

        if 0 <= int(hours) <= 23 and 0 <= int(minutes) <= 59:

            # Menyesuaikan waktu ke zona waktu WITA
            if timezone == "WITA":
                wita_time = selected_time
                wib_time = selected_time - timedelta(hours=1)
                wit_time = selected_time + timedelta(hours=1)

            # Menyesuaikan waktu ke zona waktu WIT
            if timezone == "WIT":
                wit_time = selected_time
                wita_time = wit_time - timedelta(hours=1)
                wib_time = wit_time - timedelta(hours=2)

            # Menyesuaikan waktu ke zona waktu WIB
            if timezone == "WIB":
                wib_time = selected_time
                wita_time = wib_time + timedelta(hours=1)
                wit_time = wib_time + timedelta(hours=2)

            return {"WIB": wib_time.strftime("%Y-%m-%d %H:%M:%S"), "WITA": wita_time.strftime("%Y-%m-%d %H:%M:%S"), "WIT": wit_time.strftime("%Y-%m-%d %H:%M:%S")}
        else:
            return {"WIB": "Jam atau menit tidak valid", "WITA": "Jam atau menit tidak valid", "WIT": "Jam atau menit tidak valid"}
    except ValueError:
        return {"WIB": "Jam atau menit tidak valid", "WITA": "Jam atau menit tidak valid", "WIT": "Jam atau menit tidak valid"}
