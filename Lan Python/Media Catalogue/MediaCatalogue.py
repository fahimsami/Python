class Movie:
    """Parent class representing a movie."""
    def __init__(self, title, year, director, duration):
        if not title or title.strip() == "":
            raise ValueError("Title cannot be empty.")
        if year < 1895:
            raise ValueError("Year must be 1895 or later.")
        if not director or director.strip() == "":
            raise ValueError("Director cannot be empty.")
        if duration <= 0 :
            raise ValueError("Duration must be positive.")
        
        self.title = title
        self.year = year
        self.director = director
        self.duration = duration
    
    def __str__(self):
        return f"{self.title} ({self.year}) - {self.duration} mins, {self.director}"
    
class MediaCatalogue:
    """A catalogue that can store different types of media items."""
    def __init__(self):
        self.items = []
        
    def add(self, media_item):
        if not isinstance(media_item, (Movie, TVSeries)):
            raise ValueError("Media item must be an instance of Movie or TVSeries.")
        self.items.append(media_item)
        
    def __str__(self):
        if not self.items:
            return "Media Catalogue is empty."
        result = f"Media Catalogue ({len(self.items)} items): \n\n"
        for idx, item in enumerate(self.items, start = 1):
            result += f"{idx}. {item}\n"
        return result

catalogue = MediaCatalogue()

class TVSeries(Movie):
    """Child class representing an entire TV series."""
    def __init__(self, title, year, director, duration, seasons, total_episodes):
        if seasons < 1:
            raise ValueError("Seasons must be at least 1.")
        if total_episodes < 1:
            raise ValueError("Total episodes must be at least 1."
                             )
        self.seasons = seasons
        self.total_episodes = total_episodes
        super().__init__(title, year, director, duration)
        
    def __str__ (self):
        return f"{self.title} ({self.year}) - {self.seasons} seasons, {self.total_episodes} episodes, duration per episode: {self.duration} mins, {self.director}"
        
try:
    series1 = TVSeries("Breaking Bad", 2008, "Vince Gilligan", 47, 5, 62)
    catalogue.add(series1)
    series2 = TVSeries("Game of Thrones", 2011, "David Benioff, D.B. Weiss", 57, 8, 73)
    catalogue.add(series2)
    print(catalogue)
   
    
except ValueError as e:
    print(f"Validation Error: {e}")
        
    

try:    
    movie1 = Movie("Inception", 2010, "Christopher Nolan", 148)
    movie2 = Movie("The Matrix", 1999, "Lana Wachowski, Lilly Wachowski", 136)
    catalogue.add(movie1)
    catalogue.add(movie2)
    print(catalogue)
    
except ValueError as e:
    print(f"Validation Error: {e}")
    


    

  
        