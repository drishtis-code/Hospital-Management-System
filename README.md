# Hospital Management System

A simple Hospital Management System built using Python Tkinter and MySQL.

This project allows users to:
- Add rooms
- Edit rooms
- Delete rooms
- Add patient details

The project is designed for beginners learning:
- Python GUI development
- Database connectivity
- CRUD operations
- Tkinter applications

# Technologies Used

- Python
- Tkinter
- MySQL
- mysql-connector-python

# Features

## Room Management
- Add room details
- Edit room information
- Delete rooms

## Patient Management
- Add patient records
- Store disease and medicine details


# Project Structure

Hospital-Management-System/
│
├── hospital management system.py
├── README.md


# Database Setup

## Step 1: Create Database

Run the following SQL commands in MySQL:

```sql
CREATE DATABASE team;

USE team;

CREATE TABLE Rooms(
    status VARCHAR(10),
    rn INT PRIMARY KEY,
    t VARCHAR(50),
    c VARCHAR(50),
    cp FLOAT
);

CREATE TABLE Patient(
    pid VARCHAR(20),
    name VARCHAR(50),
    disease VARCHAR(100),
    medicine VARCHAR(100)
);


Install Required Package

Install mysql connector using:

pip install mysql-connector-python


GUI Modules

Home Page

Rooms
Patient

Rooms Module
Add Rooms
Edit Rooms
Delete Rooms

Patient Module
Add Patient

Learning Outcomes:
This project helps beginners understand:

GUI development using Tkinter
MySQL database integration
CRUD operations
Python event handling


Author
Drishti Singh
BTech CSE Student