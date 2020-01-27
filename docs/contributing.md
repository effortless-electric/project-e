# Contributing

This document should be used as a reference on how to contribute to platform and develop

### Starting an app
Apps should be features, seperately built, localated within ~/project_e
Each app should be linked once in base.py config 

#### Models
Models should have clear concise naming, with snake case
If the data type you are trying to capture exists in a stable package, that field should be used and added to requirements.txt

### Views
Views are the backbone of the application layer in django. They are connecting our backend to the client side code. 
* views should be class based and generic if possible
* Only create a new form if absolutely necessary and another package does not provide the implementation you desire
* Naming should be clear and concise, typically leading with the name of the app, and the functionality you are providing 
* If accessing modifying from your view, do not forget to save the objects afterwards
* Views should be defined below the class, and saved as `as_view()`

### Urls
Urls.py provide the router functionality. This should simply link the created views in the app to new endpoints
urls module should be named the same as the app, allowing re-use through `<app-name>: <view-name>` 
* url parameters should be added only if necessary. If the url is for an object, please add on id as opposed to another field' 
* urls should be concise, and append new values onto their parent url 

### Templates
Templates provide all of the client side code for the user. They are able to both leverage other django templates, and include logic 
directly in the html 
* Logic should be in the views if possible
* don't forget to load static on a new file
* create a new `.scss` file with `static/sass/<app-name>` this will generate a new css change within static 
* add a link to the `.scss` file using the `{% block scss %} {% static 'css/app-name/file-name' %} {% endblock %}` to link properly in base.html


## Submitting Changes

Changes should be committed into your own working branch. 

Commit messages should be clear, concise and in `PRESENT TENSE` 

Once a feature is complete, create a pull request against master, and ensure that the changes you have submitted are all intentional 

#### Naming
<type>: <description> 
Types: 
* feat: a new feature
* fix: fixing an existing bug
* revert: reverting an existing PR 

Description: Should be clear and concise, present tense, and a summary of the changes to submit

Body: 
Main description: describe intention of changes and potential impact
Pictures: document as many changes as possible with before and after
