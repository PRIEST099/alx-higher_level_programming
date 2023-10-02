# 0x00 Python Hello World

Welcome to the "0x00 Python Hello World" directory in the AlX Higher-Level Programming repository! 🐍🌍

## About
This directory contains a collection of introductory Python scripts and projects to help you get started with Python programming. Whether you're a beginner or looking to refresh your Python skills, you'll find valuable resources here.

## Contents
- **`0-run`**: A shell script that runs a Python script specified in the `PYFILE` environment variable.
- **`main.py`**: A simple Python script that prints "Best School" to the console.
- **`1-run_inline`**: A shell script that runs Python code specified in the `PYCODE` environment variable.
- **`2-print.py`**: A Python script that prints a multilingual puzzle.
- **`3-print_number.py`**: A Python script that prints a number with a specified format.
- **`4-print_float.py`**: A Python script that prints a floating-point number with a specified format.
- **`5-print_string.py`**: A Python script that prints a string and its substring.
- **`6-concat.py`**: A Python script that concatenates strings.
- **`7-edges.py`**: A Python script that extracts and prints substrings from a string.
- **`8-concat_edges.py`**: A Python script that extracts substrings from a string and concatenates them.
- **`9-easter_egg.py`**: A Python script that prints "The Zen of Python" by Tim Peters.

## Getting Started
1. Clone the entire AlX Higher-Level Programming repository to your local machine using `git clone`.
2. Navigate to the "0x00-python-hello_world" directory.
3. Explore the Python scripts and run them to see the results.
4. Start your Python journey and have fun learning!
## Self Test
You can use the exercises in this repository to test your Python programming language. Here are  some of the exercises available:

**`0.run python file`**

<div class="panel-body">
    <span id="user_id" data-id="64688"></span>

    <!-- Progress vs Score -->

    <!-- Task Body -->
    <p>Write a Shell script that runs a Python script.</p>

<p>The Python file name will be saved in the environment variable <code>$PYFILE</code></p>

<pre><code>guillaume@ubuntu:~/py/0x00$ cat main.py 
#!/usr/bin/python3
print("Best School")

guillaume@ubuntu:~/py/0x00$ export PYFILE=main.py
guillaume@ubuntu:~/py/0x00$ ./0-run
Best School
guillaume@ubuntu:~/py/0x00$ 
</code></pre>

  </div>


**`1.Run inline`**

<div class="panel-body">
    <span id="user_id" data-id="64688"></span>

    <!-- Progress vs Score -->

    <!-- Task Body -->
    <p>Write a Shell script that runs Python code.</p>

<p>The Python code will be saved in the environment variable <code>$PYCODE</code></p>

<pre><code>guillaume@ubuntu:~/py/0x00$ export PYCODE='print(f"Best School: {88+10}")'
guillaume@ubuntu:~/py/0x00$ ./1-run_inline 
Best School: 98
guillaume@ubuntu:~/py/0x00$ 
</code></pre>

  </div>

**`2.Hello_print`**

<div class="panel-body">
    <span id="user_id" data-id="64688"></span>

    <!-- Progress vs Score -->

    <!-- Task Body -->
    <p>Write a Python script that prints exactly <code>"Programming is like building a multilingual puzzle</code>, followed by a new line.</p>

<ul>
<li>Use the function <code>print</code></li>
</ul>

<pre><code>guillaume@ubuntu:~/py/0x00$ ./2-print.py 
"Programming is like building a multilingual puzzle
guillaume@ubuntu:~/py/0x00$
</code></pre>

  </div>


**`Print Integer`**

<div class="panel-body">
    <span id="user_id" data-id="64688"></span>

    <!-- Progress vs Score -->

    <!-- Task Body -->
    <p>Complete this <a href="https://github.com/alx-tools/0x00.py/blob/master/3-print_number.py" title="source code" target="_blank">source code</a> in order to print the integer stored in the variable <code>number</code>, followed by <code>Battery street</code>, followed by a new line.</p>

<ul>
<li>You can find the source code <a href="https://github.com/alx-tools/0x00.py/blob/master/3-print_number.py" title="here" target="_blank">here</a></li>
<li>The output of the script should be:

<ul>
<li>the number, followed by <code>Battery street</code>,</li>
<li>followed by a new line</li>
</ul></li>
<li>You are not allowed to cast the variable <code>number</code> into a string</li>
<li>Your code must be 3 lines long</li>
<li>You have to use f-strings <a href="/rltoken/Ju0J8BxkuPX5yKZctyKfsQ" title="tips" target="_blank">tips</a></li>
</ul>

<pre><code>guillaume@ubuntu:~/py/0x00$ ./3-print_number.py
98 Battery street
guillaume@ubuntu:~/py/0x00$ 
</code></pre>

  </div>


**`Print Float`**

<div class="panel-body">
    <span id="user_id" data-id="64688"></span>

    <!-- Progress vs Score -->

    <!-- Task Body -->
    <p>Complete the source code in order to print the float stored in the variable <code>number</code> with a precision of 2 digits.</p>

<ul>
<li>You can find the source code <a href="https://github.com/alx-tools/0x00.py/blob/master/4-print_float.py" title="here" target="_blank">here</a></li>
<li>The output of the program should be:

<ul>
<li><code>Float:</code>, followed by the float with only 2 digits</li>
<li>followed by a new line</li>
</ul></li>
<li>You are not allowed to cast <code>number</code> to string</li>
<li>You have to use f-strings</li>
</ul>

<pre><code>guillaume@ubuntu:~/py/0x00$ ./4-print_float.py
Float: 3.14
guillaume@ubuntu:~/py/0x00$ 
</code></pre>

  </div>


**`Print String`**

