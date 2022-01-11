# ASSIGNMENT 2
# hotel database application




##########################
# IMPORTING SQLITE3 LIBRARY AND ESTABLISHING CONNECTION
##########################

# importing sqlite3 library
import sqlite3

# importing pandas library for better viewing of SQL queries
import pandas

# creating a connection to the database
conn = sqlite3.connect(':memory:')

# opening a cursor to the database
cursor = conn.cursor()








##########################
# CREATING TABLES
##########################


# This enables the foreign key constraint to actually work in practice
cursor.execute('pragma foreign_keys=ON;')



# CUSTOMERS
cursor.executescript(
    """
    CREATE TABLE customers (
        id INTEGER NOT NULL, 
        first_name VARCHAR(30) NOT NULL, 
        last_name VARCHAR(30) NOT NULL, 
        gender VARCHAR(30) NOT NULL, 
        email VARCHAR(30) NOT NULL, 
        phone INTEGER NOT NULL, 
        PRIMARY KEY (id)
    );
    """
)

# HOTELS
cursor.executescript(
    """
    CREATE TABLE hotels (
        id INTEGER NOT NULL, 
        name VARCHAR(30) NOT NULL, 
        street_address VARCHAR(30) NOT NULL, 
        city VARCHAR(30) NOT NULL, 
        postcode VARCHAR(30) NOT NULL, 
        max_capacity INTEGER NOT NULL, 
        CHECK (max_capacity > 0),
        PRIMARY KEY (id)
    );
    """
)

# EMPLOYEES
cursor.executescript(
    """
    CREATE TABLE employees (
        id INTEGER NOT NULL, 
        first_name VARCHAR(30) NOT NULL, 
        last_name VARCHAR(30) NOT NULL, 
        gender VARCHAR(30) NOT NULL, 
        dob DATE NOT NULL, 
        email VARCHAR(30) NOT NULL, 
        phone INTEGER NOT NULL, 
        role VARCHAR(30) NOT NULL, 
        salary INTEGER NOT NULL, 
        hotel_id INTEGER NOT NULL, 
        CHECK(role IN ('manager', 'cook', 'cleaner', 'waiter', 'bellboy', 'doorman', 'electrician', 'accountant')),
        CHECK (salary > 0),
        PRIMARY KEY (id), 
        FOREIGN KEY(hotel_id) REFERENCES hotels (id)
    );
    """
)

# BOOKINGS
cursor.executescript(
    """
    CREATE TABLE bookings (
        id INTEGER NOT NULL, 
        start_date DATETIME NOT NULL, 
        end_date DATETIME NOT NULL, 
        room_no INTEGER NOT NULL, 
        hotel_id INTEGER NOT NULL, 
        lead_guest_id INTEGER NOT NULL, 
        no_of_guests INTEGER NOT NULL, 
        PRIMARY KEY (id), 
        CHECK (end_date > start_date), 
        CHECK (no_of_guests > 0),
        FOREIGN KEY(hotel_id) REFERENCES hotels (id), 
        FOREIGN KEY(lead_guest_id) REFERENCES customers (id)
    );
    """
)

# CHECKINS
cursor.executescript(
    """
    CREATE TABLE checkins (
        check_in_time DATETIME NOT NULL, 
        booking_id INTEGER NOT NULL, 
        PRIMARY KEY (booking_id), 
        FOREIGN KEY(booking_id) REFERENCES bookings (id)
    );
    """
)

# CHECKOUTS
cursor.executescript(
    """
    CREATE TABLE checkouts (
        checkout_time DATETIME NOT NULL, 
        rating FLOAT, 
        review VARCHAR, 
        booking_id INTEGER NOT NULL, 
        PRIMARY KEY (booking_id), 
        CHECK (rating <= 10), 
        CHECK (rating >= 0), 
        FOREIGN KEY(booking_id) REFERENCES checkins (booking_id)
    );
    """

)







##########################
# INSERT DATA
##########################

