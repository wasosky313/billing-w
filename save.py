    @staticmethod
    def future_date_post_fixed():
        today = datetime.today()

        if today.day == 15:
            # Para los meses con 30 días, generar boletos para el día 30
            if today.month in [4, 6, 9, 11]:
                return datetime(today.year, today.month, 30)

            # Para los meses con 31 días, generar boletos para los días 30 y 31
            if today.month in [1, 3, 5, 7, 8, 10, 12]:
                return datetime(today.year, today.month, 31)

            # Para febrero, generar boletos para el último día del mes (28 o 29)
            if today.month == 2:
                return datetime(today.year, today.month + 1, 1) - timedelta(days=1)

        if today.day == 16:
            if today.month == 12:
                return datetime(today.year + 1, 1, 1)
            return datetime(today.year, today.month + 1, 1)

        return today + timedelta(days=15)


# Unittests

class TestFutureDatePostFixed(unittest.TestCase):
    @freeze_time("2023-04-15")
    def test_future_date_post_fixed_30_day_month(self):
        """
        The 15th day of the month has 30 days (april)
        result: future_date = 2023-04-30
        """
        future_date = DateHelper().future_date_post_fixed()
        self.assertEqual(future_date, datetime(2023, 4, 30))
        self.assertNotEquals(future_date, datetime(2023, 5, 1))

    @freeze_time("2023-01-15")
    def test_future_date_post_fixed_31_day_month(self):
        """
        The 15th day of the month has 31 days (january)
        result: future_date = 2023-05-31
        """
        future_date = DateHelper().future_date_post_fixed()
        self.assertEqual(future_date, datetime(2023, 1, 31))
        self.assertNotEquals(future_date, datetime(2023, 1, 30))
        self.assertNotEquals(future_date, datetime(2023, 2, 1))

    @freeze_time("2023-02-15")
    def test_future_date_post_fixed_february_28(self):
        """
        The 15th day of the february 28 days
        result: future_date = 2023-02-28
        """
        future_date = DateHelper().future_date_post_fixed()
        self.assertEqual(future_date, datetime(2023, 2, 28))
        self.assertNotEquals(future_date, datetime(2023, 3, 1))

    @freeze_time("2020-02-15")
    def test_future_date_post_fixed_february_29(self):
        """
        The 15th day of the february 28 days
        result: future_date = 2023-02-28
        """
        future_date = DateHelper().future_date_post_fixed()
        self.assertEqual(future_date, datetime(2020, 2, 29))
        self.assertNotEquals(future_date, datetime(2020, 2, 28))

    @freeze_time("2023-04-16")
    def test_future_date_post_fixed_30_day_month(self):
        """
        The 16th day of the month has 30 days (april)
        result: future_date = 2023-05-01
        """
        future_date = DateHelper().future_date_post_fixed()
        self.assertEqual(future_date, datetime(2023, 5, 1))
        self.assertNotEquals(future_date, datetime(2023, 6, 1))

    @freeze_time("2023-01-16")
    def test_future_date_post_fixed_31_day_month(self):
        """
        The 16th day of the month has 31 days (january)
        result: future_date = 2023-02-01
        """
        future_date = DateHelper().future_date_post_fixed()
        self.assertEqual(future_date, datetime(2023, 2, 1))
        self.assertNotEquals(future_date, datetime(2023, 2, 2))

    @freeze_time("2023-12-16")
    def test_future_date_post_fixed_december(self):
        """
        The 16th day of the december
        result: future_date = 2024-01-01
        """
        future_date = DateHelper().future_date_post_fixed()
        self.assertEqual(future_date, datetime(2024, 1, 1))
        self.assertNotEquals(future_date, datetime(2023, 1, 1))

    @freeze_time("2023-02-17")
    def test_future_date_post_fixed_31_day_month17(self):
        """
        The 17th day of the february
        result: future_date = 2023-03-04 (vai pular 3 dias acho melhor o dia 16 pegar a partir do 2 e 17 do 4)
        """
        future_date = DateHelper().future_date_post_fixed()
        self.assertEqual(future_date, datetime(2023, 3, 4))

    # TODO testar com o resto dos dias do mes
    @freeze_time("2023-01-01")
    def test_future_date_post_fixed_31_day_month17(self):
        """
        The 17th day of the february
        result: future_date = 2023-03-04
        """
        future_date = DateHelper().future_date_post_fixed()
        self.assertEqual(future_date, datetime(2023, 1, 16))

