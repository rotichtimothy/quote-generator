import random

def get_random_quote(quotes):
    return random.choice(quotes)

def display_quote(quote):
    print("Here is your quote:")
    print(quote)

def main():
    quotes = [
        "The greatest glory in living lies not in never falling, but in rising every time we fall. - Nelson Mandela",
        "The way to get started is to quit talking and begin doing. - Walt Disney",
        "Your time is limited, don't waste it living someone else's life. - Steve Jobs",
        "If life were predictable it would cease to be life, and be without flavor. - Eleanor Roosevelt",
        "If you look at what you have in life, you'll always have more. - Oprah Winfrey",
        "If you set your goals ridiculously high and it's a failure, you will fail above everyone else's success. - James Cameron",
        "Life is what happens when you're busy making other plans. - John Lennon",
        "The only true wisdom is in knowing you know nothing. - Socrates",
        "The only way to do great work is to love what you do. - Steve Jobs",
        "You miss 100% of the shots you don't take. - Wayne Gretzky",
        "The journey of a thousand miles begins with one step. - Lao Tzu",
        "Believe you can and you're halfway there. - Theodore Roosevelt",
        "Success is not final, failure is not fatal: It is the courage to continue that counts. - Winston Churchill",
        "Don't watch the clock; do what it does. Keep going. - Sam Levenson",
        "The best way to predict the future is to invent it. - Alan Kay",
        "Don't be afraid to give up the good to go for the great. - John D. Rockefeller",
        "In the end, it's not the years in your life that count. It's the life in your years. - Abraham Lincoln",
        "You only live once, but if you do it right, once is enough. - Mae West",
        "The best thing to hold onto in life is each other. - Audrey Hepburn",
        "Love is composed of a single soul inhabiting two bodies. - Aristotle",
        "To love and be loved is to feel the sun from both sides. - David Viscott",
        "We are shaped and fashioned by what we love. - Johann Wolfgang von Goethe",
        "The unexamined life is not worth living. - Socrates",
        "Knowing yourself is the beginning of all wisdom. - Aristotle",
        "A friend is someone who knows all about you and still loves you. - Elbert Hubbard",
        "Friendship is born at that moment when one person says to another, ‘What! You too? I thought I was the only one.’ - C.S. Lewis",
        "A real friend is one who walks in when the rest of the world walks out. - Walter Winchell",
        "Success is walking from failure to failure with no loss of enthusiasm. - Winston Churchill",
        "Opportunities don't happen. You create them. - Chris Grosser",
        "The most important thing is to enjoy your life – to be happy – it’s all that matters. - Audrey Hepburn",
        "For every minute you are angry you lose sixty seconds of happiness. - Ralph Waldo Emerson",
        "The function of leadership is to produce more leaders, not more followers. - Ralph Nader",
        "A leader is one who knows the way, goes the way, and shows the way. - John C. Maxwell",
    ]
    
    random_quote = get_random_quote(quotes)
    display_quote(random_quote)

if __name__ == "__main__":
    main()
