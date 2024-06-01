import test_send_tg
from request_data import Sapsan





def test_june_14():
     obj = Sapsan(city_dep="2004000", city_arr="2000000", day="14", mounth="06")
     test_send_tg.send_tg(obj.request())

def test_june_15():
     obj = Sapsan(city_dep="2004000", city_arr="2000000", day="15", mounth="06")
     test_send_tg.send_tg(obj.request())

def test_june_16():
     obj = Sapsan(city_dep="2004000", city_arr="2000000", day="16", mounth="06")
     test_send_tg.send_tg(obj.request())


def test_search_seats_from():
    test_june_14()
    test_june_15()
    test_june_16()
