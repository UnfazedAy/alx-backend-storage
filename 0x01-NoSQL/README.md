# 0x01. NoSQL
This directory contains all the solution for the tasks below.

# Tasks
## 0. List all databases
Write a script that lists all databases in MongoDB.

    guillaume@ubuntu:~/0x01$ cat 0-list_databases | mongo
    MongoDB shell version v3.6.3
    connecting to: mongodb://127.0.0.1:27017
    MongoDB server version: 3.6.3
    admin        0.000GB
    config       0.000GB
    local        0.000GB
    logs         0.005GB
    bye
    guillaume@ubuntu:~/0x01$

## 1. Create a database
Write a script that creates or uses the database my_db

    guillaume@ubuntu:~/0x01$ cat 0-list_databases | mongo
    MongoDB shell version v3.6.3
    connecting to: mongodb://127.0.0.1:27017
    MongoDB server version: 3.6.3
    admin        0.000GB
    config       0.000GB
    local        0.000GB
    logs         0.005GB
    bye
    guillaume@ubuntu:~/0x01$
    guillaume@ubuntu:~/0x01$ cat 1-use_or_create_database | mongo
    MongoDB shell version v3.6.3
    connecting to: mongodb://127.0.0.1:27017
    MongoDB server version: 3.6.3
    switched to db my_db
    bye
    guillaume@ubuntu:~/0x01$

## 2. Insert document
Write a script that inserts a document in the collection school:

- The document must have one attribute name with value “Holberton school”
- The database name will be passed as option of mongo command

        guillaume@ubuntu:~/0x01$ cat 2-insert | mongo my_db
        MongoDB shell version v3.6.3
        connecting to: mongodb://127.0.0.1:27017/my_db
        MongoDB server version: 3.6.3
        WriteResult({ "nInserted" : 1 })
        bye
        guillaume@ubuntu:~/0x01$