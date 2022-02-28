# Challenge The 8Agency
Angular | Python | Django
----
This project was carried out based on a slogan provided by The 8 Agency, the Angular framework was used for frontend and Python with Django for backend, for the database mysql was used.

The following tools were used for the development of the project:
- For the deploy, a virtual environment ***venv*** and ***pip*** were created as a package management system.
- For the configuration of the ***Python-decouple*** project with a ***.env*** file.
- The database is stored in a ***MySQL*** database.
- For the web template engine, ***Jinja2*** is used

### Target 
----
To solve this challenge, a project was created that, through the backend, a person interested in participating in an event entered their data, that information was verified to be correct and the fields were mandatory, then it was stored in a MySQL database.

### Installation
----
#### 1 He passed
- ***1 shape***. Click on Code and then on Download Zip 
- ***2 shape***. Create a folder, enter git bash and run

```css
  git clone https://github.com/JuanFernandez87/test_the8agency.git
```

#### 2 He passed
- Create a database with the name the8agency

#### 3 He passed
- Rename the file template.env to .env
- Set password on file .env
- Configure the user in the file .env

#### 4 He passed
- Install virtualenv
```css
pip install virtualenv
```
- Inside the project folder start the virtual environment
```css
virtualenv entornoProyecto
```
- Activate the virtual environment
```css
source entornoProyecto/bin/activate
```
- Install the libraries used
```css
pip install -r requirements.txt
```
#### 5 He passed
- Install Angular in the virtual-invitation folder
```css
npm install -g @angular/cli
```
#### 6 He passed
- In the testApi folder, start the Django server with the command
```css
python3 manage.py runserver
```
#### 7 He passed
- In the virtual-invitation folder, start the Angular server with the command
```css
ng serve 