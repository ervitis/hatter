from pytz import timezone
from datetime import datetime

# date time format
fmt_wo_utc = '%Y-%m-%d %H:%M:%S'


def get_horas_minutos_utc(var_utc):
    """
    Get time in json format
    :return: dict
    """

    horas = int(var_utc.utc[1:3])
    minutos = int(var_utc.utc[3:])

    return {
        'horas':    horas,
        'minutos':  minutos,
    }


def set_utc_from_dict(dict_h):
    """
    Get the utc timezone from a dict
    :param dict_h: dict
    :return: string in utc format
    """

    if len(dict_h['horas']) == 1:
        dict_h['horas'] = '0' + dict_h['horas']

    if len(dict_h['minutos']) == 1:
        dict_h['minutos'] = '0' + dict_h['minutos']

    return dict_h['signo'] + dict_h['horas'] + ':' + dict_h['minutos']


def spain_timezone():
    """
    Get the spain timezone
    :return: datetime object
    """

    fecha_actual_utc = datetime.now(timezone('UTC'))

    # Convert to Spain local time
    now_spain = fecha_actual_utc.astimezone(timezone('Europe/Madrid'))

    return now_spain


def get_datetime_utc(time):
    """
    Get the utc time difference
    :param time: string with the time
    :return: dict
    """

    # Separate time and utc
    utc = time[-5:]

    utc = {
        'signo':    utc[:1],
        'horas':    utc[2:3],
        'minutos':  utc[4:],
    }

    date_time = time[:-10]

    return {
        'v_utc':        utc,
        'v_horamin':    datetime.strptime(date_time, fmt_wo_utc),
    }
