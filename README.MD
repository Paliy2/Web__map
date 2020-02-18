<p align="center"><h2>Web map</h2></p>

The application visualizes up to 10 closest locations of the year you want on the world map.

<h3>What map can show you?</h3>

Map that is provided by OpenStreetMap.
Nearest filming locations to your input data by the year.
10 closest places where films were taken.

<h3>Usage</h3>

To start the application you have to have installed python 3+ version.
To run world_map you have to have all libraries that are used in this project.
To run file just install geopy and folium python libraries and run web map.py file.
It will create map in file Map.html.
To access file of the map just go into tests and then open in your browser file Map.html.


<i>After that you will have a field:</i>

Enter a year(XXXX-format) you want to be showed on map:
You have to enter the proper year.
Please enter your location (format: lat, long):
You have to enter the proper location like <36.7, -98.12>. After that you have to wait a littele bit(around 1 minute).
You can see location and it's coordinates during generating process.

<ing src="https://github.com/Paliy2/Web__map/blob/master/%D0%BB%D0%B0%D0%B1%D0%BA%D0%B0%202/tests/Map_example.png">
![Equalizer](https://github.com/Paliy2/Web__map/blob/master/%D0%BB%D0%B0%D0%B1%D0%BA%D0%B0%202/tests/Map_example.png)
  
<h3>Common errors</h3>

You can bump into geopy.exc.GeocoderQuotaExceeded: HTTP Error 429: Too Many Requests or geopy.exc.GeocoderTimedOut: Service timed out problems.
It's recommended to change the wifi network or use VPN.

<h3>Some Html tags:</h3>

&lt;!DOCTYPE html&gt; - to define that the type of file is HTML5.

&lt;head&gt; - the most important information

&lt;meta&gt; - metadata

&lt;body&gt; - information displayed in the web page

&lt;!DOCTYPE html&gt, &lt;head&gt;, &lt;body&gt; make structure of any HTML file

&lt;script&gt; - use scripts like JS inside the HTML file

&lt;link&gt; - connect CSS to the HTML file

&lt;style&gt; - write CSS code inside HTML file

&lt;div&gt; -block of items. Easy grouping

<h3>Let's sum up</h3>
The program shows us a map with the nearest locations where the films of the chosen year were filmed.
<p>I dont know if this web map will be usefull for you. But you can try it. </p>
