# Milestone 3 - Your Recipe Hub - by Kevin Bourke

This project is a recipe website where users can search for recipes via text search or categories. If they wish they can also submit their own recipes to the site. There many sites in existence that have this kind of functionailty already, such as Kitchen Stories and Allrecipes.

## UX

I wanted the site to have 2 main features.
 - [x] Users should be able to browse or search the site for recipes.
 - [x] If they would like, users should be able to upload their own recipes.

### User Stories

This section provides insight into the UX process, focusing on who this website is for, what it is that they want to achieve and how this project is the best way to help them achieve these things.  

#### As a User

 

#### As a developer




### Strategy

The goals of this type of website are to:

1. 

### Scope

This section determines what the users should be able to do on the website. Users should be able to:

1. 

### Structure

To list the pages I needed and to visialise the site structure, I designed my visual sitemap in Gloomap. In the sitemap below, the pages marked in green represent site User (logged in) pages:

![Sitemap](README_resources/gloomap-sitemap.png)

I also listed out the features I wanted on the homepage.

### Skeleton

I sketched up some very rough ideas on paper and then designed the final wireframes, which were created in Balsamiq:

- [Home page on desktop wireframe](README_resources/wireframes/homepage-desktop.png)
- [Home page on mobile wireframe](README_resources/wireframes/homepage-mobile.png)
- [All Recipes on desktop wireframe](README_resources/wireframes/all-recipes-desktop.png)
- [All Recipes on mobile wireframe](README_resources/wireframes/all-recipes-mobile.png)
- [Recipe page on desktop wireframe](README_resources/wireframes/recipe-page-desktop.png)
- [Recipe page on mobile wireframe](README_resources/wireframes/recipe-page-mobile.png)
- [Add Recipe on desktop wireframe](README_resources/wireframes/add-recipe-desktop.png)
- [Add Recipe on mobile wireframe](README_resources/wireframes/add-recipe-mobile.png)
- [Recipes Category on desktop wireframe](README_resources/wireframes/category-recipes-desktop.png)
- [Recipes Category on mobile wireframe](README_resources/wireframes/category-recipes-mobile.png)
- [Sign up on desktop wireframe](README_resources/wireframes/sign-up-desktop.png)
- [Sign up on mobile wireframe](README_resources/wireframes/sign-up-mobile.png)

There is also a login page which is very similar to the sign up page except with no email field and different intro text, and also an Edit Recipe page which is basically identical to Add Recipe except the values are pre-populated from the database.

### Surface

Green stands for nature and growth, and . It is also a literal representation of healthy foods, like vegetables and salads.
https://99designs.ie/blog/tips/color-psychology/
https://99designs.ie/blog/creative-inspiration/color-combinations/

### Database Schema

Based on the functionality required and the data to be stored, I created my database structure. The Recipe and Categories documents (or tables) would have fields of the same name, so a recipe can be saved to a course type and a category.

![Schema](README_resources/recipe-app-DB-diagram.png)

## Technologies Used

