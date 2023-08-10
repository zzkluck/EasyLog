import re, string
from typing import List, Dict, Tuple, Any
from collections import defaultdict
from datetime import datetime

date_alias = {'JAN', 'FEB', 'MAR', 'APR', 'MAY', 'JUN', 'JUL', 'AUG', 'SEP', 'OCT', 'NOV', 'DEC',
              'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN',
              'PDT', 'UTC'}


def is_variable(token: str) -> bool:
    return token == '' or \
        token[0] == '<' or \
        (len(token) == 1 and token[0] in string.punctuation) or \
        any(char.isdigit() for char in token) or \
        all('a' <= c.lower() <= 'f' or c.isdigit() for c in token) or \
        token.upper() in date_alias


def parse_time(logline: str, time_regex: str, time_format: str):
    match = re.search(time_regex, logline)
    if match:
        data_str = match.group(1)
        if time_format == '%UNIX_TIMESTAMP':
            date_obj = datetime.utcfromtimestamp(int(data_str))
        else:
            date_obj = datetime.strptime(match.group(1), time_format)
        logline = re.sub(time_regex, '<DATETIME>', logline)
        return date_obj, logline
    else:
        return None, logline


def parse_lines(log_lines: List[str],
                settings: Dict[str, Any],
                enable_time_parse=True,
                enable_specific_key=True,
                enable_regex_substitute=True,
                enable_regex_split=True,
                ):
    parse_result: List[str] = []
    key_id_map: Dict[Tuple, int] = {}
    cluster: Dict[Tuple, List] = defaultdict(list)

    for line in log_lines:
        specific_keys = []

        if enable_time_parse:
            log_date, line = parse_time(line, settings['time_regex'], settings['time_format'])

        if enable_specific_key:
            for currentSpec in settings['specific']:
                specific_keys.extend(re.findall(currentSpec, line))

        if enable_regex_substitute:
            for i, (currentRex, replace) in enumerate(settings['substitute_regex'].items()):
                if 'replace_once' in settings and i in settings['replace_once']:
                    line = re.sub(currentRex, replace, line, count=1)
                else:
                    line = re.sub(currentRex, replace, line)

        if enable_regex_split:
            for currentRex, replace in settings['split_regex'].items():
                line = re.sub(currentRex, replace, line)

        tokens = [str(token) for token in line.strip().split() if token != ""]

        log_key = (
            *(token for token in tokens if not is_variable(token)),
            *specific_keys
        )

        if log_key not in key_id_map:
            key_id_map[log_key] = len(key_id_map)
        parse_result.append(f'E{key_id_map[log_key]}')
        cluster[log_key].append(line)

    return parse_result, key_id_map, cluster
