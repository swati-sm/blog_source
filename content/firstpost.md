Title:My first blog post
Author: Swati S Maddur
Date: 2019-10-20 13:50
Category:blogging


blog post content goes here
Title, author,date,and category are must specify metadata for any site
#largest heading
##next largest
######smallest heading

1. hello
3. world

This paragraph is to demonstrate __bold__  syntax and also _italics_ syntax.

Below is the URL link to google.To add a link mention the alternate text within sqaure brackets followed by image path in the curved brackets.

[google](www.google.com)

bulltet list:

* yaay*( star followed by a space followed by content to create list)
    * Sub ya (for indented bullet list 4spaces followed by * followed by space)
    * Sub ay
* woohoo 


Code blocks are preceeded by an indent, three : symbols and the name of the language.
All of the following code will be highlighted while the text is indented.

    :::python3
    def do_twice(func):
    def wrapper_do_twice(*args, **kwargs):
        return func(*args, **kwargs).lower()
    return wrapper_do_twice

    @do_twice
    def say_whee(some_text):
        print(some_text)

    x = 'Whee!'
    say_whee(x)


####to add an image put excalmatory mark followed by alt text within sqaure bracketsfollowed by path in curved braces.its mentioned as static coz the image is saved in the folder on system and is not a url
![tux, the linux mascot]({static}/tux.jpeg)


####blockquote
>this is so cool
>>im loving it
