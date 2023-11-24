import copy
import requests
import time
from abc import ABC, abstractmethod
from datetime import datetime, timedelta
from .core.info import CITY_INFORMATION, CATEGORIES


class Validator(ABC):
    """
    Abstract base class for all validators
    """

    @abstractmethod
    def validate(self, value):
        """
        Validates the given value and returns
        the validated value or raises an exception
        """
        pass


class SortValidator(Validator):
    @staticmethod
    def validate(sort):
        valid_sorts = ["sort_date", "cheapest", "most_expensive"]
        if sort not in valid_sorts:
            raise ValueError(f"sort must be one of {valid_sorts}")
        return sort


class CategoryValidator(Validator):
    @staticmethod
    def validate(category):
        valid_cats = CATEGORIES
        if category not in valid_cats:
            raise ValueError(f"Invalid category {category}")
        return category


class CitiesValidator(Validator):
    @staticmethod
    def validate(cities):
        if cities == "__all__":
            cities = [
                str(city["id"])
                for province in CITY_INFORMATION
                for city in province["children"]
                if not city["isProvince"]
            ]
        else:
            cities = [str(_id) for _id in cities]
        return cities


class DivarAPI:
    BASE_URL = "https://api.divar.ir/v8/web-search/"
    PARAMS = {
        "page": 1,
        "json_schema": {
            "category": {"value": "ROOT"},
            "sort": {"value": "sort_date"},
            "cities": [],
        },
    }

    @staticmethod
    def build_url(category, cities, sort=None, method="GET", filters={}):
        if method == "GET":
            url = DivarAPI.BASE_URL + "iran/" + CATEGORIES.get(category)
            url += "?cities=" + "%2C".join(cities)
            if sort:
                url += "&sort=" + sort
            if filters:
                for filter_name, filter_value in filters.items():
                    if isinstance(filter_value, list):
                        filter_value = "%2C".join(filter_value)
                    url += f"&{filter_name}={filter_value}"
        elif method == "POST":
            url = DivarAPI.BASE_URL + "1/" + category
        else:
            raise ValueError('method must be one of "GET", "POST"')
        return url

    @staticmethod
    def build_params(category, sort, cities, last_post_date, filters={}):
        sort = SortValidator.validate(sort)
        category = CategoryValidator.validate(category)
        cities = CitiesValidator.validate(cities)
        params = copy.deepcopy(DivarAPI.PARAMS)
        params["json_schema"]["sort"]["value"] = sort
        params["json_schema"]["cities"] = cities
        params["json_schema"]["category"]["value"] = category
        params["last-post-date"] = last_post_date
        for filter_name, filter_value in filters.items():
                params["json_schema"][filter_name] = {"value": filter_value}
        return params


class DivarParser:
    @staticmethod
    def extract_ads(data):
        ads = []
        for ad in data["web_widgets"]["post_list"]:
            if ad["widget_type"] == "POST_ROW":
                ad = ad["data"]
                ads.append(ad)
        return ads


class DivarClient:
    """
    A class representing a client for interacting with the Divar API.

    Methods:
    - get(url): Sends a GET request to the specified URL and returns the extracted ads and the last post date.
    - post(url, params): Sends a POST request to the specified URL with the given parameters and returns the ads and a flag indicating if it's the last page.
    """

    @staticmethod
    def get(url):
        response = requests.get(url)
        if response.status_code == 200:
            response = response.json()
            return DivarParser.extract_ads(response), response["last_post_date"]
        elif response.status_code == 404:
            return [], -1
        else:
            time.sleep(5)
            return DivarClient.get(url)

    @staticmethod
    def post(url, params):
        while True:
            response = requests.post(url, json=params)
            if response.status_code == 429:
                time.sleep(5)
                continue
            if response.status_code >= 500:
                continue
            break
        data = response.json()
        _is_last_page = "last_post_date" not in data or data["last_post_date"] == -1
        if _is_last_page:
            return [], _is_last_page

        params["page"] += 1
        last_post_date = data["last_post_date"]
        params["last-post-date"] = last_post_date
        ads = DivarParser.extract_ads(data)
        return ads, _is_last_page


class AdFetcher:
    @staticmethod
    def get_ads(
        category,
        sort="sort_date",
        cities="__all__",
        _from=int((datetime.now() - timedelta(days=1)).strftime("%s%f")),
        filters={},
    ):
        """
        Retrieves ads from Divar API based on the specified category, sort order, cities, and other optional parameters.

        Parameters:
        - category (str): The category of ads to retrieve.
        - sort (str, optional): The sort order of the ads. Defaults to 'sort_date'.
        - cities (str, optional): The cities to filter the ads by. Defaults to '__all__'.
        - _from (int, optional): The timestamp indicating the starting point to retrieve ads from. Defaults to 24 hours ago.
        - filters (dict, optional): The filters to apply to the ads. Defaults to {}.

        Returns:
        - ads (list): A list of ads retrieved from the Divar API.
        """

        sort = SortValidator.validate(sort)
        category = CategoryValidator.validate(category)
        cities = CitiesValidator.validate(cities)

        url = DivarAPI.build_url(category, cities, sort, method="GET", filters=filters)
        ads, last_post_date = DivarClient.get(url)
        for ad in ads:
            yield ad

        params = DivarAPI.build_params(category, sort, cities, last_post_date, filters=filters)
        while params["last-post-date"] >= _from:
            url = DivarAPI.build_url(category, cities, sort, method="POST", filters=filters)
            ads, is_last_page = DivarClient.post(url, params)
            for ad in ads:
                yield ad
            if is_last_page:
                break