# HOTELS
cursor.executescript(
    """
    INSERT INTO hotels (id, name, street_address, city, postcode, max_capacity) VALUES (1, 'Anaconda Hotel', '123 Street', 'London', 'EC1 3QE', 20);
    INSERT INTO hotels (id, name, street_address, city, postcode, max_capacity) VALUES (2, 'Bayview Hotel', '456 Street', 'New York', '10075', 100);
    INSERT INTO hotels (id, name, street_address, city, postcode, max_capacity) VALUES (3, 'Citylife Hotel', '789 Avenue', 'London', 'SE1 9RT', 30);
    INSERT INTO hotels (id, name, street_address, city, postcode, max_capacity) VALUES (4, 'Darfour Hotel', '321 Place', 'Darfour', '93764', 20);
    INSERT INTO hotels (id, name, street_address, city, postcode, max_capacity) VALUES (5, 'Etna Hotel', '654 Way', 'London', 'W1 8YT', 50);
    """
)

# CUSTOMERS
cursor.executescript(
    """
    INSERT INTO customers (id, first_name, last_name, gender, email, phone) VALUES (1, 'Timmie', 'Daville', 'Male', 'tdaville0@e-recht24.de', '5464973714');
    INSERT INTO customers (id, first_name, last_name, gender, email, phone) VALUES (2, 'Wake', 'Meekin', 'Male', 'wmeekin1@barnesandnoble.com', '6488322514');
    INSERT INTO customers (id, first_name, last_name, gender, email, phone) VALUES (3, 'Tera', 'Stainton', 'Female', 'tstainton2@eventbrite.com', '9087664099');
    INSERT INTO customers (id, first_name, last_name, gender, email, phone) VALUES (4, 'Darnall', 'Arstall', 'Male', 'darstall3@simplemachines.org', '4465691125');
    INSERT INTO customers (id, first_name, last_name, gender, email, phone) VALUES (5, 'Raquel', 'Fattorini', 'Genderqueer', 'rfattorini4@ustream.tv', '9171367937');
    INSERT INTO customers (id, first_name, last_name, gender, email, phone) VALUES (6, 'Harold', 'Klebes', 'Male', 'hklebes5@yahoo.com', '5033375444');
    INSERT INTO customers (id, first_name, last_name, gender, email, phone) VALUES (7, 'Thia', 'Paramore', 'Female', 'tparamore6@washingtonpost.com', '8325606382');
    INSERT INTO customers (id, first_name, last_name, gender, email, phone) VALUES (8, 'Tish', 'Breslane', 'Female', 'tbreslane7@illinois.edu', '6788872422');
    """
)

# EMPLOYEES
cursor.executescript(
    """
    INSERT INTO employees (id, first_name, last_name, gender, dob, email, phone, role, salary, hotel_id) VALUES (1, 'Melodee', 'Arboin', 'Female', '2000-03-02', 'marboin9@statcounter.com', 728363826, 'manager', 200, 1);
    INSERT INTO employees (id, first_name, last_name, gender, dob, email, phone, role, salary, hotel_id) VALUES (2, 'Scarlett', 'Giddy', 'Female', '1990-05-02', 'sgiddya@apache.org', 927362836, 'cook', 30, 1);
    INSERT INTO employees (id, first_name, last_name, gender, dob, email, phone, role, salary, hotel_id) VALUES (3, 'Bob', 'Steckings', 'Male', '1992-09-22', 'bsteckingsb@admin.ch', 92735847, 'cleaner', 15, 1);
    INSERT INTO employees (id, first_name, last_name, gender, dob, email, phone, role, salary, hotel_id) VALUES (4, 'Amalia', 'OKinneally', 'Female', '1986-03-01', 'aokinneallyc@icio.us', 7262392618, 'cleaner', 15, 1);
    INSERT INTO employees (id, first_name, last_name, gender, dob, email, phone, role, salary, hotel_id) VALUES (5, 'Antoinette', 'Prydie', 'Female', '1966-09-12', 'gmickelwrighte@msu.edu', 7253927638, 'manager', 200, 2);
    INSERT INTO employees (id, first_name, last_name, gender, dob, email, phone, role, salary, hotel_id) VALUES (6, 'Giacopo', 'Mickelwright', 'Male', '2001-12-30', 'aprydied@google.com.hk', 927353827, 'cleaner', 15, 1);
    INSERT INTO employees (id, first_name, last_name, gender, dob, email, phone, role, salary, hotel_id) VALUES (7, 'Meryl', 'Durnall', 'Female', '1997-05-15', 'gdenneh@nature.com', 847264927, 'manager', 500, 2);
    INSERT INTO employees (id, first_name, last_name, gender, dob, email, phone, role, salary, hotel_id) VALUES (8, 'Andy', 'Kirtley', 'Male', '1993-10-02', 'akirtleyg@google.pl', 7557958331, 'manager', 200, 3);
    """
)

