"""This script scrapes news from the news website and saves it in a csv file."""
import csv
from typing import List, Dict

import requests
import pandas as pd
from bs4 import BeautifulSoup

from assignment_14_web_scrapping.utils import get_date_from_string, is_in_range

NEWS_WEBSITE = "https://www.cbsnews.com"


def get_page(url: str) -> BeautifulSoup | None:
    """
    Loads HTML and returns BeautifulSoup object.

    Args:
         url (str): URL to scrape.
    Returns:
        BeautifulSoup | None: BeautifulSoup object or None
    """
    try:
        response = requests.get(url)
        return BeautifulSoup(response.content, "html.parser")
    except requests.exceptions.RequestException as exception:
        print(exception)
        return None


def parse_news(soup: BeautifulSoup) -> List[Dict]:
    """
    Scrapes news from the BeautifulSoup object

    Args:
        soup (BeautifulSoup): BeautifulSoup object
    Returns:
        List[Dict]: list of news data
    """
    articles = soup.find_all("article", {"class": "item"})
    result = []

    for article in articles:
        title = article.find("h4", {"class": "item__hed"})
        link = article.find("a", {"class": "item__anchor"})
        date = article.find("li", {"class": "item__date"})
        summary = article.find("p", {"class": "item__dek"})

        if title and link and date and summary:
            result.append({
                "title": title.text.strip(),
                "link": link.get("href"),
                "date": get_date_from_string(date.text.strip()),
                "summary": summary.text.strip(),
            })
    return result


def save_to_csv(news_data: List[Dict], file_name: str = "news") -> None:
    """
    Saves news data to a csv file

    Args:
        news_data (List[Dict]): list of news data
        file_name (str): name of the file (news by default)
    """
    keys = data[0].keys()

    with open(f"{file_name}.csv", "w", newline="") as csvfile:
        dict_writer = csv.DictWriter(csvfile, keys)
        dict_writer.writeheader()
        dict_writer.writerows(news_data)


def filter_by_days(news_data: List[Dict], days: int = 7) -> List[Dict]:
    """
    Filters news data by days

    Args:
        news_data (List[Dict]): list of news data
        days (int): number of days to filter (7 by default)
    Returns:
        List[Dict]: list of filtered news data
    """
    filtered_news = []

    for new in news_data:
        if is_in_range(new["date"], days):
            filtered_news.append(new)
    return filtered_news


def show_statistics(news_data: List[Dict]) -> None:
    """
    Shows statistics about news data

    Args:
        news_data (List[Dict]): list of news data
    """
    df = pd.DataFrame(news_data)
    df["date_dt"] = pd.to_datetime(df["date"], dayfirst=True)

    stats = df.groupby(df["date_dt"].dt.date).size().reset_index(name="Number of news")
    stats.columns = ["Date", "Number of news"]
    stats = stats.sort_values(by='Date', ascending=False)

    print(f"Stats report\n{stats.to_string(index=False)}")


if __name__ == "__main__":
    new_soup = get_page(NEWS_WEBSITE)
    if new_soup:
        data = parse_news(new_soup)
        news = filter_by_days(data)
        save_to_csv(data)
        save_to_csv(news, "filtered_news")
        show_statistics(data)
