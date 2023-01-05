<h2 class="code-line" data-line-start=0 data-line-end=1 ><a id="LunchBoxy_0"></a>LunchBoxy</h2>
<p class="has-line-data" data-line-start="1" data-line-end="2">LunchBoxy is a full stack web application that provides users with easy, kid-approved meals for their child’s lunch box.</p>
<p class="has-line-data" data-line-start="3" data-line-end="4">Watch a LunchBoxy presentation video <a href="https://youtu.be/EnDWrE_RAqg">here</a>.</p>

![LunchBoxy_main](https://user-images.githubusercontent.com/110854972/210654824-e32eebf6-4696-4e44-b10c-7ff329a7ad28.gif)

</ul>
<h2 class="code-line" data-line-start=18 data-line-end=19 ><a id="Features_18"></a>Features</h2>
<p class="has-line-data" data-line-start="19" data-line-end="20">At the click of a button, LunchBoxy generates a Lunch Idea that consists of a Something Filling (main item), Something Crunchy (side) and Something Fresh (veggie/fruit sides). Users can also view all available meals and their recipes. From both the View All and Lunch Idea pages, the user can add meals to favorites for easy reference, and manage them from their Favorites page. 
<p>Future phases will include the ability to swap out side components, plan a week’s worth of meals, and generate a grocery list.</p>


![ezgifcom-gif-maker-1](https://user-images.githubusercontent.com/110854972/210671480-7004e131-6fdb-4727-9c5b-bcc70e929508.gif)


<h2 class="code-line" data-line-start=5 data-line-end=6 ><a id="Tech_5"></a>Tech Stack</h2>
<ul>
<li class="has-line-data" data-line-start="6" data-line-end="7">Python</li>
<li class="has-line-data" data-line-start="7" data-line-end="8">JavaScript</li>
<li class="has-line-data" data-line-start="8" data-line-end="9">React</li>
<li class="has-line-data" data-line-start="9" data-line-end="10">Flask</li>
<li class="has-line-data" data-line-start="10" data-line-end="11">PostgreSQL</li>
<li class="has-line-data" data-line-start="11" data-line-end="12">SQLAlchemy</li>
<li class="has-line-data" data-line-start="12" data-line-end="13">HTML</li>
<li class="has-line-data" data-line-start="13" data-line-end="14">CSS</li>
<li class="has-line-data" data-line-start="14" data-line-end="15">Bootstrap</li>
<li class="has-line-data" data-line-start="15" data-line-end="18">Jinja2<br>
(dependencies are listed in requirements.txt)</li>

<h2 class="code-line" data-line-start=21 data-line-end=22 ><a id="Running_the_App_21"></a>Running the App</h2>
<p class="has-line-data" data-line-start="22" data-line-end="23">LunchBoxy has not yet been deployed, so here is how to run the app locally on your machine:</p>
<h4 class="code-line" data-line-start=23 data-line-end=24 ><a id="Create_and_activate_a_Python_virtual_enrivonment_and_install_dependencies_23"></a>Create and activate a Python virtual enrivonment and install dependencies</h5>
<pre><code class="has-line-data" data-line-start="25" data-line-end="29" class="language-python">virtualenv env
source env/bin/activate
pip3 install -r requirements.txt
</code></pre>
<p class="has-line-data" data-line-start="29" data-line-end="30">If you are on a Windows, you may need to clear stale pid files using the following command:</p>
<pre><code class="has-line-data" data-line-start="31" data-line-end="33" class="language-python">sudo pg_ctlcluster <span class="hljs-number">13</span> main start
</code></pre>
<h4 class="code-line" data-line-start=33 data-line-end=34 ><a id="Run_the_server_file_33"></a>Run the server file</h5>
<pre><code class="has-line-data" data-line-start="35" data-line-end="37" class="language-python">python3 server.py
</code></pre>
<p class="has-line-data" data-line-start="37" data-line-end="38">Verify the deployment by navigating to your server address in your preferred browser</p>
<pre><code class="has-line-data" data-line-start="39" data-line-end="41">localhost:5000
</code></pre>
<h2 class="code-line" data-line-start=41 data-line-end=42 ><a id="Author_41"></a>Author</h2>
<p class="has-line-data" data-line-start="42" data-line-end="43">Meagan St Clair is software engineer located in the Greater Houston area.</p>
