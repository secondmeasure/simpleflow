from enum import Enum


NAME = "main"
DESCRIPTION = "Retrieve main data from a given url : http code, delays, date crawled, depth..."
PRIORITY = 0

GROUPS = Enum('Groups',
              [('scheme', 'Url Scheme'), ('main', 'Main')])
