from stack_queue_animal_shelter import __version__
from stack_queue_animal_shelter.stack_queue_animal_shelter import AnimalShelter,Cat,Dog

def test_enqueue_cat():
    soker = Cat('soker')
    animal_shelter = AnimalShelter()
    animal_shelter.EnQueue(soker)
    actual = animal_shelter.frontCat.dataval
    expected = 'soker'
    assert actual == expected

def test_enqueue_cat2():
    soker = Cat('soker')
    soker2 = Cat('soker2')
    animal_shelter = AnimalShelter()
    animal_shelter.EnQueue(soker)
    animal_shelter.EnQueue(soker2)
    actual = animal_shelter.frontCat.dataval
    expected = 'soker'
    assert actual == expected


def test_dequeue_cat():
    soker = Cat('soker')
    soker2 = Cat('socker2')
    animal_shelter = AnimalShelter()
    animal_shelter.EnQueue(soker)
    animal_shelter.EnQueue(soker2)
    animal_shelter.DeQueue('cat')
    actual = animal_shelter.frontCat.dataval
    expected = 'socker2'
    assert actual == expected

def test_enqueue_dog():
    soker = Dog('soker')
    animal_shelter = AnimalShelter()
    animal_shelter.EnQueue(soker)
    actual = animal_shelter.frontDog.dataval
    expected = 'soker'
    assert actual == expected

def test_enqueue_dog2():
    soker = Dog('soker')
    soker2 = Dog('soker2')
    animal_shelter = AnimalShelter()
    animal_shelter.EnQueue(soker)
    animal_shelter.EnQueue(soker2)
    actual = animal_shelter.frontDog.dataval
    expected = 'soker'
    assert actual == expected


def test_dequeue_dog():
    soker = Dog('soker')
    soker2 = Dog('socker2')
    animal_shelter = AnimalShelter()
    animal_shelter.EnQueue(soker)
    animal_shelter.EnQueue(soker2)
    animal_shelter.DeQueue('dog')
    actual = animal_shelter.frontDog.dataval
    expected = 'socker2'
    assert actual == expected




def test_enqueue_dog_and_cat():
    soker = Cat('soker')
    bull = Dog('bull')
    animal_shelter = AnimalShelter()
    animal_shelter.EnQueue(bull)
    animal_shelter.EnQueue(soker)
    actual1 = animal_shelter.frontDog.dataval
    expected1 = 'bull'
    actual2 = animal_shelter.frontCat.dataval
    expected2 = 'soker'
    assert actual1 == expected1
    assert actual2 == expected2


def test_null_case():
    rock = Dog('rock')
    rox = Cat('rox')
    animal_shelter = AnimalShelter()
    animal_shelter.EnQueue(rox)
    animal_shelter.EnQueue(rock)
    animal_shelter.DeQueue('dog')
    animal_shelter.DeQueue('cat')
    actual = animal_shelter.DeQueue('dog')
    expected = 'null'
    assert actual == expected
