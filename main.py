import mechanicalsoup
import wget
import os

browser = mechanicalsoup.StatefulBrowser()
base_url = 'https://www.google.com/imghp?hl=EN'

browser.open(base_url)

# select form
browser.select_form()
# browser.get_current_form().print_summary()

# image to search
search_term = 'robot'
browser['q'] = search_term

# browser.launch_browser()
response = browser.submit_selected()

new_url = browser.get_url()
browser.open(new_url)

# get HTML
page = browser.get_current_page()
all_images = page.find_all('img')

image_source = []
for img in all_images:
    img = img.get('src')
    if img.startswith('https'):
        image_source.append(img)

path = os.getcwd()
path = os.path.join(path, search_term + 's')

os.mkdir(path)

# download images
counter = 1

for img in image_source:
    save_as = os.path.join(path, search_term + str(counter) + '.jpg')
    wget.download(img, save_as)
    counter += 1

print('Done!')
