<h2>Web map</h2>

The application visualizes up to 10 closest locations of the year you want on the world map.

<h3>What map can show you?</h3>

Map that is provided by OpenStreetMap
Nearest filming locations to your input data by the year
10 closest places where films were taken

<h3>Usage</h3>

To start the application you have to have installed python 3+ version
To run world_map you have to have all libraries that are used in this project. So run this line in your cmd:


<italc>After that you will have a field:</italic>

Enter a year(XXXX-format) you want to be showed on map:
You have to enter the proper year.
Please enter your location (format: lat, long):
You have to enter the proper location like <36.7, -98.12>. After that you have to wait a littele bit(around 1 minute).
You can see location and it's coordinates during generating process

<h3>Common errors</h3>

You can bump into geopy.exc.GeocoderQuotaExceeded: HTTP Error 429: Too Many Requests or geopy.exc.GeocoderTimedOut: Service timed out problems.
It's recommended to change the wifi network or use VPN.

<h3>Some Html tags:</h3>

<pre><xmp><!DOCTYPE html></xmp></pre> - to define that the type of file isHTML5.

<head> - the most important information

<meta> - metadata

<body> - information displayed in the web page

<script> - use scripts like JS inside the HTML file

<link> - connect CSS to the HTML file

<style> - write CSS code inside HTML file

<a> - link to the site

<pre><xmp><h1></xmp></pre> - choose size of the text(from h1 to h6 - bigger/smaller)

<div> -block of items. Easy grouping

Let's sum up
The program shows us a map with the nearest locations where the films of the chosen year were filmed.

I dont know if this web map will be usefull for you. But you can try it. 
