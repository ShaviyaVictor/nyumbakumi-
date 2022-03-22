# nyumbakumi!

This is a web application that allows users to be in the loop about everything happening in their neighborhood. From contact information of different handyman to meeting announcements or even alerts.       
Below is the project's screenshots:     
![nyumbakumi!_Home.Pg_Screenshot](https://github.com/ShaviyaVictor/nyumbakumi-/blob/main/media/Home.png)                
![nyumbakumi!_Profile.Pg_Screenshot](https://github.com/ShaviyaVictor/nyumbakumi-/blob/main/media/Profile.png)          


#### Live link to site
The project was deployed to Heroku and GitHub pages for publication.     
* To view the [project's Heroku live site](https://nyumbakumi.herokuapp.com/).         
* To view the [project's Figma mockup design](https://www.figma.com/file/Bi89jjzMDXCN9H17UGHwBI/nyumbakumi!?node-id=0%3A1).

## Application Setup Instructions
- Open Terminal {Ctrl+Alt+T}     
- git clone [nyumbakumi!_project](https://github.com/ShaviyaVictor/nyumbakumi-)      
- cd instagram_project      
- code . or atom . based on the text editor you have.


### Running the application

To run the application locally, open the cloned file in terminal and run the following commands:     
  > `$ python manage.py runserver`  

### Installing

Below is a step by step series of how to work on the project after cloning it:

Navigate into the folder and install requirements by running the below command:

```
$ cd instagram_project pip install -r requirements.txt 
```

Create a new directory and inside it create a new environment(virtual) by running the below command:

```
$ python3 -m venv --without-pip virtual
```

Activate the virtual environment:

```
$ source virtual/bin/activate
```

View the **cloned project** and continue editting or follow the below commands to build your own Django application.

Install pip in the virtual environment for installing additional packages for the project:

```
$ curl https://bootstrap.pypa.io/get-pip.py | python
```

Use pip to install Django inside your vrtual environment:

```
$ pip install django
```

SetUp your database User,Password, Host then make migration:

```
$ python manage.py makemigrations shawards_project
```

Make migrations:

```
$ python manage.py migrate 
```



### Running the tests

Below is a command for running the TestCases of the application:      
  > `$ python3 manager.py test`


Open the application on your browser:
```
127.0.0.1:8000
```



## Deployment

Follow along with this [Deployment Documentation](https://gist.github.com/newtonkiragu/42f2500e56d9c2375a087233587eddd0) to deploy your version of the application to Heroku.

## Built With

* [Python](https://docs.python.org/3/)        
* [Django](https://docs.djangoproject.com/en/4.0/)       
* [Bootstrap](https://getbootstrap.com/docs/5.1/getting-started/introduction/)       
* [Heroku](https://devcenter.heroku.com/categories/reference)       

## License

This project is licensed under the [MIT License](https://github.com/ShaviyaVictor/ShawardS/blob/main/LICENSE).      
You can also see the [LICENSE.md](https://github.com/ShaviyaVictor/ShawardS/blob/main/LICENSE) file for details.

## Acknowledgments

* Corey Schafer
* Pretty Printed
* Inspiration from [nextdoor](https://nextdoor.com/)

### Author

* **Victor Shaviya**        
    - [LinkedIn](https://www.linkedin.com/in/victor-shaviya-532ab0110/)          
    - [Instagram](https://www.instagram.com/ignition_reads/)
