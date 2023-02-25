import spacy


def watch_next(description: str):
    """Returns the title of a movie from 'movies.txt' whose description is most similar to 'description'."""
    nlp = spacy.load('en_core_web_md')

    # Reading in movie descriptions to compare
    with open("movies.txt", "r", encoding="utf-8") as movies:
        movie_descriptions = movies.read().split("\n")

    # Dict to hold titles and similarity scores
    movie_titles = {}

    for index, movie in enumerate(movie_descriptions):

        # Correcting for blank lines in movies.txt
        if movie.strip() == "":
            movie_descriptions.pop(index)

        # Performing similarity analysis
        else:
            title = movie.split(" :")[0]
            movie_descriptions[index] = movie.split(" :")[1]

            movie_titles[title] = nlp(movie).similarity(nlp(description))

    for title in movie_titles:
        if movie_titles[title] == max(movie_titles.values()):
            return title


description_to_compare = "Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a planet where the Hulk can live in peace. Unfortunately, Hulk land on the planet Sakaar where he is sold into slavery and trained as a gladiator."

recommended = watch_next(description_to_compare)

print(f"The description for '{recommended}' is most similar to the description for 'Planet Hulk'")
