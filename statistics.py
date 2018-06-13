'''
statistics('story.txt') 
# {'lines': 172, 'words': 2145, 'characters': 11227}
'''
import pdb 

stats = {
    'lines': 0,
    'words': 0,
    'characters': 0,
}

def statistics(filename):
    with open(filename, "r", encoding="UTF-8") as f:
        story_line_list = f.readlines()
        stats['lines'] = len(story_line_list)
        for line in story_line_list:
            stats['characters'] += len(line)
            line_list = line.split(' ')
            stats['words'] += len(line_list)

statistics('story.txt') 
print(stats)
pdb.set_trace()