# BOOKINGS
cursor.executescript(
    """
    INSERT INTO bookings (id, start_date, end_date, room_no, hotel_id, lead_guest_id, no_of_guests) VALUES (1, '2020-05-06 00:00:00.000000', '2020-05-10 00:00:00.000000', 14, 1, 1, 15);
    INSERT INTO bookings (id, start_date, end_date, room_no, hotel_id, lead_guest_id, no_of_guests) VALUES (2, '2020-05-06 00:00:00.000000', '2020-05-10 00:00:00.000000', 10, 2, 5, 8);
    INSERT INTO bookings (id, start_date, end_date, room_no, hotel_id, lead_guest_id, no_of_guests) VALUES (3, '2020-05-06 00:00:00.000000', '2020-05-10 00:00:00.000000', 1, 2, 5, 80);
    INSERT INTO bookings (id, start_date, end_date, room_no, hotel_id, lead_guest_id, no_of_guests) VALUES (4, '2020-05-06 00:00:00.000000', '2020-05-30 00:00:00.000000', 1, 3, 2, 1);
    INSERT INTO bookings (id, start_date, end_date, room_no, hotel_id, lead_guest_id, no_of_guests) VALUES (5, '2020-05-12 00:00:00.000000', '2020-05-25 00:00:00.000000', 8, 1, 3, 2);
    """
)

# CHECKINS
cursor.executescript(
    """
    INSERT INTO checkins (check_in_time, booking_id) VALUES ('2020-05-06 00:00:00.000000', 1);
    INSERT INTO checkins (check_in_time, booking_id) VALUES ('2020-05-06 00:00:00.000000', 2);
    INSERT INTO checkins (check_in_time, booking_id) VALUES ('2020-05-06 00:00:00.000000', 3);
    INSERT INTO checkins (check_in_time, booking_id) VALUES ('2020-05-06 00:00:00.000000', 4);
    INSERT INTO checkins (check_in_time, booking_id) VALUES ('2020-05-12 00:00:00.000000', 5);
    """
)

# CHECKOUTS
cursor.executescript(
    """
    INSERT INTO checkouts (checkout_time, rating, review, booking_id) VALUES ('2020-05-10 00:00:00.000000', 1, 'awful review', 1);
    INSERT INTO checkouts (checkout_time, rating, review, booking_id) VALUES ('2020-05-10 00:00:00.000000', 9, 'amazing review', 2);
    INSERT INTO checkouts (checkout_time, rating, review, booking_id) VALUES ('2020-05-10 00:00:00.000000', 6, 'average review', 3);
    INSERT INTO checkouts (checkout_time, rating, review, booking_id) VALUES ('2020-05-25 00:00:00.000000', 4, 'average review', 5);
    """
)




###############################
# CHECKING RELATIONAL CONSTRAINTS
###############################

###### IMPORTANT!!!!
# These commands intentionally violate these constraints.
# Therefore, they have been wrapped in '''quotation marks''' to prevent them from being run.
# To run a command, remove the '''quotation marks'''.

# PK EXAMPLE - this insertion will violate the uniqueness constraint
'''
cursor.executescript(
    """
    INSERT INTO bookings (id, start_date, end_date, room_no, hotel_id, lead_guest_id, no_of_guests) VALUES (1, '2020-05-06 00:00:00.000000', '2020-05-10 00:00:00.000000', 17, 1, 1, 1);
    """
)
'''

# FK EXAMPLE - this insertion will violate the foreign key constraint
'''
cursor.executescript(
    """
    INSERT INTO checkins (check_in_time, booking_id) VALUES ('2020-05-06 00:00:00.000000', 100);
    """
)
'''

