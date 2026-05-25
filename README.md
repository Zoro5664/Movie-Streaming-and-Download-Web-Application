# StreamFlex
StreamFlex is a web application that allows users to watch and download movies and their associated trailer. The application is built using the Django framework and utilizes a MySQL database to store movie information.

## Installation
1.Clone the repository: 
```bash
git clone https://github.com/arjun0084/movie
```
2.Install the required dependencies: 
```bash
pip install django
```
3.Create a MysqlSQL database and update the database settings in ```settings.py```

4.Run database migrations:
```bash
python manage.py migrate
```
5.Create a superuser to access the admin controls:
```bash
python manage.py createsuperuser
```
Start the development server: python manage.py runserver
## Usage
Navigate to ```http://localhost:8000``` in your web browser.

Browse the list of movies.

Click the ```Trailer``` button to Watch trailer of the movie.

Click the ```Watch``` button to start streaming the movie.

Click the ```Download``` button to download movie to your pc.

Log in as a superuser to access the admin controls and manage movie data.

To log in as a superuser, run 
```bash
python manage.py createsuperuser
```
 to create a superuser account. 

Then, navigate to ```http://localhost:8000/admin``` and enter your superuser credentials to access the admin controls.

## Contributing
If you'd like to contribute to StreamFlex, please fork the repository and create a new branch for your changes. Once you've made your changes, submit a pull request and we'll review your changes.

## Credits
StreamFlex was created by the following developers:

[Sumit Pawar](https://github.com/sp0759)

[Kshitij Lavhe](https://github.com/arjun0084)

[Jayesh Pawar](https://github.com/jayesh12p)

[Sourav Jagtap](https://github.com/resist15)


