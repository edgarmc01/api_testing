@movies @api
Feature: Movies
    As anplication developer, i want to work with the Movie
    API, so that i can work with Movies data.

    @tc_01 @functional @smoke
    Scenario: search all the movies when there are no records
        when the user send "GET" request to "/movies" endpoint
        then the response status code should be "200"
        and the response body should have "0" elements
        and the response should fit the following schma "get_movies_schema.json"
        