# Intelligent-Farming-Sensors-Scripts
Intelligent Farming was my Final Year Project for which I used following Configuration.
Sensors--->Raspberry Pi(Python Script)----->Web-API-server=======>Database-&&-Mobile Application(User Interface)
Multiple Raspberry Pi were sensing the data and by using APIs they data were stored in the Database server and user can view all the 
sensed data with the help of Android Application which are accessing data by using APIs

This Script uses DHT-11 Library from GitHub URl https://github.com/szazo/DHT11_Python and senses the humidity Controller Sensors current state and dump the values to 
Database server by creating a Request with POST parameters.
This script can be  improvised to control water pumps and trigger notification to user for particular Action or State Alert System.