# NOT NULL EXAMPLE - this insertion will violate the not null constraint.
'''
cursor.executescript(
    """
    INSERT INTO hotels (id, name) VALUES (6, 'Constraint failed Hotel');
    """
)
'''

# CUSTOME MADE EXAMPLE - this insertion will violate the custom made CHECK (rating <= 10) constraint.
'''
cursor.executescript(
    """
    INSERT INTO checkouts (checkout_time, rating, review, booking_id) VALUES ('2020-05-25 00:00:00.000000', 100, 'average review', 4);
    """
)
'''





###############################
# VIEW CREATION
###############################


# VIEW 1: customer_reviews

# This view is needed in order to provide an easy way to see the rating and review which each customer provides for each booking where they have succesfully checked in and checked out.
# This view is ordered by the customer_id.

# This view has the attributes: CUSTOMER_ID, HOTEL_ID, RATING, REVIEW, CHECKIN_TIME, and CHECKOUT_TIME.

cursor.executescript(
    """
    CREATE VIEW customer_reviews AS
        SELECT customers.id AS CUSTOMER_ID, hotels.id AS HOTEL_ID, checkouts.rating AS RATING, checkouts.review AS REVIEW, checkins.check_in_time AS CHECKIN_TIME, checkouts.checkout_time AS CHECKOUT_TIME
        FROM checkouts
        JOIN bookings 
            ON bookings.id = checkouts.booking_id
        JOIN hotels 
            ON hotels.id = bookings.hotel_id
        JOIN customers 
            ON customers.id = bookings.lead_guest_id 
        JOIN checkins 
            ON checkins.booking_id = checkouts.booking_id
        ORDER BY customers.id;
    """
)

# VIEW 1: testing
text = "SELECT * FROM customer_reviews;"
result = cursor.execute(text).fetchall()

print("\n\nTESTING VIEW 1: customer_reviews\n")
df = pandas.read_sql_query(text, conn)
print(df)



# VIEW 2: current_customers

# This view is needed in order to provide an easy way to see the contact details of which customers are currently staying in any hotel, and to see which hotel and room they are staying in.
# This means that they have checked in, but they haven't checked out.

# This view has the attributes: CUSTOMER_ID, customer FIRST_NAME, customer LAST_NAME, customer EMAIL, customer PHONE, the HOTEL_ID they are currently in, and the ROOM_NO they are staying in.

cursor.executescript(
    """
    CREATE VIEW current_customers AS
    SELECT customers.id AS CUSTOMER_ID, customers.first_name AS FIRST_NAME, customers.last_name AS LAST_NAME, customers.email AS EMAIL, customers.phone AS PHONE, bookings.hotel_id AS HOTEL_ID, bookings.room_no AS ROOM_NO
    FROM customers
    JOIN bookings
        ON customers.id = bookings.lead_guest_id
    WHERE bookings.id IN (SELECT checkins.booking_id FROM checkins) AND bookings.id NOT IN (SELECT checkouts.booking_id FROM checkouts);
    """
)

# VIEW 2: testing
text = "SELECT * FROM current_customers;"
result = cursor.execute(text).fetchall()

print("\n\nTESTING VIEW 2: current_customers\n")
df = pandas.read_sql_query(text, conn)
print(df)







###############################
# TRIGGERS AND TRIGGER TESTING
###############################

##### IMPORTANT!!!!!!!

# Under every trigger there is a test to see if the trigger works.
# All the tests deliberately invoke the trigger.
# The tests have been wrapped by '''quotation marks''' in order to prevent them from being run.
# If you want to run a test, remove the '''quotation marks''' which wrap the test.
# Before running a different test, re-wrap the previous test you ran in '''quotation marks'''.


############
# BEFORE INSERTING
############


