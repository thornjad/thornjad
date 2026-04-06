#!/usr/bin/env python3

import os
import json
import urllib.request

icons = {
  "clear-day": "☀️",
  "clear-night": "🌙",
  "cloudy": "☁️",
  "foggy": "🌁",
  "partly-cloudy-day": "⛅",
  "partly-cloudy-night": "☁️",
  "possibly-rainy-day": "🌦️",
  "possibly-rainy-night": "🌧️",
  "possibly-sleet-day": "🌨️",
  "possibly-sleet-night": "🌨️",
  "possibly-snow-day": "🌨️",
  "possibly-snow-night": "🌨️",
  "possibly-thunderstorm-day": "⛈️",
  "possibly-thunderstorm-night": "⛈️",
  "rainy": "🌧️",
  "sleet": "🌨️",
  "snow": "🌨️",
  "thunderstorm": "⛈️",
  "windy": "🍃"
}

conditions = {
    "Clear": "clear",
    "Partly Cloudy": "partly cloudy",
    "Mostly Cloudy": "mostly cloudy",
    "Cloudy": "cloudy",
    "Very Light Rain": "very lightly raining",
    "Light Rain": "lightly raining",
    "Moderate Rain": "moderately raining",
    "Heavy Rain": "heavily raining",
    "Very Heavy Rain": "very heavily raining",
    "Light Snow": "lightly snowing",
    "Moderate Snow": "moderately snowing",
    "Heavy Snow": "heavily snowing",
    "Light Sleet": "lightly sleeting",
    "Moderate Sleet": "moderately sleeting",
    "Heavy Sleet": "heavily sleeting",
    "Thunderstorm": "thunderstorming",
    "Thunderstorms Possible": "looking stormy",
    "Thunderstorms Likely": "looking stormy soon",
    "Snow": "snowing",
    "Snow Possible": "looking snowy",
    "Snow Likely": "looking snowy soon",
    "Rain Possible": "looking rainy",
    "Rain Likely": "looking rainy soon",
    "Wintry Mix Possible": "looking wintry",
    "Wintry Mix Likely": "looking wintry soon",
    "Fog": "foggy",
    "Windy": "windy",
    "Light Wind": "a little windy",
}

url = f'https://swd.weatherflow.com/swd/rest/better_forecast?station_id=' + os.environ['TEMPEST_STATION'] + '&token=' + os.environ['TEMPEST_PUT'] + '&units_temp=f'
with urllib.request.urlopen(url) as response:
  data = response.read()
  weather = json.loads(data.decode('utf-8'))

print(weather)

profile = open('README.md', 'r', encoding='utf-8').read()
start_pos = profile.find('\u200B') + len('\u200B') # zero-width spaces
end_pos = profile.find('\u200B', start_pos)

temp = str(round(weather['current_conditions']['air_temperature'])) + '°' + weather['units']['units_temp'].upper()
raw_condition = weather['current_conditions']['conditions']
condition = icons[weather['current_conditions']['icon']] + ' ' + conditions.get(raw_condition, raw_condition.lower())
profile = profile[:start_pos] + temp + ' and ' + condition + profile[end_pos:]

overwrite = open('README.md', 'w', encoding='utf-8')
overwrite.write(profile)
overwrite.close()
