import re
from pathlib import Path
from random import randint

def find_photos(parent, photo_list=[]):
    parent = Path(parent)
    photos = photo_list
    photo_pattern = '.*(jpe?g|png|webp)'
    
    for child in parent.iterdir():
        if child.is_file():
            if re.match(photo_pattern, child.name):
                photo = str(child).replace('static/', '')
                photos.append(photo)
        elif child.is_dir():
            find_photos(child, photos)
    return photos

secret_path = '/Users/hanson-nordstokke/Documents/Coding/IMHanson/secrets.env'

#####   Pages   #####

adventures = {
    'name': 'adventures',
    'blurb': "Who knows what's gonna happen!",
    'logo': 'logos/navbar/adventure.png'}

music = {
    'name': 'music',
    'blurb': 'listen, learn, play',
    'logo': 'logos/navbar/record-player.png'}

projects = {
    'name': 'projects',
    'blurb': 'making, fixing, restoring',
    'logo': 'logos/navbar/projects.png'}

about = {
    'name': 'about',
    'blurb': 'who am I?',
    'logo': 'logos/navbar/about.png'}

pages = [adventures, music, projects, about]

for page in pages:
    base_path = './static/pictures/page-links/'
    dir_name = f"{page['name']}"
    parent_path = Path(base_path + dir_name)
    pattern = '.*(jpe?g|webp)'
    photo_path = ''

    for file in parent_path.iterdir():
        if re.match(pattern, file.name):
            photo_path = str(file).replace('static/', '')
    page['photo'] = photo_path

#####   Social Media    #####

instagram = {
    'link': 'https://www.instagram.com/ian_the_dryfool/', 
    'logo': 'logos/social-media/instagram.png',
    'name': 'instagram'
    }

youtube = {
    'link': 'https://www.youtube.com/@imhanson-video',
    'logo': 'logos/social-media/youtube.png',
    'name': 'youtube'
    }

tiktok = {
    'link': 'https://www.tiktok.com/@imhanson',
    'logo': 'logos/social-media/tiktok.png',
    'name': 'tiktok'
          }

github = {
    'link': 'https://github.com/imhanson', 
    'logo': 'logos/social-media/github.png', 
    'name': 'github'
          }

social_media = [instagram, youtube, tiktok, github]

#####   About Me    #####

growing_up = {
    'title-text': 'growing up',
    'title-pic': ['posts/about-me/photos/growing-up/skijumping/hanging-out-in-calgary.jpeg', 'hanging out in calgary'],
    'photos': ['posts/about-me/photos/growing-up/me-and-bre-at-the-jones-cabin.jpeg', 'posts/about-me/photos/growing-up/playing-in-the-snow-with-mom-and-bre.jpeg', 'posts/about-me/photos/growing-up/skijumping/hip-xray-after-crash-in-steamboat.jpeg']
}

norway = {
    'title-text': 'norway',
    'title-pic': ['posts/about-me/photos/norway/17.-mai-in-lillehammer.jpg', '17. main in lillehammer'],
    'photos': ['posts/about-me/photos/norway/performing-with-johan-in-lillehammer.jpeg', 'posts/about-me/photos/norway/Longyearbyen.jpg', 'posts/about-me/photos/norway/cabins-somewhere-in-norway.jpeg']
}

studying = {
    'title-text': 'studying',
    'title-pic': ['posts/about-me/photos/studying/fanaråki.jpeg', 'Fanaråki'],
    'photos': ['posts/about-me/photos/studying/xray-of-my-hip-replacement.jpeg', 'posts/about-me/photos/studying/flowers-bøverbreen.jpeg', 'posts/about-me/photos/studying/canoeing-on-tinnsjø.jpeg']
}

climbing = {
    'title-text': 'climbing',
    'title-pic': ['posts/about-me/photos/climbing/guiding_view.jpg', 'view while guiding'],
    'photos': ['posts/about-me/photos/climbing/spotting-wildlife-in-zion-national-park-on-our-honeymoon.jpg', 'posts/about-me/photos/climbing/winter-climbing-near-home.jpg']
}

covid = {
    'title-text': 'life after covid',
    'title-pic': ['posts/about-me/photos/life-after-covid/reel-to-reel-chassis.jpg', 'Reel-to-reel chassis'],
    'photos': ['posts/about-me/photos/life-after-covid/holding-my-baby-boy.jpeg', 'posts/about-me/photos/life-after-covid/finished-building-my-resonator-guitar.jpeg', 'static/posts/about-me/photos/life-after-covid/making-a-guitar-pickup.jpeg']
}

about_me = [growing_up, norway, studying, climbing, covid]

for era in about_me:
    base_path = './static/posts/about-me/'
    era_name = era['title-text'].replace(' ', '-')
    text_path = Path(base_path + 'text')
    photo_path = f'{base_path}photos/{era_name}'
    text_pattern = f'{era_name}.txt'
    era_text = ''
    era_photos = find_photos(photo_path, [])
    era['captions'] = []

    for child in text_path.iterdir():
        if re.match(text_pattern, child.name):
            era_text = child.read_text()
    while len(era['photos']) < 9:
        index = randint(0, len(era_photos)-1)
        if not era_photos[index] in era['photos'] and era_photos[index] != era['title-pic'][0]:
            era['photos'].append(era_photos[index])

    for photo in era['photos']:
        picture_name = Path(photo).name
        name_sans_prefix = re.sub(r'\.(jpe?g|png)', '', picture_name)
        caption = name_sans_prefix.replace('-', ' ').title()
        era['captions'].append(caption)

    era['text'] = era_text
