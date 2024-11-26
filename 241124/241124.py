oscar_winners = {"Leonardo DiCaprio", "Meryl Streep", "Denzel Washington", "Emma Stone", "Tom Hanks", "Natalie Portman", "Robert De Niro", "Al Pacino"}
titanic_actors = {"Leonardo DiCaprio", "Kate Winslet", "Billy Zane", "Kathy Bates"}
dark_knight_actors = {"Christian Bale", "Heath Ledger", "Michael Caine", "Gary Oldman", "Aaron Eckhart"}
avengers_actors = {"Robert Downey Jr.", "Chris Evans", "Scarlett Johansson", "Mark Ruffalo", "Chris Hemsworth", "Jeremy Renner"}
iron_man_actors = {"Robert Downey Jr.", "Gwyneth Paltrow", "Terrence Howard"}
legendary_actors = {"Al Pacino", "Robert De Niro", "Marlon Brando", "Jack Nicholson", "Dustin Hoffman"}
actor_list = {"Robert Downey Jr.", "Chris Evans", "Scarlett Johansson", "Leonardo DiCaprio", "Tom Hanks"}
movie_cast = {"Tom Hanks", "Tom Cruise", "Will Smith", "Matt Damon", "Brad Pitt"}

# Exercise
oscar_winners.add("Emma Watson")

oscar_winners2 = oscar_winners.copy()
oscar_winners2.remove("Meryl Streep")
oscar_winners2.clear()

print(titanic_actors & dark_knight_actors)

print("yes" if avengers_actors & iron_man_actors else "no")

print("yes" if actor_list <= oscar_winners else "no")

movie_cast.pop()

movie_cast.discard("Matt Damon")

print(titanic_actors - oscar_winners)

print(titanic_actors ^ dark_knight_actors)

oscar_winners.update({"Blanchett Cate", "Lewis-Day Daniel"})

print(titanic_actors.union(dark_knight_actors))
