from src.utils import get_executed_operations
from src.classes import Operation


def test_get_executed_operations():
    operations = [
        {
            "state": "EXECUTED",
        },
        {
            "state": "EXECUTED",
        },
        {},
        {
            "state": "FFFFFFFFFFFFFF",
        },
    ]

    expected_operations = [
        {
            "state": "EXECUTED",
        },
        {
            "state": "EXECUTED",
        },
    ]

    assert get_executed_operations(operations) == expected_operations
    assert get_executed_operations([]) == []


def test_operation_instance():
    op = Operation(
        pk=142264268,
        state="EXECUTED",
        date="2019-04-04T23:20:05.206878",
        amount="79114.93",
        currency_name="USD",
        description="Перевод со счета на счет",
        from_="Счет 19708645243227258542",
        to="Счет 75651667383060284188"
    )

    assert op.from_ == "Счет **8542"
    assert op.to == "Счет **4188"
    assert op.convert_payment_date() == "04.04.2019"
    assert str(op) == (
        "04.04.2019 Перевод со счета на счет\n"
        "Счет **8542 -> Счет **4188\n"
        "79114.93 USD\n"
    )
