import requests
from bs4 import BeautifulSoup


class Scraper:
    """This class is for handling scraper"""
    def __init__(self, base_url, food_url, trip_url, experiences, course_url, story_url):
        self.base_url = base_url
        self.food_url = food_url
        self.trip_url = trip_url
        self.experiences = experiences
        self.course_url = course_url
        self.story_url = story_url

    def search_trips(self, continent: str) -> None:
        """Search for trips"""
        response = requests.get(self.trip_url.format(continent=continent))
        print(response.status_code)
        soup = BeautifulSoup(response.text, 'html.parser')
        links = soup.find_all(
            name='div',
            attrs={'class': 'card__body relative flex h-full flex-col gap-1 text-gray-700'}
        )

        for link in links:
            url = self.base_url+link.find('a')['href']
            Scraper.get_trip_info(url=url)

    @staticmethod
    def get_trip_info(url):
        """Scrape trip info from the url"""
        response = requests.get(url=url)
        soup = BeautifulSoup(response.text, 'html.parser')
        title = soup.find(name='h2', attrs={'class': 'hermes-heading-small mb-14'}).text
        info = soup.find_all(name='p', attrs={'class': 'text-sm font-medium leading-5 text-gray-900'})
        continent = info[0].text.strip()
        days = info[1].text.strip()
        nights = info[2].text.strip()
        group_size = info[3].text.strip()
        activity = info[4].text.strip()
        interest = info[5].text.strip()
        description = soup.find(
            name='div',
            attrs={'class': 'prose prose-p:hermes-body-small prose-p:text-gray-800 prose-a:hermes-link-inline mb-14'}
        ).find(name='p').text
        print(
            title,
            continent,
            days,
            nights,
            group_size,
            activity,
            interest,
            description,
        )
        print('-'*50)
