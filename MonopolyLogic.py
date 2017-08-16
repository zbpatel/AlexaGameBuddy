# Provides a set of functions related to the board game monopoly


# given an intent related to monopoly, calls the appropriate handling methods
# this is basically a monopoly specfic version of the more general method in
# GameBuddy
def monopoly_handler(intent):
    return None

# Helper methods for interacting with the properties object
BAD_SEARCH = "BAD_SEARCH"

# given a list that is the "object path" to the attribute we want, return the
# value of that item in property, or "BAD_SEARCH" if it does not exist
# example call: path = ['boardwalk', 'price']
def get_attribute(path):
    def get_reduce(obj, attr):
        if obj in attr:
            return obj[attr]
        else:
            return "BAD_SEARCH"
    reduce(get_reduce, path)

# long json object that contains information about the various properties
# sure, we could have used some sql or something here, but that is a little
# excessive for something meant to run quickly on lambda
properties= {
    'mediterranean vvenue': {
        'price': 60,
        'rent': 2,
        'group': 'purple'
    },
    'baltic avenue': {
        'price': 60,
        'rent' 4,
        'group': 'purple'
    },
    'oriental avenue': {
        'price': 100,
        'rent': 6,
        'group': 'light blue'
    },
    'vermont avenue': {
        'price': 100,
        'rent': 6,
        'group': 'light blue'
    },
    'connecticut avenue': {
        'price': 120,
        'rent': 8,
        'group': 'light blue'
    },
    'saint charles place': {
        'price' = 120,
        'rent' = 10,
        'group' = 'violet'
    },
    'states avenue': {
        'price' = 140,
        'rent' = 10,
        'group' = 'violet'
    },
    'virginia avenue': {
        'price' = 160,
        'rent' = 12,
        'group' = 'violet'
    },
    'saint james place': {
        'price' = 180,
        'rent' = 14,
        'group' = 'orange'
    },
    'tennessee avenue': {
        'price' = 180,
        'rent' = 14,
        'group' = 'orange'
    },
    'new york avenue': {
        'price' = 200,
        'rent' = 16,
        'group' = 'orange'
    },
    'kentucky avenue': {
        'price' = 220,
        'rent' = 18,
        'group' = 'red'
    },
    'indiana avenue': {
        'price' = 220,
        'rent' = 18,
        'group' = 'red'
    },
    'illinois avenue': {
        'price' = 240,
        'rent' = 20,
        'group' = 'red'
    },
    'atlantic avenue': {
        'price' = 260,
        'rent' = 22,
        'group' = 'yellow'
    },
    'ventnor avenue': {
        'price' = 260,
        'rent' = 22,
        'group' = 'yellow'
    },
    'marvin gardens': {
        'price' = 280,
        'rent' = 24,
        'group' = 'yellow'
    },
    'pacific avenue': {
        'price' = 300,
        'rent' = 26,
        'group' = 'green'
    },
    'north carolina avenue': {
        'price' = 300,
        'rent' = 26,
        'group' = 'green'
    },
    'pennsylvania avenue': {
        'price' = 320,
        'rent' = 28,
        'group' = 'green'
    },
    'park place': {
        'price' = 350,
        'rent' = 35,
        'group' = 'dark blue'
    },
    'boardwalk': {
        'price': 400,
        'rent': 50,
        'group': 'dark blue'
    },
    'electric company': {
        'price': 150,
        'rent': 'variable',
        'group': 'utilities'
    },
    'water works': {
        'price': 150,
        'rent': 'variable',
        'group': 'utilities'
    },
    'reading railroad': {
        'price': 200,
        'rent': 'variable',
        'group': 'railroad'
    },
    'pennsylvania railroad': {
        'price': 200,
        'rent': 'variable',
        'group': 'railroad'
    },
    'b&o railroad': {
        'price': 200,
        'rent': 'variable',
        'group': 'railroad'
    },
    'short line railroad': {
        'price': 200,
        'rent': variable,
        'group': 'railroad'
    }
}
