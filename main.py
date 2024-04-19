from constants import (
    BASE_URL, FOOD_URL, TRIP_URL, EXPERIENCES_URL, COURSES_URL, STORY_URL, PAGE_NUMBER, TITLE, CONTINENT
)
from database_manager import DatabaseManager
from local_settings import DATABASE
import models
import scraper
import logging


# Logging basic configs
logging.basicConfig(filename='logs.log')

scraper_handler = scraper.Scraper(
    base_url=BASE_URL,
    food_url=FOOD_URL,
    trip_url=TRIP_URL,
    experience_url=EXPERIENCES_URL,
    course_url=COURSES_URL,
    story_url=STORY_URL,
)

db_manager = DatabaseManager(
    database_name=DATABASE['name'],
    user=DATABASE['user'],
    password=DATABASE['password'],
    host=DATABASE['host'],
    port=DATABASE['port'],
)


if __name__ == '__main__':

    try:
        db_manager.create_tables([models.Trip, models.SearchKey])

        title = input('What are you looking for?(Trips - Experiences - Courses - Foods - Stories): ').lower() or TITLE

        if title == 'foods':
            page = input('Please enter page number: ') or PAGE_NUMBER
            models.SearchKey.get_or_create(
                title=title,
                page=page
            )
        elif title == 'trips':
            continent = input('please enter a continent: ').lower() or CONTINENT
            models.SearchKey.get_or_create(
                title=title,
                continent=continent
            )
            scraper_handler.search_trips(continent=continent)
        elif title == 'experiences':
            models.SearchKey.get_or_create(
                title=title,
            )

    except ValueError as error:
        print('ValueError:', error)
        logging.error(f'ValueError: {error}')
    except TimeoutError as error:
        print('TimeoutError:', error)
        logging.error(f'TimeoutError: {error}')
    except AttributeError as error:
        print('AttributeError:', error)
        logging.error(f'AttributeError: {error}')
    except KeyError as error:
        print('KeyError:', error)
        logging.error(f'KeyError: {error}')
    finally:
        if db_manager.db:
            db_manager.close_connection()
            print('Database connection closed')


