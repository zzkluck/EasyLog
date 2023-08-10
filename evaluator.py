"""
Description : This file implements the function to evaluation accuracy of log parsing.
              Modified by zzkluck for stand-alone usage, involve only built-in python modules.
Author      : LogPAI team
Modifier    : zzkluck
License     : MIT
"""
import csv
from typing import Tuple, List
from collections import defaultdict, Counter
from math import comb
from pathlib import Path

# when use python version < 3.8, use comb_2(n) instead of math.comb(n, 2)
# def comb_2(n: int): return n * (n - 1) // 2


def evaluateEX(ground_truth_path: Path, parsed_result: List[str],
               output=True, output_detail=True) -> tuple[float, float]:
    """
    Evaluation function to benchmark log parsing accuracy

    :param ground_truth_path: Path, pathlib.Path of ground truth structured csv file
    :param parsed_result: List[str], A list of parsed event Ids
    :param output: Boolean, Indicates whether the function produces output
    :param output_detail: Boolean, Indicates whether the function produces detailed output
    :return: (group_accuracy, template_accuracy)
    """
    invalid_line_id = set()
    ground_truth_event_id = []
    parsed_result_event_id = []

    with ground_truth_path.open('r') as gt_file:
        reader = csv.DictReader(gt_file)
        for i, line in enumerate(reader):
            if line['EventId'] == "":
                invalid_line_id.add(i)
            else:
                ground_truth_event_id.append(line['EventId'])
                parsed_result_event_id.append(parsed_result[i])

    (precision, recall, f_measure, g_accuracy) = get_accuracy(ground_truth_event_id, parsed_result_event_id)
    (yes, tot, t_accuracy) = get_template_accuracy(ground_truth_event_id, parsed_result_event_id)
    if output:
        print(f'GroupAcc: {g_accuracy:.4f}, TemplateAcc: {t_accuracy:.2f} ({yes:3}/{tot:3})')
    if output and output_detail:
        get_detail_accuracy(ground_truth_event_id, parsed_result_event_id)

    return g_accuracy, t_accuracy


def evaluate(ground_truth_file: str, parsed_result_file: str) -> Tuple[float, float]:
    """
    Evaluation function to benchmark log parsing accuracy

    :param ground_truth_file: str, file path of ground truth structured csv file
    :param parsed_result_file: str, file path of parsed structured csv file
    :return: (f_measure, accuracy)
    """
    invalid_line_id = set()
    ground_truth_event_id = []
    parsed_result_event_id = []

    with open(ground_truth_file, 'r') as gt_file:
        reader = csv.DictReader(gt_file)
        for i, line in enumerate(reader):
            if line['EventId'] == "":
                invalid_line_id.add(i)
            else:
                ground_truth_event_id.append(line['EventId'])

    with open(parsed_result_file, 'r') as pr_file:
        reader = csv.DictReader(pr_file)
        for i, line in enumerate(reader):
            if i not in invalid_line_id:
                parsed_result_event_id.append(line['EventId'])

    (precision, recall, f_measure, accuracy) = get_accuracy(ground_truth_event_id, parsed_result_event_id)
    print(f'Precision: {precision:.4f}, Recall: {recall:.4f}, '
          f'F1_measure: {f_measure:.4f}, Parsing_Accuracy: {accuracy:.4f}')
    return f_measure, accuracy


def get_accuracy(ground_truth: List[str], parsed_result: List[str]) -> Tuple[float, float, float, float]:
    """
    Compute accuracy metrics between log parsing results and ground truth

    :param ground_truth:  List[str], A list of ground truth event Ids
    :param parsed_result: List[str], A list of parsed event Ids
    :return: (precision, recall, f_measure, accuracy)
    """
    gt_counter = defaultdict(list)
    for i, eventId in enumerate(ground_truth):
        gt_counter[eventId].append(i)
    real_pairs = sum(comb(len(ids), 2) for ids in gt_counter.values())

    pr_counter = defaultdict(list)
    for i, eventId in enumerate(parsed_result):
        pr_counter[eventId].append(i)
    parsed_pairs = sum(comb(len(ids), 2) for ids in pr_counter.values())
    accurate_pairs = 0
    accurate_events = 0  # determine how many lines are correctly parsed
    for parsed_eventId in pr_counter.keys():
        error_counter = Counter(ground_truth[i] for i in pr_counter[parsed_eventId])
        if len(error_counter) == 1:
            ground_truth_eventId = next(iter(error_counter.keys()))
            if len(gt_counter[ground_truth_eventId]) == len(pr_counter[parsed_eventId]):
                accurate_events += len(pr_counter[parsed_eventId])
        for count in error_counter.values():
            if count > 1:
                accurate_pairs += comb(count, 2)

    precision = float(accurate_pairs) / parsed_pairs
    recall = float(accurate_pairs) / real_pairs
    f_measure = 2 * precision * recall / (precision + recall)
    accuracy = float(accurate_events) / len(ground_truth)
    return precision, recall, f_measure, accuracy


def get_template_accuracy(ground_truth: List[str], parsed_result: List[str]) -> Tuple[float, float, float]:
    """
    Compute accuracy metrics between log parsing results and ground truth

    :param ground_truth:  List[str], A list of ground truth event Ids
    :param parsed_result: List[str], A list of parsed event Ids
    :return: (precision, recall, f_measure, accuracy)
    """
    gt_counter = defaultdict(list)
    for i, eventId in enumerate(ground_truth):
        gt_counter[eventId].append(i)

    pr_counter = defaultdict(list)
    for i, eventId in enumerate(parsed_result):
        pr_counter[eventId].append(i)
    accurate_events = 0  # determine how many lines are correctly parsed
    for parsed_eventId in pr_counter.keys():
        error_counter = Counter(ground_truth[i] for i in pr_counter[parsed_eventId])
        if len(error_counter) == 1:
            ground_truth_eventId = next(iter(error_counter.keys()))
            if len(gt_counter[ground_truth_eventId]) == len(pr_counter[parsed_eventId]):
                accurate_events += 1

    return accurate_events, len(gt_counter), accurate_events/len(gt_counter)


def get_detail_accuracy(ground_truth: List[str], parsed_result: List[str]):
    """
    Compute accuracy metrics between log parsing results and ground truth

    :param ground_truth:  List[str], A list of ground truth event Ids
    :param parsed_result: List[str], A list of parsed event Ids
    :return: (precision, recall, f_measure, accuracy)
    """
    gt_counter = defaultdict(list)
    for i, eventId in enumerate(ground_truth):
        gt_counter[eventId].append(i)

    pr_counter = defaultdict(list)
    for i, eventId in enumerate(parsed_result):
        pr_counter[eventId].append(i)

    for parsed_eventId in pr_counter.keys():
        error_counter = Counter(ground_truth[i] for i in pr_counter[parsed_eventId])
        if len(error_counter) != 1:
            print(parsed_eventId, error_counter, len(pr_counter[parsed_eventId]))

    for gt_eventId in gt_counter.keys():
        error_counter = Counter(parsed_result[i] for i in gt_counter[gt_eventId])
        if len(error_counter) != 1:
            print(error_counter, gt_eventId, len(gt_counter[gt_eventId]))
