import datetime


class Operation:
    """
    Класс Operation
    """

    def __init__(
            self,
            pk: int,
            state: str,
            date: str,
            amount: str,
            currency_name: str,
            description: str,
            to: str,
            from_: str = None
    ):
        self.pk = pk
        self.state = state
        self.date = date
        self.amount = amount
        self.currency_name = currency_name
        self.description = description
        self.from_ = self.covert_payment_data(from_) if from_ is not None else ""
        self.to = self.covert_payment_data(to)

    def covert_payment_data(self, payment_data: str) -> str:
        """
        Маскирование номеров счета и платежной карты
        :param self:
        :param payment_data:
        :return:
        """
        cov_num = ""
        card_name = ""
        if payment_data.startswith('Счет'):
            for i in range(len(payment_data)-4, len(payment_data)):
                cov_num += payment_data[i]
                # print(cov_num)
            return f"Счет **{cov_num}"
            # return f"{payment_data} **"
        else:
            for i in range(0, len(payment_data)):
                if payment_data[i].isalpha() or payment_data[i] == " ":
                    card_name += payment_data[i]
                else:
                    cov_num += payment_data[i]

        # cov_num = self.covert_card(cov_num)
        return f"{card_name}{self.covert_card(cov_num)}"

        # return f"{payment_data} ****"


    def covert_card(self, card_data: str) -> str:
        """
        Маскирование номера платежной карты
        :param card_data:
        :return:
        """
        new_num = ""
        for i in range(0, len(card_data)):
            if i not in [3, 7, 11, 15]:
                new_num += card_data[i] if i not in [6, 7, 8, 9, 10, 11] else "*"
            else:
                new_num += card_data[i] if i not in [6, 7, 8, 9, 10, 11] else "*"
                new_num += " "

        return f"{new_num[:len(card_data)+3]}"


    def convert_payment_date(self) -> str:
        """
        Конвертирование даты в формат дд.мм.гггг
        :param self:
        :return:
        """
        iso_date = datetime.datetime.fromisoformat(self.date)
        return iso_date.strftime("%d.%m.%Y")

    def __lt__(self, other):
        """

        :param other:
        :return:
        """
        return self.date < other.date

    def __gt__(self, other):
        """

        :param other:
        :return:
        """
        return self.date > other.date

    def __str__(self):
        """

        :return:
        """
        # return f"{self.__dict__}"
        date = self.convert_payment_date()

        out_str = f"{date} {self.description}\n"
        if self.from_ != "":
            out_str += f"{self.from_} -> {self.to}\n"
        else:
            out_str += f"{self.to}\n"
        out_str += f"{self.amount} {self.currency_name}\n"

        return out_str

