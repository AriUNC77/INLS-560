import os 
# Operating system function
'''The os module provides functions that interact with the computer's operating
system. The Geeks for Geeks site lists a few functions contained in the os
module, such as getting the current working directory with os.getcwd() or
making a directory with os.makedir() or os.makedirs().'''
import re 
# Regular expression function
'''the re module provides regular expression matching operations like those
in perl, according to python's 3.13.0 documentation. Regular expressions use /
to indicate a special form or allow special characters to be used without invoking
their meaning. One thing regular expressions can do is search for a sequence of 
characters and return it with a Match object. They can also return the group of
text the match came from or the first mention of a character.'''

# Slugify function.
'''A slug is the unique part of a URL that helps act as a unique identifier for
the page. The slugify function uses the page title to make a slug that works as
a file name by replacing all spaces with hyphens.'''
def slugify(title):
    """Convert the page title to a filename-friendly slug."""
    if title.lower() == "home":  # Ensure 'Home' becomes 'index.html'
        return "index.html"
        # strip() and lower() are string methods that when combined remove all white space
    # and ensure all characters are lowercase.
    return re.sub(r'\W+', '-', title.strip().lower()) + ".html"

# Navigation function.
def generate_nav(titles, active_title):
    """Generate a dynamic navigation bar with an active page highlight."""
    nav_links = ""
    for title in titles:
        filename = slugify(title)
        active_class = ' class="active"' if title == active_title else ""
        nav_links += f'\t\t\t<a href="{filename}"{active_class}>{title}</a>\n'
    return nav_links.strip()

# Create html function.

def create_html_file(title, titles, output_dir="build"):
    """Generate and write HTML content based on the page title."""
    filename = slugify(title)
    nav = generate_nav(titles, active_title=title)
#lower() is used in the below block to make the title lowercase.
    html_content = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>{title}</title>
        <link rel="stylesheet" href="style.css">
    </head>
    <body>
        <nav>
            {nav}
        </nav>
        <div class="content">
            <h1>{title}</h1>
            <p>This is the {title.lower()} content.</p>
        </div>
    </body>
    </html>
    """

    output_path = os.path.join(output_dir, filename)
    os.makedirs(output_dir, exist_ok=True)  # Ensure the directory exists

    with open(output_path, 'w') as file:
        file.write(html_content)

    print(f"Created {filename} in the '{output_dir}' directory.")

    # Create CSS file function

# uses pass for the program to ignore create_css_file()
def create_css_file():
    pass

# Main Function

def main():
    """Main function to generate pages and styles. MUST HAVE HOME!!!"""
    # A dictionary with page titles.
    titles = ["Home", "School", "Work", "Hobbies"]

    # Create HTML files for each title
    for title in titles:
        create_html_file(title, titles)

    # Create the style.css file
    #create_css_file() 
    # uncomment the create_css_file() function if you add the function.

if __name__ == "__main__":
    main()
