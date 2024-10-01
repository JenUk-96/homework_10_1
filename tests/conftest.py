list_of_dict_all_states_canceled = [
    {"id": 41428829, "state": "CANCELED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 939719570, "state": "CANCELED", "date": "2018-06-30T02:08:58.425572"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
]

list_of_dict_sorted_1 = [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
]

list_of_dict_sorted_2 = [
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
]

list_of_dict_without_state = [
    {"id": 41428829, "date": "2019-07-03T18:35:29.512364"},
    {"id": 939719570, "date": "2018-06-30T02:08:58.425572"},
    {"id": 594226727, "date": "2018-09-12T21:27:25.241689"},
    {"id": 615064591, "date": "2018-10-14T08:21:33.419441"},
]

list_of_dict_sort_res_true = [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
]

list_of_dict_sort_res_false = [
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
]

list_of_dict_ident_dates_sort = [
    {"id": 10243698, "state": "EXECUTED", "date": "2020-10-10T10:10:10.0"},
    {"id": 96563213, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    {"id": 87458965, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 36982147, "state": "EXECUTED", "date": "2000-11-12T12:12:12.0"},
    {"id": 52148965, "state": "EXECUTED", "date": "1998-06-19T04:00:05.12"},
]
