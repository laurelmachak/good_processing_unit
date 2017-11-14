import methods, os, re


post_content = methods.get_blog_post('./post_01.txt')
post_id = {'title': post_content[0], 'post_body': post_content[1]}
