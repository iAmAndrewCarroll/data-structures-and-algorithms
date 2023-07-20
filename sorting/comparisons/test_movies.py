# Expected test output of test #1
expected1 = ["The Intouchables", "Valkyrie", "Stardust", "Ratatouille", "City of God", "Memento", "The Shawshank Redemption", "Beetlejuice", "Crocodile Dundee", "The Cotton Club"]

# Expected test output of test #2
expected2 = ["Beetlejuice", "City of God", "The Cotton Club", "Crocodile Dundee", "The Intouchables", "Memento", "Ratatouille", "The Shawshank  edemption", "Stardust", "Valkyrie"];

# Test the function
test1 = sort_by_recent_year(movies)
print([movie['title'] for movie in test1])  # Output: ["The Intouchables", "Valkyrie", ..., "The Cotton Club"]

# Test the function
test2 = sort_by_title_without_articles(movies)
print([movie['title'] for movie in test2])  # Output: ["Beetlejuice", "City of God", ..., "Valkyrie"]

# Comparator function for sorting movies by most recent year first
def compare_years_desc(a, b):
    return b['year'] - a['year']

# Comparator function for sorting movie titles alphabetically without articles
def compare_titles_without_articles(a, b):
    def remove_articles(title):
        return title.lstrip("A ").lstrip("An ").lstrip("The ")

    title_a = remove_articles(a['title'])
    title_b = remove_articles(b['title'])

    return 1 if title_a > title_b else (-1 if title_a < title_b else 0)

# Test for compare_years_desc function
assert compare_years_desc(movies[0], movies[1]) == -4
assert compare_years_desc(movies[1], movies[2]) == 10
# Add more tests as needed

# Test for compare_titles_without_articles function
assert compare_titles_without_articles(movies[0], movies[1]) == -10
assert compare_titles_without_articles(movies[1], movies[2]) == -10
# Add more tests as needed
