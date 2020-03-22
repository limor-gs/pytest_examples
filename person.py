#version 1
class Person:
    def __init__(self, name, favorite_color, year_born):
        self.name = name
        self.favorite_color = favorite_color
        self.year_born = year_born
        self.friends = set()

    def add_friend(self, other_person):
        if not isinstance(other_person, Person): raise TypeError(other_person, 'is not a', Person)
        self.friends.add(other_person)
        other_person.friends.add(self)

    def __repr__(self):
        return f'Person(name={self.name!r}, '  \
               f'favorite_color={self.favorite_color!r}, ' \
               f'year_born={self.year_born!r}, ' \
               f'friends={[f.name for f in self.friends]})'
               
