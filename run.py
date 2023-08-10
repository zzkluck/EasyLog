import csv
from pathlib import Path

from settings import parse_settings
from easylog import parse_lines
from evaluator import evaluateEX

default_running_settings = {
    'enable_time_parse': True,
    'enable_specific_key': True,
    'enable_regex_substitute': True,
    'enable_regex_split': True,
    'parse_result_output': True,
    'parse_detail_output': False,
    'exclude_dataset': {'Total'},
    'specific_dataset': {},
    'origin_data_type': 'csv',
    'log_data_dir': './logs'
}


def run_benchmark(running_settings):
    log_data_dir = Path(running_settings["log_data_dir"])
    log_dataset_types = [t.name for t in log_data_dir.glob("*") if t.is_dir()]

    benchmark_result = []
    for log_type in log_dataset_types:
        if log_type in running_settings['exclude_dataset']: continue
        if running_settings['specific_dataset'] and log_type not in running_settings['specific_dataset']: continue
        if running_settings['parse_result_output']: print(f"{log_type:12}", end='')

        raw_log_file = log_data_dir / log_type / f"{log_type}_2k.log"
        structured_log_file = log_data_dir / log_type / f"{log_type}_2k.log_structured.csv"

        if (data_type := running_settings['origin_data_type']) == 'raw':
            all_log_lines = raw_log_file.read_text().strip().split('\n')
        elif data_type == 'csv':
            running_settings['enable_time_parse'] = False
            all_log_lines = []
            with structured_log_file.open('r') as f:
                reader = csv.DictReader(f)
                for line in reader:
                    all_log_lines.append(line['Content'])
        else:
            all_log_lines = []

        res, _, _ = parse_lines(all_log_lines, parse_settings[log_type],
                                enable_time_parse=running_settings['enable_time_parse'],
                                enable_specific_key=running_settings['enable_specific_key'],
                                enable_regex_substitute=running_settings['enable_regex_substitute'],
                                enable_regex_split=running_settings['enable_regex_split'])

        g_accuracy, t_accuracy = \
            evaluateEX(structured_log_file, res,
                       output=running_settings['parse_result_output'],
                       output_detail=running_settings['parse_detail_output'])
        benchmark_result.append((g_accuracy, t_accuracy))
    return benchmark_result


if __name__ == '__main__':
    run_benchmark(default_running_settings)
