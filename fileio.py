'''
copy_and_reverse('story.txt', 'story_reversed.txt') # None
# expect the contents of story_reversed.txt to be the reverse of the contents of story.txt
'''

# def copy_and_reverse(org_file, new_file):
#     with open(org_file, encoding="utf8") as orgf:
#         data = orgf.readlines()
#         # print(data)
#     with open(new_file, 'w') as new:
#         data.reverse()
#         for line in data:
#             new.write(line)

def copy_and_reverse(file_name, new_file_name):
    with open(file_name, encoding="utf8") as file:
        text = file.read()
 
    with open(new_file_name, "w") as new_file:
        new_file.write(text[::-1])

copy_and_reverse('story.txt', 'story_reversed.txt') 
