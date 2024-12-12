import logging
from unittest import TestCase
from for_log_12_4 import Runner

class runner_test(TestCase):
    def test_walk(self):
        try:
            # tester = Runner(5, 5)  # не строка в имени
            # tester = Runner('qwerty', -5) # отрицательная скорость
            tester = Runner("qwerty")
            for _ in range(10):
                tester.walk()
            self.assertEqual(tester.distance, 50)
            logging.info('"test_walk" выполнен успешно')
        except ValueError:
            logging.error("Неверная скорость для Runner", exc_info=True)
        except TypeError:
            logging.error("Не правильный тип данных", exc_info=True)

    def test_run(self):
        try:
            # tester = Runner(5, 5)  # не строка в имени
            tester = Runner("30", -5) # отрицательная скорость
            # tester = Runner('qwerty', 5)
            for _ in range(10):
                tester.run()
            self.assertEqual(tester.distance, 100)
            logging.info('"test_run" выполнен успешно')
        except ValueError:
            logging.error("Неверная скорость для Runner" , exc_info= True)
        except TypeError:
            logging.error("Неправильный тип данных ", exc_info=True)


# if __name__ == '__main__':
    logging.basicConfig(
        level= logging.DEBUG,
        filemode= "w",
        filename= 'runner_test.log',
        format= " %(asctime)s | %(levelname)s | %(message)s",
        encoding= "utf-8")
    logging.debug("AAAAAAAAAAAAAAAA", )
