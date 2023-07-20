def sort_by_recent_year(movies):
    # Use the 'year' attribute of each movie for sorting in descending order
    sorted_movies = sorted(movies, key=lambda movie: movie['year'], reverse=True)
    return sorted_movies

def sort_by_title_without_articles(movies):
    def remove_articles(title):
        # Remove leading "A", "An", or "The" from the title for sorting
        return title.lstrip("A ").lstrip("An ").lstrip("The ")

    # Use the 'title' attribute of each movie after removing articles for sorting
    sorted_movies = sorted(movies, key=lambda movie: remove_articles(movie['title']))
    return sorted_movies




