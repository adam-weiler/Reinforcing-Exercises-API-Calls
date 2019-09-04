### Thursday, Aug 15th
# 01 - Reinforcing Exercises: API Calls

These short exercises will give you a chance to practice the fundamental web development concepts you've learned so far by making API calls to [this data API about every politician in the world](http://docs.everypolitician.org/use_the_data.html).

## Prerequisites

+ HTTP request/response fundamentals
+ Python fundamentals
+ making API calls
+ JSON

## Getting Started

Create a new Python file and require the `requests` package to help you make these API calls.

## Exercise

1. [Check out the documentation.](http://docs.everypolitician.org/use_the_data.html)

1. Make request to get the [countries.json file](https://raw.githubusercontent.com/everypolitician/everypolitician-data/master/countries.json) that they talk about in the documentation.

1. Examine the structure of the JSON data.

1. Pick a country.

1. Extract the URL for the JSON data about the government of the country of your choice (if the country has more than one governmental body - like how Canada has both the House of Commons and the Senate - you can just pick one of them).

1. Make another request to get that government-specific JSON data.

1. Extract the name of one politician from that JSON response and save it in a variable.
