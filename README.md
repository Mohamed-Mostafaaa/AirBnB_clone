<!-- @format -->

![img](https://assets.imaginablefutures.com/media/images/ALX_Logo.max-200x150.png)

> AirBNB clone Console

![hbnb](./images/hbtn.png)

## Description :house:

AirBnb is a complete web application, integrating database storage,
a back-end API, and front-end interfacing in a clone of AirBnB.

The project currently only implements the back-end console.

## About

This is the First Project towards our AirBnB clone project at [ALX](alxafrica.com). Done by [Mohamed](https://github.com/Mohamed-Mostafaaa) and [Eman](https://github.com/emanelkamel)

This is the first step towards building your first full web application: the AirBnB clone. This first step is very important because you will use what you build during this project with all other following projects: HTML/CSS templating, database storage, API, front-end integration

## General Use

Step 1.
Clone the repository and cd into the repository

Step 2.
Inside the repository, there is a "console.py" file which contains the command line interpreter. Run this command in the terminal to see how it works
"$ python3 console.py"

Step 3.
When this command is run this appears
(hbnb)

Step 4.
Type ? to view all the commands in the interpreter

## Resources

**Read or watch**:

1. [cmd module](https://docs.python.org/3.8/library/cmd.html)
2. [cmd module in depth](http://pymotw.com/2/cmd/)
3. [uuid module](https://docs.python.org/3.8/library/uuid.html)
4. [datetime](https://docs.python.org/3.8/library/datetime.html)
5. [unittest module](https://docs.python.org/3.8/library/unittest.html#module-unittest)
6. [args/kwargs](https://yasoob.me/2013/08/04/args-and-kwargs-in-python-explained/)
7. [python test cheatsheet](https://www.pythonsheets.com/notes/python-tests.html)
8. [cmd module wiki page](https://wiki.python.org/moin/CmdModule)
9. [python unittests](https://realpython.com/python-testing/)

## Classes :cl:

AirBnB utilizes the following classes:

|                                | BaseModel                            | FileStorage                          | User                                                 | State                     | City                      | Amenity                   | Place                                                                                                                                                                      | Review                            |
| ------------------------------ | ------------------------------------ | ------------------------------------ | ---------------------------------------------------- | ------------------------- | ------------------------- | ------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------- |
| **PUBLIC INSTANCE ATTRIBUTES** | `id`<br>`created_at`<br>`updated_at` |                                      | Inherits from `BaseModel`                            | Inherits from `BaseModel` | Inherits from `BaseModel` | Inherits from `BaseModel` | Inherits from `BaseModel`                                                                                                                                                  | Inherits from `BaseModel`         |
| **PUBLIC INSTANCE METHODS**    | `save`<br>`to_dict`                  | `all`<br>`new`<br>`save`<br>`reload` | ""                                                   | ""                        | ""                        | ""                        | ""                                                                                                                                                                         | ""                                |
| **PUBLIC CLASS ATTRIBUTES**    |                                      |                                      | `email`<br>`password`<br>`first_name`<br>`last_name` | `name`                    | `state_id`<br>`name`      | `name`                    | `city_id`<br>`user_id`<br>`name`<br>`description`<br>`number_rooms`<br>`number_bathrooms`<br>`max_guest`<br>`price_by_night`<br>`latitude`<br>`longitude`<br>`amenity_ids` | `place_id`<br>`user_id`<br>`text` |
| **PRIVATE CLASS ATTRIBUTES**   |                                      | `file_path`<br>`objects`             |                                                      |                           |                           |                           |                                                                                                                                                                            |                                   |

## Storage :baggage_claim:

The above classes are handled by the abstracted storage engine defined in the
[FileStorage](./models/engine/file_storage.py) class.

Every time the backend is initialized, AirBnB instantiates an instance of
`FileStorage` called `storage`. The `storage` object is loaded/re-loaded from
any class instances stored in the JSON file `file.json`. As class instances are
created, updated, or deleted, the `storage` object is used to register
corresponding changes in the `file.json`.

## Console :computer:

The console is a command line interpreter that permits management of the backend
of AirBnB. It can be used to handle and manipulate all classes utilized by
the application (achieved by calls on the `storage` object defined above).

### Using the Console

The AirBnB console can be run both interactively and non-interactively.
To run the console in non-interactive mode, pipe any command(s) into an execution
of the file `console.py` at the command line.

```
$ echo "help" | ./console.py
(hbnb)
Documented commands (type help <topic>):
========================================
EOF  all  count  create  destroy  help  quit  show  update

(hbnb)
$
```

Alternatively, to use the AirBnB console in interactive mode, run the
file `console.py` by itself:

```
$ ./console.py
```

While running in interactive mode, the console displays a prompt for input:

```
$ ./console.py
(hbnb)
```

To quit the console, enter the command `quit`, or input an EOF signal
(`ctrl-D`).

```
$ ./console.py
(hbnb) quit
$
```

```
$ ./console.py
(hbnb) EOF
$
```

All tests should also pass in non-interactive mode:` $ echo "python3 -m unittest discover tests" | bash`

![console](./images/console.png)

## Testing :straight_ruler:

Unittests for the AirBnB project are defined in the [tests](./tests)
folder. To run the entire test suite simultaneously, execute the following command:

```
$ python3 unittest -m discover tests
```

Alternatively, you can specify a single test file to run at a time:

```
$ python3 unittest -m tests/test_console.py
```

## Authors :black_nib:

- **Mohamed Mostafa** <[Mohamed-Mostafaaa](https://github.com/Mohamed-Mostafaaa)>
- **Eman Elkamel** <[emanelkamed](https://github.com/emanelkamed)>
