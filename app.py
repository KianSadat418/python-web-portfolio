from flask import Flask, render_template

category_descriptions = ["""I've been learning software development independently 
                         since 2021. My main focuses have been mobile app development 
                         with flutter and web development with flask. Software 
                         develpoment has provided me a medium to solve the probelems 
                         of the world""", 
                         """I've always had a love for engineering. I have a deep love
                         for the process of ideation and reification. I've been
                         applying my technical skills to engineer many projects
                         which solve problems and automate my life. I intend
                         to continue my engineering aspirations in college
                         as a computer engineer. I plan to work on computer systems 
                         in powered prosthetics.""",
                         """Music has been a big part of my life for as long as I can 
                         remember. Music provides me an intellectual and creative medium 
                         to express myself to the world. I've been playing jazz trumpet 
                         since 2020 and jazz piano since 2022."""
                        ]

all_projects = {
    'software': [{'name': 'BMI Calculator App', 
                  'short_description': 'I programmed a mobile app that calculates a users BMI and provides information regarding their health.',
                  'long_description': 'This project was one that I worked on while I was still learning the fundamentals of mobile app development with flutter. I mainly wanted to include stateful widgets in a manner that improved the user experience. In this case, The color of the input field changes to indicate what units are being used. Additionally, the color of the result changes to indicate the health of a certain BMI range.',
                  'skills': ['Flutter', 'Dart', 'Mobile Dev'], 
                  'images': ['images/software/bmi1.png', 'images/software/bmi2.png', 'images/software/bmi3.png', 'images/software/bmi4.png']
                  },
                 {'name': 'Meals App', 
                  'short_description': 'I made a mobile app that stores and organizes multiple recipes for meals.',
                  'long_description': 'I made a mobile app that stores and organizes multiple recipes for meals. I am very proud of the meals app as it was the culmination of all experienced I had gained as a mobile app developer. The app featuers complex state management as well as multiple screens. Additionally, I added a filter system that narrows down the listed results. You can also mark meals as favorites and they will be sent to the favorites tab where you can unfavorite them if you please. I tried to make the UI of this app as sophisticated as possible.',
                  'skills': ['Flutter', 'Dart', 'Mobile Dev'], 
                  'images': ['images/software/meals2.png', 'images/software/meals1.png', 'images/software/meals3.png', 'images/software/meals4.png', 'images/software/meals5.png', 'images/software/meals6.png']
                  },
                 {'name': 'Expense Tracker App', 
                  'short_description': 'I programmed a mobile app that tracks expenses and compares them to each other.',
                  'long_description': 'The expense tracker app is a way for users to record their expenses over time and compare them with eachother. The complexity of this app lies in the data management systems. The models and widgets of this app are all designed to be able to store large amounts of information in a dynamic and efficient way.',
                  'skills': ['Flutter', 'Dart', 'Mobile Dev'], 
                  'images': ['images/software/expenses3.png', 'images/software/expenses1.png', 'images/software/expenses2.png', 'images/software/expenses4.png']
                  },
                 {'name': 'Flutter Quiz App', 
                  'short_description': 'I made a mobile app to test a users knowledge on Flutter and provide them feedback.',
                  'long_description': 'This quiz app is a quick and simple project that aims to measure the users familiarity with flutter concepts. The quiz is the same every time and users can take it again and again untill they achieve their desired result. The correct answers are show next to the chosen answers after every attempt.',
                  'skills': ['Flutter', 'Dart', 'Mobile Dev'], 
                  'images': ['images/software/quiz1.png', 'images/software/quiz2.png', 'images/software/quiz3.png']
                  },
                 {'name': 'Dice App', 
                  'short_description': 'I programmed a mobile app that allows users to roll a dice multiple times.',
                  'long_description': 'This app is a simple approach at a dice roller. The users rolls the dice and a random number 1 through 6 is generated and displayed as a dice roll. This was the first mobile app I ever made and it serves as a reminder of how far I have come in terms of the complexity of my apps. ',
                  'skills': ['Flutter', 'Dart', 'Mobile Dev'], 
                  'images': ['images/software/dice1.png', 'images/software/dice2.png']},
                 {'name': 'Personal Website', 
                  'short_description': 'I made the website that you are using right now to display my projects and experience!',
                  'long_description': 'My personal website might just be the software project that I have devoted the most time and resources to. It serves not only as a way for me to display my portfolio, experiences, and accomplishments to whomever might be interested but also to practice my software engineering skills in a capstone project. From Python and Flask to HTML, CSS, and Javascript I had to hone many software engineering skills to make this possible.',
                  'skills': ['Python', 'HTML', 'CSS'], 
                  'images': ['images/software/pw1.png']
                  },
                 ], 
    'engineering': [{'name': 'Powered Prosthetic Knee', 
                     'short_description': 'I built an open source powered prosthetic knee with the University of Utah',
                     'long_description': '',
                     'skills': ['Python, HTML, CSS'], 
                     'images': ['images/engineering/osl.png']
                     },
                    {'name': 'IoT Garage Door Opener', 
                     'short_description': 'I made a device that enabled me to operate my garage door over the internet using my phone.',
                     'long_description': '', 
                     'skills': ['Python, HTML, CSS'], 
                     'images': ['images/engineering/gdo.png']
                     },
                    ], 
    'music': []
    }

def create_app():
  app = Flask(__name__)
  
  @app.route('/')
  def index():
      return render_template('index.html', 
                             title='Kian Sadat', 
                          )
  
  @app.route('/about')
  def about():
      return render_template('about.html', 
                             title='Kian Sadat | About'
                          )
  
  @app.route('/experience')
  def experience():
      return render_template('experience.html',
                             title='Kian Sadat | Experience'
                          )
  
  @app.route('/portfolio')
  def portfolio():
      return render_template('portfolio.html',
                             title='Kian Sadat | Portfolio'
                          )
  
  @app.route('/portfolio/<string:category>')
  def projects(category):
      if category == 'software':
          title = 'Kian Sadat | Software Projects'
          description = category_descriptions[0]
          projects = all_projects['software']
      elif category == 'engineering':
          title = 'Kian Sadat | Engineering Projects'
          description = category_descriptions[1]
          projects = all_projects['engineering']
      else:
          title = 'Kian Sadat | Music Projects'
          description = category_descriptions[2]
          projects = all_projects['music']
      return render_template('projects.html', 
                             title=title, 
                             heading=title[12:], 
                             description=description,
                             category=category,
                             projects=projects
                          )
  
  @app.route('/portfolio/<string:category>/<string:project>')
  def details(category, project):
      for card in all_projects[category]:
          if card['name'] == project:
              information = card
      return render_template('details.html',
                             information=information,
                             category=category
                          )
  return app
