import folium
import time
from geopy.geocoders import Nominatim
from geopy.extra.rate_limiter import RateLimiter

# create geolocator and set time delay to it
geolocator = Nominatim(user_agent="Romanyk", timeout=3)
geocode = RateLimiter(geolocator.geocode, min_delay_seconds=0.1)


def lst_to_str(lst):
    '''
    list -> str
    convert all items of list into 1 str
    >>> lst_to_str([1, 2, 3])
    '1 2 3 '
    '''
    s1 = ''
    for el in lst:
        s1 += str(el) + ' '
    return s1


def get_counties(file):
    '''
    str -> dict
    Read file and return dictionary with keys by year
    and values as place name
    '''
    with open(file, encoding='utf-8', errors='ignore') as f:
        countries = {}  # year: country
        # get keys(years) and add country, location to each

        for line1 in f:
            try:
                line = line1.strip().split('\t')
                if line[-1].startswith('(') and line[-1].endswith(')'):
                    line.pop(-1)
                data = line[0].split(' ')
                for item in data:
                    if item.startswith('(') and item.endswith(')'):
                        item = item[1:5]
                        try:
                            year = int(item)  # got year
                        except:
                            continue
                if year not in countries.keys():
                    countries[year] = []
                countries[year].append(line1)
            except:
                continue

        return countries


def change_all_locations(lst):
    '''
    list -> list
    Transfer every location name into coordinates
    '''
    start_time = time.time()
    all_locs = []
    for place in lst:
        location = geocode(place)
        if location:
            print(place, (location.latitude, location.longitude))
            all_locs.append((location.latitude, location.longitude))
        if time.time() - start_time >= 180:
            break
    return all_locs


def generate_map(locations, user_location):
    '''
    list, list -> ()
    Create a map with Folium and set up to 10 markers on it
    '''
    map = folium.Map(location=user_location, zoom_start=12)
    tooltip = 'filming place'

    radius = 0.0001
    for item in locations:
        distance = find_distance(item, user_location)
        if distance > radius:
            radius = distance

    fg = folium.FeatureGroup(name="Marker map")
    fg.add_child(folium.Marker(user_location,
                               icon=folium.Icon(color='green'),
                               tooltip='you are here'))

    cl = folium.FeatureGroup(name='Circle map')
    print(radius)
    cl.add_child(folium.Circle(location=user_location,
                               radius=radius*11113.9,
                               fill_color='green',
                               color='red',
                               fill=True,
                               popup='closest filming places',
                               tooltip='Closest filming places'))

    x = 0
    for coord in locations:
        x += 1
        fg.add_child(folium.Marker(coord, tooltip=tooltip))
        if x == 10:
            break
    print('Map generated.\
Check out new-created file Map.html in tests directory')
    map.add_child(fg)
    map.add_child(cl)
    map.add_child(folium.LayerControl())
    map.save('tests/Map.html')


def find_distance(loc1, loc2):
    '''
    list, list -> int
    find the distance between two points on the map
    >>> find_distance([3, 4], [4, 3])
    1.4142135623730951
    '''
    distance = ((loc1[0] - loc2[0]) ** 2 + (loc1[1] - loc2[1]) ** 2) ** 0.5
    return distance


def compare_distance(user_loc, locations):
    '''
    list, list -> dict
    get 10 max distances from all locations
    >>> compare_distance([2.34, 1.33], [(1, 3), (3, 4)])
    {2.1411445537375564: (1, 3), 2.7503636123247412: (3, 4)}
    '''
    all_dist = {}
    for item in locations:
        distance = find_distance(user_loc, item)
        all_dist[distance] = item
        if len(all_dist.keys()) > 10 and distance < max(all_dist.keys()):
            del all_dist[max(all_dist.keys())]
    return all_dist


def get_user_input():
    '''
    () -> int, list
    gather user data
    '''

    def log_out():
        exit = input('Wrong data, try again(eg. year: 2000\nlocation: 49.83826, 24.02324)\n.\
    If you want to quit press Q key: ')
        return exit

    result = ()
    breakdown = True
    while breakdown:
        # check year
        year = input('Enter a year(XXXX-format) you\
want to be showed on map: ')
        year = year.strip()

        try:
            year = int(year)
            if 1800 <= year <= 2019:
                breakdown = False
            else:
                print('Wrong data, eg. year: 2005')
        except:
            continue

        coordinates = input('Please enter your location (format: lat, long): ')
        coordinates = coordinates.strip().split(',')
        try:
            coordinates[0] = float(coordinates[0])
            coordinates[1] = float(coordinates[1])
            # all ok
            breakdown = False
        except:
            print('wrong data. ')
            breakdown = True

        if len(coordinates) != 2:
            print('Enter coorect coordinates.')
            breakdown = True

        if breakdown:
            result = log_out()
        if len(result) == 1 and result.lower().strip() == 'q':
            print('Be careful, we know ')
            return 0, 0
        result = (year, coordinates)

    return result


def get_cities(file):
    '''
    str -> dict
    collect data from cities list and return a dict with them
    {year: line}
    '''
    dict = {}
    with open(file, 'r', encoding='utf-8', errors='ignore') as f:
        for line in f:
            line = line.strip().split('\t')
            # print(line)

            if len(line) >= 3:
                try:
                    coords = [float(line[-2]), float(line[-1])]
                    city = line[-3]
                    dict[city] = coords
                except:
                    continue
    return dict


def check_for_films(locations, film_data):
    '''
    list, str -> list
    check if there is such place in all places data
    >>> check_for_films(['USA', 'Ukraine', 'Russia'], 'USA, Ukraine')
    ['Ukraine']
    '''
    for place in locations:
        place1 = place.lower().replace("'", '')
        if place1 not in film_data:
            locations.remove(place)
    return locations


def find_closest_city(user_loc, data, counter=100):
    '''
    list, dict -> dict
    search the closest city to the users location
    return dictionary with the name of city and location
    >>> find_closest_city([2.33, 3.44], {'a': (13, 12), 'b': (24, 15)})
    {'name': 100000, 'a': 13.679272641482076, 'b': 24.560588348001765}
    '''
    min_dist = 100000
    all_dist = [min_dist]
    all_city = ['name']
    for key in data.keys():
        dist2 = find_distance(user_loc, data[key])
        if len(all_dist) < counter:
            all_dist.append(dist2)
            all_city.append(key)
        else:
            max_dist = max(all_dist)
            if dist2 < max(all_dist):
                all_city.pop(all_dist.index(max_dist))
                all_dist.remove(max_dist)

                all_dist.append(dist2)
                all_city.append(key)

    return dict(zip(all_city, all_dist))


def main():
    print('Preparing data, please wait... ')
    countries_dict = get_counties('docs/locations.list')
    film_data = lst_to_str(countries_dict.values())
    citi_locs = get_cities('docs/cities.csv')

    year, location = get_user_input()
    if year == 0:
        return
    # find the closest city:
    citi_and_locations = find_closest_city(location, citi_locs, counter=100)
    # print(citi_and_locations)

    places_to_check = citi_and_locations.keys()
    # shorten the list by using most detailized data
    # transfer into locations
    places_to_check = check_for_films(list(places_to_check), film_data)

    print('amount of filming locations in ', year,
          ' year: ', len(places_to_check))

    print('Please, wait, it can take up to 5 minutes')
    locations = change_all_locations(places_to_check)
    current_locations = compare_distance(location, locations)
    generate_map(current_locations.values(), location)
    print('Finished')


if __name__ == '__main__':
    main()

