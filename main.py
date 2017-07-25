#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
import logging

HOMEPAGE = """
<html>
  <head>
    <link rel = "stylesheet" href = "/resources/Blogasaurus.css">
    <script src=""/resources/Blogasaurs.js"></script>
    <title>All About Mo</title>
  </head>
  <body>
    <h1>Welcome!</h1>
    <h3>Here at All About Mo, we tell you a bit about our creator. From her background
      to her likes and dislikes, you'll learn so much about a person that you could easily be
      by just humaning. </h3>
    <h2>Check these neat links to her newest posts:</h2>
    <a href="Random_Facts.html">Random Fun Facts</a>
    <br>
    <a href="Favorites.html">My Favorite Things</a>
    <br>
    <a href = "Dislikes.html">What I Can't Stand and Kind of Hate</a>
    <br>
    <a href = "Future_Plans.html">My Plans for the Future</a>
    <br>
    <a href = "Education.html">My Education</a>
  </body>
  </html>
"""

DISLIKES = """
<html>
<head>
  <title>Mo's Dislikes</title>
  <link rel = "stylesheet" href = "/resources/Blogasaurus.css">
</head>
<body>
  <h1>My Dislikes</h1>
  <h2>Fish</h2>
  <h3>Reasons Why:</h3>
  <ul>
    <li>They're gross.</li>
    <li>They smell awful - dead or alive.</li>
    <li>They make me feel sick when I eat them.</li>
  </ul>
  <h2>Mobile Apps</h2>
  <h3 id="WARNING">Warning: What I'm about to say is very hypocritical as I am
    the possessor of mutliple apps on my cell phone</h3>
    <br>
    <br>
    <br>
  <h2>Other Pages You May Enjoy:</h2>
  <a href="Blogasaurus.html">Home</a>
  <br>
    <a href="Random_Facts.html">Random Fun Facts</a>
    <br>
    <a href="Favorites.html">My Favorite Things</a>
    <br>
    <a href = "Future_Plans.html">My Plans for the Future</a>
    <br>
    <a href = "Education.html">My Education</a>
    <br>
    <br>
    <br>
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.3/jquery.min.js"></script>
    <script src="Blogasaurus.js"></script>
    <h2>Comments</h2>
    <form name="CommentsSection">
    <input type="text" id="comments"/>
    <input type="button" id="comments_button" value="OK"/>
    <h3 id="UserComments"></h3>
    </form>
</body>
</html>
"""

EDUCATION = """
<html>
<head>
  <title>My Education</title>
  <link rel = "stylesheet" href = "/resources/Blogasaurus.css">
</head>
<body>
  <h1>Education</h1>
  <h3>I attended Timothy Christian School for the entirety of my educational
    career and am now going to Rutgers University</h3>
  <br>
  <br>
  <br>
<h2>Other Pages You May Enjoy:</h2>
<a href="Blogasaurus.html">Home</a>
<br>
  <a href="Random_Facts.html">Random Fun Facts</a>
  <br>
  <a href="Favorites.html">My Favorite Things</a>
  <br>
  <a href = "Dislikes.html">What I Can't Stand and Kind of Hate</a>
  <br>
  <a href = "Future_Plans.html">My Plans for the Future</a>
  <br>
  <br>
  <br>
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.3/jquery.min.js"></script>
  <script src="Blogasaurus.js"></script>
  <h2>Comments</h2>
  <form name="CommentsSection">
  <input type="text" id="comments"/>
  <input type="button" id="comments_button" value="OK"/>
  <h3 id="UserComments"></h3>
  <p></p>
  </form>
</body>
</html>
"""

FAVORITES = """
<html>
<head>
  <title>Mo's Favs</title>
  <link rel = "stylesheet" href = "Blogasaurus.css">
</head>
<body>
  <h1>Favorites</h1>
  <img src ="http://cdn1-www.dogtime.com/assets/uploads/gallery/siberian-husky-dog-breed-pictures/siberian-husky-dog-breed-pictures-3.jpg"/>
  <h2>Movies</h2>
  <ol>
    <li><em>The Breakfast Club</li>
    <li>Rain Man</li>
    <li>Tropic Thunder</em></li>
  </ol>
  <h2>TV Shows</h2>
  <ul>
    <li>Archer</li>
    <li>Futurama</li>
    <li>Are You the One?</li>
  </ul>
  <h2>Favorite Websites</h2>
  <a href="http://www.youtube.com">YouTube</a>
  <br>
  <a href="http://www.poptropica.com/">Classic Online Gaming</a>
  <br>
  <br>
  <br>
<h2>Other Pages You May Enjoy:</h2>
<a href="Blogasaurus.html">Home</a>
<br>
  <a href="Random_Facts.html">Random Fun Facts</a>
  <br>
  <a href = "Dislikes.html">What I Can't Stand and Kind of Hate</a>
  <br>
  <a href = "Future_Plans.html">My Plans for the Future</a>
  <br>
  <a href = "Education.html">My Education</a>

</body>
</html>
"""

FUTUREPLANS = """
<html>
<head>
  <title>My Plants for the Future</title>
  <link rel = "stylesheet" href = "Blogasaurus.css">
</head>
<body>
  <h2>No se ahora. Quizas manana?</h2>
  <br>
  <br>
  <br>
<h2>Other Pages You May Enjoy:</h2>
<a href="Blogasaurus.html">Home</a>
<br>
  <a href="Random_Facts.html">Random Fun Facts</a>
  <br>
  <a href="Favorites.html">My Favorite Things</a>
  <br>
  <a href = "Dislikes.html">What I Can't Stand and Kind of Hate</a>
  <br>
  <a href = "Education.html">My Education</a>
  <br>
  <br>
  <br>
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.3/jquery.min.js"></script>
  <script src="Blogasaurus.js"></script>
  <h2>Comments</h2>
  <form name="CommentsSection">
  <input type="text" id="comments"/>
  <input type="button" id="comments_button" value="OK"/>
  <h3 id="UserComments"></h3>
  </form>
</body>
</html>
"""

RANDOMFACTS = """
<html>
  <head>
    <title>Random Fun Facts about Me!</title>
    <link rel="stylesheet" href="Blogasaurus.css">
  </head>
  <body>
    <h1>Random Facts with Mo about Mo</h1>
    <h3>My nickname from the end of Junior year and throughout Senior year was 'Savage',
      because I rejected the guy who asked me to prom 11th grade year.</h3>
      <br>
      <br>
      <br>
    <h2>Other Pages You May Enjoy:</h2>
    <a href="Blogasaurus.html">Home</a>
    <br>
    <a href="Favorites.html">My Favorite Things</a>
    <br>
    <a href = "Dislikes.html">What I Can't Stand and Kind of Hate</a>
    <br>
    <a href = "Future_Plans.html">My Plans for the Future</a>
    <br>
    <a href = "Education.html">My Education</a>
    <br>
    <br>
    <br>
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.3/jquery.min.js"></script>
    <script src="Blogasaurus.js"></script>
    <h2>Comments</h2>
    <form name="CommentsSection">
    <input type="text" id="comments"/>
    <input type="button" id="comments_button" value="OK"/>
    <h3 id="UserComments"></h3>
    </form>
  </body>
</html>
"""

class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write(HOMEPAGE)

class DislikesHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write(DISLIKES)

app = webapp2.WSGIApplication([
    ("/", MainHandler),
    ("/dislikes", DislikesHandler)
], debug=True)
