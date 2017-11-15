#import methods, os, re

beg_file_name_regex = re.compile(r'post_.*')


path_to_all_db_files = "/Users/Laurel/Desktop/good_processing_unit/flask_server/database"
all_files_in_database = os.listdir(path_to_all_db_files)

post_file_names = []

for file in all_files_in_database:
    if len(beg_file_name_regex.findall(file)) > 0:
        post_file_names.append(file)
print(post_file_names)

post_ids_list = []
all_posts = []

for file in post_file_names:
    post_content = methods.get_blog_post(path_to_all_db_files + '/' + file)
    all_posts.append({'id': len(post_ids_list), 'source': file, 'title': post_content[0], 'post_body': post_content[1]})
    post_ids_list.append(len(post_ids_list))

#post_content = methods.get_blog_post(path_to_all_db_files + '/post_01.txt')
#post_id = {'title': post_content[0], 'post_body': post_content[1]}

#print(post_id)

print(all_posts)