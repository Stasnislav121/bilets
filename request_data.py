import requests
import json


class Sapsan:
    city_dep = str
    city_arr = str
    day = str
    mounth = str
    name = str
    url = 'https://ticket.rzd.ru/apib2b/p/Railway/V1/Search/TrainPricing?service_provider=B2B_RZD'
    result_str = str
    counter = 0
    headers = {
      'Accept': 'application/json, text/plain, */*',
      'Accept-Language': 'ru,en;q=0.9',
      'Cache-Control': 'no-cache',
      'Connection': 'keep-alive',
      'Content-Type': 'application/json',
      'Cookie': '_ym_uid=1698702116426645021; _ym_d=1698702116; uwyii=51ea59ad-39a1-3d80-ab1a-dcc33b8029c8; acceptCookies=1; session-cookie=179fdf3ab7df06f9731c6c5b80267f938eb700abda3577e2708b39fdf51119059ccfa22673460b61f801196227442da9; accessible=false; _ym_isad=2; _ym_visorc=b; LANG_SITE=ru; oxxfgh=dcad9c19-0698-469d-ac6f-0eb5621ade38%230%2386400000%235000%231800000%2322900; uwyiert=9ac20eb2-085f-121f-1a09-661da69c2922; LANG_SITE=ru; session-cookie=179fe0b44de58bc7731c6c5b18991a24e5a8475b9db4aff28e9fc4571827eba89f602645d0fb41c8269e56f41cc64d32',
      'Origin': 'https://ticket.rzd.ru',
      'Pragma': 'no-cache',
      'Referer': 'https://ticket.rzd.ru/searchresults/v/1/5a3244bc340c7441a0a556ca/5a323c29340c7441a0a556bb/2024-02-17',
      'Sec-Fetch-Dest': 'empty',
      'Sec-Fetch-Mode': 'cors',
      'Sec-Fetch-Site': 'same-origin',
      'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.5993.731 YaBrowser/23.11.1.731 Yowser/2.5 Safari/537.36',
      'sec-ch-ua': '"Chromium";v="118", "YaBrowser";v="23", "Not=A?Brand";v="99"',
      'sec-ch-ua-mobile': '?0',
      'sec-ch-ua-platform': '"Windows"',
      'sentry-trace': 'a89052c4dbcf4e3c81bd6e6c8f8f761a-a4747c6b729caa29-1'
    }


    def __init__(self, city_dep, city_arr, day, mounth):
      self.city_dep = city_dep
      self.city_arr = city_arr
      self.day = day
      self.mounth = mounth
      self.name = f'{day}_{mounth}'


    def do_data(self):
        data = """
            {
                "Origin": """ + self.city_dep + """,
                "Destination": """ + self.city_arr + """,
                "DepartureDate": "2024-"""+self.mounth+"""-"""+self.day+""" T 00:00:00",
                "TimeFrom": 0,
                "TimeTo": 24,
                "CarGrouping": "DontGroup",
                "GetByLocalTime": true,
                "SpecialPlacesDemand": "StandardPlacesAndForDisabledPersons",
                "CarIssuingType": "PassengersAndBaggage"
            }
            """
        return data

    def request(self):
      try:
        response = requests.request(method="post", url=self.url, data=self.do_data(),
                                    headers=self.headers)
      except ConnectionError:
        response = requests.request(method="post", url=self.url, data=self.do_data(),
                                    headers=self.headers)

      response_json = json.loads(response.text)
      train = response_json['Trains']

      arr_sapsans = []
      result = [self.name]

      for el in range(len(train)):
        if train[el]["TrainName"] == "САПСАН":
          arr_sapsans.append(train[el])

      for el in range(len(arr_sapsans)):
        # if arr_sapsans[el]["LocalDepartureDateTime"] <= '2024-02-17T15:10:00':
        classes_sapsan = arr_sapsans[el]["CarGroups"]
        for clas in range(len(classes_sapsan)):
          if ((classes_sapsan[clas]["ServiceClassNameEn"] == "Economy+") or (
                  classes_sapsan[clas]["ServiceClassNameEn"] == "Family") or (classes_sapsan[clas]["ServiceClassNameEn"] == "Economy")) and (
                  classes_sapsan[clas]["TotalPlaceQuantity"] > 2):
                self.counter += 1
                result.append(
                  f'{self.counter}) {classes_sapsan[clas]["ServiceClassNameEn"]}Plus, Seats:{classes_sapsan[clas]["TotalPlaceQuantity"]},'
                  f'Dep: {arr_sapsans[el]["LocalDepartureDateTime"]}')

      if len(result) == 1:
        result.append(f"Don't have seats")

      result_str='\n'.join(result)
      return result_str




