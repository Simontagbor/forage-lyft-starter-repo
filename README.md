# Lyft Backend Software Engineer Job Simulation Program

## Task 1 - Backend Business Logic Re-Design

I inherited a convoluted inheritance hierarchy and messy codebase from the previous engineer, the task was to leverage scalable and maintainable patterns to come up with a new design for the business logic. After gathering enough details about the goals of this simple project, I used the following patterns to come up with a new design:

- **Inheritance and Composition**: I used inheritance to create a base class for the different types of vehicles and then used composition to create a class that would handle the different types of vehicles. The inheritance pattern is a method of creating a base class that can be extended by other classes. This pattern allows the creation of a base class that can be extended by other classes. learn more here: [Inheritance and Composition](https://refactoring.guru/design-patterns/strategy)

- **Factory Pattern**: I used the factory pattern to create a class that would handle the creation of the different types of vehicles. The factory pattern is a method of creating an interface for creating objects. This pattern allows the creation of objects to be independent of the client that uses them. learn more here: [Factory Pattern](https://refactoring.guru/design-patterns/factory-method)

- **Strategy pattern**: I used the strategy pattern to create a class that would handle the different types of vehicles. The Strategy pattern is a method of creating an interface for a family of algorithms. This pattern allows the algorithms to be interchangeable and independent of the client that uses them. learn more here: [Strategy Pattern](https://refactoring.guru/design-patterns/strategy)

## Before and After

### Before Redesign
![Current Design - LYFT Rental Fleet logistics System Component drawio (1)](https://github.com/Simontagbor/forage-lyft-starter-repo/assets/62922135/d01e815d-adfb-4f80-bb58-262fed483e47)

### After Redesign
![Updated Design - LYFT Rental Fleet logistics System Component (1)](https://github.com/Simontagbor/forage-lyft-starter-repo/assets/62922135/688433b2-60e7-474a-8414-38e28c0dfd70)


## Task 2 - Refactor and Optimize Codebase

I refactored the codebase based on the new design to make it more maintainable and scalable.
The new codebase has the following updates:

- **New Directory Structure**: I restructured the codebase to make it more organized and maintainable.
The new directory structure is as follows:

```bash
├── root
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
|   ├── security
|   |   |── __init__.py
|   |   ├── input_validator.py
```

The new structure is based on the re-designed codebase in Task 1. The new structure is more organized and maintainable.
Based on the `Factory Method Pattern`, We will not need to create new models to represent new fleets of cars. We can simply create a new class that inherits from the base class and implement the methods that are specific to the new fleet of cars. we will no longer need the `/engine/models/` directory where these specialized car models were defined.

The new structure also includes:

- a `battery` directory to define battery components for car objects.

- a `security` directory to define input validation for creating components and cars.

- removal of the `engine/model` directory.

- updated all modules inside the `engine` directory to reflect the new design.

- updated the `car.py` module to reflect the new design.

- added the `car_factory.py` module to leverage the factory method and strategy design patterns.

- added the `serviceable.py` module to define the base class for the different types of vehicles.

## Task 3 - Write Unittests
