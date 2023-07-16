@frontoffice @all
Feature: Search in Destinia

    @destinia_cheapest_accomodation
    Scenario: Search for an accomodation in Madrid
      Given access the web application 'url_destinia'
      When fill in the search fields
      And click on 'Buscar' button
      And filter results and choose the cheapest hotel
      Then verify the accommodation description
