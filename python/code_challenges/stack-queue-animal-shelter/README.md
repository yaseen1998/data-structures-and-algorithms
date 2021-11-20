# Challenge Summary
<!-- Description of the challenge -->
create class called animelShater and class cat and dog then use dequeue and enqueue for each class
## Whiteboard Process
<!-- Embedded whiteboard image -->
<img src='animel-shelter.png>
## Approach & Efficiency
<!-- What approach did you take? Why? What is the Big O space/time for this approach? -->

## Solution
<!-- Show how to run your code, and examples of it in action -->
soker = Cat('soker')
    animal_shelter = AnimalShelter()
    animal_shelter.EnQueue(soker)
    actual = animal_shelter.frontCat.dataval
    expected = 'soker'
    assert actual == expected
## test
test 1 enqueue one cat
test 2 enqueue two cat
test 3 dequeue two cat
test 4 enqueue one dog
test 5 enqueue two dog
test 6 dequeue two dog
test 7 enqueue cat and dog
test 8 null case
