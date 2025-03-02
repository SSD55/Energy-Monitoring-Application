# Energy-Monitoring-Application

This project is a simple web application that visualizes energy consumption data for various smart home devices. <br />
It consists of a backend built with Flask and a frontend built with React.

# Features:

Fetches real-time energy consumption data from a simulated API.<br />
Stores energy data in an SQLite database.<br />
Displays energy consumption trends using interactive charts.<br />
Allows users to select different devices and view their energy usage.<br />

# Technologies Used:

Backend (Flask)<br />
Flask (Python framework)<br />
SQLite (Database for storing energy data)<br />
Requests (For API calls)<br />
Frontend (React)<br />
React (JavaScript library for UI)<br />
Axios (For making API requests)<br />
Chart.js (For displaying energy consumption trends)<br />
Bootstrap (For styling the UI)<br />

# How to Use:

Start both the backend and frontend servers.<br />
Open the React app in a browser.<br />
Select a device from the dropdown.<br />
View real-time energy consumption trends in the chart.<br />

# Design Choices:

Flask for the backend: Chosen for its lightweight nature, easy integration with SQLite, and simplicity in handling API requests.<br />
SQLite for storage: Suitable for a small-scale project that doesn't require complex database management.<br />
React for the frontend: Provides a dynamic UI and seamless interaction with the backend API.<br />
Chart.js for visualization: Offers interactive charts for a better user experience.<br />
Bootstrap for styling: Ensures a clean and responsive design across devices.<br />

# Challenges Faced:

Real-time Data Handling: Implementing a mechanism to simulate real-time energy data updates efficiently.<br />
Database Management: Ensuring proper handling of energy consumption data in SQLite without performance bottlenecks.<br />
Frontend-Backend Communication: Managing smooth communication between Flask and React, especially for fetching and displaying real-time data.<br />
