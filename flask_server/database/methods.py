def dummy_text():
    return """and that this thought of the end and advantage is even
stronger than its strongest impulse not to be tempted to inexpedient
activities by its impulses that is its wisdom and inspiration In
comparison with the ignoble nature the higher nature is more
irrational for the noble magnanimous and self sacrificing person
succumbs in fact to his impulses and in his best moments his reason
lapses altogether An animal which at the risk of life protects its
young or in the pairing season follows the female where it meets with
death does not think of the risk and the death its reason pauses
likewise because its delight in its young or in the female and the
fear of being deprived of this delight dominate it exclusively it
becomes stupider than at other times like the noble and magnanimous
person He possesses feelings of pleasure and pain of such intensity
that the intellect must either be silent before them or yield itself to
their service his heart then goes into his head and one henceforth"""

def get_blog_post(filename):
    ''' reads the content from a text file
    and returns 2 item tuple
    containing the title and post '''
    with open(filename,'r') as f:
        content = f.readlines()
        title = content[0].strip()
        post = " ".join(content[1:])
        post.replace("\n", " ")
    return title, post


get_blog_post('./database/post_01.txt')

class BlogPost (object):
    def __init__(self, title, content, author="anonymous"):
        pass

    