class Article:
    all = []  # Class variable to store all article instances

    def __init__(self, author, magazine, title):
        # Validating input parameters
        if not isinstance(author, Author):
            print("Error: Author must be of type Author.")
        elif not isinstance(magazine, Magazine):
            print("Error: Magazine must be of type Magazine.")
        elif not isinstance(title, str) or not (5 <= len(title) <= 50):
            print("Error: Title must be a string between 5 and 50 characters.")
        else:
            # If validation passes, assign attributes and add to Article.all
            self.author = author
            self.magazine = magazine
            self._title = title
            Article.all.append(self)

    @property
    def title(self):
        # Getter for title
        return self._title

    @title.setter
    def title(self, value):
        # Setter for title with immutability check
        if hasattr(self, '_title'):
            print("Error: Title is immutable once set.")
        elif not isinstance(value, str) or not (5 <= len(value) <= 50):
            print("Error: Title must be a string between 5 and 50 characters.")
        else:
            # If validation passes, set the title
            self._title = value


class Author:
    def __init__(self, name):
        # Validating the name parameter
        if not isinstance(name, str) or len(name) == 0:
            print("Error: Name must be a non-empty string.")
        else:
            # If valid, assign the name to _name
            self._name = name

    @property
    def name(self):
        # Getter for author's name
        return self._name

    @name.setter
    def name(self, value):
        # Setter for author's name with immutability check
        print("Error: Author name is immutable once set.")

    def articles(self):
        # Returns a list of articles written by the author
        return [article for article in Article.all if article.author == self]

    def magazines(self):
        # Returns a list of unique magazines the author has written for
        return list({article.magazine for article in self.articles()})

    def add_article(self, magazine, title):
        # Adds a new article to the magazine with the given title
        return Article(self, magazine, title)

    def topic_areas(self):
        # Returns the topic categories of the magazines the author writes for
        if not self.magazines():
            return None
        return list({magazine.category for magazine in self.magazines()})


class Magazine:
    def __init__(self, name, category):
        # Validating the name and category parameters
        if not isinstance(name, str) or not (2 <= len(name) <= 16):
            print("Error: Name must be a string between 2 and 16 characters.")
        elif not isinstance(category, str) or len(category) == 0:
            print("Error: Category must be a non-empty string.")
        else:
            # If valid, assign the name and category
            self._name = name
            self._category = category

    @property
    def name(self):
        # Getter for magazine name
        return self._name

    @name.setter
    def name(self, value):
        # Setter for magazine name with validation
        if not isinstance(value, str) or not (2 <= len(value) <= 16):
            print("Error: Name must be a string between 2 and 16 characters.")
        else:
            self._name = value

    @property
    def category(self):
        # Getter for category
        return self._category

    @category.setter
    def category(self, value):
        # Setter for category with validation
        if not isinstance(value, str) or len(value) == 0:
            print("Error: Category must be a non-empty string.")
        else:
            self._category = value

    def articles(self):
        # Returns a list of articles published in the magazine
        return [article for article in Article.all if article.magazine == self]

    def contributors(self):
        # Returns a list of unique authors who have contributed to the magazine
        return list({article.author for article in self.articles()})

    def article_titles(self):
        # Returns a list of titles of the articles published in the magazine
        titles = [article.title for article in self.articles()]
        return titles if titles else None

    def contributing_authors(self):
        # Returns a list of authors who have contributed more than 2 articles to the magazine
        author_counts = {}
        for article in self.articles():
            author_counts[article.author] = author_counts.get(article.author, 0) + 1
        contributors = [author for author, count in author_counts.items() if count > 2]
        return contributors if contributors else None
