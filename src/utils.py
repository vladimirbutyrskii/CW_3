import json
from pathlib import Path
from src.classes import Operation


def load_json(path: Path):    #   -> list[dict]
    """
    Загрузка данных об операциях из json-файла
    :param path:
    :return:
    """
    with open(path, encoding='utf-8') as f:
        return json.load(f)


def get_executed_operations(operations):    #   : list[dict]) -> list[dict]
    """
    Получение операций EXECUTED
    :param operations:
    :return:
    """
    return [
        operation
        for operation in operations
        if operation.get("state") == "EXECUTED"
    ]


def get_operation_instances(operations):      # : list[dict]) -> list[Operation]
    """
    Получение экземпляров класса Operation
    :param operations:
    :return:
    """
    operation_instances = []
    for operation in operations:
        operation_amount = operation["operationAmount"]
        op = Operation(
            date=operation["date"],
            pk=operation["id"],
            state=operation["state"],
            amount=operation_amount["amount"],
            currency_name=operation_amount["currency"]["name"],
            description=operation["description"],
            to=operation["to"],
            from_=operation.get("from"),
        )
        operation_instances.append(op)

    return operation_instances


def sort_operations_by_date(operations):     # list[Operation]) -> list[Operation]:
    """

    :param operations:
    :return:
    """
    return sorted(operations,  reverse=True)

