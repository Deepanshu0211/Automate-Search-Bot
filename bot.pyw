import tkinter as tk
import random
import webbrowser
import time
import threading

# The same code you provided for searching
search_terms = [
    "Artificial Intelligence", 
    "Machine Learning", 
    "Data Science", 
    "Blockchain", 
    "Cryptocurrency", 
    "Cybersecurity", 
    "Web Development", 
    "Mobile Apps", 
    "Augmented Reality", 
    "Virtual Reality", 
    "Gaming", 
    "Programming", 
    "Technology", 
    "Innovation", 
    "Robotics", 
    "Space Exploration", 
    "Astronomy", 
    "Physics", 
    "Quantum Computing", 
    "Biotechnology", 
    "Environmental Science", 
    "Renewable Energy", 
    "Sustainability", 
    "Green Living", 
    "Travel", 
    "Adventure", 
    "Culture", 
    "Food", 
    "Cooking", 
    "Nutrition", 
    "Fitness", 
    "Health", 
    "Wellness", 
    "Yoga", 
    "Meditation", 
    "Mindfulness", 
    "Art", 
    "Photography", 
    "Music", 
    "Movies", 
    "Books", 
    "Fashion", 
    "Design", 
    "History", 
    "Nature", 
    "Wildlife", 
    "Pets", 
    "Dog Breeds", 
    "Cat Breeds", 
    "Pet Care", 
    "Gardening", 
    "Home Decor", 
    "DIY Projects", 
    "Crafts", 
    "Parenting", 
    "Pregnancy", 
    "Baby Care", 
    "Toddler Development", 
    "Teenagers", 
    "Education", 
    "Online Learning", 
    "Study Tips", 
    "Language Learning", 
    "Travel Photography", 
    "Adventure Sports", 
    "Camping", 
    "Survival Skills", 
    "Cooking Techniques", 
    "Healthy Recipes", 
    "Gourmet Cooking", 
    "Landscaping", 
    "Indoor Plants", 
    "Wildlife Photography", 
    "Endangered Species", 
    "Climate Action", 
    "Astrobiology", 
    "Neuroscience", 
    "Mind-Body Connection", 
    "Mental Health Apps", 
    "Motivational Speakers", 
    "Investment Strategies", 
    "Real Estate Investments", 
    "Small Business Success", 
    "Digital Marketing Trends", 
    "Innovative Tech Startups", 
    "Leadership Skills", 
    "Athlete Profiles", 
    "Fitness Wearables", 
    "Travel Safety Tips"
    # Add more terms as needed
]
search_terms += [
    "Mobile Development", 
    "Internet of Things", 
    "Smart Homes", 
    "Digital Art", 
    "Graphic Design", 
    "Street Art", 
    "Classical Music", 
    "Live Performances", 
    "Documentary Films", 
    "Fiction Books", 
    "Science Fiction", 
    "Fantasy", 
    "Fashion Trends", 
    "Haute Couture", 
    "Ancient Civilizations", 
    "Historical Figures", 
    "Ecotourism", 
    "Backpacking", 
    "Luxury Travel", 
    "Eclectic Cuisine", 
    "Vegetarian Cooking", 
    "Gluten-Free Baking", 
    "Healthy Snacks", 
    "DIY Home Improvement", 
    "Upcycling Projects", 
    "Parenting Tips", 
    "Newborn Essentials", 
    "Educational Apps", 
    "Foreign Language Apps", 
    "Adventure Photography", 
    "Extreme Sports", 
    "Hiking Trails", 
    "Bushcraft Skills", 
    "Paleontology", 
    "Space Telescopes", 
    "Particle Physics", 
    "Genetic Engineering", 
    "Renewable Energy Solutions", 
    "Zero-Waste Living", 
    "Mindful Eating", 
    "Fitness Challenges", 
    "Mental Health Resources", 
    "Motivational Podcasts", 
    "Personal Finance Blogs", 
    "Real Estate Market Trends", 
    "Startup Ecosystems", 
    "Influencer Marketing", 
    "Team Building Activities", 
    "Sports Nutrition", 
    "Athlete Training", 
    "Adventure Travel Tips", 
    "International Festivals", 
    "Artificial Intelligence Ethics", 
    "Quantum Computing Applications", 
    "AR in Education", 
    "Digital Nomad Lifestyle", 
    "Home Office Design", 
    "Eco-Friendly Fashion", 
    "Artisanal Crafts", 
    "Positive Psychology", 
    "Goal Setting Strategies", 
    "Online Investment Platforms", 
    "Cryptocurrency News", 
    "Green Energy Innovations", 
    "Space Colonization", 
    "Neuroplasticity", 
    "Biodegradable Products", 
    "Mindful Parenting", 
    "Edutainment for Kids", 
    "Sustainable Agriculture", 
    "Alternative Medicine", 
    "Wildlife Conservation Projects", 
    "Nature Reserves", 
    "Slow Travel Movement"
]

search_engines = ["bing", "bing"]
num_searches = 40 #number of searches 

custom_search_delay=0.9
# ...

# Create a global variable to track whether searches are running and the number of searches
searches_running = False
custom_num_searches = 40  # Default number of searches

def generate_random_search_term():
    prefixes = ["Latest on", "How to", "Exploring", "Interesting facts about", "Reviews for","more about"]
    topics = random.choice(search_terms)
    return f"{random.choice(prefixes)} {topics}"

def perform_random_search(search_engine):
    search_term = generate_random_search_term()
    if search_engine == "bing":
        search_url = f"https://www.bing.com/search?q={search_term}"
    elif search_engine == "bing":
        search_url = f"https://www.bing.com/search?q={search_term}"
    else:
        print("Invalid search engine choice.")
        return

    try:
        webbrowser.open_new_tab(search_url)
        time.sleep(custom_delay_entry)
    except Exception as e:
        print(f"An error occurred: {str(e)}")

def start_searches():
    global searches_running
    global custom_num_searches
    global custom_search_delay
    searches_running = True
    for _ in range(custom_num_searches):
        if not searches_running:
            break  # Stop the loop if the "Stop Searches" button is clicked
        print("Performing a random search in a new tab in the default web browser...")
        perform_random_search(random.choice(search_engines))
        time.sleep(custom_search_delay)
    searches_running = False
    print("Searches completed.")

def start_program():
    global searches_running
    global custom_num_searches
    global custom_search_delay

    if not searches_running:
        custom_num_searches = int(num_searches_entry.get())
        # Create a new thread to run the searches
        search_thread = threading.Thread(target=start_searches)
        search_thread.start()

def stop_program():
    global searches_running
    searches_running = False

# Create a Tkinter window
window = tk.Tk()
window.title("Random Search App")

# Create an entry field for custom number of searches
num_searches_label = tk.Label(window, text="Enter the number of searches:")
num_searches_label.pack(pady=10)

num_searches_entry = tk.Entry(window)
num_searches_entry.pack(pady=5)
num_searches_entry.insert(0, str(custom_num_searches))

custom_delay_label = tk.Label(window, text="Enter the custom delay (in seconds):")
custom_delay_label.pack(pady=10)

custom_delay_entry = tk.Entry(window)
custom_delay_entry.pack(pady=5)
custom_delay_entry.insert(0, str(custom_search_delay))

  # Set the default value

# Create a button that starts the program
start_button = tk.Button(window, text="Start Random Searches", command=start_program)
start_button.pack(pady=10)

# Create a button to stop the searches
stop_button = tk.Button(window, text="Stop Searches", command=stop_program)
stop_button.pack(pady=5)

# Run the Tkinter main loop
window.mainloop()
