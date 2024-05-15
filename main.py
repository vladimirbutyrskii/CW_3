from settings import OPERATION_PATH, OPERATIONS_COUNT
from src.utils import load_json, get_executed_operations, get_operation_instances, sort_operations_by_date

operations = load_json(OPERATION_PATH)
executed_operations = get_executed_operations(operations)
operation_instances = get_operation_instances(executed_operations)
sort_operations = sort_operations_by_date(operation_instances)
for op in sort_operations[:OPERATIONS_COUNT]:
    print(op)

