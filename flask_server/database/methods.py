import os, re

def get_blog_post(filename):
    ''' reads the content from a text file
    and returns 2 item tuple
    containing the title (line 1) and post (rest of content) 
    as strings '''
    with open(filename,'r') as f:
        content = f.readlines()
        title = content[0].strip()
        post = " ".join(content[1:])
        post.replace("\n", " ")
    return title, post


#get_blog_post('./database/post_01.txt')


def get_all_posts():
    CWD = os.getcwd()
    beg_file_name_regex = re.compile(r'post_*')
    path_to_all_db_files = CWD + "/database"
    all_files_in_db = os.listdir(path_to_all_db_files)
    
    post_file_names = []
    for file in all_files_in_db:
        if len(beg_file_name_regex.findall(file)) > 0:
            post_file_names.append(file)
            
    post_ids_list = []
    all_posts = []
    
   
    
    for file in post_file_names:
        post_content = get_blog_post(path_to_all_db_files + '/' + file)
        all_posts.append({'id': len(post_ids_list), 'source': file, 'title': post_content[0], 'post_body': post_content[1]})
        post_ids_list.append(len(post_ids_list))
    
    return all_posts, post_ids_list

def create_post_file(title,body):
    existing_posts = get_all_posts()[0]
    post_id = len(existing_posts) + 1
    path_to_all_db_files = "/Users/Laurel/Desktop/good_processing_unit/flask_server/database"
    filename = "post_" + str(post_id) + ".txt"
    with open(path_to_all_db_files + "/" + filename, 'w') as f:
        f.write(title + "\n")
        f.write(body)


    