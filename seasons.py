# 7dtd seasons

# configurable options

# the 'year' is 60 days long
year_length = 60
# announce sunrise?
# announce sunset?
# announce season?
# announcement time

# maximum hours of daylight in midsummer
max_daylight = 21
# minimum hours of daylight in midwinter
min_daylight = 4


# split into 4 month/seasons of 15 days each

# days 1-15 = summer
# 16-30 = autumn
# 31-45 = winter
# 46-60 = spring

# and then it repeats!

# every midnight, there's an announcement of the sunrise and sunrise and sunset times,
# plus what time of year it is:

# early/mid/late
# spring/summer/autumn/winter

# each month 
# 1-5 = early
# 6-10 = mid
# 11-15 = late

# day lngth is based on a simple sinusoidal pattern.


# daylight hours = min + range + (sin(x) * range ),
# where range = (max-min)/2

# The daylightLength preference only supports whole integers in hours,
# so it's a somewhat drastic shift on days where it changes. 


# this mod needs the server's control panel (telnet) functionality to be enabled, in order to work.
# Since it's written in Python, obviously it also requires Python to be installed.

# Python 3, of course! Python 2 is no longer supported, remember?

# like everything in the base game, the daylight length is a very rough approximation of how it works in real life (on earth),
# designed to 'feel' realistic, but to be more fun than true realism.

# The shorter month/season and year lengths also reflect that.

# PLEASE NOTE: this mod makes NO OTHER seasonal changes, like tree leaves falling,
# plant growth, temperature changes.

# I have no idea how I'd implement those. If you do, send me a message!
