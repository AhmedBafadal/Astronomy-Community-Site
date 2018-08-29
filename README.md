
# Astro-Space.com



## Description

An astronomy community site developed with Python using the Django web framework, as well as HTML, CSS and Javascript.

The 'Astro-Space' web app enables registered users create their own groups to publish posts on various topics related to space and astronomy (e.g. SpaceX,NASA, Pluto) as well as subscribe to existing groups and view posts submitted by others.

All posts are timestamped, and users can publish and delete posts on any existing group, as well as leave and join the respective groups at any time.



## Implementation

It is possible to view all posts, groups and group members without signing up. However, please note that upon registration any username or group name created must be unique.

Users are identified by an '@' handle, and clicking the user's hyperlink displays a list of the their entire post history, as well as the group associated with each post.

Once registered, clicking 'Post' on the navigation bar enables the user to publish a new post within any existing group. 

Clicking 'Groups' enables the user to view an interactive list of all existing groups, including a count of the number of members and posts published within each group, as well as the option to create a new group. Within the 'Groups' page, logged in users can also click on their own username to gain access to their own post history.



## Installation

```
pip install django
pip install pillow
pip install bcrypt
pip install argon2_cffi
pip install django-bootstrap3
pip install misaka

python manage.py migrate
python manage.py runserver
```