# TRIGGER 1: prevents a booking from being inserted if that hotel would exceed its maximum capacity between the booking's start date and end date.
cursor.executescript(
    """
    CREATE TRIGGER hotel_full_insert BEFORE INSERT ON bookings
    BEGIN
        SELECT CASE
        WHEN ((SELECT SUM(bookings.no_of_guests) + NEW.no_of_guests FROM bookings WHERE bookings.hotel_id = NEW.hotel_id AND NEW.start_date < bookings.end_date AND NEW.end_date > bookings.start_date) > (SELECT hotels.max_capacity FROM hotels WHERE hotels.id = NEW.hotel_id))
        THEN RAISE(FAIL, 'ERROR: This booking exceeds maximum capacity for this hotel.')
    END;
    END;
    """
)

# TRIGGER 1 testing:
'''
cursor.executescript(
    """
    INSERT INTO bookings (id, start_date, end_date, room_no, hotel_id, lead_guest_id, no_of_guests) VALUES (6, '2020-05-06 00:00:00.000000', '2020-05-10 00:00:00.000000', 14, 1, 1, 15);
    """
)
'''


# TRIGGER 2: prevents a booking from being made in the same hotel in the same room on overlapping dates.
cursor.executescript(
    """
    CREATE TRIGGER room_full_insert BEFORE INSERT ON bookings
    BEGIN
        SELECT CASE
        WHEN ((SELECT bookings.no_of_guests FROM bookings WHERE bookings.hotel_id = NEW.hotel_id AND bookings.room_no = NEW.room_no AND NEW.start_date < bookings.end_date AND NEW.end_date > bookings.start_date) > 0)
        THEN RAISE(FAIL, 'ERROR: This hotel room has already been booked for these dates.')
    END;
    END;
    """
)

# TRIGGER 2 testing:
'''
cursor.executescript(
    """
    INSERT INTO bookings (id, start_date, end_date, room_no, hotel_id, lead_guest_id, no_of_guests) VALUES (7, '2020-05-06 00:00:00.000000', '2020-05-10 00:00:00.000000', 14, 1, 2, 5);
    """
)
'''

# TRIGGER 3: The checkout date must be after the checkin date.
cursor.executescript(
    """
    CREATE TRIGGER checkout_after_checkin BEFORE INSERT ON checkouts
    BEGIN
        SELECT CASE
        WHEN ((SELECT checkins.check_in_time FROM checkins WHERE checkins.booking_id = NEW.booking_id) > NEW.checkout_time)
        THEN RAISE(FAIL, 'ERROR: The checkout time cannot be before the checkin time.')
    END;
    END;
    """
)

# TRIGGER 3 testing:
'''
cursor.executescript(
    """
    INSERT INTO checkouts (checkout_time, rating, review, booking_id) VALUES ('2020-05-01 00:00:00.000000', 5, 'some review', 4);
    """
)
'''





############
# BEFORE UPDATING
############


# TRIGGER 4: prevents a booking from being updated if that hotel would exceed its maximum capacity between the booking's start date and end date.
cursor.executescript(
    """
    CREATE TRIGGER hotel_full_update BEFORE UPDATE ON bookings
    BEGIN
        SELECT CASE
        WHEN ((SELECT SUM(bookings.no_of_guests) + NEW.no_of_guests - OLD.no_of_guests FROM bookings WHERE bookings.hotel_id = NEW.hotel_id AND NEW.start_date < bookings.end_date AND NEW.end_date > bookings.start_date) > (SELECT hotels.max_capacity FROM hotels WHERE hotels.id = NEW.hotel_id))
        THEN RAISE(FAIL, 'ERROR: This booking exceeds maximum capacity for this hotel.')
    END;
    END;
    """
)

# TRIGGER 4 testing:
'''
cursor.executescript(
    """
    UPDATE bookings
    SET no_of_guests = 21
    WHERE id=1;
    """
)
'''



# TRIGGER 5: prevents a booking from being updated to a specific hotel room which is already claimed by another booking.
cursor.executescript(
    """
    CREATE TRIGGER room_full_update BEFORE UPDATE ON bookings
    BEGIN
        SELECT CASE
        WHEN ((SELECT bookings.no_of_guests - OLD.no_of_guests FROM bookings WHERE bookings.hotel_id = NEW.hotel_id AND bookings.room_no = NEW.room_no AND NEW.start_date < bookings.end_date AND NEW.end_date > bookings.start_date) > 0)
        THEN RAISE(FAIL, 'ERROR: This hotel room has already been booked for these dates.')
    END;
    END;
    """
)

