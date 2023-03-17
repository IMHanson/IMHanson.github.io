class Page:
    def __init__(self, name, photo=None, blurb=None, logo=None):
        self.name = name
        self.photo = photo
        self.blurb = blurb
        self.logo = logo
    
    def photo(self):
        return self.photo

    def set_photo(self, new_photo):
        self.photo = new_photo

    def blurb(self):
        return self.blurb
    
    def set_blurb(self, new_blurb):
        self.blurb = new_blurb

    def logo(self):
        return self.logo
    
    def set_logo(self, new_logo):
        self.logo = new_logo


######   Pages  #####
adventures = Page('adventures','pictures/climbing/kandersteg.jpg', "Who knows what's gonna happen!", 'logos/adventure-logo.png')

music = Page('music', 'pictures/music/rhodes-keybed.jpg', 'listen, learn, play', 'logos/projects-logo.png')

projects = Page('projects', 'pictures/misc/sailboat-sketch.jpg', 'making, fixing, restoring', 'logos/projects-logo.png')

about_me = Page('about', 'pictures/climbing/skeissfjell.jpg', 'Who am I?', 'logos/ian-logo.png')


#####   Dictionaries    #####
pages = {}
page_photo = {}
page_blurb = {}
page_logo = {}

def add_page(new_page):
    name = new_page.name
    pages[name] = new_page

add_page(adventures)
add_page(music)
add_page(projects)
add_page(about_me)

for key, val in pages.items():
    page_photo[key] = val.photo
    page_blurb[key] = val.blurb
    page_logo[key] = val.logo
