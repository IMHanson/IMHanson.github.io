class Post:
    def __init__(self, post_title, post_type, text_path, **media):
        self.post_title = post_title
        self.post_type = post_type
        
        with open(text_path, 'r') as post_text:
            self.post_text = post_text.read()
