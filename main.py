import json
import requests
import mechanize
import re
import random
import datetime

time = datetime.datetime.now()

default = {
    'year_min': '1930',
    'year_max': '2010',
    'gender': 'both',
    'path_to_save_img': 'generated_img.png',
    'parents': 'True',
    'fav_music_genre': 'False',
    'fav_sport': 'True',
    'fav_tv_show': 'False',
}


def start():
    print('                               _     _            _   _ _         ')
    print('                              (_)   | |          | | (_) |        ')
    print('  _ __   _____      __         _  __| | ___ _ __ | |_ _| |_ _   _ ')
    print(' | \'_ \ / _ \ \ /\ / /        | |/ _` |/ _ \ \'_ \| __| | __| | | |')
    print(' | | | |  __/\ V  V / ______  | | (_| |  __/ | | | |_| | |_| |_| |')
    print(' |_| |_|\___| \_/\_/ |______| |_|\__,_|\___|_| |_|\__|_|\__|\__, |')
    print('                                                             __/ |')
    print('                                                            |___/ \n')
    print('Type \'help\' for a list of commands\n')


start()


def restore_variables_to_default():
    variables = open("variables.json", "w")
    json.dump(default, variables)
    print('Variables restored to the default values')


def generate_img():
    img_link = requests.get("https://thispersondoesnotexist.com/image")
    file = open(variables['path_to_save_img'], "wb")
    file.write(img_link.content)
    file.close()
    print('Image generated')


def generate_city():
    br = mechanize.Browser()
    br.open('https://randomcity.net')
    city = re.sub("Random Cities - ", "", br.title())
    print('Lives in: {}'.format(city))


json_file = open("variables.json")
variables = json.load(json_file)
json_file.close()

first_name_load = open('name.json')
first_name_load = json.load(first_name_load)

surnames_both = open('name_both.json')
surnames_both = json.load(surnames_both)

surnames_m = open('m_names.json')
surnames_m = json.load(surnames_m)

surnames_f = open('f_names.json')
surnames_f = json.load(surnames_f)

occupation = open('jobs.json')
occupation = json.load(occupation)

fav_music_genre = open('music_genre.json')
fav_music_genre = json.load(fav_music_genre)

fav_sport = open('sports.json')
fav_sport = json.load(fav_sport)

fav_tv_show = open('tv_shows.json')
fav_tv_show = json.load(fav_tv_show)


while True:
    usr_input = input('\n> ').lower()
    if usr_input == 'new' or usr_input == 'generate':
        if variables['gender'] == 'both':
            first_name = random.sample(first_name_load, 1)
            full_name = str(random.sample(surnames_both, 1) + first_name)
            print('Name: {}'.format(re.sub(']|,|\'|\[|', '', full_name)))
        elif variables['gender'] == 'male':
            first_name = random.sample(first_name_load, 1)
            full_name = str(random.sample(surnames_m, random.randint(1, 2)) + first_name)
            print('Name: {}'.format(re.sub(']|,|\'|\[|', '', full_name)))
        elif variables['gender'] == 'female':
            first_name = random.sample(first_name_load, 1)
            full_name = str(random.sample(surnames_f, random.randint(1, 2)) + first_name)
            print('Name: {}'.format(re.sub(']|,|\'|\[|', '', full_name)))

        birth_year = time.year - random.randint(int(variables['year_min']), int(variables['year_max']))

        if (birth_year > 18) is True:
            job = str(random.sample(occupation, 1))
            print('Occupation: {}'.format(re.sub(']|,|\'|\[|', '', job)))
        else:
            print('No occupation')

        print('Date of birth: {}.{}.{} (dd.mm.yyyy)'.format(random.randint(1, 31), random.randint(1, 12), time.year - birth_year))

        first_name = str(first_name)
        first_name = re.sub(']|,|\'|\[|', '', first_name)

        if variables['parents'] == 'True':
            mother_sur = str(random.sample(surnames_f, 1))
            mother_sur = re.sub(']|,|\'|\[|', '', mother_sur)
            father_sur = str(random.sample(surnames_m, 1))
            father_sur = re.sub(']|,|\'|\[|', '', father_sur)
            print('Mother: {} {}'.format(mother_sur, first_name))
            print('Father: {} {}'.format(father_sur, first_name))

        generate_city()

        if variables['fav_music_genre'] == 'True':
            str_fav_music = str(random.sample(fav_music_genre, 1))
            print('Favourite music genre: {}'.format(re.sub(']|,|\'|\[|', '', str_fav_music)))

        if variables['fav_sport'] == 'True':
            str_fav_sport = str(random.sample(fav_sport, 1))
            print('Favourite sport: {}'.format(re.sub(']|,|\'|\[|', '', str_fav_sport)))

        if variables['fav_tv_show'] == 'True':
            str_fav_tv = str(random.sample(fav_tv_show, 1))
            print('Favourite tv show: {}'.format(re.sub(']|,|\'|\[|', '', str_fav_tv)))

    if usr_input == 'default' or usr_input == 'restore':
        restore_variables_to_default()

    if usr_input == 'img' or usr_input == 'image' or usr_input == 'photo':
        generate_img()

    if usr_input == 'help':
        print('\nnew - generates a new \'identity\'')
        print('img - generates a image of a person that does not exist (thispersondoesnotexist.com)')
        print('default - restores all the variables to their initial value')
        print('\n-------------------\n')
        print('variables.json')
        print('year_min and year_max - sets between what values to generate the birth year')
        print('gender - both: mixed names, male: male names, female: female names')
        print('path_to_save_img - the path where to save the generated img')
        print('parents - generate parents name')
        print('fav_music_genre - random music genre')
        print('fav_sport - random sport')
        print('fav_tv_show - random tv show\n')
