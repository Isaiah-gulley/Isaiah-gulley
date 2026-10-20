import datetime

# Add your quotes here
quotes = [
    "Your time is limited, so don't waste it living someone else's life. - Steve Jobs",
    "Stay hungry, stay foolish. - Steve Jobs",
    "Talk is cheap. Show me the code. - Linus Torvalds",
    "Programs must be written for people to read, and only incidentally for machines to execute. - Harold Abelson",
    "Simplicity is prerequisite for reliability. - Edsger W. Dijkstra"
]

# Pick a quote based on the day of the year so it changes daily
day_of_year = datetime.datetime.utcnow().timetuple().tm_yday
selected_quote = quotes[day_of_year % len(quotes)]

# Read your README.md file
with open("README.md", "r", encoding="utf-8") as f:
    content = f.read()

# We look for custom comment tags in your README.md to know where to swap the quote
start_tag = "<!-- QUOTE_START -->"
end_tag = "<!-- QUOTE_END -->"

if start_tag in content and end_tag in content:
    start_idx = content.find(start_tag) + len(start_tag)
    end_idx = content.find(end_tag)
    
    # Replace the old quote with the new one
    new_content = content[:start_idx] + f"\n{selected_quote}\n" + content[end_idx:]
    
    with open("README.md", "w", encoding="utf-8") as f:
        f.write(new_content)
    print("README updated successfully with quote:", selected_quote)
else:
    print("Tags not found in README.md!")
