# Lesson 15 - Dictionaries

monthConversations = {
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Sep": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December"
}

print(monthConversations.get('ball','Not a valid key')) # Output: Not a valid key
print(monthConversations.get('Sep','Not a valid key')) # Output: September
