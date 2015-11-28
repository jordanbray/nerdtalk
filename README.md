# Non-Funcitonal Project Warning

This project only does authentication via LDAP, and integration with MongoDB at this exact moment -- nothing else.

Clone at your own peril.

# NerdTalk Application

This project is a chat web application which will (eventually) sync with IRC to provide a nice chat interface that can be locally
hosted.  This project is also to test the limits of the django-nonrel fork, which allows you to use non-relational databases within
the django web framework.  For this project, I've selected mongodb.

This project also uses LDAP as a backend for authentication, so that it can (eventually) manage users for many services, not just one.

## Installation

To install this application, you'll need my forks of django-nonrel (needed for python 3.5 support),
and my fork of mongodb-engine (needed for python 3).

Once you do that, you'll need to edit the nerdtalk/settings.py file to point to your MongoDB database, and your LDAP server.

More installation instructions will follow at some point, maybe.