# TRIGGER 5 testing:
'''
cursor.executescript(
    """
    UPDATE bookings
    SET room_no = 1
    WHERE id=2;
    """
)
'''



############
# BEFORE DELETING
############

# TRIGGER 6: prevents a hotel from being deleted if it has an employee associated with it, thus preventing a foreign key violation in employees.
cursor.executescript(
    """
    CREATE TRIGGER hotel_deletion_employee BEFORE DELETE ON hotels
    BEGIN
        SELECT CASE
        WHEN ((SELECT COUNT(*) FROM employees WHERE employees.hotel_id = OLD.id) > 0)
        THEN RAISE(FAIL, 'ERROR: Foreign Key violation: employee rows need to be deleted or updated first.')
    END;
    END;
    """
)

# TRIGGER 6 testing:
'''
cursor.executescript(
    """
    DELETE FROM hotels WHERE id = 1;
    """
)
'''

# TRIGGER 7: prevents a hotel from being deleted if it has a booking associated with it, thus preventing a foreign key violation in bookings.
cursor.executescript(
    """
    CREATE TRIGGER hotel_deletion_booking BEFORE DELETE ON hotels
    BEGIN
        SELECT CASE
        WHEN ((SELECT COUNT(*) FROM bookings WHERE bookings.hotel_id = OLD.id) > 0)
        THEN RAISE(FAIL, 'ERROR: Foreign Key violation: booking rows need to be deleted or updated first.')
    END;
    END;
    """
)

# TRIGGER 7 testing:
'''
cursor.executescript(
    """
    DELETE FROM hotels WHERE id=1;
    """
)
'''


# TRIGGER 8: prevents a customer from being deleted if they have made a booking, thus preventing a foreign key violation in bookings.
cursor.executescript(
    """
    CREATE TRIGGER customer_deletion BEFORE DELETE ON customers
    BEGIN
        SELECT CASE
        WHEN ((SELECT COUNT(*) FROM bookings WHERE bookings.lead_guest_id = OLD.id) > 0)
        THEN RAISE(FAIL, 'ERROR: Foreign Key violation: bookings rows need to be deleted or updated first.')
    END;
    END;
    """
)

# TRIGGER 8 testing
'''
cursor.executescript(
    """
    DELETE FROM customers WHERE id=1;
    """
)
'''

# TRIGGER 9: prevents a booking from being deleted if it has a checkin associated with it, thus preventing a foreign key violation in checkins.
cursor.executescript(
    """
    CREATE TRIGGER booking_deletion BEFORE DELETE ON bookings
    BEGIN
        SELECT CASE
        WHEN ((SELECT COUNT(*) FROM checkins WHERE checkins.booking_id = OLD.id) > 0)
        THEN RAISE(FAIL, 'ERROR: Foreign Key violation: checkin rows need to be deleted or updated first.')
    END;
    END;
    """
)

# TRIGGER 9 testing
'''
cursor.executescript(
    """
    DELETE FROM bookings WHERE id=1;
    """
)
'''

# TRIGGER 10: prevents a checkin from being deleted if it has an associated checkout, thus preventing a foreign key violation in checkouts.
cursor.executescript(
    """
    CREATE TRIGGER checkin_deletion BEFORE DELETE ON checkins
    BEGIN
        SELECT CASE
        WHEN ((SELECT COUNT(*) FROM checkouts WHERE checkouts.booking_id = OLD.booking_id) > 0)
        THEN RAISE(FAIL, 'ERROR: Foreign Key violation: checkout rows need to be deleted or updated first.')
    END;
    END;
    """
)

# TRIGGER 10 testing
'''
cursor.executescript(
    """
    DELETE FROM checkins WHERE booking_id=1;
    """
)
'''






###########################
# SUCCESSFUL DML COMMANDS (insert, update, delete)
###########################

### INSERTING ###
cursor.executescript(
    """
    INSERT INTO customers (id, first_name, last_name, gender, email, phone) VALUES (9, 'Gus', 'Fowle', 'Male', 'gusfowle1@gmail.com', '9999999999');
    """
)

