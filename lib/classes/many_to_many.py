class Article:
    def __init__(self, author, magazine, title):
        self._author = author  
        self._magazine = magazine  
        self._title = None  # Initialize private attribute title
        self.title = title  # Set title through setter
        self._author.add_article(self)  # Add this article to the author's list
        self._magazine.add_article(self)  # Add this article to the magazine's list

    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, value):
        # Set the title while ensuring immutability (it cannot be changed once set)
        if self._title is not None:
            raise AttributeError("Title cannot be changed once set.")  # Ensure immutability
        # Ensure the title is a string between 5 and 50 characters
        if isinstance(value, str) and 5 <= len(value) <= 50:
            self._title = value
        else:
            raise ValueError("Title must be a string between 5 and 50 characters.")
    
    @property
    def author(self):
        return self._author
    
    @author.setter
    def author(self, value):
         # Ensure that the author is an instance of the Author class
        if isinstance(value, Author):
            self._author = value
        else:
            raise ValueError("Author must be an instance of the Author")
    
    @property
    def magazine(self):
        return self._magazine
    
    @magazine.setter
    def magazine(self, value):
        # Ensure that the magazine is an instance of the Magazine class
        if isinstance(value, Magazine):
            self._magazine = value
        else:
            raise ValueError("Magazine must be an instance of the Magazine")



class Author:
    def __init__(self, name):
        # Initialize the author with a name and an empty list of articles
        if isinstance(name, str) and len(name) > 0:
            self._name = name
        else:
            raise ValueError("Name must be a non-empty string.")
        self._articles = []  # List to store articles
        
    @property
    def name(self):
        return self._name 
    
    def add_article(self, article):
        # Add an article to the author's list of articles
        if isinstance(article, Article):
            self._articles.append(article)
        else:
            raise ValueError("Article must be an instance of the Article.")

    def articles(self):
        return self._articles

    def magazines(self):
         # Return a list of unique magazines that the author has contributed to
        return list(set(article.magazine for article in self._articles))

    def topic_areas(self):
         # Return a list of unique magazine categories that the author has written in
        if not self._articles:
            return None
        return list(set(article.magazine.category for article in self._articles))


class Magazine:
    _all_magazines = []  # Class variable to store all magazine instances

    def __init__(self, name, category):
        self.name = name  # Will use the setter for validation
        self.category = category  # Will use the setter for validation
        self._articles = []  # Initialize the list of articles
        Magazine._all_magazines.append(self)  # Track all magazines
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        # Ensure the name is a string with 2 to 16 characters
        if isinstance(value, str) and 2 <= len(value) <= 16:
            self._name = value
        else:
            raise ValueError("Name must be a string between 2 and 16 characters.")

    @property
    def category(self):
        return self._category
    
    @category.setter
    def category(self, value):
        if isinstance(value, str) and len(value) > 0:
            self._category = value
        else:
            raise ValueError("Category must be a non-empty string.")
    
    def add_article(self, article):
        # Add an article to the magazine's list of articles
        if isinstance(article, Article):
            self._articles.append(article)
        else:
            raise ValueError("Article must be an instance of the Article.")

    def articles(self):
        return self._articles

    def contributors(self):
         # Return a list of unique authors who have contributed to the magazine
        contributors = {article.author for article in self._articles}
        return list(contributors)

    def article_titles(self):
         # Return a list of titles of all articles in the magazine
        if not self._articles:
            return None
        return [article.title for article in self._articles]

    def contributing_authors(self):
         # Return authors who have contributed more than two articles to the magazine
        if not self._articles:
            return None
        author_count = {}
        for article in self._articles:
            author = article.author
            author_count[author] = author_count.get(author, 0) + 1
        # Return authors who have contributed more than two articles, or None if no such authors exist
        return [author for author, count in author_count.items() if count > 2] or None

    @classmethod
    def top_publisher(cls):
        # Class method to return the magazine with the most articles published
        if not cls._all_magazines:
            return None
        return max(cls._all_magazines, key=lambda magazine: len(magazine.articles()))



