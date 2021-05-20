# UOCIS322 - Project 6 #
Brevet time calculator with AJAX, MongoDB, and a RESTful API!

## What is in this repository

You have a minimal example of `docker-compose` in `DockerRestAPI`, using which you can create RESTful API-based services (as demonstrated in class). 

## IMPORTANT NOTES

**MAKE SURE TO USE THE SOLUTION `acp_times.py` from Canvas for this project!**

**MAKE SURE TO KEEP YOUR FILES in `brevets`! REMOVE `DockerRestAPI` after you're done!**

## Getting started 

You will reuse *your* code from Project 5.

Recall that you created the following functionalities:

1. Add two buttons `Submit` and `Display` in the ACP calculator page.

2. Upon clicking the `Submit` button, the control times should be inserted into a MongoDB database.

3. Upon clicking the `Display` button, the entries from the database should be displayed in a new page.

4. Handle error cases appropriately. For example, `Submit` should return an error if no control times are input. One can imagine many such cases: you'll come up with as many cases as possible.

### Functionality you will add

This project has following four parts. Change the values for host and port according to your machine, and use the web browser to check the results.

* You will design RESTful service to expose what is stored in MongoDB. Specifically, you'll use the boilerplate given in DockerRestAPI folder, and create the following three basic APIs:
    * "http://<host:port>/listAll" should return all open and close times in the database
    * "http://<host:port>/listOpenOnly" should return open times only
    * "http://<host:port>/listCloseOnly" should return close times only

* You will also design two different representations: one in csv and one in json. For the above, JSON should be your default representation for the above three basic APIs. 
    * "http://<host:port>/listAll/csv" should return all open and close times in CSV format
    * "http://<host:port>/listOpenOnly/csv" should return open times only in CSV format
    * "http://<host:port>/listCloseOnly/csv" should return close times only in CSV format

    * "http://<host:port>/listAll/json" should return all open and close times in JSON format
    * "http://<host:port>/listOpenOnly/json" should return open times only in JSON format
    * "http://<host:port>/listCloseOnly/json" should return close times only in JSON format

* You will also add a query parameter to get top "k" open and close times. For examples, see below.

    * "http://<host:port>/listOpenOnly/csv?top=3" should return top 3 open times only (in ascending order) in CSV format 
    * "http://<host:port>/listOpenOnly/json?top=5" should return top 5 open times only (in ascending order) in JSON format
    * "http://<host:port>/listCloseOnly/csv?top=6" should return top 5 close times only (in ascending order) in CSV format
    * "http://<host:port>/listCloseOnly/json?top=4" should return top 4 close times only (in ascending order) in JSON format

* You'll also design consumer programs (e.g., in jQuery) to use the service that you expose. `website` inside `DockerRestAPI` is an example of that. It is uses PHP. You're welcome to use either PHP or jQuery to consume your services. NOTE: your consumer program should be in a different container like example in `DockerRestAPI`.


## Tasks

As always you'll turn in your `credentials.ini` using Canvas, which will point to your repository on GitHub, which should contain:

* The working application with all 4 parts.

* `docker-compose.yml`.

* An updated `README`.

## Grading Rubric

* If your code works as expected: 100 points. This includes:
    * Basic APIs work as expected.
    * Representations work as expected.
    * Query parameter-based APIs work as expected.
    * Consumer program works as expected. 

* For each non-working API, 5 points will be docked off. If none of them work,
  you'll get 35 points assuming
    * `README` is updated with your name, email, and details.
    * `docker-compose.yml` works/builds without any errors.
    * `Dockerfile` is present. 
    * `credentials.ini` is submitted with the correct URL of your repo.

* If the `README` is not clear or missing, 5 points will be docked off. 

* If `Dockerfile` or `docker-compose` is missing, doesn't build or doesn't run, **15** points will be docked off.
	
* If `credentials.ini` is not submitted or the repo is not found, 0 will be assigned.

## Credits

Michal Young, Ram Durairajan, Steven Walton, Joe Istas.