### UPDATING ###
cursor.executescript(
    """
    UPDATE checkouts
    SET review = 'truly terrible experience'
    WHERE booking_id=1;
    """
)

### DELETING ###
cursor.executescript(
    """
    DELETE FROM employees WHERE id=2;
    """
)






##############################
# FIVE QUERIES
##############################



# QUERY 1: select the names of the highest paid employee in each hotel, along with how much they are paid.
text = "SELECT hotels.name AS HOTEL_NAME, employees.first_name ||' '|| employees.last_name AS EMPLOYEE_NAME, MAX(employees.salary) AS SALARY, employees.role AS ROLE FROM employees JOIN hotels ON hotels.id = employees.hotel_id GROUP BY hotels.id;"

print("\n\nQUERY 1: who is the highest paid employee in each hotel?\n")
df = pandas.read_sql_query(text, conn)
print(df)




# QUERY 2: select the names of each customer who has checked out and given a rating, the average of each customer's rating ordered highest to lowest, and how many ratings each customer has given.

text = "SELECT customers.first_name ||' '|| customers.last_name AS CUSTOMER_NAME, SUM(customer_reviews.rating) / COUNT(customer_reviews.rating) AS AVERAGE_RATING_GIVEN, COUNT(customer_reviews.rating) AS NO_OF_RATINGS_GIVEN FROM customer_reviews JOIN customers ON customers.id = customer_reviews.customer_id GROUP BY customer_reviews.customer_id ORDER BY average_rating_given DESC;"

print("\n\nQUERY 2: list the average rating which each customer has given ordered highest to lowest.\n")
df = pandas.read_sql_query(text, conn)
print(df)




# QUERY 3: select the average rating for each hotel ordered from highest rating to lowest rating.

text = "SELECT hotels.name AS HOTEL_NAME, SUM(checkouts.rating) / COUNT(checkouts.rating) AS AVERAGE_RATING_RECEIVED, COUNT(checkouts.rating) AS NO_OF_RATINGS_RECEIVED FROM bookings JOIN checkouts ON bookings.id = checkouts.booking_id JOIN hotels ON hotels.id = bookings.hotel_id GROUP BY bookings.hotel_id ORDER BY average_rating_received DESC;"

print("\n\nQUERY 3: list the average rating for each hotel ordered highest to lowest.\n")
df = pandas.read_sql_query(text, conn)
print(df)




# QUERY 4: list the hotels ordered by the total number of guests they have received to date (i.e. the total number of people ever checked in). Do not include hotels which have never checked in a guest.

text = "SELECT hotels.name AS HOTEL_NAME, SUM(bookings.no_of_guests) AS TOTAL_GUESTS_RECEIVED FROM hotels JOIN bookings ON bookings.hotel_id = hotels.id WHERE bookings.id IN (SELECT checkins.booking_id FROM checkins) GROUP BY hotels.id ORDER BY total_guests_received DESC;"

print("\n\nQUERY 4: list the hotels ordered by the total number of guests they have received to date (i.e. the total number of people ever checked in). Do not include hotels which have never checked in a guest.\n")
df = pandas.read_sql_query(text, conn)
print(df)




# QUERY 5: select the hotel which has the highest number of guests in it at this current moment (i.e those who have checked in but haven't checked out), listing the hotel details, number of people currently checked in to that hotel, and its maximum capacity.

text = "SELECT hotels.name AS HOTEL_NAME, SUM(bookings.no_of_guests) AS TOTAL_CURRENT_GUESTS, hotels.max_capacity AS MAX_CAPACITY FROM hotels JOIN bookings ON hotels.id = bookings.hotel_id WHERE bookings.id IN (SELECT checkins.booking_id FROM checkins) AND bookings.id NOT IN (SELECT checkouts.booking_id FROM checkouts) GROUP BY hotels.id ORDER BY total_current_guests DESC LIMIT 1;"

print("\n\nQUERY 5: select the hotel which has the highest number of guests in it at this current moment, along with its respective maximum capacity.\n")
df = pandas.read_sql_query(text, conn)
print(df)
print("\n")