## Version 2.0
## language: en

#Keep comments if they start with double sharp ##

#M: Mandatory
#O: Optional

#{} are template tags. A final feature should not contain any of these.

Feature: {code}-{category}-{site} #M
  """
  This section is intended for the hacker to provide general information about
  the challenge he is trying to solve, what his goal is and location of the
  challenge.
  """
  Code: #O
    {code} #Code of the challenge if it exists
  Site: #M
    {site} #Site where the challenge can be found
  Category: #O
    {category} #Category of the challenge within the site e.g: decoding, BoF...
  User: #M
    {user} #Username used in the site when solving the challenge
  Goal: #M
    {goal} #Short description of your goal

  Background:
  """
  In this section the hacker has to provide a list containing versions and names
  of the software he used for capturing the flag (OS, Browser, etc).
  Also, information about the machine where the challenge takes place like:
  Relevant services with their versions, OS and kernel with their versions, etc
  has to be provided
  """
  Hacker's software:
    | <Software name> | <Version>   |
    | {os}            | {version 1} |
    | {browser}       | {version 2} |
    | {name1}         | {version 3} |
  Machine information:
    Given I am accessing the {machine} through a VPN
    And SSH with {command}
    And enter a console that allows me to {A}
    And the server is running MySQL version {B}
    And PHP version {C}
    And SSH version {D}
    And is running on Ubuntu {E} with kernel {F}

  Scenario: {Fail|Success}:{metohd-used-1}
  """
  Scenarios allow the hacker to describe in a time-based order what he tried
  to solve the challenge.

  {Fail|Success}: Success if the flag was caught and Fail if it wasn't
  {method-used-*}: Brief description of what is done in the scenario
  """
    Given I am logged in the machine
    And I print {A}
    Then I can see {B}
    Then I try to decrypt {B} by doing {C}
    And get {D}
    Then I conclude that I can't use {D} for my purpose
    And {C} did not work
    And I could not capture the flag

  Scenario: {Fail|Success}:{method-used-2}
    Given I print {A}
    Then I can see {B}
    Then I try to decrypt {B} by doing {E}
    And get {F}
    Then I can actually read the flag from {F}
    And I conclude that {E} worked
    And solved the challenge
    And I caught the flag

  """
  Evidences:
  Presenting evidence of some kind of graphical output, like websites,
  might be difficult when using plain feature files.
  Think, for example, of a hacked blog via XSS that ended up with different font
  styles and such.
  Evidences are a way to include PNG pictures associated to a feature file so
  the hacker can graphically show anything he might consider relevant

  How they work?
  - Any feature file {name}.feature can have a {name} evidences folder in the
  same directory.
  - Evidence folders only accept PNG images
  - Evidences are referenced in two different ways:
    - Creating an <evidence> tag in a table inside a Scenario Outline like shown
      on the Extraction Scenario example
      (useful for referencing multiple evidences).
    - By using the following syntax: [evidence](image.png) like shown on the
      Normal use case Scenario example.
      (useful for referencing one or two evidences at most.)
  """
