<section>
<div class="herosection">
<h1>What I learned as a Junior Backend Software Engineer at Lyft. - A Forage Job Simulation Experience</h1>
</div>
</section>

## Introduction

> I took a job simulation as a junior backend software engineer at Lyft on [Forage](https://www.theforage.com/virtual-experience/xSw9echtixLAoPdsH/lyft/back-end-engineering-he82/). The goal was straight forward: redesign the existing backend business logic of Lyft's Rental Fleet logistics system and refactor the codebase to make it more maintainable and scalable. I also wrote extensive unittests and implemented new features for the rental fleet logistics System.
<section class="intro-section"> 
<div id="myModal" class="modal">
<div class="modal-content">
<span class="close">&times;</span>
<h1>
Executive Summary
</h1>
<p>I successfully redesigned the backend business logic for the fleet management system, refactored and optimized the codebase, wrote extensive unittests, and implemented new tire servicing criteria. The new codebase is more maintainable and scalable and has a <a href="#">test coverage</a> of 99%. I also learned a lot about design patterns, TDD, and unittesting techniques.</p>
</div>
</div>
</section>
## Situation

I inherited a codebase from a previous Engineer who started working on a new system responsible for managing the servicing and maintenance of different types of vehicles in LYFT's rental fleet. The previous engineer who worked on the project had to be assigned to another project.

The current structure of the codebase is not scalable and maintainable. The codebase is not organized and the inheritance hierarchy is convoluted. Servicing and maintenance criteria may change frequently as the system evolves, so the codebase needs to be refactored to make it more maintainable and scalable. Furthermore, the codebase lacks unittests with extensive coverage.

## Tasks

For this project, I completed the following tasks:

- [x] Task 1: Re-designed backend Business Logic for Fleet Management System.
- [x] Task 2: Refactored and Optimized Codebase
- [x] Task 3: Wrote Extensive Unittests
- [x] Task 4: Implement a New Tire Servicing Criteria.

### Task 1 - Backend Business Logic Re-Design

After gathering enough details about the goals of the fleet management system and familiarising myself with the inherited codebase and project, I looked into design patterns that could help in designing a more scalable and maintainable codebase.

I relied on the following patterns to come up with a new design:

- **Inheritance and Composition**: I used inheritance to create a base class for the different types of vehicles and then used composition to create a class that would handle the different types of vehicles. The inheritance pattern is a method of creating a base class that can be extended by other classes. This pattern allows the creation of a base class that can be extended by other classes. learn more here: [Inheritance and Composition](https://refactoring.guru/design-patterns/strategy)

- **Factory Pattern**: I used the factory pattern to create a class that would handle the creation of the different types of vehicles. The factory pattern is a method of creating an interface for creating objects. This pattern allows the creation of objects to be independent of the client that uses them. learn more here: [Factory Pattern](https://refactoring.guru/design-patterns/factory-method)

- **Strategy pattern**: I used the strategy pattern to create a class that would handle the different types of vehicles. The Strategy pattern is a method of creating an interface for a family of algorithms. This pattern allows the algorithms to be interchangeable and independent of the client that uses them. learn more here: [Strategy Pattern](https://refactoring.guru/design-patterns/strategy)



#### Before Redesign

![Current Design - LYFT Rental Fleet logistics System Component drawio (1)](https://github.com/Simontagbor/forage-lyft-starter-repo/assets/62922135/d01e815d-adfb-4f80-bb58-262fed483e47)

#### After Redesign

![Updated Design - LYFT Rental Fleet logistics System Component (1)](https://github.com/Simontagbor/forage-lyft-starter-repo/assets/62922135/688433b2-60e7-474a-8414-38e28c0dfd70)

### Task 2 - Refactor and Optimize Codebase

I refactored the codebase based on the new design to make it more maintainable and scalable.
The new codebase has the following updates:

- **New Directory Structure**: I restructured the codebase to make it more organized and maintainable.
The new directory structure is as follows:

```bash
├── .
│   ├── serviceable.py
│   ├── car.py
│   ├── car_factory.py
│   ├── .gitingore
│   ├── README.md
|   ├── battery
|   |   |── __init__.py
|   |   ├── base_battery.py
|   |   ├── spindler_battery.py
|   |   ├── nubbin_battery.py
|   ├── engine
|   |   |── __init__.py
|   |   ├── base_engine.py
|   |   ├── capulet_engine.py
|   |   ├── wiloughby_engine.py
|   |   |── sternman_engine.py
|   ├── test
|   |   ├── __init__.py
|   |   ├── test_car.py
|   ├── utils
|   |   |── __init__.py
|   |   ├── input_validator.py
```

The new structure is based on the re-designed codebase in Task 1. The new structure is more organized and maintainable.
Based on the [`Factory Method Pattern`](https://refactoring.guru/design-patterns/factory-method), We will not need to create new models to represent new fleets of cars. We can simply create a new class that inherits from the base class and implement the methods that are specific to the new fleet of cars. we will no longer need the `/engine/models/` directory where these specialized car models were defined.

The new structure also includes:

- a `battery` directory to define battery components for car objects.

- a `utils` directory to define input validation and other helper functions for creating components and cars.

- removal of the `engine/model` directory.

- updated all modules inside the `engine` directory to reflect the new design.

- updated the `car.py` module to reflect the new design.

- added the `car_factory.py` module to leverage the factory method and strategy design patterns.

- added the `serviceable.py` module to define the base class for the different types of vehicles.

### Task 3 - Write Unittests

I wrote unittests to test the new codebase. The unittests are located in the `test` directory. The unittests cover the following:

- Test the creation of different types of vehicles.
- Test the creation of different types of engines.
- Test the creation of different types of batteries.
- Test that the Car class is correctly implemented.
- Test that the Base Engine and Base Battery classes are correctly implemented.
- Test that the derived classes from the Base Engine and Base Battery classes are correctly implemented.
- Test the input validation for creating components and cars.

#### Testing Approach

I mostly wrote standard unittests, however I used `@patch`decorator to mock the creation of different types of vehicles, engines, and batteries using the `Factory Method Pattern`- Implemented Via `car_factory.py` module.
This is to ensure that the tests are independent of the client that uses them.

Mocking the creation of objects allows me to focus on testing the functionality of the code in isolation, without relying on the specific details of the instantiated objects.

#### Test Coverage

In total, the code coverage is about 98% and all tests 71 tests passed. The only module not tested is the `serviceable.py` which is an interface for serviceable objects like cars. I can safely assume that the interface is correctly implemented since all the derived classes from the interface are acting as expected.

```bash

python3 -m unittest -v
```

![Screenshot 2024-02-27 121019](https://github.com/Simontagbor/forage-lyft-starter-repo/assets/62922135/4a077316-d855-40f9-a8ed-cca219856b99)

### Task 4 - Implement New Tire Servicing Criteria
Now that the codebase is more maintainable and scalable, I implemented a new tire servicing criteria. However I used the Test-Driven Development (TDD) approach to implement the new tire servicing criteria.

#### Test-Driven Development (TDD) Approach

[Test-Driven Development (TDD)](http://www.jamesshore.com/v2/books/aoad1/test_driven_development) is a software development process that relies on the repetition of a very short development cycle: first, the developer writes an (initially failing) automated test case that defines a desired improvement or new function, then produces the minimum amount of code to pass that test, and finally refactors the new code to acceptable standards.

##### My Steps

- 1. update the `test_car.py` module to include a new test case for the new tire servicing criteria.
- 2. Add new tests for tire objects and tire servicing criteria.
- 3. Run the tests to ensure that the new tests fail.
- 4. Implement the new tire servicing criteria in the `car.py` module. by ensuring that the car class has tire attributesImplement tire-related classes and tire servicing criteria in the `tire` directory.
- 5. Run the tests to ensure that the new tests pass.

###### Test Results
![image of test coverage report](<Screenshot 2024-03-09 210813.png>)

see full test coverage report [here]()

#### Final Structure of Codebase

```bash
├── .
│   ├── serviceable.py
│   ├── car.py
│   ├── car_factory.py
│   ├── .gitingore
│   ├── README.md
|   ├── battery
|   |   |── __init__.py
|   |   ├── base_battery.py
|   |   ├── spindler_battery.py
|   |   ├── nubbin_battery.py
|   ├── engine
|   |   |── __init__.py
|   |   ├── base_engine.py
|   |   ├── capulet_engine.py
|   |   ├── wiloughby_engine.py
|   |   |── sternman_engine.py
|   ├── tire
|   |   |── __init__.py
|   |   ├── base_tire.py
|   |   ├── carrigan_tire.py
|   |   ├── octo_prime_tire.py
|   ├── test
|   |   ├── __init__.py
|   |   ├── test_battery
|   |   |   ├── test_battery.py
|   |   ├── test_car
|   |   |   ├── __init__.py
|   |   |   ├── test_car.py
|   |   |   ├── test_car_factory.py
|   |   ├── test_engine
|   |   |   ├── __init__.py
|   |   |   ├── test_engine.py
|   |   ├── test_tire
|   |   |   ├── __init__.py
|   |   |   ├── test_tire.py
|   |   ├── test_utils
|   |   |   ├── __init__.py
|   |   |   ├── test_input_validator.py
|   ├── utils
|   |   |── __init__.py
|   |   ├── input_validator.py
```

### Key Learning Outcomes

I enjoyed working on this project and learned a lot about the following:

1. **Design Patterns**: I learned about different design patterns such as the Factory Method Pattern and Strategy Pattern. I learned how to use these patterns to create a more scalable and maintainable codebase. I will always have it in mind that different design patterns can be used to solve different problems and understanding the problem domain is key to choosing the right design pattern.

2. **Test-Driven Development (TDD)**: having known about the concept for a while, I finally got to use it in my workflow as a developer. I saw firsthand that TDD is a great way to ensure that the code is working as expected and to catch bugs early in the development process.

3. Unit Testing: I reinforced my understanding of unittesting techniques and I am now committed to writing extensive unit tests in future projects. I also learned how to use the `@patch` decorator from the `unittest` module to mock the creation of objects. I also discovered a neat way to measure the coverage of tests inside the codebase using the `coverage` package.

