RPi-GroveStreams-Tutorial-Python
================================

Simple Python Hello World Tutorial for GroveStreams


Install Python Libraries
========================
<pre class="code-text-only" style="display: none;">
<code>sudo apt-get install python-dev
curl -O http://python-distribute.org/distribute_setup.py
python distribute_setup.py
curl -O https://raw.github.com/pypa/pip/master/contrib/get-pip.py
python get-pip.py
sudo pip install virtualenv</code></pre>

Install Simplejson
==================
<pre class="code-text-only" style="display: none;">
<code>sudo pip install simplejson</code></pre>

Simplejson is a free library and can be found here: https://pypi.python.org/pypi/simplejson/<br>

Follow GroveStreams Tutorials
=============================
1. Follow GroveStreams Java Hello World Tutorial Steps 1-4
https://grovestreams.com/developers/getting_started_helloworld.html<br>
This will create your account and set up a feed to view data from the RPi. This will also configure organization UID and secret API Key.<br>
2. See Python Hellow World Tutorial for further information https://grovestreams.com/developers/getting_started_helloworld_python.html<br>

Git the code from GitHub
========================
From your /home/pi directory, git the code
<pre class="code-text-only" style="display: none;">
<code>sudo git clone https://github.com/mvartani76/RPi-GroveStreams-Tutorial-Python/</code></pre>

Run the Python Code
===================
<pre class="code-text-only" style="display: none;">
<code>sudo python grovestreams_demo.py</code></pre>
Remember to update your Organization UID and Secret API Key!!<br>