<div class="panel-body">
    <span id="user_id" data-id="64688"></span>

    <!-- Progress vs Score -->

    <!-- Task Body -->
    <p>Complete this <a href="https://github.com/alx-tools/0x00.py/blob/master/5-print_string.py" title="source code" target="_blank">source code</a> in order to print 3 times a string stored in the variable <code>str</code>, followed by its first 9 characters.</p>

<ul>
<li>You can find the source code <a href="https://github.com/alx-tools/0x00.py/blob/master/5-print_string.py" title="here" target="_blank">here</a></li>
<li>The output of the program should be:

<ul>
<li>3 times the value of <code>str</code></li>
<li>followed by a new line</li>
<li>followed by the 9 first characters of <code>str</code></li>
<li>followed by a new line</li>
</ul></li>
<li>You are not allowed to use any loops or conditional statement</li>
<li>Your program should be maximum 5 lines long</li>
</ul>

<pre><code>guillaume@ubuntu:~/py/0x00$ ./5-print_string.py 
Holberton SchoolHolberton SchoolHolberton School
Holberton
guillaume@ubuntu:~/py/0x00$ 
</code></pre>

  </div>


**`Play With String`**

<div class="panel-body">
    <span id="user_id" data-id="64688"></span>

    <!-- Progress vs Score -->

    <!-- Task Body -->
    <p>Complete this <a href="https://github.com/alx-tools/0x00.py/blob/master/6-concat.py" title="source code" target="_blank">source code</a> to print <code>Welcome to Holberton School!</code></p>

<ul>
<li>You can find the source code <a href="https://github.com/alx-tools/0x00.py/blob/master/6-concat.py" title="here" target="_blank">here</a></li>
<li>You are not allowed to use any loops or conditional statements.</li>
<li>You have to use the variables <code>str1</code> and <code>str2</code> in your new line of code</li>
<li>Your program should be exactly 5 lines long</li>
</ul>

<pre><code>guillaume@ubuntu:~/py/0x00$ ./6-concat.py
Welcome to Holberton School!
guillaume@ubuntu:~/py/0x00$ wc -l 6-concat.py
5 6-concat.py
guillaume@ubuntu:~/py/0x00$ 
</code></pre>

  </div>


**`Copy - Cut - Paste`**

<div class="panel-body">
    <span id="user_id" data-id="64688"></span>

    <!-- Progress vs Score -->

    <!-- Task Body -->
    <p>Complete this <a href="https://github.com/alx-tools/0x00.py/blob/master/7-edges.py" title="source code" target="_blank">source code</a></p>

<ul>
<li>You can find the source code <a href="https://github.com/alx-tools/0x00.py/blob/master/7-edges.py" title="here" target="_blank">here</a></li>
<li>You are not allowed to use any loops or conditional statements</li>
<li>Your program should be exactly 8 lines long</li>
<li><code>word_first_3</code> should contain the first 3 letters of the variable <code>word</code></li>
<li><code>word_last_2</code> should contain the last 2 letters of the variable <code>word</code></li>
<li><code>middle_word</code> should contain the value of the variable <code>word</code> without the first and last letters</li>
</ul>

<pre><code>guillaume@ubuntu:~/py/0x00$ ./7-edges.py
First 3 letters: Hol
Last 2 letters: on
Middle word: olberto
guillaume@ubuntu:~/py/0x00$ wc -l 7-edges.py
8 7-edges.py
guillaume@ubuntu:~/py/0x00$ 
</code></pre>

  </div>


**`Create New Sentence`**

<div class="panel-body">
    <span id="user_id" data-id="64688"></span>

    <!-- Progress vs Score -->

    <!-- Task Body -->
    <p>Complete this <a href="https://github.com/alx-tools/0x00.py/blob/master/8-concat_edges.py" title="source code" target="_blank">source code</a> to print <code>object-oriented programming with Python</code>, followed by a new line.</p>

<ul>
<li>You can find the source code <a href="https://github.com/alx-tools/0x00.py/blob/master/8-concat_edges.py" title="here" target="_blank">here</a></li>
<li>You are not allowed to use any loops or conditional statements</li>
<li>Your program should be exactly 5 lines long</li>
<li>You are not allowed to create new variables</li>
<li>You are not allowed to use string literals</li>
</ul>

<pre><code>guillaume@ubuntu:~/py/0x00$ ./8-concat_edges.py
object-oriented programming with Python
guillaume@ubuntu:~/py/0x00$ wc -l 8-concat_edges.py
5 8-concat_edges.py
guillaume@ubuntu:~/py/0x00$ 
</code></pre>

  </div>

**`Easter egg`**

<div class="panel-body">
    <span id="user_id" data-id="64688"></span>

    <!-- Progress vs Score -->

    <!-- Task Body -->
    <p>Write a Python script that prints “The Zen of Python”, by TimPeters, followed by a new line.</p>

<ul>
<li>Your script should be maximum 98 characters long (please check with <code>wc -m 9-easter_egg.py</code>)</li>
</ul>

<pre><code>guillaume@ubuntu:~/py/0x00$ ./9-easter_egg.py
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
guillaume@ubuntu:~/py/0x00$
</code></pre>

  </div>


## Contributing
Feel free to contribute to this directory by adding more Python scripts or improving the existing ones. If you have ideas or enhancements, please open a pull request.

## C Files
In addition to Python scripts, this directory also includes C files and a header file for working with linked lists and checking for cycles in linked lists. You can find these files under the following names:
- **`lists.h`**: Header file for linked list functions.
- **`10-linked_lists.c`**: C source file containing linked list functions.
- **`10-main.c`**: C source file containing a sample program that uses linked lists.
- **`10-check_cycle.c`**: C source file containing a function to check for cycles in linked lists.
- **`100-write.py`**: A Python script that writes a message to stderr.

Happy Coding! 🚀🐍

