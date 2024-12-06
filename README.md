## Magazine Article Management System

## Overview
This Python project models a system for managing articles, authors, and magazines. It allows for the creation and management of articles, their authors, and the magazines they are associated with. Key features include:

* Author: An author can write multiple articles and contribute to different magazines.
* Magazine: Magazines can store multiple articles and track contributors.
* Article: Articles are associated with a specific author and magazine, with constraints on their titles to ensure data integrity.
Features

# Article Class:
* Represents an article written by an author for a specific magazine.
* Ensures title immutability, proper validation of the title, and associations with the author and magazine.

# Author Class:
* Represents an author with a name and a list of articles they have written.
* Provides functionality to retrieve all articles written by the author, the magazines they have contributed to, and their topic areas.

# Magazine Class:
* Represents a magazine with a name, category, and a list of articles published in it.
* Tracks contributors and article titles, and can find the magazine with the most articles.

# Requirements
Python 3.x

# Installation
To use this code, simply clone or download the repository and run it with Python.

git clone git@github.com:Shadrack-Kipkemei/python-non-sqlalchemy-code-challenge-articles.git


## Class Details
# Article Class
# Attributes:
* author: The author of the article.
* magazine: The magazine the article is published in.
*title: The title of the article. This must be a string between 5 and 50 characters.

# Methods:
* title: A getter and setter to ensure the title is immutable once set and falls within the required character length.
* author: A getter for the author of the article.
* magazine: A getter for the magazine associated with the article.

## Author Class
# Attributes:
* name: The name of the author.
* articles: A list of articles written by the author.

# Methods:
* add_article: Adds an article to the author's list.
* articles: Returns a list of articles written by the author.
* magazines: Returns a list of unique magazines the author has contributed to.
* topic_areas: Returns a list of unique topic areas (categories) for all articles written by the author.

## Magazine Class
# Attributes:
* name: The name of the magazine.
* category: The category or topic area the magazine covers (e.g., Technology, Health).
* articles: A list of articles published in the magazine.

# Methods:
* add_article: Adds an article to the magazine's list of articles.
* articles: Returns a list of articles published in the magazine.
* contributors: Returns a list of unique authors who have contributed to the magazine.
* article_titles: Returns a list of article titles for the magazine.
* contributing_authors: Returns a list of authors who have contributed more than twice to the magazine.
* top_publisher: A class method that returns the magazine with the most articles.

## Contributing
Feel free to fork the repository, create a branch, and submit a pull request with any improvements or fixes.

## License
The content of this project is licensed under the MIT license Copyright (c) 2024.


