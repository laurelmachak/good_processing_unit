# database for all the blog posts
all the posts are saved as .txt files in this directory. This directory also holds all the logic for reading and organizing the post files in the `methods.py` file.

## creating a post:
- the logic in the `methods.py` file will look for any file in this directory with names that start with `post_`. *I am working on making a more dynamic and modular way of doing this in the future* 
- the first line of your `.txt` file will be the title of the post. Everything after that(starting with the second line) will be the content of your post. *the formatting is very simple right now, so i'm currently working on a better way to do this* 

### tl;dr:
- save all new posts as a `.txt` file within the database directory. The filename *must* start with the chars `post_` 
- the first line of your `.txt` file will be the title of the post. Everything after that(starting with the second line) will be the content of your post.


## schema:
the `get_all_posts()` method returns 2lists:
- `all_posts` : a list of dictionary objects . accessed with `get_all_posts()[0]`
- `post_ids_list` : accessed with `get_all_posts()[1]`
