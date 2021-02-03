# recipebox-v1

Django is the most popular Python web framework for making user-facing applications, and it's easy to see why. With the famous tagline of "batteries included" and thousands of plugins on PyPI, it makes sense that you can find it in a lot of platforms.

*   The entirety of Instagram is a single monolithic Django app; as of 2016, they leveraged over 50k instances of their software on over 12k machines
*   The grand majority of the Washington Post
*   Most of USA Today and accompanying sites
*   All of Mozilla's support / documentation sites (all that Javascript documentation you were reading a few months ago? That was Django talking!)
*   Disqus comments; the plug-and-play comment system is the most popular system of its type, and it's one giant Django app
*   Most of Atlassian Bitbucket, a competitor to GitHub and Gitlab
*   The entirety of Eventbrite
*   The question-and-answer site Quora

Most of these won't advertise that they're looking for "django developers" because they want to make sure that people can work with their stack; instead, they'll focus on finding "python developers". It's up to us to learn how to leverage Django and its vast ecosystem to handle different types of applications.

#### **Your Task**

For our introduction, we want to get familiar with creating a new Django application. Create a new application that serves recipes from different authors, much like our demo application does for news. Intended layout:

*   An index page that lists all titles of the loaded recipes (they don't have to be real recipes; just fill them with lorem ipsum and some numbers.)
*   Each title is a link that takes you to a single page with the content of that recipe.
*   Each detail view for a recipe has the author name, along with all the information for the recipe arranged in a reasonable format.
*   Clicking on the author's name should take you to an Author Detail page, where you can see a list of all the recipes that the Author has contributed to.
*   Make editing all of the models accessible through the admin panel only.

So we have three types of pages: a simple list view, a recipe detail view, and an author detail view. The admin panel will handle the creation views, so we don't need to worry about that.

**Important Info:**

*   Python 3.9, latest version of Django (3.1.2 as of this writing)
*   Start a project with `django-admin startproject {project name} .` -- note the period at the end! (for example, `django-admin startproject recipebox .`)
*   Start an app with `python manage.py startapp {app name}` (for example, `python manage.py startapp recipe_app`)
*   Start the server with `python manage.py runserver`
*   After you create your models, run `python manage.py makemigrations {foldername}` (where foldername is the top-level folder for your project) to create them, then `python manage.py migrate` to push them to the db. If you get stuck, delete the db and run the command again
*   If you change your models after running the migrations, run makemigrations and migrate again. If the migrations require the creation of a new table, django will automatically handle it
*   Create an admin user by running `python manage.py createsuperuser`
*   Don't go crazy on the front end. The goal is to just handle the database interactions and basic view path
*   Make sure that every detail page (author and recipe) has its own unique URL. If you reload the URL, the same page should appear -- no modals or manipulating the current information on the page. That's too complicated for what we're trying to achieve.
*   REITERATING: There are no extra points for pretty HTML! Don't spend time making everything on the front end look gorgeous; we just want to make sure we're serving the right information.
*   Please don't commit any extraneous files! It's best practice to use a .gitignore file to keep a clean repository. In this project, a .gitignore file is already included.  For future projects, always confirm that a .gitignore file exists in the root directory of your project including the following contents:
* <details>
   <summary markdown="span">.gitignore contents</summary>
   <pre>
   # Inspired by https://www.toptal.com/developers/gitignore/api/venv,linux,macos,django,python,visualstudiocode,pycharm
  # Django
  *.log
  *.pot
  *.py[cod]
  *$py.class
  __pycache__/
  local_settings.py
  db.sqlite3
  db.sqlite3-journal
  # pyenv
  .python-version
  # Environments
  .env
  .venv
  env/
  venv/
  ENV/
  env.bak/
  venv.bak/
  ### VisualStudioCode ###
  .vscode/
  !.vscode/settings.json
  !.vscode/tasks.json
  !.vscode/launch.json
  !.vscode/extensions.json
  *.code-workspace
  .history
  ### PyCharm ###
  .idea/
  ### macOS ###
  # General
  .DS_Store
  ### Linux ###
  *~
  # temporary files which can be created if a process still has a handle open of a deleted file
  .fuse_hidden*
  # KDE directory preferences
  .directory
  # Linux trash folder which might appear on any partition or disk
  .Trash-*
  # .nfs files are created when an open file is removed but is still being accessed
  .nfs*   
  # C extensions
  *.so
  # Distribution / packaging
  .Python
  build/
  develop-eggs/
  dist/
  downloads/
  eggs/
  .eggs/
  lib/
  lib64/
  parts/
  sdist/
  var/
  wheels/
  pip-wheel-metadata/
  share/python-wheels/
  *.egg-info/
  .installed.cfg
  *.egg
  MANIFEST   
  # PyInstaller
  #  Usually these files are written by a python script from a template
  #  before PyInstaller builds the exe, so as to inject date/other infos into it.
  *.manifest
  *.spec 
  # Installer logs
  pip-log.txt
  pip-delete-this-directory.txt  
  # Unit test / coverage reports
  htmlcov/
  .tox/
  .nox/
  .coverage
  .coverage.*
  .cache
  nosetests.xml
  coverage.xml
  *.cover
  *.py,cover
  .hypothesis/
  .pytest_cache/  
  # Translations
  *.mo
  *.pot
  # Flask stuff:
  instance/
  .webassets-cache   
  # Scrapy stuff:
  .scrapy
  # Sphinx documentation
  docs/_build/  
  # PyBuilder
  target/    
  # Jupyter Notebook
  .ipynb_checkpoints
  # IPython
  profile_default/
  ipython_config.py 
  # PEP 582; used by e.g. github.com/David-OConnor/pyflow
  __pypackages__/   
  # Celery stuff
  celerybeat-schedule
  celerybeat.pid  
  # SageMath parsed files
  *.sage.py
  # Spyder project settings
  .spyderproject
  .spyproject
  # Rope project settings
  .ropeproject
  # mkdocs documentation
  /site
  # mypy
  .mypy_cache/
  .dmypy.json
  dmypy.json
  # Pyre type checker
  .pyre/
  </pre>
</details>

Author model:

*   Name (CharField)
*   Bio (TextField)

Recipe Model:

*   Title (CharField)
*   Author (ForeignKey)
*   Description (TextField)
*   Time Required (Charfield) (for example, "One hour")
*   Instructions (TextField)

<span style="text-decoration: underline;">Note</span>: Follow PEP8 naming conventions with your models and field names. An easy way to check is by looking at examples of code in Django's docs --> [https://docs.djangoproject.com/en/3.0/topics/db/models/#quick-example](https://docs.djangoproject.com/en/3.0/topics/db/models/#quick-example)

If you have any questions or get stuck at any point, don't hesitate to ask. Welcome to a new side of web development!

#### **Submission**

Push up your code to your main branch and submit the link to the repo.

<pre>https://github.com/kenzie-se-q4/recipebox-v1/&ltgithub_username&gt</pre>