### Languages and Frameworks
1. HTML
2. CSS
3. Javascript 
4. Python
5. [Flask Framework](https://palletsprojects.com/p/flask/)
6. Jinja templating for Python
4. [Bootstrap Framework](https://getbootstrap.com/)
5. [Font Awesome](https://fontawesome.com/)
6. Google Fonts
9. [JQuery](https://jquery.com) - The project uses **JQuery** to simplify DOM manipulation, and animation of certain elements.

### Tools Used
1. [VS Code](https://code.visualstudio.com/) and [Brackets](http://brackets.io/) code editors.
2. [Git](https://git-scm.com/) - Installed on local devices and integrated with VS Code and Brackets, to allow version control.
3. [GitHub](https://github.com/) - Used a repository for the project files and previous versions. Also used to deploy the website.
4. [Balsamiq](https://balsamiq.com/) - Used for creating wireframes for different variations and different screen sizes.
5. I used Photoshop and Illustrator for image and svg manipulation.
6. [TinyPNG](https://tinypng.com/) - To keep transparent png sizes to a minimum I used the online png compressing service [TinyPNG](https://tinypng.com/), as well as the desktop application.
7. [Coolor](https://coolors.co/) - Used top help determine the colour scheme.
8. [The Padwan Project](https://github.com/Eventyret/Padawan) - While I did not use this tool to generate my project's starting point as I started with [Code Institute's Full template](https://github.com/Code-Institute-Org/gitpod-full-template), I did use it as a reference.
9. [Gloomaps](https://www.gloomaps.com/) - For creating my sitemap.


## Features
 
### Existing Features


#### Minor Features
Expand the sections below for more info on details

<details>
  <summary><strong>Responsive images</strong></summary>
As the recipe images are provided by external users I could not make these smaller for mobile.
To allow me to use a different image for the 'no recipe image' for mobile I used the `<picture>` element. This allowed me to create a smaller image just for a mobile.
</details>

<details>
  <summary><strong>Skip to main content</strong></summary>

 There is a 'Skip to main content' link just inside the body tag for accessibility for screenreaders. The main content is not usually the first thing on a web page. Keyboard and screen reader users generally must navigate a long list of navigation links, sub-lists of links, corporate icons, site searches, and other elements before ever arriving at the main content. This is then hidden from view with the bootstrap class 'sr-only', however when it receives focus from keyboard it becomes visible, by basically reversing the Bootstrap CSS properties on focus. This is based on accessibility recommendations from https://webaim.org/techniques/skipnav/. This can be checked by pressing tab when a pages loads.
 </details>

##### Form input count
The text area fields have a max number of characters allowed so I added a simple JavaScript character count on input to give the user an idea of how many characters they have used. This was based on references from [w3schools oninput](https://www.w3schools.com/jsref/event_oninput.asp) and [w3schools output](https://www.w3schools.com/tags/tag_output.asp).

### Features to consider implementing in the future

1. 

## Testing

Please see [Testing Document](TESTING.md) for all my testing


## Deployment



To run locally, you can clone this repository directly into the editor of your choice by pasting `git clone https://github.com/Bourkekev/ms3-your-recipe-hub.git` into your terminal. To cut ties with this GitHub repository, type `git remote rm origin` into the terminal.



## Issues I had to overcome

### Formatting of Ingredients and method

I wanted my ingredients on different lines, as they are easier to read and then I could style them a bit nicer, but when my Ingredients were output it was all in what looked like one paragraph with no line breaks. I thought it was to do with the input field not saving the line breaks. But after going down the wrong path with that, it turned out the ingredients just needed the CSS property 'white-space' set to pre-wrap.

### Delete category in modal window was deleting the wrong category.

I wanted to warn the user about the deletion of a category by having a pop-up warning, otherwise it just happened as soon as they press the delete button. But when I first had the delete button in the pop-up it was deleting the first category and not the one I clicked. This worked fine for the delete recipe button, but that was a single page and not looping through the recipes. The problem was that the modal had to be inside the 'categories' loop or I could not get the category id to tell it which category to delete. But this then generated multiple modals with the id of 'delete-category', which is what the modal trigger (Delete button) was looking for. But it comes across the first `id="delete-category` which contains the first category on the page, and deletes that one.

So my first thought was to pass the category name into the modal id so like `<div id="delete-{{category.category_name}}"`. However this leads to an issue where, because the category can be entered by a user, the html ID for this can have spaces and odd characters, and also might not be unique, I might have multiple categories with the same name, hence the duplicate ID issue for the modal again. 

So I knew I need something unique that users do not have control over, so the category id is what I used and it works for this modal with no duplications.

## Credits and References

### Design and Research
 I took inspiration for this site from the following places:
 - 

### Technical
 - For general references for Python and Flask I used my Code Institue notes, [MDN web docs](https://developer.mozilla.org/en-US/), [w3schools](https://www.w3schools.com/js/default.asp), [Python Offical Docs](https://www.python.org/doc/).
 - For Python's datetime formatting I referenced https://www.programiz.com/python-programming/datetime/strftime
 - Form field character count - [w3schools oninput](https://www.w3schools.com/jsref/event_oninput.asp) and [w3schools output](https://www.w3schools.com/tags/tag_output.asp).
 
### Content


 
### Media
- The photos and vectors (except logo) used in this site were obtained from:

 - Ha'Penny Bridge - [Shutterstock](https://www.shutterstock.com/g/madrugadaverde)
 - Fictional logo was designed on https://www.freelogodesign.org/

 - The favicons were generated at https://realfavicongenerator.net/



### Acknowledgements

 - Thanks to my mentor Anthony Ngene for his suggestions and his time.
 - [Simen Daehlin](https://github.com/Eventyret) - [The Padwan Project](https://github.com/Eventyret/Padawan)
 - Thanks to those on Slack for reviewing my project and making suggestions.