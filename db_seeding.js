p = {
    'firstname': 'John',
    'lastname': 'Milton',
    'role': ["author"],
    'location': {
        'address': '15th Golden Avenue',
        'city': 'London'
    },

};
db.people.insert(p);

p1 = {
    'firstname': 'Harry',
    'lastname': 'Potter',
    'role': ["contributor"],
    'location': {
        'address': 'Movies Studio 12',
        'city': 'New York'
    },

};
db.people.insert(p1);
