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
    'title-pic': 'posts/about-me/photos/growing-up/snow-cave.jpg'
}

norway = {
    'title-text': 'norway',
    'title-pic': 'posts/about-me/photos/norway/Torghatten.jpeg'
}

studying = {
    'title-text': 'studying',
    'title-pic': 'posts/about-me/photos/studying/fanaråki.jpeg'
}

climbing = {
    'title-text': 'climbing',
    'title-pic': 'posts/about-me/photos/climbing/guiding_view.jpg'
}

covid = {
    'title-text': 'life after covid',
    'title-pic': 'posts/about-me/photos/life-after-covid/reel-to-reel-chassis.jpg'
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
    random_photos = []

    for child in text_path.iterdir():
        if re.match(text_pattern, child.name):
            era_text = child.read_text()
    while len(random_photos) < 16:
        index = randint(0, len(era_photos)-1)
        if not era_photos[index] in random_photos:
            random_photos.append(era_photos[index])

    era['text'] = era_text
    era['photos'] = random_photos
