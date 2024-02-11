# AirBnB_console
AirBnB_clone for ALX

# Project README


## User Class:

The `User` class, located in `models/user.py`, inherits from `BaseModel` and represents user data with the following attributes:

- `email`: string - empty string
- `password`: string - empty string
- `first_name`: string - empty string
- `last_name`: string - empty string


## State Class:

The `State` class, located in `models/state.py`, inherits from `BaseModel` and represents a state with the following public class attributes:

- `name`: string - empty string

## City Class:

The `City` class, located in `models/city.py`, inherits from `BaseModel` and represents a city with the following public class attributes:

- `state_id`: string - empty string: it will be the State.id
- `name`: string - empty string

## Amenity Class:

The `Amenity` class, located in `models/amenity.py`, inherits from `BaseModel` and represents an amenity with the following public class attributes:

- `name`: string - empty string

## Place Class:

The `Place` class, located in `models/place.py`, inherits from `BaseModel` and represents a place with the following public class attributes:

- `city_id`: string - empty string: it will be the City.id
- `user_id`: string - empty string: it will be the User.id
- `name`: string - empty string
- `description`: string - empty string
- `number_rooms`: integer - 0
- `number_bathrooms`: integer - 0
- `max_guest`: integer - 0
- `price_by_night`: integer - 0
- `latitude`: float - 0.0
- `longitude`: float - 0.0
- `amenity_ids`: list of string - empty list: it will be the list of Amenity.id later

## Review Class:

The `Review` class, located in `models/review.py`, inherits from `BaseModel` and represents a review with the following public class attributes:

- `place_id`: string - empty string: it will be the Place.id
- `user_id`: string - empty string: it will be the User.id
- `text`: string - empty string

## FileStorage Class:

This class, located in `models/engine/file_storage.py`, provides functionality for serializing instances to a JSON file and deserializing a JSON file to instances.

### Private Class Attributes:

- `__file_path`: string representing the path to the JSON file (e.g., `file.json`)
- `__objects`: dictionary to store all objects by `<class name>.id` (e.g., `BaseModel.12121212`)

### Public Instance Methods:

- `all(self)`: returns the dictionary `__objects`
- `new(self, obj)`: sets in `__objects` the object with key `<obj class name>.id`
- `save(self)`: serializes `__objects` to the JSON file (path: `__file_path`)
- `reload(self)`: deserializes the JSON file to `__objects` (only if the JSON file (`__file_path`) exists; otherwise, does nothing)

## Initialization:

- Update `models/__init__.py` to create a unique `FileStorage` instance for the application.
- Import `file_storage.py`.
- Create the variable `storage`, an instance of `FileStorage`.
- Call the `reload()` method on this variable.

## BaseModel Class:

- Import the variable `storage` from `models`.
- In the `save(self)` method, call the `save(self)` method of `storage`.
- In the `__init__(self, *args, **kwargs)` method, if it’s a new instance (not from a dictionary representation), add a call to the method `new(self)` on `storage`.

## Command Interpreter

This command interpreter, `console.py`, is designed to provide a set of commands for managing instances of different classes in a JSON file. Below are the commands available and their functionalities:

### create:
Creates a new instance of a specified class, saves it to the JSON file, and prints the instance's ID.


### show:
Prints the string representation of an instance based on the class name and ID.


### destroy:
Deletes an instance based on the class name and ID, saving the change into the JSON file.


### all:
Prints all string representations of instances based on the class name or prints all instances if no class name is specified.


### update:
Updates an instance based on the class name and ID by adding or updating an attribute, saving the change into the JSON file.
