import random


def test_smoke():
    print("fire?")


def test_rg1():
    random.seed(1)
    result = []
    for i in range(20):
        result += [round(random.random(), 2)]
    assert result == [
        0.13, 0.85, 0.76, 0.26, 0.5, 0.45, 0.65, 0.79, 0.09, 0.03, 0.84,
        0.43, 0.76, 0.0, 0.45, 0.72, 0.23, 0.95, 0.9, 0.03
    ]


def test_rg2():
    random.seed(1)
    result = []
    for i in range(20):
        result += [round(random.random(), 2)]
    assert result == [
        0.13, 0.85, 0.76, 0.26, 0.5, 0.45, 0.65, 0.79, 0.09, 0.03,
        0.84, 0.43, 0.76, 0.0, 0.45, 0.72, 0.23, 0.95, 0.9, 0.03
    ]


def test_rg3():
    random.seed(1)
    result = []
    for i in range(20):
        result += [round(random.uniform(1, 100), 2)]
    assert result == [
        14.3, 84.9, 76.61, 26.25, 50.05, 45.5, 65.51, 79.08, 10.29, 3.81,
        83.74, 43.84, 76.47, 1.21, 45.09, 72.43, 23.65, 94.58, 90.24, 4.03
    ]


def test_rg4():
    random.seed(1)
    result = []
    for i in range(20):
        result += [round(random.randint(-100, 100), 2)]
    assert result == [-66, 45, 95, -84, -35, -70, 26, 94, 15, 20, 66, -3, -47, -76, 24, -93, -1, 10, 55, 95]


def test_rg5():
    random.seed(1)
    result = []
    for i in range(20):
        result += [random.randrange(0, 100, 5)]
    assert result == [20, 90, 10, 40, 15, 75, 70, 75, 60, 30, 15, 75, 0, 60, 65, 95, 0, 70, 40, 35]


def test_rg6():
    random.seed(1)
    CitiesList = [
        'Rome', 'New York', 'London', 'Berlin', 'Moskov', 'Los Angeles', 'Paris', 'Madrid', 'Tokio', 'Toronto'
    ]
    result = []
    for i in range(10):
        CitiesItem = random.choice(CitiesList)
        result += [CitiesItem]
    assert result == [
        'London', 'Toronto', 'New York', 'Moskov', 'New York', 'Madrid', 'Madrid', 'Madrid', 'Paris', 'Berlin'
    ]


def test_rg7():
    random.seed(1)
    DataList = range(10, 100, 10)
    print("Initial Data List = ", DataList)
    DataSample = random.sample(DataList, k=5)
    assert DataSample == [30, 20, 90, 10, 40]
