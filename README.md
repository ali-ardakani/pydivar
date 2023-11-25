# pydivar: Effortless Divar data extraction in Python

| | |
| --- | --- |
| Testing | [![CI - Test](https://github.com/ali-ardakani/pydivar/actions/workflows/unit-tests.yml/badge.svg)](https://github.com/ali-ardakani/pydivar/actions/workflows/unit-tests.yml) |
| Package | [![PyPI Latest Release](https://img.shields.io/pypi/v/pydivar.svg)](https://pypi.org/project/pydivar/) [![PyPI Downloads](https://img.shields.io/pypi/dm/pydivar.svg?label=PyPI%20downloads)](https://pypi.org/project/pydivar/)
| Meta | [![License](https://img.shields.io/pypi/l/pydivar.svg)](https://github.com/aliardakani/pydivar/blob/master/LICENSE)

## What is it?

**pydivar** is a Python library designed for efficiently crawling data from Divar, leveraging the Divar API. This versatile library supports data retrieval across all categories available on Divar, providing comprehensive crawling capabilities with support for various filters. Whether you need to collect data for analysis, research, or any other purpose, **pydivar** streamlines the process, making it easy to harness the power of Divar's diverse dataset. Start exploring and extracting valuable insights with **pydivar** today!

## Table of Contents

- [Key Features](#key-features)
- [Where to get it](#where-to-get-it)
- [Dependencies](#dependencies)
- [Installation from Source](#installation-from-source)
- [Usage Guide](#usage-guide)
- [City Information](#city-information)
- [Category Information](#category-information)
- [Background](#background)
- [Discussion and Development](#discussion-and-development)
- [License](#license)

## Key Features

- Utilizes the Divar API for seamless and reliable data retrieval.
- Supports crawling data from all categories offered on Divar.
- Implements a flexible and user-friendly interface for applying filters to the crawled data.
- Empowers users to gather rich and diverse information by leveraging the full range of available Divar categories.

## Where to get it
The source code is currently hosted on GitHub at: `https://github.com/ali-ardakani/pydivar.git`

Binary installers for the latest released version are available at the [Python Package Index (PyPI)](https://pypi.org/project/pandas).
    
```sh
pip install pydivar
```

## Dependencies

- [requests](https://pypi.org/project/requests/)
- [aiohttp](https://pypi.org/project/aiohttp/)

See [requirements.txt](requirements.txt) for more information.

## Installation from Source

To install pydivar from the source code, follow these steps:

1. Clone the GitHub repository:

```bash
git clone https://github.com/yourusername/pydivar.git
```

2. Navigate to the pydivar directory:

```bash
cd pydivar
```

3. Install the required dependencies:

```bash
pip install -r requirements.txt
```

After these steps, PyDivar should be installed on your system. You can then use it in your Python projects or scripts.

If you encounter any issues during the installation process, please refer to the troubleshooting section in the repository or open an issue on GitHub for assistance.
 
## Usage Guide

### AdFetcher Class

The `AdFetcher` class provides a static method `get_ads` to retrieve ads from the Divar API based on specified parameters. By using this, you can easily fetch a list of advertisements.

```python
from pydivar import AdFetcher

# Retrieve ads for the "apartment-rent" category in all cities, sorted by date.
ads = AdFetcher.get_ads(category="light", sort="sort_date", cities=[16, 5], filters={"body_status": ["some-scratches", "paintless-dent-removal"]})

# Print the retrieved ads
for ad in ads:
    print(ad)
```

Parameters for get_ads method:

* category (str): The category of ads to retrieve. You can see the list of available categories in the [Category Information](#category-information) section.
* sort (str, optional): The sort order of the ads. Defaults to 'sort_date'.
* cities (str, optional): The cities to filter the ads by. Defaults to 'all'. You can see the list of available cities in the [City Information](#city-information) section.
* _from (int, optional): The timestamp indicating the starting point to retrieve ads from. Defaults to 24 hours ago.
* filters (dict, optional): The filters to apply to the ads. Defaults to {}.You can refer to the [Category Information](#category-information) section to find the available filters for the specified category.

### PostDetailService Class

The PostDetailService class is a service class for retrieving post details.

1. Retrieve details for a single post using its token:
```python
from pydivar import PostDetailService

# Create an instance of PostDetailService
post_detail_service = PostDetailService()

# Retrieve details for a single post using its token
post_token = "example_post_token"
post_details = post_detail_service.get_post_details(token=post_token)

# Print the details of the post
print(post_details)
```

2. Retrieve details for multiple posts using their tokens:
```python
from pydivar import PostDetailService, AdFetcher

# Use AdFetcher to get ads
ads = AdFetcher.get_ads(category="light", sort="sort_date", cities=[16, 5], filters={"body_status": ["some-scratches", "paintless-dent-removal"]})

# Get the tokens of the retrieved ads
ad_tokens = [ad["token"] for ad in ads]

# Use PostDetailService to get details for the retrieved ad tokens
post_detail_service = PostDetailService()
```
* Concurrently:
```python
# Get details for the retrieved ad tokens concurrently
post_details = post_detail_service.get_post_details(token=ad_tokens, maximum_task=10)
```
* Sequentially:
```python
# Get details for the retrieved ad tokens sequentially
post_details = post_detail_service.get_post_details(token=ad_tokens, maximum_task=10)
```

Parameters for get_post_details method:

* token (str or list): The token(s) of the post(s). Can be a single token or a list of tokens.
* maximum_task (int): The maximum number of concurrent tasks. Defaults to 5.

This example demonstrates how to integrate both AdFetcher and PostDetailService to retrieve ads and their details concurrently.

## City Information

To retrieve ads for multiple cities, instantiate the `AdFetcher` class and call the `get_ads` method with the required parameters, including a list of city IDs. The following table lists the available city IDs for each province.

### Azarbaijan East Province
- 853: Azarshahr
- 759: Ahar
- 760: Bonab
- 5: Tabriz
- 852: Sarab
- 761: Sahand
- 762: Maragheh
- 763: Marand
- 764: Mianeh

### Azerbaijan West Province
- 10: Urmia
- 859: Oshnavieh
- 765: Bukan
- 766: Piranshahr
- 767: Khoy
- 857: Sardasht
- 768: Salmas
- 858: Shahin Dej
- 856: Maku
- 769: Mahabad
- 792: Miandoab
- 770: Naqadeh

### Ardabil Province
- 17: Ardabil
- 771: Parsabad
- 772: Khalkhal
- 1741: Sarein
- 1743: Germi
- 773: Meshgin Shahr
- 1742: Namin

### Isfahan Province
- 1737: Aran Va Bidgol
- 1723: Abrisham Isfahan
- 4: Isfahan
- 1747: Khomeyni Shahr
- 1727: Khansar
- 1750: Khour
- 1724: Daran
- 1725: Semirom
- 1744: Shahin Shahr
- 849: Falavarjan
- 1745: Foolad Shahr
- 1746: Ghamsar
- 30: Kashan
- 848: Golpayegan
- 1749: Lenjan
- 1748: Mobarakeh
- 31: Najafabad

### Alborz Province
- 1722: Asara
- 1721: Eshtehard
- 1739: Tankaman
- 1740: Charbagh Alborz
- 850: Taleqan
- 1751: Fardis
- 2: Karaj
- 1738: Koohsar
- 1720: Garmdareh
- 1753: Mahdasht
- 1752: Mohammad Shahr
- 774: Nazarabad
- 1754: Hashtgerd

### Ilam Province
- 775: Abdanan
- 32: Ilam
- 776: Eyvan
- 777: Dehloran
- 1823: Mehran

### Bushehr Province
- 778: Borazjan
- 1756: Dayyer
- 779: Bandar Kangan
- 780: Bandar Ganaveh
- 25: Bushehr
- 1757: Jam
- 1755: Khormoj

### Tehran Province
- 1709: Absard
- 1715: Abali
- 1714: Arjmand
- 29: Eslamshahr
- 1764: Andisheh New Town
- 1707: Baghershahr
- 1768: Bumehen
- 1760: Pakdasht
- 1767: Pardis
- 1766: Parand
- 781: Pishva
- 1: Tehran
- 1718: Javadabad
- 782: Chahar Dangeh
- 783: Damavand
- 1765: Robat Karim
- 1769: Rudehen
- 1763: Shahr E Rey
- 1713: Shahedshahr
- 1717: Shemshak
- 1759: Shahriar
- 1712: Sabashahr
- 1710: Safadasht Industrial City
- 1716: Ferdosiye
- 1772: Fasham
- 1770: Firuzkooh
- 1758: Qods
- 1761: Qarchak
- 1708: Kahrizak
- 1719: Kilan
- 1706: Golestan Baharestan
- 1771: Lavasan
- 784: Nasimshahr
- 1711: Vahidieh
- 1762: Varamin

### Chahar Mahaal And Bakhtiari Province
- 785: Boroujen
- 1833: Saman
- 36: Shahrekord
- 786: Farrokhshahr
- 787: Lordegan

### Khorasan South Province
- 34: Birjand
- 788: Tabas
- 789: Ferdows
- 790: Ghayen

### Khorasan Razavi Province
- 1735: Bardaskan
- 1729: Taybad
- 791: Torbat Jam
- 1776: Torbat Heydariyeh
- 1732: Chenaran
- 1736: Khaf
- 316: Sabzevar
- 1775: Shandiz
- 1774: Torghabeh
- 1733: Qasemabad Khaf
- 1777: Quchan
- 1773: Golbahar
- 847: Gonabad
- 3: Mashhad
- 1778: Molkabad
- 318: Neyshabur

### Khorasan North Province
- 793: Ashkhaneh
- 794: Esfarāyen
- 39: Bojnurd
- 795: Shirvan

### Khuzestan Province
- 24: Abadan
- 1779: Omidiyeh
- 796: Andimeshk
- 7: Ahvaz
- 797: Izeh
- 798: Bandar Imam Khomeini
- 37: Bandar Mahshahr
- 314: Behbahan
- 1782: Chamran Town
- 1784: Hamidiyeh
- 799: Khorramshahr
- 23: Dezful
- 1781: Ramshir
- 800: Ramhormoz
- 756: Susangerd
- 1780: Shadeghan
- 754: Shush
- 602: Shooshtar
- 317: Masjed Soleyman
- 1783: Hendijan

### Zanjan Province
- 802: Abhar
- 803: Khorramdarreh
- 20: Zanjan
- 804: Qeydar

### Semnan Province
- 805: Damghan
- 35: Semnan
- 707: Shahroud
- 806: Garmsar

### Sistan And Baluchestan Province
- 807: Iranshahr
- 747: Chabahar
- 1785: Khash
- 706: Zabol
- 11: Zahedan
- 1787: Zahak
- 865: Saravan
- 1786: Konarak

### Fars Province
- 851: Abadeh
- 1728: Eqlid
- 808: Jahrom
- 1793: Khoour
- 809: Darab
- 1791: Zarghan
- 6: Shiraz
- 810: Sadra
- 1789: Fasa
- 1734: Firuzabad
- 1790: Kazeroon
- 1730: Lar
- 1731: Lamerd
- 1788: Marvdasht
- 1792: Mohr
- 1794: Norabad
- 1726: Neyriz

### Qazvin Province
- 869: Abyek
- 1795: Eqbaliyeh
- 872: Alvand
- 811: Takestan
- 1796: Shal
- 19: Qazvin
- 873: Mohammadiyeh

### Qom Province
- 8: Qom

### Kurdistan Province
- 662: Baneh
- 868: Bijar
- 1798: Dehgolan
- 812: Saqqez
- 28: Sanandaj
- 813: Qorveh
- 1797: Kamyaran
- 814: Marivan

### Kerman Province
- 1804: Baft
- 1805: Bardsir
- 1807: Boluk
- 815: Bam
- 816: Jiroft
- 817: Rafsanjan
- 867: Zarand
- 818: Sirjan
- 13: Kerman
- 1803: Kahnooj
- 1806: Mahan

### Kermanshah Province
- 819: Eslamabad Gharb
- 1801: Bisotun
- 820: Javanrud
- 854: Sarpol Zahab
- 855: Sonqor
- 1800: Sahneh
- 9: Kermanshah
- 821: Kangavar
- 1802: Gahvareh
- 1799: Harsin

### Kohgiluyeh And Boyer Ahmad Province
- 874: Dogonbadan
- 822: Dehdasht
- 1808: Sisakht
- 38: Yasuj

### Golestan Province
- 1691: Azadshahr Golestan
- 748: Aq Qala
- 751: Bandar Torkaman
- 823: Aliabad Katul
- 750: Kordkuy
- 1692: Kalale
- 1832: Galikesh
- 21: Gorgan
- 749: Gomishan
- 743: Gonbad Kavus
- 1693: Minoodasht

### Gilan Province
- 824: Astara
- 825: Astaneh Ashrafiyeh
- 1852: Ahmadsar Gourab
- 1812: Asalem
- 1688: Amlash
- 1854: Barah Sar
- 708: Bandar Anzali
- 1841: Pareh Sar
- 829: Talesh
- 1855: Toutkabon
- 1850: Jirandeh
- 864: Chaboksar
- 1686: Chaf Chamkhale
- 1844: Chobar
- 1847: Haviq
- 1689: Khoshkbijar
- 1809: Khomam
- 1814: Deylaman
- 1851: Rankouh
- 1839: Rahim Abad
- 1835: Rostam Abad
- 12: Rasht
- 1684: Rezvanshahr
- 1810: Rudbar
- 1849: Roudbaneh
- 826: Rudsar
- 1683: Zibakenar
- 1811: Sangar
- 861: Siahkal
- 1813: Shaft
- 1845: Shelman
- 827: Someh Sara
- 860: Fuman
- 863: Kelachay
- 1840: Kouchesfahan
- 1843: Koumeleh
- 1687: Kiashahr
- 1846: Gourab Zarmikh
- 746: Lahijan
- 1690: Lashtenesha
- 828: Langarud
- 1836: Loshan
- 1842: Loulman
- 1837: Lavandevil
- 1848: Lisar
- 862: Masal
- 1815: Masuleh
- 1853: Makloan
- 1834: Manjil

### Lorestan Province
- 870: Azna
- 1816: Aleshtar
- 830: Aligudarz
- 26: Borujerd
- 1817: Pol Dokhtar
- 27: Khorramabad
- 752: Dorud
- 831: Kuhdasht
- 753: Nurabad

### Mazandaran Province
- 1871: Aalasht
- 663: Amol
- 1703: Amirkala
- 1701: Izadshahr
- 664: Babol
- 710: Babolsar
- 1873: Baladeh
- 832: Behshahr
- 1865: Bahnamir
- 1702: Polsefid
- 833: Tonekabon
- 834: Juybar
- 835: Chalus
- 1694: Chamestan
- 1861: Khalil Shahr
- 1868: Khoshroud Pey
- 745: Ramsar
- 1860: Rostamkola
- 1698: Royan
- 1872: Reyneh
- 1859: Ziraab
- 22: Sari
- 1700: Sorkhrood
- 1699: Salman Shahr
- 1862: Sourek
- 1863: Shirgah
- 1697: Abbasabad Mazandaran
- 1819: Farahabad
- 836: Fereydunkenar
- 1875: Farim
- 665: Qaemshahr
- 1858: Katalem Sadatshahr
- 1695: Kelarabad
- 1696: Kelarestan
- 1870: Kouhi Kheyl
- 1869: Kiasar
- 1864: Kiakola
- 1866: Gatab
- 1876: Gazanak
- 1856: Galougah Babol
- 837: Mahmudabad
- 1867: Marzan Abad
- 1874: Marzikola
- 1818: Nashtarud
- 838: Neka
- 744: Nur
- 709: Nowshahr

### Markazi Province
- 15: Arak
- 839: Khomein
- 1824: Delijan
- 671: Saveh
- 1825: Shazand
- 840: Mahalat
- 1826: Mohajeran

### Hormozgan Province
- 18: Bandar Abbas
- 1822: Takht
- 1820: Dargahan
- 660: Qeshm
- 33: Kish
- 841: Minab
- 1821: Hormuz

### Hamadan Province
- 842: Asadabad
- 1828: Bahar
- 866: Tuyserkan
- 1827: Kabudrahang
- 843: Malayer
- 844: Nahavand
- 14: Hamedan

### Yazd Province
- 846: Ardakan
- 1829: Bafq
- 1831: Taft
- 871: Hamidia
- 1830: Mehriz
- 845: Meybod
- 16: Yazd

## Category Information

To use a category, you must pass the category name to the `AdFetcher.get_ads()` method when retrieving ads. The `category` parameter is required and helps narrow down the type of ads you want to fetch.
<br>
Depending on the type of category, you can use filters to refine your search. Pass the filter name to the AdFetcher.get_ads() method to apply specific filters to your query.

---

### Category: ROOT



### category
- **Title**: دسته‌بندی
- **Type**: object

### goods-business-type
- **Title**: نوع آگهی‌دهنده
- **Type**: object
- **Queries**: 
  - all -> همه
  - personal -> شخصی
  - marketplace -> فروشگاه

### has-photo
- **Title**: فقط عکس‌دار
- **Type**: boolean

### price
- **Title**: قیمت
- **Type**: object
 - **Minimum**: 0
 - **Maximum**: N/A

### sort
- **Title**: ترتیب نمایش آگهی‌ها براساس
- **Type**: object
- **Queries**: 
  - quality_and_sort_date -> quality_and_sort_date
  - sort_date -> sort_date
  - cheapest -> cheapest
  - most_expensive -> most_expensive
  - production_year -> production_year
  - usage -> usage
  - most_popular -> most_popular
  - most_relevant -> most_relevant

### urgent
- **Title**: فقط فوری‌ها
- **Type**: boolean



---

### Category: accessories



### category
- **Title**: دسته‌بندی
- **Type**: object

### divider
- **Title**: سایر فیلتر‌ها
- **Type**: object

### exchange
- **Title**: نمایش معاوضه‌ها
- **Type**: object
- **Queries**: 
  - only-exchanges -> نمایش فقط معاوضه‌ها
  - exclude-exchanges -> حذف معاوضه‌ها

### has-photo
- **Title**: فقط عکس‌دار
- **Type**: boolean

### price
- **Title**: قیمت
- **Type**: object
 - **Minimum**: 0
 - **Maximum**: N/A

### sort
- **Title**: ترتیب نمایش آگهی‌ها براساس
- **Type**: object
- **Queries**: 
  - quality_and_sort_date -> quality_and_sort_date
  - sort_date -> sort_date
  - cheapest -> cheapest
  - most_expensive -> most_expensive
  - production_year -> production_year
  - usage -> usage
  - most_popular -> most_popular
  - most_relevant -> most_relevant

### urgent
- **Title**: فقط فوری‌ها
- **Type**: boolean



---

### Category: accounting-and-finance



### category
- **Title**: دسته‌بندی
- **Type**: object

### expertises
- **Title**: تخصص
- **Type**: object
 - **Items Type**: array
- **Queries**: 
  - ROOT -> همه تخصص‌ها
  - insurance-services -> خدمات بیمه
  - third-party-insurance -> بیمهٔ شخص ثالث
  - body-insurance -> بیمهٔ بدنه
  - life-insurance -> بیمهٔ عمر و سرمایه گذاری
  - supplementary-insurance -> بیمهٔ تکمیلی
  - accident-insurance -> بیمهٔ حوادث
  - legal-services -> خدمات حقوقی
  - family-lawsuits -> دعاوی خانواده
  - criminal-lawsuits -> دعاوی کیفری
  - real-estate-lawsuit -> دعاوی ملکی
  - inheritance-litigation -> دعاوی انحصار وراثت
  - tax-business-documents-claims -> دعاوی مالیاتی و اسناد تجاری
  - labor-litigation -> دعاوی روابط کار و تامین اجتماعی
  - contract-negotiation -> مذاکره و تنظیم قراردادها
  - finance-taxation-services -> امور مالی و مالیاتی
  - tax-services -> خدمات مالیاتی
  - accounting-audit-services -> خدمات حسابداری و حسابرسی
  - registration-services -> امور ثبتی
  - company-registration -> ثبت، انحلال و رتبه بندی شرکت
  - brand-registration -> ثبت برند، لوگو و اختراع
  - business-license -> اخذ جواز، پروانه و کارت بازرگانی
  - financing-accounting-insurance-others -> سایر مالی/حسابداری/بیمه

### has-photo
- **Title**: فقط عکس‌دار
- **Type**: boolean

### sort
- **Title**: ترتیب نمایش آگهی‌ها براساس
- **Type**: object
- **Queries**: 
  - quality_and_sort_date -> quality_and_sort_date
  - sort_date -> sort_date
  - cheapest -> cheapest
  - most_expensive -> most_expensive
  - production_year -> production_year
  - usage -> usage
  - most_popular -> most_popular
  - most_relevant -> most_relevant

### urgent
- **Title**: فقط فوری‌ها
- **Type**: boolean



---

### Category: accounting-finance-legal



### category
- **Title**: دسته‌بندی
- **Type**: object

### divider
- **Title**: سایر فیلتر‌ها
- **Type**: object

### employee_gender
- **Title**: جنسیت کارجو
- **Type**: object
- **Queries**: 
  - female -> زن
  - male -> مرد
  - neutral -> فرقی ندارد

### experience
- **Title**: سابقهٔ مورد نیاز
- **Type**: object
 - **Minimum**: N/A
 - **Maximum**: N/A

### has-photo
- **Title**: فقط عکس‌دار
- **Type**: boolean

### health_insurance
- **Title**: با بیمه
- **Type**: boolean

### job_type
- **Title**: نوع همکاری
- **Type**: object
 - **Items Type**: array
- **Queries**: 
  - full_time -> تمام وقت
  - part_time -> پاره وقت
  - contract -> پیمان‌کاری/پروژه‌ای
  - internship -> کارآموزی
  - adaptive -> توافقی
  - other -> سایر

### military_service_status
- **Title**: پایان خدمت/معافیت
- **Type**: object
- **Queries**: 
  - finish_or_exemption_required -> الزامی
  - finish_not_required -> اختیاری

### no_experience_required
- **Title**: بدون نیاز به سابقه
- **Type**: boolean

### payment_method
- **Title**: شیوهٔ پرداخت
- **Type**: object
 - **Items Type**: array
- **Queries**: 
  - monthly -> ماهانه
  - daily -> روزانه
  - hourly -> ساعتی
  - percentage_commission -> پورسانتی/درصدی
  - adaptive -> توافقی
  - other -> سایر

### remote
- **Title**: با امکان دورکاری
- **Type**: boolean

### sort
- **Title**: ترتیب نمایش آگهی‌ها براساس
- **Type**: object
- **Queries**: 
  - quality_and_sort_date -> quality_and_sort_date
  - sort_date -> sort_date
  - cheapest -> cheapest
  - most_expensive -> most_expensive
  - production_year -> production_year
  - usage -> usage
  - most_popular -> most_popular
  - most_relevant -> most_relevant

### urgent
- **Title**: فقط فوری‌ها
- **Type**: boolean



---

### Category: administration-and-hr



### category
- **Title**: دسته‌بندی
- **Type**: object

### divider
- **Title**: سایر فیلتر‌ها
- **Type**: object

### employee_gender
- **Title**: جنسیت کارجو
- **Type**: object
- **Queries**: 
  - female -> زن
  - male -> مرد
  - neutral -> فرقی ندارد

### experience
- **Title**: سابقهٔ مورد نیاز
- **Type**: object
 - **Minimum**: N/A
 - **Maximum**: N/A

### has-photo
- **Title**: فقط عکس‌دار
- **Type**: boolean

### health_insurance
- **Title**: با بیمه
- **Type**: boolean

### job_type
- **Title**: نوع همکاری
- **Type**: object
 - **Items Type**: array
- **Queries**: 
  - full_time -> تمام وقت
  - part_time -> پاره وقت
  - contract -> پیمان‌کاری/پروژه‌ای
  - internship -> کارآموزی
  - adaptive -> توافقی
  - other -> سایر

### military_service_status
- **Title**: پایان خدمت/معافیت
- **Type**: object
- **Queries**: 
  - finish_or_exemption_required -> الزامی
  - finish_not_required -> اختیاری

### no_experience_required
- **Title**: بدون نیاز به سابقه
- **Type**: boolean

### payment_method
- **Title**: شیوهٔ پرداخت
- **Type**: object
 - **Items Type**: array
- **Queries**: 
  - monthly -> ماهانه
  - daily -> روزانه
  - hourly -> ساعتی
  - percentage_commission -> پورسانتی/درصدی
  - adaptive -> توافقی
  - other -> سایر

### remote
- **Title**: با امکان دورکاری
- **Type**: boolean

### sort
- **Title**: ترتیب نمایش آگهی‌ها براساس
- **Type**: object
- **Queries**: 
  - quality_and_sort_date -> quality_and_sort_date
  - sort_date -> sort_date
  - cheapest -> cheapest
  - most_expensive -> most_expensive
  - production_year -> production_year
  - usage -> usage
  - most_popular -> most_popular
  - most_relevant -> most_relevant

### urgent
- **Title**: فقط فوری‌ها
- **Type**: boolean



---

### Category: air-conditioning-fan-coil



### category
- **Title**: دسته‌بندی
- **Type**: object

### divider
- **Title**: سایر فیلتر‌ها
- **Type**: object

### exchange
- **Title**: نمایش معاوضه‌ها
- **Type**: object
- **Queries**: 
  - only-exchanges -> نمایش فقط معاوضه‌ها
  - exclude-exchanges -> حذف معاوضه‌ها

### goods-business-type
- **Title**: نوع آگهی‌دهنده
- **Type**: object
- **Queries**: 
  - all -> همه
  - personal -> شخصی
  - marketplace -> فروشگاه

### has-photo
- **Title**: فقط عکس‌دار
- **Type**: boolean

### price
- **Title**: قیمت
- **Type**: object
 - **Minimum**: 0
 - **Maximum**: N/A

### sort
- **Title**: ترتیب نمایش آگهی‌ها براساس
- **Type**: object
- **Queries**: 
  - quality_and_sort_date -> quality_and_sort_date
  - sort_date -> sort_date
  - cheapest -> cheapest
  - most_expensive -> most_expensive
  - production_year -> production_year
  - usage -> usage
  - most_popular -> most_popular
  - most_relevant -> most_relevant

### status
- **Title**: وضعیت کالا
- **Type**: object
 - **Items Type**: array
- **Queries**: 
  - new -> نو
  - like-new -> در حد نو
  - used -> کارکرده
  - repair-needed -> نیازمند تعمیر

### urgent
- **Title**: فقط فوری‌ها
- **Type**: boolean



---

### Category: animals



### category
- **Title**: دسته‌بندی
- **Type**: object

### divider
- **Title**: سایر فیلتر‌ها
- **Type**: object

### exchange
- **Title**: نمایش معاوضه‌ها
- **Type**: object
- **Queries**: 
  - only-exchanges -> نمایش فقط معاوضه‌ها
  - exclude-exchanges -> حذف معاوضه‌ها

### has-photo
- **Title**: فقط عکس‌دار
- **Type**: boolean

### price
- **Title**: قیمت
- **Type**: object
 - **Minimum**: 0
 - **Maximum**: N/A

### sort
- **Title**: ترتیب نمایش آگهی‌ها براساس
- **Type**: object
- **Queries**: 
  - quality_and_sort_date -> quality_and_sort_date
  - sort_date -> sort_date
  - cheapest -> cheapest
  - most_expensive -> most_expensive
  - production_year -> production_year
  - usage -> usage
  - most_popular -> most_popular
  - most_relevant -> most_relevant

### urgent
- **Title**: فقط فوری‌ها
- **Type**: boolean



---

### Category: apartment-rent



### building-age
- **Title**: سن بنا
- **Type**: object
- **Queries**: 
  - {"min": 0, "max": 1} -> حداکثر ۱ سال
  - {"min": 0, "max": 2} -> حداکثر ۲ سال
  - {"min": 0, "max": 5} -> حداکثر ۵ سال
  - {"min": 0, "max": 10} -> حداکثر ۱۰ سال
  - {"min": 0, "max": 15} -> حداکثر ۱۵ سال
  - {"min": 0, "max": 20} -> حداکثر ۲۰ سال
  - {"min": 0, "max": 30} -> حداکثر ۳۰ سال
  - {"min": 30} -> بیش از ۳۰ سال

### building_direction
- **Title**: جهت ساختمان
- **Type**: object
 - **Items Type**: array
- **Queries**: 
  - east -> شرقی
  - west -> غربی
  - north -> شمالی
  - south -> جنوبی

### business-type
- **Title**: آگهی‌دهنده
- **Type**: object
- **Queries**: 
  - personal -> شخصی
  - real-estate-business -> مشاور املاک

### category
- **Title**: دسته‌بندی
- **Type**: object

### cooling_system
- **Title**: سرمایش
- **Type**: object
 - **Items Type**: array
- **Queries**: 
  - water_cooler -> کولر آبی
  - air_conditioner -> کولر گازی
  - duct_split -> داکت اسپلیت
  - split -> اسپلیت
  - fan_coil -> فن کوئل

### credit
- **Title**: ودیعه
- **Type**: object
 - **Minimum**: 0
 - **Maximum**: N/A

### elevator
- **Title**: با آسانسور
- **Type**: boolean

### floor
- **Title**: طبقه
- **Type**: object
 - **Minimum**: -1
 - **Maximum**: N/A

### floor_type
- **Title**: جنس کف
- **Type**: object
 - **Items Type**: array
- **Queries**: 
  - ceramic -> سرامیک
  - wood_parquet -> پارکت چوب
  - laminate_parquet -> پارکت لمینت
  - stone -> سنگ
  - floor_covering -> کف‌پوش PVC
  - carpet -> موکت
  - mosaic -> موزائیک

### floors_count
- **Title**: تعداد کل طبقات ساختمان
- **Type**: object
 - **Minimum**: 1
 - **Maximum**: N/A

### has-photo
- **Title**: عکس‌دار
- **Type**: boolean

### has-video
- **Title**: ویدیو‌دار
- **Type**: boolean

### heating_system
- **Title**: گرمایش
- **Type**: object
 - **Items Type**: array
- **Queries**: 
  - heater -> بخاری
  - shoofaj -> شوفاژ
  - fan_coil -> فن کوئل
  - floor_heating -> از کف
  - duct_split -> داکت اسپلیت
  - split -> اسپلیت
  - fireplace -> شومینه

### parking
- **Title**: با پارکینگ
- **Type**: boolean

### rebuilt
- **Title**: بازسازی شده
- **Type**: boolean

### rent
- **Title**: اجاره
- **Type**: object
 - **Minimum**: 0
 - **Maximum**: N/A

### rent_to_single
- **Title**: مناسب مجرد
- **Type**: boolean

### rooms
- **Title**: تعداد اتاق
- **Type**: object
- **Queries**: 
  - بدون اتاق -> بدون اتاق
  - یک -> ۱
  - دو -> ۲
  - سه -> ۳
  - چهار -> ۴
  - بیشتر -> بیشتر از ۴

### size
- **Title**: متراژ
- **Type**: object
 - **Minimum**: 0
 - **Maximum**: 1000000000

### sort
- **Title**: ترتیب نمایش آگهی‌ها براساس
- **Type**: object
- **Queries**: 
  - quality_and_sort_date -> quality_and_sort_date
  - sort_date -> sort_date
  - cheapest -> cheapest
  - most_expensive -> most_expensive
  - production_year -> production_year
  - usage -> usage
  - most_popular -> most_popular
  - most_relevant -> most_relevant

### toilet
- **Title**: سرویس بهداشتی
- **Type**: object
- **Queries**: 
  - squat -> ایرانی
  - seat -> فرنگی
  - squat_seat -> ایرانی و فرنگی

### unit_per_floor
- **Title**: تعداد واحد در هر طبقه
- **Type**: object
 - **Minimum**: 1
 - **Maximum**: N/A

### urgent
- **Title**: فقط فوری‌ها
- **Type**: boolean

### warehouse
- **Title**: با انباری
- **Type**: boolean

### warm_water_provider
- **Title**: تأمین‌کننده آب گرم
- **Type**: object
 - **Items Type**: array
- **Queries**: 
  - water_heater -> آبگرم‌کن
  - powerhouse -> موتورخانه
  - package -> پکیج



---

### Category: apartment-sell



### building-age
- **Title**: سن بنا
- **Type**: object
- **Queries**: 
  - {"min": 0, "max": 1} -> حداکثر ۱ سال
  - {"min": 0, "max": 2} -> حداکثر ۲ سال
  - {"min": 0, "max": 5} -> حداکثر ۵ سال
  - {"min": 0, "max": 10} -> حداکثر ۱۰ سال
  - {"min": 0, "max": 15} -> حداکثر ۱۵ سال
  - {"min": 0, "max": 20} -> حداکثر ۲۰ سال
  - {"min": 0, "max": 30} -> حداکثر ۳۰ سال
  - {"min": 30} -> بیش از ۳۰ سال

### building_direction
- **Title**: جهت ساختمان
- **Type**: object
 - **Items Type**: array
- **Queries**: 
  - east -> شرقی
  - west -> غربی
  - north -> شمالی
  - south -> جنوبی

### business-type
- **Title**: آگهی‌دهنده
- **Type**: object
- **Queries**: 
  - personal -> شخصی
  - real-estate-business -> مشاور املاک

### category
- **Title**: دسته‌بندی
- **Type**: object

### cooling_system
- **Title**: سرمایش
- **Type**: object
 - **Items Type**: array
- **Queries**: 
  - water_cooler -> کولر آبی
  - air_conditioner -> کولر گازی
  - duct_split -> داکت اسپلیت
  - split -> اسپلیت
  - fan_coil -> فن کوئل

### deed_type
- **Title**: سند
- **Type**: object
 - **Items Type**: array
- **Queries**: 
  - single_page -> تک‌برگ
  - multi_page -> منگوله‌دار
  - written_agreement -> قول‌نامه‌ای
  - other -> سایر

### elevator
- **Title**: با آسانسور
- **Type**: boolean

### floor
- **Title**: طبقه
- **Type**: object
 - **Minimum**: -1
 - **Maximum**: N/A

### floor_type
- **Title**: جنس کف
- **Type**: object
 - **Items Type**: array
- **Queries**: 
  - ceramic -> سرامیک
  - wood_parquet -> پارکت چوب
  - laminate_parquet -> پارکت لمینت
  - stone -> سنگ
  - floor_covering -> کف‌پوش PVC
  - carpet -> موکت
  - mosaic -> موزائیک

### floors_count
- **Title**: تعداد کل طبقات ساختمان
- **Type**: object
 - **Minimum**: 1
 - **Maximum**: N/A

### has-photo
- **Title**: عکس‌دار
- **Type**: boolean

### has-video
- **Title**: ویدیو‌دار
- **Type**: boolean

### heating_system
- **Title**: گرمایش
- **Type**: object
 - **Items Type**: array
- **Queries**: 
  - heater -> بخاری
  - shoofaj -> شوفاژ
  - fan_coil -> فن کوئل
  - floor_heating -> از کف
  - duct_split -> داکت اسپلیت
  - split -> اسپلیت
  - fireplace -> شومینه

### parking
- **Title**: با پارکینگ
- **Type**: boolean

### price
- **Title**: قیمت کل
- **Type**: object
 - **Minimum**: 0
 - **Maximum**: N/A

### rebuilt
- **Title**: بازسازی شده
- **Type**: boolean

### rooms
- **Title**: تعداد اتاق
- **Type**: object
- **Queries**: 
  - بدون اتاق -> بدون اتاق
  - یک -> ۱
  - دو -> ۲
  - سه -> ۳
  - چهار -> ۴
  - بیشتر -> بیشتر از ۴

### size
- **Title**: متراژ
- **Type**: object
 - **Minimum**: 0
 - **Maximum**: 1000000000

### sort
- **Title**: ترتیب نمایش آگهی‌ها براساس
- **Type**: object
- **Queries**: 
  - quality_and_sort_date -> quality_and_sort_date
  - sort_date -> sort_date
  - cheapest -> cheapest
  - most_expensive -> most_expensive
  - production_year -> production_year
  - usage -> usage
  - most_popular -> most_popular
  - most_relevant -> most_relevant

### toilet
- **Title**: سرویس بهداشتی
- **Type**: object
- **Queries**: 
  - squat -> ایرانی
  - seat -> فرنگی
  - squat_seat -> ایرانی و فرنگی

### unit_per_floor
- **Title**: تعداد واحد در هر طبقه
- **Type**: object
 - **Minimum**: 1
 - **Maximum**: N/A

### urgent
- **Title**: فقط فوری‌ها
- **Type**: boolean

### warehouse
- **Title**: با انباری
- **Type**: boolean

### warm_water_provider
- **Title**: تأمین‌کننده آب گرم
- **Type**: object
 - **Items Type**: array
- **Queries**: 
  - water_heater -> آبگرم‌کن
  - powerhouse -> موتورخانه
  - package -> پکیج



---

### Category: appliance



### category
- **Title**: دسته‌بندی
- **Type**: object

### divider
- **Title**: سایر فیلتر‌ها
- **Type**: object

### exchange
- **Title**: نمایش معاوضه‌ها
- **Type**: object
- **Queries**: 
  - only-exchanges -> نمایش فقط معاوضه‌ها
  - exclude-exchanges -> حذف معاوضه‌ها

### goods-business-type
- **Title**: نوع آگهی‌دهنده
- **Type**: object
- **Queries**: 
  - all -> همه
  - personal -> شخصی
  - marketplace -> فروشگاه

### has-photo
- **Title**: فقط عکس‌دار
- **Type**: boolean

### price
- **Title**: قیمت
- **Type**: object
 - **Minimum**: 0
 - **Maximum**: N/A

### sort
- **Title**: ترتیب نمایش آگهی‌ها براساس
- **Type**: object
- **Queries**: 
  - quality_and_sort_date -> quality_and_sort_date
  - sort_date -> sort_date
  - cheapest -> cheapest
  - most_expensive -> most_expensive
  - production_year -> production_year
  - usage -> usage
  - most_popular -> most_popular
  - most_relevant -> most_relevant

### status
- **Title**: وضعیت کالا
- **Type**: object
 - **Items Type**: array
- **Queries**: 
  - new -> نو
  - like-new -> در حد نو
  - used -> کارکرده
  - repair-needed -> نیازمند تعمیر

### urgent
- **Title**: فقط فوری‌ها
- **Type**: boolean



---

### Category: artificial-flower



### category
- **Title**: دسته‌بندی
- **Type**: object

### divider
- **Title**: سایر فیلتر‌ها
- **Type**: object

### exchange
- **Title**: نمایش معاوضه‌ها
- **Type**: object
- **Queries**: 
  - only-exchanges -> نمایش فقط معاوضه‌ها
  - exclude-exchanges -> حذف معاوضه‌ها

### goods-business-type
- **Title**: نوع آگهی‌دهنده
- **Type**: object
- **Queries**: 
  - all -> همه
  - personal -> شخصی
  - marketplace -> فروشگاه

### has-photo
- **Title**: فقط عکس‌دار
- **Type**: boolean

### price
- **Title**: قیمت
- **Type**: object
 - **Minimum**: 0
 - **Maximum**: N/A

### sort
- **Title**: ترتیب نمایش آگهی‌ها براساس
- **Type**: object
- **Queries**: 
  - quality_and_sort_date -> quality_and_sort_date
  - sort_date -> sort_date
  - cheapest -> cheapest
  - most_expensive -> most_expensive
  - production_year -> production_year
  - usage -> usage
  - most_popular -> most_popular
  - most_relevant -> most_relevant

### status
- **Title**: وضعیت کالا
- **Type**: object
 - **Items Type**: array
- **Queries**: 
  - new -> نو
  - like-new -> در حد نو
  - used -> کارکرده
  - repair-needed -> نیازمند تعمیر

### urgent
- **Title**: فقط فوری‌ها
- **Type**: boolean



---

### Category: audio-video



### category
- **Title**: دسته‌بندی
- **Type**: object

### divider
- **Title**: سایر فیلتر‌ها
- **Type**: object

### exchange
- **Title**: نمایش معاوضه‌ها
- **Type**: object
- **Queries**: 
  - only-exchanges -> نمایش فقط معاوضه‌ها
  - exclude-exchanges -> حذف معاوضه‌ها

### goods-business-type
- **Title**: نوع آگهی‌دهنده
- **Type**: object
- **Queries**: 
  - all -> همه
  - personal -> شخصی
  - marketplace -> فروشگاه

### has-photo
- **Title**: فقط عکس‌دار
- **Type**: boolean

### price
- **Title**: قیمت
- **Type**: object
 - **Minimum**: 0
 - **Maximum**: N/A

### sort
- **Title**: ترتیب نمایش آگهی‌ها براساس
- **Type**: object
- **Queries**: 
  - quality_and_sort_date -> quality_and_sort_date
  - sort_date -> sort_date
  - cheapest -> cheapest
  - most_expensive -> most_expensive
  - production_year -> production_year
  - usage -> usage
  - most_popular -> most_popular
  - most_relevant -> most_relevant

### status
- **Title**: وضعیت کالا
- **Type**: object
 - **Items Type**: array
- **Queries**: 
  - new -> نو
  - like-new -> در حد نو
  - used -> کارکرده
  - repair-needed -> نیازمند تعمیر

### urgent
- **Title**: فقط فوری‌ها
- **Type**: boolean



---

### Category: baby-and-toys



### category
- **Title**: دسته‌بندی
- **Type**: object

### divider
- **Title**: سایر فیلتر‌ها
- **Type**: object

### exchange
- **Title**: نمایش معاوضه‌ها
- **Type**: object
- **Queries**: 
  - only-exchanges -> نمایش فقط معاوضه‌ها
  - exclude-exchanges -> حذف معاوضه‌ها

### goods-business-type
- **Title**: نوع آگهی‌دهنده
- **Type**: object
- **Queries**: 
  - all -> همه
  - personal -> شخصی
  - marketplace -> فروشگاه

### has-photo
- **Title**: فقط عکس‌دار
- **Type**: boolean

### price
- **Title**: قیمت
- **Type**: object
 - **Minimum**: 0
 - **Maximum**: N/A

### sort
- **Title**: ترتیب نمایش آگهی‌ها براساس
- **Type**: object
- **Queries**: 
  - quality_and_sort_date -> quality_and_sort_date
  - sort_date -> sort_date
  - cheapest -> cheapest
  - most_expensive -> most_expensive
  - production_year -> production_year
  - usage -> usage
  - most_popular -> most_popular
  - most_relevant -> most_relevant

### status
- **Title**: وضعیت کالا
- **Type**: object
 - **Items Type**: array
- **Queries**: 
  - new -> نو
  - like-new -> در حد نو
  - used -> کارکرده
  - repair-needed -> نیازمند تعمیر

### urgent
- **Title**: فقط فوری‌ها
- **Type**: boolean



---

### Category: ball-sports



### category
- **Title**: دسته‌بندی
- **Type**: object

### divider
- **Title**: سایر فیلتر‌ها
- **Type**: object

### exchange
- **Title**: نمایش معاوضه‌ها
- **Type**: object
- **Queries**: 
  - only-exchanges -> نمایش فقط معاوضه‌ها
  - exclude-exchanges -> حذف معاوضه‌ها

### goods-business-type
- **Title**: نوع آگهی‌دهنده
- **Type**: object
- **Queries**: 
  - all -> همه
  - personal -> شخصی
  - marketplace -> فروشگاه

### has-photo
- **Title**: فقط عکس‌دار
- **Type**: boolean

### price
- **Title**: قیمت
- **Type**: object
 - **Minimum**: 0
 - **Maximum**: N/A

### sort
- **Title**: ترتیب نمایش آگهی‌ها براساس
- **Type**: object
- **Queries**: 
  - quality_and_sort_date -> quality_and_sort_date
  - sort_date -> sort_date
  - cheapest -> cheapest
  - most_expensive -> most_expensive
  - production_year -> production_year
  - usage -> usage
  - most_popular -> most_popular
  - most_relevant -> most_relevant

### status
- **Title**: وضعیت کالا
- **Type**: object
 - **Items Type**: array
- **Queries**: 
  - new -> نو
  - like-new -> در حد نو
  - used -> کارکرده
  - repair-needed -> نیازمند تعمیر

### urgent
- **Title**: فقط فوری‌ها
- **Type**: boolean



---

### Category: barbershop-and-beautysalon



### category
- **Title**: دسته‌بندی
- **Type**: object

### divider
- **Title**: سایر فیلتر‌ها
- **Type**: object

### exchange
- **Title**: نمایش معاوضه‌ها
- **Type**: object
- **Queries**: 
  - only-exchanges -> نمایش فقط معاوضه‌ها
  - exclude-exchanges -> حذف معاوضه‌ها

### goods-business-type
- **Title**: نوع آگهی‌دهنده
- **Type**: object
- **Queries**: 
  - all -> همه
  - personal -> شخصی
  - marketplace -> فروشگاه

### has-photo
- **Title**: فقط عکس‌دار
- **Type**: boolean

### price
- **Title**: قیمت
- **Type**: object
 - **Minimum**: 0
 - **Maximum**: N/A

### sort
- **Title**: ترتیب نمایش آگهی‌ها براساس
- **Type**: object
- **Queries**: 
  - quality_and_sort_date -> quality_and_sort_date
  - sort_date -> sort_date
  - cheapest -> cheapest
  - most_expensive -> most_expensive
  - production_year -> production_year
  - usage -> usage
  - most_popular -> most_popular
  - most_relevant -> most_relevant

### status
- **Title**: وضعیت کالا
- **Type**: object
 - **Items Type**: array
- **Queries**: 
  - new -> نو
  - like-new -> در حد نو
  - used -> کارکرده
  - repair-needed -> نیازمند تعمیر

### urgent
- **Title**: فقط فوری‌ها
- **Type**: boolean



---

### Category: bathroom-accessories



### category
- **Title**: دسته‌بندی
- **Type**: object

### divider
- **Title**: سایر فیلتر‌ها
- **Type**: object

### exchange
- **Title**: نمایش معاوضه‌ها
- **Type**: object
- **Queries**: 
  - only-exchanges -> نمایش فقط معاوضه‌ها
  - exclude-exchanges -> حذف معاوضه‌ها

### goods-business-type
- **Title**: نوع آگهی‌دهنده
- **Type**: object
- **Queries**: 
  - all -> همه
  - personal -> شخصی
  - marketplace -> فروشگاه

### has-photo
- **Title**: فقط عکس‌دار
- **Type**: boolean

### price
- **Title**: قیمت
- **Type**: object
 - **Minimum**: 0
 - **Maximum**: N/A

### sort
- **Title**: ترتیب نمایش آگهی‌ها براساس
- **Type**: object
- **Queries**: 
  - quality_and_sort_date -> quality_and_sort_date
  - sort_date -> sort_date
  - cheapest -> cheapest
  - most_expensive -> most_expensive
  - production_year -> production_year
  - usage -> usage
  - most_popular -> most_popular
  - most_relevant -> most_relevant

### status
- **Title**: وضعیت کالا
- **Type**: object
 - **Items Type**: array
- **Queries**: 
  - new -> نو
  - like-new -> در حد نو
  - used -> کارکرده
  - repair-needed -> نیازمند تعمیر

### urgent
- **Title**: فقط فوری‌ها
- **Type**: boolean



---

### Category: bathrooms



### category
- **Title**: دسته‌بندی
- **Type**: object

### divider
- **Title**: سایر فیلتر‌ها
- **Type**: object

### exchange
- **Title**: نمایش معاوضه‌ها
- **Type**: object
- **Queries**: 
  - only-exchanges -> نمایش فقط معاوضه‌ها
  - exclude-exchanges -> حذف معاوضه‌ها

### goods-business-type
- **Title**: نوع آگهی‌دهنده
- **Type**: object
- **Queries**: 
  - all -> همه
  - personal -> شخصی
  - marketplace -> فروشگاه

### has-photo
- **Title**: فقط عکس‌دار
- **Type**: boolean

### price
- **Title**: قیمت
- **Type**: object
 - **Minimum**: 0
 - **Maximum**: N/A

### sort
- **Title**: ترتیب نمایش آگهی‌ها براساس
- **Type**: object
- **Queries**: 
  - quality_and_sort_date -> quality_and_sort_date
  - sort_date -> sort_date
  - cheapest -> cheapest
  - most_expensive -> most_expensive
  - production_year -> production_year
  - usage -> usage
  - most_popular -> most_popular
  - most_relevant -> most_relevant

### status
- **Title**: وضعیت کالا
- **Type**: object
 - **Items Type**: array
- **Queries**: 
  - new -> نو
  - like-new -> در حد نو
  - used -> کارکرده
  - repair-needed -> نیازمند تعمیر

### urgent
- **Title**: فقط فوری‌ها
- **Type**: boolean



---

### Category: beauty-and-haircare



### category
- **Title**: دسته‌بندی
- **Type**: object

### expertises
- **Title**: تخصص
- **Type**: object
 - **Items Type**: array
- **Queries**: 
  - ROOT -> همه تخصص‌ها
  - body-beauty -> زیبایی بدن
  - skin-rejuvenation-and-facial -> پاکسازی و جوانسازی پوست و صورت
  - waxing-and-laser -> اپیلاسیون و لیزر
  - brow-and-hair-transplantation -> کاشت مو و ابرو
  - mesotherapy-botox-fat-filler -> مزو، بوتاکس، چربی، فیلر
  - cosmetic-surgery -> جراحی و زیبایی صورت و بدن
  - teeth-health-and-beauty -> سلامت و زیبایی دندان
  - face-and-brows-beauty -> زیبایی ابرو و صورت
  - brown-and-face-tweeze -> اصلاح صورت و ابرو
  - makeup -> آرایش و میکاپ
  - face-and-body-tattoo -> تاتوی آرایشی صورت و بدن
  - lash-transplant-and-implantation -> کاشت و اکستنشن مژه
  - lash-and-brow-extensions-and-lift -> لیفت و لمینیت ابرو و مژه
  - brow-micropigmentare-microblading -> میکروپیگمنتیشن و میکروبلیدینگ ابرو
  - nails-health-and-beauty -> مراقبت و زیبایی ناخن
  - nail-repair-and-implantation -> ترمیم و کاشت
  - pedicure-and-manicure -> پدیکور و مانیکور
  - hair-beauty -> زیبایی مو
  - all-over-or-multi-tone-hair-color -> رنگ مو
  - hair-extension -> اکستنشن مو
  - hair-braiding -> بافت مو
  - hair-cut -> کوتاهی مو
  - chignon-hairstyle -> شنیون مو
  - hair-keratin-treatment -> کراتینهٔ مو
  - hair-micropigmentare-microblading -> میکروپیگمنتیشن و میکروبلیدینگ موی سر
  - health-and-care -> سلامت و درمان
  - baby-sitter -> پرستار کودک
  - counseling-and-psychology-therapy -> مشاوره و روان‌درمانی
  - injection-and-bondage-and-stitch -> تزریقات و پانسمان و بخیه
  - elderly-sitter -> پرستار سالمند
  - patient-sitter -> پرستار بیمار
  - beauty-and-makeup-other -> سایر آرایشی و زیبایی

### sort
- **Title**: ترتیب نمایش آگهی‌ها براساس
- **Type**: object
- **Queries**: 
  - quality_and_sort_date -> quality_and_sort_date
  - sort_date -> sort_date
  - cheapest -> cheapest
  - most_expensive -> most_expensive
  - production_year -> production_year
  - usage -> usage
  - most_popular -> most_popular
  - most_relevant -> most_relevant

### urgent
- **Title**: فقط فوری‌ها
- **Type**: boolean



---

### Category: bed-pillow-blanket



### category
- **Title**: دسته‌بندی
- **Type**: object

### divider
- **Title**: سایر فیلتر‌ها
- **Type**: object

### exchange
- **Title**: نمایش معاوضه‌ها
- **Type**: object
- **Queries**: 
  - only-exchanges -> نمایش فقط معاوضه‌ها
  - exclude-exchanges -> حذف معاوضه‌ها

### goods-business-type
- **Title**: نوع آگهی‌دهنده
- **Type**: object
- **Queries**: 
  - all -> همه
  - personal -> شخصی
  - marketplace -> فروشگاه

### has-photo
- **Title**: فقط عکس‌دار
- **Type**: boolean

### price
- **Title**: قیمت
- **Type**: object
 - **Minimum**: 0
 - **Maximum**: N/A

### sort
- **Title**: ترتیب نمایش آگهی‌ها براساس
- **Type**: object
- **Queries**: 
  - quality_and_sort_date -> quality_and_sort_date
  - sort_date -> sort_date
  - cheapest -> cheapest
  - most_expensive -> most_expensive
  - production_year -> production_year
  - usage -> usage
  - most_popular -> most_popular
  - most_relevant -> most_relevant

### status
- **Title**: وضعیت کالا
- **Type**: object
 - **Items Type**: array
- **Queries**: 
  - new -> نو
  - like-new -> در حد نو
  - used -> کارکرده
  - repair-needed -> نیازمند تعمیر

### urgent
- **Title**: فقط فوری‌ها
- **Type**: boolean



---

### Category: bed-service



### category
- **Title**: دسته‌بندی
- **Type**: object

### divider
- **Title**: سایر فیلتر‌ها
- **Type**: object

### exchange
- **Title**: نمایش معاوضه‌ها
- **Type**: object
- **Queries**: 
  - only-exchanges -> نمایش فقط معاوضه‌ها
  - exclude-exchanges -> حذف معاوضه‌ها

### goods-business-type
- **Title**: نوع آگهی‌دهنده
- **Type**: object
- **Queries**: 
  - all -> همه
  - personal -> شخصی
  - marketplace -> فروشگاه

### has-photo
- **Title**: فقط عکس‌دار
- **Type**: boolean

### price
- **Title**: قیمت
- **Type**: object
 - **Minimum**: 0
 - **Maximum**: N/A

### sort
- **Title**: ترتیب نمایش آگهی‌ها براساس
- **Type**: object
- **Queries**: 
  - quality_and_sort_date -> quality_and_sort_date
  - sort_date -> sort_date
  - cheapest -> cheapest
  - most_expensive -> most_expensive
  - production_year -> production_year
  - usage -> usage
  - most_popular -> most_popular
  - most_relevant -> most_relevant

### status
- **Title**: وضعیت کالا
- **Type**: object
 - **Items Type**: array
- **Queries**: 
  - new -> نو
  - like-new -> در حد نو
  - used -> کارکرده
  - repair-needed -> نیازمند تعمیر

### urgent
- **Title**: فقط فوری‌ها
- **Type**: boolean



---

### Category: bed-sheet



### category
- **Title**: دسته‌بندی
- **Type**: object

### divider
- **Title**: سایر فیلتر‌ها
- **Type**: object

### exchange
- **Title**: نمایش معاوضه‌ها
- **Type**: object
- **Queries**: 
  - only-exchanges -> نمایش فقط معاوضه‌ها
  - exclude-exchanges -> حذف معاوضه‌ها

### goods-business-type
- **Title**: نوع آگهی‌دهنده
- **Type**: object
- **Queries**: 
  - all -> همه
  - personal -> شخصی
  - marketplace -> فروشگاه

### has-photo
- **Title**: فقط عکس‌دار
- **Type**: boolean

### price
- **Title**: قیمت
- **Type**: object
 - **Minimum**: 0
 - **Maximum**: N/A

### sort
- **Title**: ترتیب نمایش آگهی‌ها براساس
- **Type**: object
- **Queries**: 
  - quality_and_sort_date -> quality_and_sort_date
  - sort_date -> sort_date
  - cheapest -> cheapest
  - most_expensive -> most_expensive
  - production_year -> production_year
  - usage -> usage
  - most_popular -> most_popular
  - most_relevant -> most_relevant

### status
- **Title**: وضعیت کالا
- **Type**: object
 - **Items Type**: array
- **Queries**: 
  - new -> نو
  - like-new -> در حد نو
  - used -> کارکرده
  - repair-needed -> نیازمند تعمیر

### urgent
- **Title**: فقط فوری‌ها
- **Type**: boolean



---

### Category: bicycle



### category
- **Title**: دسته‌بندی
- **Type**: object

### divider
- **Title**: سایر فیلتر‌ها
- **Type**: object

### exchange
- **Title**: نمایش معاوضه‌ها
- **Type**: object
- **Queries**: 
  - only-exchanges -> نمایش فقط معاوضه‌ها
  - exclude-exchanges -> حذف معاوضه‌ها

### goods-business-type
- **Title**: نوع آگهی‌دهنده
- **Type**: object
- **Queries**: 
  - all -> همه
  - personal -> شخصی
  - marketplace -> فروشگاه

### has-photo
- **Title**: فقط عکس‌دار
- **Type**: boolean

### price
- **Title**: قیمت
- **Type**: object
 - **Minimum**: 0
 - **Maximum**: N/A

### sort
- **Title**: ترتیب نمایش آگهی‌ها براساس
- **Type**: object
- **Queries**: 
  - quality_and_sort_date -> quality_and_sort_date
  - sort_date -> sort_date
  - cheapest -> cheapest
  - most_expensive -> most_expensive
  - production_year -> production_year
  - usage -> usage
  - most_popular -> most_popular
  - most_relevant -> most_relevant

### status
- **Title**: وضعیت کالا
- **Type**: object
 - **Items Type**: array
- **Queries**: 
  - new -> نو
  - like-new -> در حد نو
  - used -> کارکرده
  - repair-needed -> نیازمند تعمیر

### urgent
- **Title**: فقط فوری‌ها
- **Type**: boolean



---

### Category: birds



### category
- **Title**: دسته‌بندی
- **Type**: object

### divider
- **Title**: سایر فیلتر‌ها
- **Type**: object

### exchange
- **Title**: نمایش معاوضه‌ها
- **Type**: object
- **Queries**: 
  - only-exchanges -> نمایش فقط معاوضه‌ها
  - exclude-exchanges -> حذف معاوضه‌ها

### has-photo
- **Title**: فقط عکس‌دار
- **Type**: boolean

### price
- **Title**: قیمت
- **Type**: object
 - **Minimum**: 0
 - **Maximum**: N/A

### sort
- **Title**: ترتیب نمایش آگهی‌ها براساس
- **Type**: object
- **Queries**: 
  - quality_and_sort_date -> quality_and_sort_date
  - sort_date -> sort_date
  - cheapest -> cheapest
  - most_expensive -> most_expensive
  - production_year -> production_year
  - usage -> usage
  - most_popular -> most_popular
  - most_relevant -> most_relevant

### urgent
- **Title**: فقط فوری‌ها
- **Type**: boolean



---

### Category: boat



### category
- **Title**: دسته‌بندی
- **Type**: object

### divider
- **Title**: سایر فیلتر‌ها
- **Type**: object

### exchange
- **Title**: نمایش معاوضه‌ها
- **Type**: object
- **Queries**: 
  - only-exchanges -> نمایش فقط معاوضه‌ها
  - exclude-exchanges -> حذف معاوضه‌ها

### has-photo
- **Title**: فقط عکس‌دار
- **Type**: boolean

### non-negotiable
- **Title**: حذف توافقی‌ها
- **Type**: boolean

### post-type
- **Title**: نوع آگهی
- **Type**: object
- **Queries**: 
  - فروشی -> فروشی
  - درخواستی -> درخواستی

### price
- **Title**: قیمت
- **Type**: object
 - **Minimum**: 0
 - **Maximum**: N/A

### sort
- **Title**: ترتیب نمایش آگهی‌ها براساس
- **Type**: object
- **Queries**: 
  - quality_and_sort_date -> quality_and_sort_date
  - sort_date -> sort_date
  - cheapest -> cheapest
  - most_expensive -> most_expensive
  - production_year -> production_year
  - usage -> usage
  - most_popular -> most_popular
  - most_relevant -> most_relevant

### urgent
- **Title**: فقط فوری‌ها
- **Type**: boolean



---

### Category: book-student-literature



### category
- **Title**: دسته‌بندی
- **Type**: object

### divider
- **Title**: سایر فیلتر‌ها
- **Type**: object

### exchange
- **Title**: نمایش معاوضه‌ها
- **Type**: object
- **Queries**: 
  - only-exchanges -> نمایش فقط معاوضه‌ها
  - exclude-exchanges -> حذف معاوضه‌ها

### goods-business-type
- **Title**: نوع آگهی‌دهنده
- **Type**: object
- **Queries**: 
  - all -> همه
  - personal -> شخصی
  - marketplace -> فروشگاه

### has-photo
- **Title**: فقط عکس‌دار
- **Type**: boolean

### price
- **Title**: قیمت
- **Type**: object
 - **Minimum**: 0
 - **Maximum**: N/A

### sort
- **Title**: ترتیب نمایش آگهی‌ها براساس
- **Type**: object
- **Queries**: 
  - quality_and_sort_date -> quality_and_sort_date
  - sort_date -> sort_date
  - cheapest -> cheapest
  - most_expensive -> most_expensive
  - production_year -> production_year
  - usage -> usage
  - most_popular -> most_popular
  - most_relevant -> most_relevant

### status
- **Title**: وضعیت کالا
- **Type**: object
 - **Items Type**: array
- **Queries**: 
  - new -> نو
  - like-new -> در حد نو
  - used -> کارکرده
  - repair-needed -> نیازمند تعمیر

### urgent
- **Title**: فقط فوری‌ها
- **Type**: boolean



---

### Category: bookcase-shelf



### category
- **Title**: دسته‌بندی
- **Type**: object

### divider
- **Title**: سایر فیلتر‌ها
- **Type**: object

### exchange
- **Title**: نمایش معاوضه‌ها
- **Type**: object
- **Queries**: 
  - only-exchanges -> نمایش فقط معاوضه‌ها
  - exclude-exchanges -> حذف معاوضه‌ها

### goods-business-type
- **Title**: نوع آگهی‌دهنده
- **Type**: object
- **Queries**: 
  - all -> همه
  - personal -> شخصی
  - marketplace -> فروشگاه

### has-photo
- **Title**: فقط عکس‌دار
- **Type**: boolean

### price
- **Title**: قیمت
- **Type**: object
 - **Minimum**: 0
 - **Maximum**: N/A

### sort
- **Title**: ترتیب نمایش آگهی‌ها براساس
- **Type**: object
- **Queries**: 
  - quality_and_sort_date -> quality_and_sort_date
  - sort_date -> sort_date
  - cheapest -> cheapest
  - most_expensive -> most_expensive
  - production_year -> production_year
  - usage -> usage
  - most_popular -> most_popular
  - most_relevant -> most_relevant

### status
- **Title**: وضعیت کالا
- **Type**: object
 - **Items Type**: array
- **Queries**: 
  - new -> نو
  - like-new -> در حد نو
  - used -> کارکرده
  - repair-needed -> نیازمند تعمیر

### urgent
- **Title**: فقط فوری‌ها
- **Type**: boolean



---

### Category: buffet-showcases



### category
- **Title**: دسته‌بندی
- **Type**: object

### divider
- **Title**: سایر فیلتر‌ها
- **Type**: object

### exchange
- **Title**: نمایش معاوضه‌ها
- **Type**: object
- **Queries**: 
  - only-exchanges -> نمایش فقط معاوضه‌ها
  - exclude-exchanges -> حذف معاوضه‌ها

### goods-business-type
- **Title**: نوع آگهی‌دهنده
- **Type**: object
- **Queries**: 
  - all -> همه
  - personal -> شخصی
  - marketplace -> فروشگاه

### has-photo
- **Title**: فقط عکس‌دار
- **Type**: boolean

### price
- **Title**: قیمت
- **Type**: object
 - **Minimum**: 0
 - **Maximum**: N/A

### sort
- **Title**: ترتیب نمایش آگهی‌ها براساس
- **Type**: object
- **Queries**: 
  - quality_and_sort_date -> quality_and_sort_date
  - sort_date -> sort_date
  - cheapest -> cheapest
  - most_expensive -> most_expensive
  - production_year -> production_year
  - usage -> usage
  - most_popular -> most_popular
  - most_relevant -> most_relevant

### status
- **Title**: وضعیت کالا
- **Type**: object
 - **Items Type**: array
- **Queries**: 
  - new -> نو
  - like-new -> در حد نو
  - used -> کارکرده
  - repair-needed -> نیازمند تعمیر

### urgent
- **Title**: فقط فوری‌ها
- **Type**: boolean



---

### Category: building-equipment



### category
- **Title**: دسته‌بندی
- **Type**: object

### divider
- **Title**: سایر فیلتر‌ها
- **Type**: object

### exchange
- **Title**: نمایش معاوضه‌ها
- **Type**: object
- **Queries**: 
  - only-exchanges -> نمایش فقط معاوضه‌ها
  - exclude-exchanges -> حذف معاوضه‌ها

### goods-business-type
- **Title**: نوع آگهی‌دهنده
- **Type**: object
- **Queries**: 
  - all -> همه
  - personal -> شخصی
  - marketplace -> فروشگاه

### has-photo
- **Title**: فقط عکس‌دار
- **Type**: boolean

### price
- **Title**: قیمت
- **Type**: object
 - **Minimum**: 0
 - **Maximum**: N/A

### sort
- **Title**: ترتیب نمایش آگهی‌ها براساس
- **Type**: object
- **Queries**: 
  - quality_and_sort_date -> quality_and_sort_date
  - sort_date -> sort_date
  - cheapest -> cheapest
  - most_expensive -> most_expensive
  - production_year -> production_year
  - usage -> usage
  - most_popular -> most_popular
  - most_relevant -> most_relevant

### status
- **Title**: وضعیت کالا
- **Type**: object
 - **Items Type**: array
- **Queries**: 
  - new -> نو
  - like-new -> در حد نو
  - used -> کارکرده
  - repair-needed -> نیازمند تعمیر

### urgent
- **Title**: فقط فوری‌ها
- **Type**: boolean



---

### Category: bus-metro-train



### category
- **Title**: دسته‌بندی
- **Type**: object

### divider
- **Title**: سایر فیلتر‌ها
- **Type**: object

### exchange
- **Title**: نمایش معاوضه‌ها
- **Type**: object
- **Queries**: 
  - only-exchanges -> نمایش فقط معاوضه‌ها
  - exclude-exchanges -> حذف معاوضه‌ها

### has-photo
- **Title**: فقط عکس‌دار
- **Type**: boolean

### price
- **Title**: قیمت
- **Type**: object
 - **Minimum**: 0
 - **Maximum**: N/A

### sort
- **Title**: ترتیب نمایش آگهی‌ها براساس
- **Type**: object
- **Queries**: 
  - quality_and_sort_date -> quality_and_sort_date
  - sort_date -> sort_date
  - cheapest -> cheapest
  - most_expensive -> most_expensive
  - production_year -> production_year
  - usage -> usage
  - most_popular -> most_popular
  - most_relevant -> most_relevant

### urgent
- **Title**: فقط فوری‌ها
- **Type**: boolean



---

### Category: cafe-and-restaurant



### category
- **Title**: دسته‌بندی
- **Type**: object

### divider
- **Title**: سایر فیلتر‌ها
- **Type**: object

### exchange
- **Title**: نمایش معاوضه‌ها
- **Type**: object
- **Queries**: 
  - only-exchanges -> نمایش فقط معاوضه‌ها
  - exclude-exchanges -> حذف معاوضه‌ها

### goods-business-type
- **Title**: نوع آگهی‌دهنده
- **Type**: object
- **Queries**: 
  - all -> همه
  - personal -> شخصی
  - marketplace -> فروشگاه

### has-photo
- **Title**: فقط عکس‌دار
- **Type**: boolean

### price
- **Title**: قیمت
- **Type**: object
 - **Minimum**: 0
 - **Maximum**: N/A

### sort
- **Title**: ترتیب نمایش آگهی‌ها براساس
- **Type**: object
- **Queries**: 
  - quality_and_sort_date -> quality_and_sort_date
  - sort_date -> sort_date
  - cheapest -> cheapest
  - most_expensive -> most_expensive
  - production_year -> production_year
  - usage -> usage
  - most_popular -> most_popular
  - most_relevant -> most_relevant

### status
- **Title**: وضعیت کالا
- **Type**: object
 - **Items Type**: array
- **Queries**: 
  - new -> نو
  - like-new -> در حد نو
  - used -> کارکرده
  - repair-needed -> نیازمند تعمیر

### urgent
- **Title**: فقط فوری‌ها
- **Type**: boolean



---

### Category: camera-camcoders



### accessories
- **Title**: نوع تجهیزات
- **Type**: object
 - **Items Type**: array
- **Queries**: 
  - stand-and-holder -> انواع پایه و هولدر
  - lens -> لنز
  - lighting-kit -> تجهیزات روشنایی
  - chromakey-curtain -> پرده کروماکی و فون
  - others -> سایر

### category
- **Title**: دسته‌بندی
- **Type**: object

### divider
- **Title**: سایر فیلتر‌ها
- **Type**: object

### exchange
- **Title**: نمایش معاوضه‌ها
- **Type**: object
- **Queries**: 
  - only-exchanges -> نمایش فقط معاوضه‌ها
  - exclude-exchanges -> حذف معاوضه‌ها

### goods-business-type
- **Title**: نوع آگهی‌دهنده
- **Type**: object
- **Queries**: 
  - all -> همه
  - personal -> شخصی
  - marketplace -> فروشگاه

### has-photo
- **Title**: فقط عکس‌دار
- **Type**: boolean

### price
- **Title**: قیمت
- **Type**: object
 - **Minimum**: 0
 - **Maximum**: N/A

### sort
- **Title**: ترتیب نمایش آگهی‌ها براساس
- **Type**: object
- **Queries**: 
  - quality_and_sort_date -> quality_and_sort_date
  - sort_date -> sort_date
  - cheapest -> cheapest
  - most_expensive -> most_expensive
  - production_year -> production_year
  - usage -> usage
  - most_popular -> most_popular
  - most_relevant -> most_relevant

### status
- **Title**: وضعیت کالا
- **Type**: object
 - **Items Type**: array
- **Queries**: 
  - new -> نو
  - like-new -> در حد نو
  - used -> کارکرده
  - repair-needed -> نیازمند تعمیر

### urgent
- **Title**: فقط فوری‌ها
- **Type**: boolean



---

### Category: camping-outdoor



### category
- **Title**: دسته‌بندی
- **Type**: object

### divider
- **Title**: سایر فیلتر‌ها
- **Type**: object

### exchange
- **Title**: نمایش معاوضه‌ها
- **Type**: object
- **Queries**: 
  - only-exchanges -> نمایش فقط معاوضه‌ها
  - exclude-exchanges -> حذف معاوضه‌ها

### goods-business-type
- **Title**: نوع آگهی‌دهنده
- **Type**: object
- **Queries**: 
  - all -> همه
  - personal -> شخصی
  - marketplace -> فروشگاه

### has-photo
- **Title**: فقط عکس‌دار
- **Type**: boolean

### price
- **Title**: قیمت
- **Type**: object
 - **Minimum**: 0
 - **Maximum**: N/A

### sort
- **Title**: ترتیب نمایش آگهی‌ها براساس
- **Type**: object
- **Queries**: 
  - quality_and_sort_date -> quality_and_sort_date
  - sort_date -> sort_date
  - cheapest -> cheapest
  - most_expensive -> most_expensive
  - production_year -> production_year
  - usage -> usage
  - most_popular -> most_popular
  - most_relevant -> most_relevant

### status
- **Title**: وضعیت کالا
- **Type**: object
 - **Items Type**: array
- **Queries**: 
  - new -> نو
  - like-new -> در حد نو
  - used -> کارکرده
  - repair-needed -> نیازمند تعمیر

### urgent
- **Title**: فقط فوری‌ها
- **Type**: boolean



---

### Category: car-and-motor



### category
- **Title**: دسته‌بندی
- **Type**: object

### expertises
- **Title**: تخصص
- **Type**: object
 - **Items Type**: array
- **Queries**: 
  - ROOT -> همه تخصص‌ها
  - car-wash -> نظافت خودرو
  - interior-cleaning -> توشویی
  - exterior-cleaning -> روشویی
  - full-carwash -> صفرشویی
  - car-tuning -> تیونینگ
  - car-upholstery-repair -> تعمیر صندلی و فرمان
  - car-seat-cover -> نصب روکش و کفپوش
  - car-alarm-installation -> نصب دزدگیر
  - car-window-tinting -> شیشه دودی
  - car-audio-system -> سیستم صوتی و تصویری خودرو
  - car-detailing -> زیباسازی بدنهٔ خودرو
  - car-ceramic-coating -> سرامیک خودرو
  - car-wax-polish -> واکس و پولیش
  - car-light-polish -> رفع ماتی چراغ
  - car-body-cover -> کاور و گلس خودرو
  - car-paint-sunburn-repair -> رفع آفتاب سوختگی خودرو
  - car-emergency -> اورژانس خودرو
  - car-transportation -> حمل خودرو
  - roadside-assistance -> امداد خودرو
  - key-remote-repair -> کلیدسازی و ساخت ریموت
  - glass-lights-repair -> تعویض و تعمیر آینه و شیشه
  - front-suspension -> جلوبندی خودرو
  - hydraulic-repair -> تعمیر هیدرولیک خودرو
  - front-suspension-repair -> تعمیر و تعویض جلوبندی
  - axle-repair -> تعمیر و تعویض اکسل
  - autobody-repair-car-paint -> صافکاری و نقاشی خودرو
  - autobody-repair -> صافکاری خودرو
  - car-paint -> نقاشی و رنگسازی خودرو
  - bumper-repair -> سپرسازی
  - scratch-removing -> لیسه گیری
  - car-electricity -> برق خودرو
  - car-diagnostics -> دیاگ و عیب یابی
  - battery-replacement -> تعویض باتری
  - alternator-repair -> تعمیر دینام
  - sensor-replacement -> تعویض سنسورها
  - air-conditioning -> تعمیر کولر و شارژ گاز کولر خودرو
  - spark-plug-replacement -> تعویض شمع و وایر و انژکتور خودرو
  - fuel-pump-repair -> تعویض و تعمیر پمپ بنزین
  - light-repair -> تعمیر و تعویض لامپ
  - airbag-repair -> تعمیر ایسیو و ایربگ
  - odometer-repair -> کیلومترسازی
  - wiring-repair -> تعمیر و تعویض سیم کشی خودرو
  - car-inspection -> کارشناسی خودرو
  - technical-inspection -> کارشناسی فنی خودرو
  - bodywork-inspection -> کارشناسی بدنه خودرو
  - vehicles-others -> سایر موتور و ماشین
  - periodic car service -> سرویس های دوره ای و مکانیکی
  - oil-replacement -> تعویض روغن و فیلتر
  - brake-repair -> تعویض و تعمیر ترمز و ای بی اس
  - fan-belt-replacement -> تعویض تسمه
  - car-puncture-repair -> پنچرگیری و لاستیک
  - gearbox-repair -> تعمیر گیربکس
  - radiator-repair -> تعمیر و تعویض فن و رادیاتور
  - disc-repair -> تعویض و تعمیر دیسک و صفحه
  - engine-repair -> تعمیر موتور خودرو

### has-photo
- **Title**: فقط عکس‌دار
- **Type**: boolean

### sort
- **Title**: ترتیب نمایش آگهی‌ها براساس
- **Type**: object
- **Queries**: 
  - quality_and_sort_date -> quality_and_sort_date
  - sort_date -> sort_date
  - cheapest -> cheapest
  - most_expensive -> most_expensive
  - production_year -> production_year
  - usage -> usage
  - most_popular -> most_popular
  - most_relevant -> most_relevant

### urgent
- **Title**: فقط فوری‌ها
- **Type**: boolean



---

### Category: care-health-beauty



### category
- **Title**: دسته‌بندی
- **Type**: object

### divider
- **Title**: سایر فیلتر‌ها
- **Type**: object

### employee_gender
- **Title**: جنسیت کارجو
- **Type**: object
- **Queries**: 
  - female -> زن
  - male -> مرد
  - neutral -> فرقی ندارد

### experience
- **Title**: سابقهٔ مورد نیاز
- **Type**: object
 - **Minimum**: N/A
 - **Maximum**: N/A

### has-photo
- **Title**: فقط عکس‌دار
- **Type**: boolean

### health_insurance
- **Title**: با بیمه
- **Type**: boolean

### job_type
- **Title**: نوع همکاری
- **Type**: object
 - **Items Type**: array
- **Queries**: 
  - full_time -> تمام وقت
  - part_time -> پاره وقت
  - contract -> پیمان‌کاری/پروژه‌ای
  - internship -> کارآموزی
  - adaptive -> توافقی
  - other -> سایر

### military_service_status
- **Title**: پایان خدمت/معافیت
- **Type**: object
- **Queries**: 
  - finish_or_exemption_required -> الزامی
  - finish_not_required -> اختیاری

### no_experience_required
- **Title**: بدون نیاز به سابقه
- **Type**: boolean

### payment_method
- **Title**: شیوهٔ پرداخت
- **Type**: object
 - **Items Type**: array
- **Queries**: 
  - monthly -> ماهانه
  - daily -> روزانه
  - hourly -> ساعتی
  - percentage_commission -> پورسانتی/درصدی
  - adaptive -> توافقی
  - other -> سایر

### remote
- **Title**: با امکان دورکاری
- **Type**: boolean

### sort
- **Title**: ترتیب نمایش آگهی‌ها براساس
- **Type**: object
- **Queries**: 
  - quality_and_sort_date -> quality_and_sort_date
  - sort_date -> sort_date
  - cheapest -> cheapest
  - most_expensive -> most_expensive
  - production_year -> production_year
  - usage -> usage
  - most_popular -> most_popular
  - most_relevant -> most_relevant

### urgent
- **Title**: فقط فوری‌ها
- **Type**: boolean



---

### Category: carpet



### carpet-type
- **Title**: بافت
- **Type**: object
- **Queries**: 
  - دست‌باف -> دست‌باف
  - ماشینی -> ماشینی

### category
- **Title**: دسته‌بندی
- **Type**: object

### dimensions
- **Title**: ابعاد
- **Type**: object
 - **Items Type**: array
- **Queries**: 
  - 1.5-meters -> ذرع و نیم (۱ در ۱٫۵ متر)
  - 2-meters -> ۲ متری (۱٫۲۰ در ۱٫۸۰ متر)
  - 4-meters -> ۴ متری (۱٫۵ در ۲٫۲۵ متر)
  - 4-meters-square -> ۴ متری (۲ در ۲ متر)
  - 6-meters -> ۶ متری (۲ در ۳ متر)
  - 9-meters -> ۹ متری (۲٫۵ در ۳٫۵ متر)
  - 12-meters -> ۱۲ متری (۳ در ۴ متر)
  - 24-meters -> ۲۴ متری (۴ در ۶ متر)
  - 1-meter-circular -> ۱ متری گرد (۱ در ۱ متر)
  - 3-meters-circular -> ۳ متری گرد (۱٫۵ در ۱٫۵ متر)
  - 4-meters-circular -> ۴ متری گرد (۲ در ۲ متر)
  - 6-meters-circular -> ۶ متری گرد (۲٫۵ در ۲٫۵ متر)
  - 9-meters-circular -> ۹ متری گرد (۳ در ۳ متر)
  - 0.5-meters-oval -> ۰٫۵ متری بیضی (۱ در ۰٫۵ متر)
  - 1.5-meters-oval -> ۱٫۵ متری بیضی (۱٫۵ در ۱ متر)
  - 4-meters-oval -> ۴ متری بیضی (۲٫۲۵ در ۱٫۵ متر)
  - others -> سایر ابعاد

### divider
- **Title**: سایر فیلتر‌ها
- **Type**: object

### exchange
- **Title**: نمایش معاوضه‌ها
- **Type**: object
- **Queries**: 
  - only-exchanges -> نمایش فقط معاوضه‌ها
  - exclude-exchanges -> حذف معاوضه‌ها

### goods-business-type
- **Title**: نوع آگهی‌دهنده
- **Type**: object
- **Queries**: 
  - all -> همه
  - personal -> شخصی
  - marketplace -> فروشگاه

### has-photo
- **Title**: فقط عکس‌دار
- **Type**: boolean

### price
- **Title**: قیمت
- **Type**: object
 - **Minimum**: 0
 - **Maximum**: N/A

### sort
- **Title**: ترتیب نمایش آگهی‌ها براساس
- **Type**: object
- **Queries**: 
  - quality_and_sort_date -> quality_and_sort_date
  - sort_date -> sort_date
  - cheapest -> cheapest
  - most_expensive -> most_expensive
  - production_year -> production_year
  - usage -> usage
  - most_popular -> most_popular
  - most_relevant -> most_relevant

### status
- **Title**: وضعیت کالا
- **Type**: object
 - **Items Type**: array
- **Queries**: 
  - new -> نو
  - like-new -> در حد نو
  - used -> کارکرده
  - repair-needed -> نیازمند تعمیر

### urgent
- **Title**: فقط فوری‌ها
- **Type**: boolean



---

### Category: carpet-moquette



### category
- **Title**: دسته‌بندی
- **Type**: object

### divider
- **Title**: سایر فیلتر‌ها
- **Type**: object

### exchange
- **Title**: نمایش معاوضه‌ها
- **Type**: object
- **Queries**: 
  - only-exchanges -> نمایش فقط معاوضه‌ها
  - exclude-exchanges -> حذف معاوضه‌ها

### goods-business-type
- **Title**: نوع آگهی‌دهنده
- **Type**: object
- **Queries**: 
  - all -> همه
  - personal -> شخصی
  - marketplace -> فروشگاه

### has-photo
- **Title**: فقط عکس‌دار
- **Type**: boolean

### price
- **Title**: قیمت
- **Type**: object
 - **Minimum**: 0
 - **Maximum**: N/A

### sort
- **Title**: ترتیب نمایش آگهی‌ها براساس
- **Type**: object
- **Queries**: 
  - quality_and_sort_date -> quality_and_sort_date
  - sort_date -> sort_date
  - cheapest -> cheapest
  - most_expensive -> most_expensive
  - production_year -> production_year
  - usage -> usage
  - most_popular -> most_popular
  - most_relevant -> most_relevant

### status
- **Title**: وضعیت کالا
- **Type**: object
 - **Items Type**: array
- **Queries**: 
  - new -> نو
  - like-new -> در حد نو
  - used -> کارکرده
  - repair-needed -> نیازمند تعمیر

### urgent
- **Title**: فقط فوری‌ها
- **Type**: boolean



---

### Category: cars



### category
- **Title**: دسته‌بندی
- **Type**: object

### divider
- **Title**: سایر فیلتر‌ها
- **Type**: object

### exchange
- **Title**: نمایش معاوضه‌ها
- **Type**: object
- **Queries**: 
  - only-exchanges -> نمایش فقط معاوضه‌ها
  - exclude-exchanges -> حذف معاوضه‌ها

### has-photo
- **Title**: فقط عکس‌دار
- **Type**: boolean

### non-negotiable
- **Title**: حذف توافقی‌ها
- **Type**: boolean

### post-type
- **Title**: نوع آگهی
- **Type**: object
- **Queries**: 
  - فروشی -> فروشی
  - درخواستی -> درخواستی

### price
- **Title**: قیمت
- **Type**: object
 - **Minimum**: 0
 - **Maximum**: N/A

### production-year
- **Title**: مدل (سال تولید)
- **Type**: object
 - **Minimum**: 0
 - **Maximum**: N/A

### sort
- **Title**: ترتیب نمایش آگهی‌ها براساس
- **Type**: object
- **Queries**: 
  - quality_and_sort_date -> quality_and_sort_date
  - sort_date -> sort_date
  - cheapest -> cheapest
  - most_expensive -> most_expensive
  - production_year -> production_year
  - usage -> usage
  - most_popular -> most_popular
  - most_relevant -> most_relevant

### urgent
- **Title**: فقط فوری‌ها
- **Type**: boolean

### usage
- **Title**: کارکرد
- **Type**: object
 - **Minimum**: 0
 - **Maximum**: N/A



---

### Category: cat



### category
- **Title**: دسته‌بندی
- **Type**: object

### divider
- **Title**: سایر فیلتر‌ها
- **Type**: object

### has-photo
- **Title**: فقط عکس‌دار
- **Type**: boolean

### sort
- **Title**: ترتیب نمایش آگهی‌ها براساس
- **Type**: object
- **Queries**: 
  - quality_and_sort_date -> quality_and_sort_date
  - sort_date -> sort_date
  - cheapest -> cheapest
  - most_expensive -> most_expensive
  - production_year -> production_year
  - usage -> usage
  - most_popular -> most_popular
  - most_relevant -> most_relevant

### urgent
- **Title**: فقط فوری‌ها
- **Type**: boolean



---

### Category: catering



### category
- **Title**: دسته‌بندی
- **Type**: object

### expertises
- **Title**: تخصص
- **Type**: object
 - **Items Type**: array
- **Queries**: 
  - ROOT -> همه تخصص‌ها
  - ceremony-photography -> عکاسی و فیلمبرداری مراسم
  - wedding-photography -> عکاسی و فیلمبرداری مهمانی و عروسی
  - family-photography -> عکاسی و فیلمبرداری خانوادگی
  - industrial-advertising-photography -> عکاسی و فیلمبرداری صنعتی و تبلیغاتی
  - conference-photography -> عکاسی و فیلمبرداری همایش و رویداد
  - photography-equipment-renting -> اجارهٔ تجهیزات آتلیهٔ عکاسی
  - ceremony-flower-arrangement -> گل آرایی مراسم
  - flower-vase-arrangement-bouquet -> گل آرایی باکس، جام، تاج و دسته گل
  - places-flower-arrangement -> گل آرایی اماکن
  - car-flower-arrangement -> گل آرایی خودرو
  - ceremony-music-lighting -> موسیقی و نورپردازی مراسم
  - audio-system-renting -> اجارهٔ سیستم صوتی و تصویری
  - music-performance -> اجرای موسیقی مراسم
  - eulogy -> مداحی مراسم مذهبی
  - ceremony-lighting -> نورپردازی مراسم
  - lighting-system-renting -> اجارهٔ سیستم نورپردازی
  - ceremony-design-reception -> مهمانداری و تشریفات مراسم
  - balloon-decoration -> بادکنک آرایی مراسم
  - table-decoration-fruit-arrangement -> سفره آرایی و میوه آرایی مراسم
  - dish-table-chair-renting -> اجارهٔ ظروف و میز و صندلی مراسم
  - decoration-equipment-renting -> اجارهٔ تجهیزات دکوراسیون مراسم
  - wedding-card-printing -> چاپ بنر تسلیت و کارت مراسم
  - reception-staff -> مهمانداری و پذیرایی مراسم
  - ceremony-cooking-baking -> آشپزی و شیرینی پزی مراسم
  - finger-food -> تهیهٔ فینگرفود
  - iranian-international-food -> تهیهٔ غذای ایرانی و بین الملل
  - cake-sweets -> تهیهٔ کیک و شیرینی
  - drinks -> تهیهٔ نوشیدنی
  - dessert -> تهیهٔ دسر
  - food-box -> تهیهٔ پک های مناسبتی
  - ceremony-reception-hall -> محضر و تالار پذیرایی مراسم
  - marriage-registry -> سالن عقد و محضر ازدواج
  - hotel-banquet-hall -> هتل، باغ و تالار پذیرایی مراسم
  - reception-ceremony-others -> سایر پذیرایی/مراسم

### has-photo
- **Title**: فقط عکس‌دار
- **Type**: boolean

### sort
- **Title**: ترتیب نمایش آگهی‌ها براساس
- **Type**: object
- **Queries**: 
  - quality_and_sort_date -> quality_and_sort_date
  - sort_date -> sort_date
  - cheapest -> cheapest
  - most_expensive -> most_expensive
  - production_year -> production_year
  - usage -> usage
  - most_popular -> most_popular
  - most_relevant -> most_relevant

### urgent
- **Title**: فقط فوری‌ها
- **Type**: boolean



---

### Category: chair-bench



### category
- **Title**: دسته‌بندی
- **Type**: object

### divider
- **Title**: سایر فیلتر‌ها
- **Type**: object

### exchange
- **Title**: نمایش معاوضه‌ها
- **Type**: object
- **Queries**: 
  - only-exchanges -> نمایش فقط معاوضه‌ها
  - exclude-exchanges -> حذف معاوضه‌ها

### goods-business-type
- **Title**: نوع آگهی‌دهنده
- **Type**: object
- **Queries**: 
  - all -> همه
  - personal -> شخصی
  - marketplace -> فروشگاه

### has-photo
- **Title**: فقط عکس‌دار
- **Type**: boolean

### price
- **Title**: قیمت
- **Type**: object
 - **Minimum**: 0
 - **Maximum**: N/A

### sort
- **Title**: ترتیب نمایش آگهی‌ها براساس
- **Type**: object
- **Queries**: 
  - quality_and_sort_date -> quality_and_sort_date
  - sort_date -> sort_date
  - cheapest -> cheapest
  - most_expensive -> most_expensive
  - production_year -> production_year
  - usage -> usage
  - most_popular -> most_popular
  - most_relevant -> most_relevant

### status
- **Title**: وضعیت کالا
- **Type**: object
 - **Items Type**: array
- **Queries**: 
  - new -> نو
  - like-new -> در حد نو
  - used -> کارکرده
  - repair-needed -> نیازمند تعمیر

### urgent
- **Title**: فقط فوری‌ها
- **Type**: boolean



---

### Category: chandeliers



### body-material
- **Title**: جنس بدنه
- **Type**: object
 - **Items Type**: array
- **Queries**: 
  - bronze -> برنز
  - wood -> چوب
  - metal -> فلزی
  - cristal -> کریستالی
  - other -> سایر

### branch-count
- **Title**: تعداد شاخه
- **Type**: object
 - **Items Type**: array
- **Queries**: 
  - 0 -> بدون شاخه
  - 1-4 -> ۱ تا ۴
  - 5-8 -> ۵ تا ۸
  - 9-12 -> ۹ تا ۱۲
  - 13-16 -> ۱۳ تا ۱۶
  - 17-20 -> ۱۷ تا ۲۰
  - 21-24 -> ۲۱ تا ۲۴
  - 25-28 -> ۲۵ تا ۲۸
  - 29-32 -> ۲۹ تا ۳۲
  - 33-36 -> ۳۳ تا ۳۶

### category
- **Title**: دسته‌بندی
- **Type**: object

### divider
- **Title**: سایر فیلتر‌ها
- **Type**: object

### exchange
- **Title**: نمایش معاوضه‌ها
- **Type**: object
- **Queries**: 
  - only-exchanges -> نمایش فقط معاوضه‌ها
  - exclude-exchanges -> حذف معاوضه‌ها

### goods-business-type
- **Title**: نوع آگهی‌دهنده
- **Type**: object
- **Queries**: 
  - all -> همه
  - personal -> شخصی
  - marketplace -> فروشگاه

### has-photo
- **Title**: فقط عکس‌دار
- **Type**: boolean

### price
- **Title**: قیمت
- **Type**: object
 - **Minimum**: 0
 - **Maximum**: N/A

### sort
- **Title**: ترتیب نمایش آگهی‌ها براساس
- **Type**: object
- **Queries**: 
  - quality_and_sort_date -> quality_and_sort_date
  - sort_date -> sort_date
  - cheapest -> cheapest
  - most_expensive -> most_expensive
  - production_year -> production_year
  - usage -> usage
  - most_popular -> most_popular
  - most_relevant -> most_relevant

### status
- **Title**: وضعیت کالا
- **Type**: object
 - **Items Type**: array
- **Queries**: 
  - new -> نو
  - like-new -> در حد نو
  - used -> کارکرده
  - repair-needed -> نیازمند تعمیر

### urgent
- **Title**: فقط فوری‌ها
- **Type**: boolean



---

### Category: child-car-seat



### category
- **Title**: دسته‌بندی
- **Type**: object

### divider
- **Title**: سایر فیلتر‌ها
- **Type**: object

### exchange
- **Title**: نمایش معاوضه‌ها
- **Type**: object
- **Queries**: 
  - only-exchanges -> نمایش فقط معاوضه‌ها
  - exclude-exchanges -> حذف معاوضه‌ها

### goods-business-type
- **Title**: نوع آگهی‌دهنده
- **Type**: object
- **Queries**: 
  - all -> همه
  - personal -> شخصی
  - marketplace -> فروشگاه

### has-photo
- **Title**: فقط عکس‌دار
- **Type**: boolean

### price
- **Title**: قیمت
- **Type**: object
 - **Minimum**: 0
 - **Maximum**: N/A

### sort
- **Title**: ترتیب نمایش آگهی‌ها براساس
- **Type**: object
- **Queries**: 
  - quality_and_sort_date -> quality_and_sort_date
  - sort_date -> sort_date
  - cheapest -> cheapest
  - most_expensive -> most_expensive
  - production_year -> production_year
  - usage -> usage
  - most_popular -> most_popular
  - most_relevant -> most_relevant

### status
- **Title**: وضعیت کالا
- **Type**: object
 - **Items Type**: array
- **Queries**: 
  - new -> نو
  - like-new -> در حد نو
  - used -> کارکرده
  - repair-needed -> نیازمند تعمیر

### urgent
- **Title**: فقط فوری‌ها
- **Type**: boolean



---

### Category: childrens-clothing-and-shoe



### category
- **Title**: دسته‌بندی
- **Type**: object

### divider
- **Title**: سایر فیلتر‌ها
- **Type**: object

### exchange
- **Title**: نمایش معاوضه‌ها
- **Type**: object
- **Queries**: 
  - only-exchanges -> نمایش فقط معاوضه‌ها
  - exclude-exchanges -> حذف معاوضه‌ها

### goods-business-type
- **Title**: نوع آگهی‌دهنده
- **Type**: object
- **Queries**: 
  - all -> همه
  - personal -> شخصی
  - marketplace -> فروشگاه

### has-photo
- **Title**: فقط عکس‌دار
- **Type**: boolean

### price
- **Title**: قیمت
- **Type**: object
 - **Minimum**: 0
 - **Maximum**: N/A

### sort
- **Title**: ترتیب نمایش آگهی‌ها براساس
- **Type**: object
- **Queries**: 
  - quality_and_sort_date -> quality_and_sort_date
  - sort_date -> sort_date
  - cheapest -> cheapest
  - most_expensive -> most_expensive
  - production_year -> production_year
  - usage -> usage
  - most_popular -> most_popular
  - most_relevant -> most_relevant

### status
- **Title**: وضعیت کالا
- **Type**: object
 - **Items Type**: array
- **Queries**: 
  - new -> نو
  - like-new -> در حد نو
  - used -> کارکرده
  - repair-needed -> نیازمند تعمیر

### type
- **Title**: دخترانه یا پسرانه
- **Type**: object
- **Queries**: 
  - دخترانه -> دخترانه
  - پسرانه -> پسرانه

### urgent
- **Title**: فقط فوری‌ها
- **Type**: boolean



---

### Category: childrens-furniture



### category
- **Title**: دسته‌بندی
- **Type**: object

### divider
- **Title**: سایر فیلتر‌ها
- **Type**: object

### exchange
- **Title**: نمایش معاوضه‌ها
- **Type**: object
- **Queries**: 
  - only-exchanges -> نمایش فقط معاوضه‌ها
  - exclude-exchanges -> حذف معاوضه‌ها

### goods-business-type
- **Title**: نوع آگهی‌دهنده
- **Type**: object
- **Queries**: 
  - all -> همه
  - personal -> شخصی
  - marketplace -> فروشگاه

### has-photo
- **Title**: فقط عکس‌دار
- **Type**: boolean

### price
- **Title**: قیمت
- **Type**: object
 - **Minimum**: 0
 - **Maximum**: N/A

### sort
- **Title**: ترتیب نمایش آگهی‌ها براساس
- **Type**: object
- **Queries**: 
  - quality_and_sort_date -> quality_and_sort_date
  - sort_date -> sort_date
  - cheapest -> cheapest
  - most_expensive -> most_expensive
  - production_year -> production_year
  - usage -> usage
  - most_popular -> most_popular
  - most_relevant -> most_relevant

### status
- **Title**: وضعیت کالا
- **Type**: object
 - **Items Type**: array
- **Queries**: 
  - new -> نو
  - like-new -> در حد نو
  - used -> کارکرده
  - repair-needed -> نیازمند تعمیر

### urgent
- **Title**: فقط فوری‌ها
- **Type**: boolean



---

### Category: classic



### category
- **Title**: دسته‌بندی
- **Type**: object

### divider
- **Title**: سایر فیلتر‌ها
- **Type**: object

### has-photo
- **Title**: فقط عکس‌دار
- **Type**: boolean

### non-negotiable
- **Title**: حذف توافقی‌ها
- **Type**: boolean

### post-type
- **Title**: نوع آگهی
- **Type**: object
- **Queries**: 
  - فروشی -> فروشی
  - درخواستی -> درخواستی

### price
- **Title**: قیمت
- **Type**: object
 - **Minimum**: 0
 - **Maximum**: N/A

### sort
- **Title**: ترتیب نمایش آگهی‌ها براساس
- **Type**: object
- **Queries**: 
  - quality_and_sort_date -> quality_and_sort_date
  - sort_date -> sort_date
  - cheapest -> cheapest
  - most_expensive -> most_expensive
  - production_year -> production_year
  - usage -> usage
  - most_popular -> most_popular
  - most_relevant -> most_relevant

### urgent
- **Title**: فقط فوری‌ها
- **Type**: boolean



---

### Category: cleaning



### category
- **Title**: دسته‌بندی
- **Type**: object

### expertises
- **Title**: تخصص
- **Type**: object
 - **Items Type**: array
- **Queries**: 
  - ROOT -> همه تخصص‌ها
  - dry-cleaning-ironing -> خشکشویی و اتوشویی
  - curtain-dry-cleaning -> خشکشویی و اتوکشی پرده
  - clothes-dry-cleaning-laundry -> خشکشویی و اتوکشی لباس
  - blankets-sheets-dry-cleaning -> خشکشویی پتو و ملحفه
  - clothes-dyeing -> رنگرزی لباس
  - carpet-furniture-cleaning -> قالیشویی و مبل‌شویی
  - carpet-repairing -> رفوگری فرش
  - carpet-cleaning -> قالی‌شویی
  - furniture-cleaning -> مبل‌شویی
  - moquette-cleaning -> موکت‌شویی
  - mattress-cleaning -> شستشوی خوشخواب
  - building-spraying-disinfecting -> سم‌پاشی و ضدعفونی ساختمان
  - building-disinfection -> ضدعفونی ساختمان
  - building-spraying -> سم‌پاشی ساختمان
  - home-workplace-cleaning -> نظافت منزل و محل کار
  - workplace-cleaning -> نظافت واحد اداری و تجاری
  - villa-garden-cleaning -> نظافت ویلا و باغ
  - home-cleaning -> نظافت منزل
  - building-cleaning -> نظافت ساختمان
  - polishing-stone-floor -> کف‌سابی
  - pool-cleaning -> نظافت و شستشوی استخر
  - staircase-cleaning -> نظافت راه‌پله و مشاعات
  - facade-cleaning -> نماشویی
  - cleaning-other -> سایر نظافت

### services_profile
- **Title**: فقط متخصصان تأیید هویت شده
- **Type**: boolean

### sort
- **Title**: ترتیب نمایش آگهی‌ها براساس
- **Type**: object
- **Queries**: 
  - quality_and_sort_date -> quality_and_sort_date
  - sort_date -> sort_date
  - cheapest -> cheapest
  - most_expensive -> most_expensive
  - production_year -> production_year
  - usage -> usage
  - most_popular -> most_popular
  - most_relevant -> most_relevant

### urgent
- **Title**: فقط فوری‌ها
- **Type**: boolean



---

### Category: cleaning-supplies



### category
- **Title**: دسته‌بندی
- **Type**: object

### divider
- **Title**: سایر فیلتر‌ها
- **Type**: object

### exchange
- **Title**: نمایش معاوضه‌ها
- **Type**: object
- **Queries**: 
  - only-exchanges -> نمایش فقط معاوضه‌ها
  - exclude-exchanges -> حذف معاوضه‌ها

### goods-business-type
- **Title**: نوع آگهی‌دهنده
- **Type**: object
- **Queries**: 
  - all -> همه
  - personal -> شخصی
  - marketplace -> فروشگاه

### has-photo
- **Title**: فقط عکس‌دار
- **Type**: boolean

### price
- **Title**: قیمت
- **Type**: object
 - **Minimum**: 0
 - **Maximum**: N/A

### sort
- **Title**: ترتیب نمایش آگهی‌ها براساس
- **Type**: object
- **Queries**: 
  - quality_and_sort_date -> quality_and_sort_date
  - sort_date -> sort_date
  - cheapest -> cheapest
  - most_expensive -> most_expensive
  - production_year -> production_year
  - usage -> usage
  - most_popular -> most_popular
  - most_relevant -> most_relevant

### status
- **Title**: وضعیت کالا
- **Type**: object
 - **Items Type**: array
- **Queries**: 
  - new -> نو
  - like-new -> در حد نو
  - used -> کارکرده
  - repair-needed -> نیازمند تعمیر

### urgent
- **Title**: فقط فوری‌ها
- **Type**: boolean



---

### Category: clothes-rack



### category
- **Title**: دسته‌بندی
- **Type**: object

### divider
- **Title**: سایر فیلتر‌ها
- **Type**: object

### exchange
- **Title**: نمایش معاوضه‌ها
- **Type**: object
- **Queries**: 
  - only-exchanges -> نمایش فقط معاوضه‌ها
  - exclude-exchanges -> حذف معاوضه‌ها

### goods-business-type
- **Title**: نوع آگهی‌دهنده
- **Type**: object
- **Queries**: 
  - all -> همه
  - personal -> شخصی
  - marketplace -> فروشگاه

### has-photo
- **Title**: فقط عکس‌دار
- **Type**: boolean

### price
- **Title**: قیمت
- **Type**: object
 - **Minimum**: 0
 - **Maximum**: N/A

### sort
- **Title**: ترتیب نمایش آگهی‌ها براساس
- **Type**: object
- **Queries**: 
  - quality_and_sort_date -> quality_and_sort_date
  - sort_date -> sort_date
  - cheapest -> cheapest
  - most_expensive -> most_expensive
  - production_year -> production_year
  - usage -> usage
  - most_popular -> most_popular
  - most_relevant -> most_relevant

### status
- **Title**: وضعیت کالا
- **Type**: object
 - **Items Type**: array
- **Queries**: 
  - new -> نو
  - like-new -> در حد نو
  - used -> کارکرده
  - repair-needed -> نیازمند تعمیر

### urgent
- **Title**: فقط فوری‌ها
- **Type**: boolean



---

### Category: clothing



### category
- **Title**: دسته‌بندی
- **Type**: object

### clothing-type
- **Title**: نوع لباس
- **Type**: object
 - **Items Type**: array
- **Queries**: 
  - مانتو -> مانتو
  - شال و روسری -> شال و روسری
  - ‌‌‌تیشرت -> ‌‌‌تیشرت
  - بلوز و شومیز -> بلوز و شومیز
  - شلوار -> شلوار
  - ژاکت و پلیور -> ژاکت و پلیور
  - لباس مجلسی -> لباس مجلسی
  - لباس عروس -> لباس عروس
  - کت و شلوار -> کت و شلوار
  - لباس زیر -> لباس زیر
  - کاپشن، پالتو، بارانی -> کاپشن، پالتو، بارانی
  - لباس ورزشی -> لباس ورزشی
  - جوراب، ساق، دستکش -> جوراب، ساق، دستکش
  - کلاه -> کلاه
  - سایر -> سایر

### divider
- **Title**: سایر فیلتر‌ها
- **Type**: object

### exchange
- **Title**: نمایش معاوضه‌ها
- **Type**: object
- **Queries**: 
  - only-exchanges -> نمایش فقط معاوضه‌ها
  - exclude-exchanges -> حذف معاوضه‌ها

### goods-business-type
- **Title**: نوع آگهی‌دهنده
- **Type**: object
- **Queries**: 
  - all -> همه
  - personal -> شخصی
  - marketplace -> فروشگاه

### has-color-and-pattern-variety
- **Title**: رنگ و طرح متنوع
- **Type**: boolean

### has-photo
- **Title**: فقط عکس‌دار
- **Type**: boolean

### manufacturer
- **Title**: تولیدکننده
- **Type**: object
- **Queries**: 
  - ایرانی -> ایرانی
  - خارجی -> خارجی

### price
- **Title**: قیمت
- **Type**: object
 - **Minimum**: 0
 - **Maximum**: N/A

### sort
- **Title**: ترتیب نمایش آگهی‌ها براساس
- **Type**: object
- **Queries**: 
  - quality_and_sort_date -> quality_and_sort_date
  - sort_date -> sort_date
  - cheapest -> cheapest
  - most_expensive -> most_expensive
  - production_year -> production_year
  - usage -> usage
  - most_popular -> most_popular
  - most_relevant -> most_relevant

### status
- **Title**: وضعیت کالا
- **Type**: object
 - **Items Type**: array
- **Queries**: 
  - new -> نو
  - like-new -> در حد نو
  - used -> کارکرده
  - repair-needed -> نیازمند تعمیر

### type
- **Title**: مردانه یا زنانه
- **Type**: object
- **Queries**: 
  - زنانه -> زنانه
  - مردانه -> مردانه

### urgent
- **Title**: فقط فوری‌ها
- **Type**: boolean



---

### Category: clothing-and-shoes



### category
- **Title**: دسته‌بندی
- **Type**: object

### divider
- **Title**: سایر فیلتر‌ها
- **Type**: object

### exchange
- **Title**: نمایش معاوضه‌ها
- **Type**: object
- **Queries**: 
  - only-exchanges -> نمایش فقط معاوضه‌ها
  - exclude-exchanges -> حذف معاوضه‌ها

### goods-business-type
- **Title**: نوع آگهی‌دهنده
- **Type**: object
- **Queries**: 
  - all -> همه
  - personal -> شخصی
  - marketplace -> فروشگاه

### has-photo
- **Title**: فقط عکس‌دار
- **Type**: boolean

### price
- **Title**: قیمت
- **Type**: object
 - **Minimum**: 0
 - **Maximum**: N/A

### sort
- **Title**: ترتیب نمایش آگهی‌ها براساس
- **Type**: object
- **Queries**: 
  - quality_and_sort_date -> quality_and_sort_date
  - sort_date -> sort_date
  - cheapest -> cheapest
  - most_expensive -> most_expensive
  - production_year -> production_year
  - usage -> usage
  - most_popular -> most_popular
  - most_relevant -> most_relevant

### status
- **Title**: وضعیت کالا
- **Type**: object
 - **Items Type**: array
- **Queries**: 
  - new -> نو
  - like-new -> در حد نو
  - used -> کارکرده
  - repair-needed -> نیازمند تعمیر

### type
- **Title**: مردانه یا زنانه
- **Type**: object
- **Queries**: 
  - زنانه -> زنانه
  - مردانه -> مردانه

### urgent
- **Title**: فقط فوری‌ها
- **Type**: boolean



---

### Category: coin-stamp



### category
- **Title**: دسته‌بندی
- **Type**: object

### divider
- **Title**: سایر فیلتر‌ها
- **Type**: object

### exchange
- **Title**: نمایش معاوضه‌ها
- **Type**: object
- **Queries**: 
  - only-exchanges -> نمایش فقط معاوضه‌ها
  - exclude-exchanges -> حذف معاوضه‌ها

### has-photo
- **Title**: فقط عکس‌دار
- **Type**: boolean

### price
- **Title**: قیمت
- **Type**: object
 - **Minimum**: 0
 - **Maximum**: N/A

### sort
- **Title**: ترتیب نمایش آگهی‌ها براساس
- **Type**: object
- **Queries**: 
  - quality_and_sort_date -> quality_and_sort_date
  - sort_date -> sort_date
  - cheapest -> cheapest
  - most_expensive -> most_expensive
  - production_year -> production_year
  - usage -> usage
  - most_popular -> most_popular
  - most_relevant -> most_relevant

### urgent
- **Title**: فقط فوری‌ها
- **Type**: boolean



---

### Category: commercial-rent



### business-type
- **Title**: آگهی‌دهنده
- **Type**: object
- **Queries**: 
  - personal -> شخصی
  - real-estate-business -> مشاور املاک

### category
- **Title**: دسته‌بندی
- **Type**: object

### credit
- **Title**: ودیعه
- **Type**: object
 - **Minimum**: 0
 - **Maximum**: N/A

### has-photo
- **Title**: عکس‌دار
- **Type**: boolean

### has-video
- **Title**: ویدیو‌دار
- **Type**: boolean

### rent
- **Title**: اجاره
- **Type**: object
 - **Minimum**: 0
 - **Maximum**: N/A

### size
- **Title**: متراژ
- **Type**: object
 - **Minimum**: 0
 - **Maximum**: 1000000000

### sort
- **Title**: ترتیب نمایش آگهی‌ها براساس
- **Type**: object
- **Queries**: 
  - quality_and_sort_date -> quality_and_sort_date
  - sort_date -> sort_date
  - cheapest -> cheapest
  - most_expensive -> most_expensive
  - production_year -> production_year
  - usage -> usage
  - most_popular -> most_popular
  - most_relevant -> most_relevant

### urgent
- **Title**: فقط فوری‌ها
- **Type**: boolean



---

### Category: commercial-sell



### bizzDeed
- **Title**: سند اداری
- **Type**: object
- **Queries**: 
  - True -> دارد
  - False -> ندارد

### business-type
- **Title**: آگهی‌دهنده
- **Type**: object
- **Queries**: 
  - personal -> شخصی
  - real-estate-business -> مشاور املاک

### category
- **Title**: دسته‌بندی
- **Type**: object

### has-photo
- **Title**: عکس‌دار
- **Type**: boolean

### has-video
- **Title**: ویدیو‌دار
- **Type**: boolean

### price
- **Title**: قیمت کل
- **Type**: object
 - **Minimum**: 0
 - **Maximum**: N/A

### size
- **Title**: متراژ
- **Type**: object
 - **Minimum**: 0
 - **Maximum**: 1000000000

### sort
- **Title**: ترتیب نمایش آگهی‌ها براساس
- **Type**: object
- **Queries**: 
  - quality_and_sort_date -> quality_and_sort_date
  - sort_date -> sort_date
  - cheapest -> cheapest
  - most_expensive -> most_expensive
  - production_year -> production_year
  - usage -> usage
  - most_popular -> most_popular
  - most_relevant -> most_relevant

### urgent
- **Title**: فقط فوری‌ها
- **Type**: boolean



---

### Category: community



### category
- **Title**: دسته‌بندی
- **Type**: object

### divider
- **Title**: سایر فیلتر‌ها
- **Type**: object

### exchange
- **Title**: نمایش معاوضه‌ها
- **Type**: object
- **Queries**: 
  - only-exchanges -> نمایش فقط معاوضه‌ها
  - exclude-exchanges -> حذف معاوضه‌ها

### has-photo
- **Title**: فقط عکس‌دار
- **Type**: boolean

### non-negotiable
- **Title**: حذف توافقی‌ها
- **Type**: boolean

### price
- **Title**: قیمت
- **Type**: object
 - **Minimum**: 0
 - **Maximum**: N/A

### sort
- **Title**: ترتیب نمایش آگهی‌ها براساس
- **Type**: object
- **Queries**: 
  - quality_and_sort_date -> quality_and_sort_date
  - sort_date -> sort_date
  - cheapest -> cheapest
  - most_expensive -> most_expensive
  - production_year -> production_year
  - usage -> usage
  - most_popular -> most_popular
  - most_relevant -> most_relevant

### urgent
- **Title**: فقط فوری‌ها
- **Type**: boolean



---

### Category: computer-and-it



### category
- **Title**: دسته‌بندی
- **Type**: object

### divider
- **Title**: سایر فیلتر‌ها
- **Type**: object

### employee_gender
- **Title**: جنسیت کارجو
- **Type**: object
- **Queries**: 
  - female -> زن
  - male -> مرد
  - neutral -> فرقی ندارد

### experience
- **Title**: سابقهٔ مورد نیاز
- **Type**: object
 - **Minimum**: N/A
 - **Maximum**: N/A

### has-photo
- **Title**: فقط عکس‌دار
- **Type**: boolean

### health_insurance
- **Title**: با بیمه
- **Type**: boolean

### job_type
- **Title**: نوع همکاری
- **Type**: object
 - **Items Type**: array
- **Queries**: 
  - full_time -> تمام وقت
  - part_time -> پاره وقت
  - contract -> پیمان‌کاری/پروژه‌ای
  - internship -> کارآموزی
  - adaptive -> توافقی
  - other -> سایر

### military_service_status
- **Title**: پایان خدمت/معافیت
- **Type**: object
- **Queries**: 
  - finish_or_exemption_required -> الزامی
  - finish_not_required -> اختیاری

### no_experience_required
- **Title**: بدون نیاز به سابقه
- **Type**: boolean

### payment_method
- **Title**: شیوهٔ پرداخت
- **Type**: object
 - **Items Type**: array
- **Queries**: 
  - monthly -> ماهانه
  - daily -> روزانه
  - hourly -> ساعتی
  - percentage_commission -> پورسانتی/درصدی
  - adaptive -> توافقی
  - other -> سایر

### remote
- **Title**: با امکان دورکاری
- **Type**: boolean

### sort
- **Title**: ترتیب نمایش آگهی‌ها براساس
- **Type**: object
- **Queries**: 
  - quality_and_sort_date -> quality_and_sort_date
  - sort_date -> sort_date
  - cheapest -> cheapest
  - most_expensive -> most_expensive
  - production_year -> production_year
  - usage -> usage
  - most_popular -> most_popular
  - most_relevant -> most_relevant

### urgent
- **Title**: فقط فوری‌ها
- **Type**: boolean



---

### Category: computer-and-mobile



### category
- **Title**: دسته‌بندی
- **Type**: object

### expertises
- **Title**: تخصص
- **Type**: object
 - **Items Type**: array
- **Queries**: 
  - ROOT -> همه تخصص‌ها
  - type-translation-services -> تایپ و ترجمه
  - type-powerpoint-excel -> تایپ، پاورپوینت، اکسل
  - translation -> ترجمه
  - editing-page-layout -> ویراستاری و صفحه آرایی
  - mobile-tablet-services -> نرم‌افزار، سخت‌افزار و لوازم جانبی موبایل و تبلت
  - mobile-hardware-repair -> تعمیر و تعویض قطعات سخت‌افزاری موبایل
  - airpods-repair -> تعمیر هندزفری، هدفون و ایرپاد
  - smart-watch-repair -> تعمیر ساعت هوشمند
  - mobile-software -> خدمات نرم افزاری موبایل
  - computer-laptop-services -> نرم‌افزار، سخت‌افزار و لوازم جانبی کامپیوتر و لپ‌تاپ
  - computer-software-repair -> نصب و تعمیر و تعویض نرم افزار و درایو
  - computer-accessory-repair -> تعمیر، تعویض، نصب لوازم جانبی کامپیوتر
  - computer-hardware-repair -> تعمیر، نصب، تعویض قطعات سخت افزاری کامپیوتر
  - miner-repair -> نصب، تعمیر، تعویض و لوازم جانبی ماینر
  - network-server-services -> شبکه و سرور
  - modem-repair -> نصب و تعمیر مودم و فعال‌سازی اینترنت
  - network-wiring -> سیم‌کشی شبکه
  - network installation-maintenance -> نصب و نگهداری شبکه
  - ups-installation-maintenance -> نصب و نگهداری UPS
  - office-machine-services -> ماشین‌های اداری
  - industrial-printing-machines-repair -> نصب و تعمیر دستگاه‌های چاپ صنعتی
  - printer-scanner-repair -> نصب و تعمیر پرینتر، اسکنر، کپی و فکس
  - atm-installation-repair -> نصب و تعمیر کارتخوان و ATM
  - game-console-services -> کنسول بازی
  - game-installation -> نصب بازی کنسول
  - game- console-repair -> تعمیر کنسول و دسته
  - game-console-rent -> اجارهٔ کنسول و دسته
  - printing-advertising-services -> چاپ و تبلیغات
  - office-product -> طراحی و چاپ اوراق اداری
  - advertising-product -> طراحی و چاپ محصولات بازاریابی و تبلیغات
  - packaging-product -> طراحی و چاپ محصولات بسته‌بندی
  - promotional-gift -> طراحی و چاپ هدایای تبلیغاتی
  - digital-marketing-services -> دیجیتال مارکتینگ
  - web-designing -> طراحی، ساخت، بازگردانی و حذف سایت، دامنه و شبکه‌های اجتماعی
  - social-media-security -> امنیت سایت و شبکهٔ اجتماعی
  - social-media-admin -> ادمین سایت و شبکهٔ اجتماعی
  - content-writing -> تولید محتوا
  - seo-services -> خدمات سئو
  - followers-social-media -> فالوور، بازدید، لایک شبکه‌های اجتماعی
  - technology-other -> سایر خدمات رایانه‌ای و موبایل

### has-photo
- **Title**: فقط عکس‌دار
- **Type**: boolean

### sort
- **Title**: ترتیب نمایش آگهی‌ها براساس
- **Type**: object
- **Queries**: 
  - quality_and_sort_date -> quality_and_sort_date
  - sort_date -> sort_date
  - cheapest -> cheapest
  - most_expensive -> most_expensive
  - production_year -> production_year
  - usage -> usage
  - most_popular -> most_popular
  - most_relevant -> most_relevant

### urgent
- **Title**: فقط فوری‌ها
- **Type**: boolean



---

### Category: computers



### category
- **Title**: دسته‌بندی
- **Type**: object

### divider
- **Title**: سایر فیلتر‌ها
- **Type**: object

### exchange
- **Title**: نمایش معاوضه‌ها
- **Type**: object
- **Queries**: 
  - only-exchanges -> نمایش فقط معاوضه‌ها
  - exclude-exchanges -> حذف معاوضه‌ها

### goods-business-type
- **Title**: نوع آگهی‌دهنده
- **Type**: object
- **Queries**: 
  - all -> همه
  - personal -> شخصی
  - marketplace -> فروشگاه

### has-photo
- **Title**: فقط عکس‌دار
- **Type**: boolean

### price
- **Title**: قیمت
- **Type**: object
 - **Minimum**: 0
 - **Maximum**: N/A

### sort
- **Title**: ترتیب نمایش آگهی‌ها براساس
- **Type**: object
- **Queries**: 
  - quality_and_sort_date -> quality_and_sort_date
  - sort_date -> sort_date
  - cheapest -> cheapest
  - most_expensive -> most_expensive
  - production_year -> production_year
  - usage -> usage
  - most_popular -> most_popular
  - most_relevant -> most_relevant

### status
- **Title**: وضعیت کالا
- **Type**: object
 - **Items Type**: array
- **Queries**: 
  - new -> نو
  - like-new -> در حد نو
  - used -> کارکرده
  - repair-needed -> نیازمند تعمیر

### urgent
- **Title**: فقط فوری‌ها
- **Type**: boolean



---

### Category: concert



### category
- **Title**: دسته‌بندی
- **Type**: object

### divider
- **Title**: سایر فیلتر‌ها
- **Type**: object

### exchange
- **Title**: نمایش معاوضه‌ها
- **Type**: object
- **Queries**: 
  - only-exchanges -> نمایش فقط معاوضه‌ها
  - exclude-exchanges -> حذف معاوضه‌ها

### has-photo
- **Title**: فقط عکس‌دار
- **Type**: boolean

### price
- **Title**: قیمت
- **Type**: object
 - **Minimum**: 0
 - **Maximum**: N/A

### sort
- **Title**: ترتیب نمایش آگهی‌ها براساس
- **Type**: object
- **Queries**: 
  - quality_and_sort_date -> quality_and_sort_date
  - sort_date -> sort_date
  - cheapest -> cheapest
  - most_expensive -> most_expensive
  - production_year -> production_year
  - usage -> usage
  - most_popular -> most_popular
  - most_relevant -> most_relevant

### urgent
- **Title**: فقط فوری‌ها
- **Type**: boolean



---

### Category: conference-meeting



### category
- **Title**: دسته‌بندی
- **Type**: object

### exchange
- **Title**: نمایش معاوضه‌ها
- **Type**: object
- **Queries**: 
  - only-exchanges -> نمایش فقط معاوضه‌ها
  - exclude-exchanges -> حذف معاوضه‌ها

### has-photo
- **Title**: فقط عکس‌دار
- **Type**: boolean

### non-negotiable
- **Title**: حذف توافقی‌ها
- **Type**: boolean

### price
- **Title**: قیمت
- **Type**: object
 - **Minimum**: 0
 - **Maximum**: N/A

### sort
- **Title**: ترتیب نمایش آگهی‌ها براساس
- **Type**: object
- **Queries**: 
  - quality_and_sort_date -> quality_and_sort_date
  - sort_date -> sort_date
  - cheapest -> cheapest
  - most_expensive -> most_expensive
  - production_year -> production_year
  - usage -> usage
  - most_popular -> most_popular
  - most_relevant -> most_relevant

### urgent
- **Title**: فقط فوری‌ها
- **Type**: boolean



---

### Category: construction-craft



### category
- **Title**: دسته‌بندی
- **Type**: object

### divider
- **Title**: سایر فیلتر‌ها
- **Type**: object

### employee_gender
- **Title**: جنسیت کارجو
- **Type**: object
- **Queries**: 
  - female -> زن
  - male -> مرد
  - neutral -> فرقی ندارد

### experience
- **Title**: سابقهٔ مورد نیاز
- **Type**: object
 - **Minimum**: N/A
 - **Maximum**: N/A

### has-photo
- **Title**: فقط عکس‌دار
- **Type**: boolean

### health_insurance
- **Title**: با بیمه
- **Type**: boolean

### job_type
- **Title**: نوع همکاری
- **Type**: object
 - **Items Type**: array
- **Queries**: 
  - full_time -> تمام وقت
  - part_time -> پاره وقت
  - contract -> پیمان‌کاری/پروژه‌ای
  - internship -> کارآموزی
  - adaptive -> توافقی
  - other -> سایر

### military_service_status
- **Title**: پایان خدمت/معافیت
- **Type**: object
- **Queries**: 
  - finish_or_exemption_required -> الزامی
  - finish_not_required -> اختیاری

### no_experience_required
- **Title**: بدون نیاز به سابقه
- **Type**: boolean

### payment_method
- **Title**: شیوهٔ پرداخت
- **Type**: object
 - **Items Type**: array
- **Queries**: 
  - monthly -> ماهانه
  - daily -> روزانه
  - hourly -> ساعتی
  - percentage_commission -> پورسانتی/درصدی
  - adaptive -> توافقی
  - other -> سایر

### remote
- **Title**: با امکان دورکاری
- **Type**: boolean

### sort
- **Title**: ترتیب نمایش آگهی‌ها براساس
- **Type**: object
- **Queries**: 
  - quality_and_sort_date -> quality_and_sort_date
  - sort_date -> sort_date
  - cheapest -> cheapest
  - most_expensive -> most_expensive
  - production_year -> production_year
  - usage -> usage
  - most_popular -> most_popular
  - most_relevant -> most_relevant

### urgent
- **Title**: فقط فوری‌ها
- **Type**: boolean



---

### Category: container-organizers



### category
- **Title**: دسته‌بندی
- **Type**: object

### divider
- **Title**: سایر فیلتر‌ها
- **Type**: object

### exchange
- **Title**: نمایش معاوضه‌ها
- **Type**: object
- **Queries**: 
  - only-exchanges -> نمایش فقط معاوضه‌ها
  - exclude-exchanges -> حذف معاوضه‌ها

### goods-business-type
- **Title**: نوع آگهی‌دهنده
- **Type**: object
- **Queries**: 
  - all -> همه
  - personal -> شخصی
  - marketplace -> فروشگاه

### has-photo
- **Title**: فقط عکس‌دار
- **Type**: boolean

### price
- **Title**: قیمت
- **Type**: object
 - **Minimum**: 0
 - **Maximum**: N/A

### sort
- **Title**: ترتیب نمایش آگهی‌ها براساس
- **Type**: object
- **Queries**: 
  - quality_and_sort_date -> quality_and_sort_date
  - sort_date -> sort_date
  - cheapest -> cheapest
  - most_expensive -> most_expensive
  - production_year -> production_year
  - usage -> usage
  - most_popular -> most_popular
  - most_relevant -> most_relevant

### status
- **Title**: وضعیت کالا
- **Type**: object
 - **Items Type**: array
- **Queries**: 
  - new -> نو
  - like-new -> در حد نو
  - used -> کارکرده
  - repair-needed -> نیازمند تعمیر

### urgent
- **Title**: فقط فوری‌ها
- **Type**: boolean



---

### Category: containers



### category
- **Title**: دسته‌بندی
- **Type**: object

### divider
- **Title**: سایر فیلتر‌ها
- **Type**: object

### exchange
- **Title**: نمایش معاوضه‌ها
- **Type**: object
- **Queries**: 
  - only-exchanges -> نمایش فقط معاوضه‌ها
  - exclude-exchanges -> حذف معاوضه‌ها

### goods-business-type
- **Title**: نوع آگهی‌دهنده
- **Type**: object
- **Queries**: 
  - all -> همه
  - personal -> شخصی
  - marketplace -> فروشگاه

### has-photo
- **Title**: فقط عکس‌دار
- **Type**: boolean

### price
- **Title**: قیمت
- **Type**: object
 - **Minimum**: 0
 - **Maximum**: N/A

### sort
- **Title**: ترتیب نمایش آگهی‌ها براساس
- **Type**: object
- **Queries**: 
  - quality_and_sort_date -> quality_and_sort_date
  - sort_date -> sort_date
  - cheapest -> cheapest
  - most_expensive -> most_expensive
  - production_year -> production_year
  - usage -> usage
  - most_popular -> most_popular
  - most_relevant -> most_relevant

### status
- **Title**: وضعیت کالا
- **Type**: object
 - **Items Type**: array
- **Queries**: 
  - new -> نو
  - like-new -> در حد نو
  - used -> کارکرده
  - repair-needed -> نیازمند تعمیر

### urgent
- **Title**: فقط فوری‌ها
- **Type**: boolean



---

### Category: cooking-utensils



### category
- **Title**: دسته‌بندی
- **Type**: object

### divider
- **Title**: سایر فیلتر‌ها
- **Type**: object

### exchange
- **Title**: نمایش معاوضه‌ها
- **Type**: object
- **Queries**: 
  - only-exchanges -> نمایش فقط معاوضه‌ها
  - exclude-exchanges -> حذف معاوضه‌ها

### goods-business-type
- **Title**: نوع آگهی‌دهنده
- **Type**: object
- **Queries**: 
  - all -> همه
  - personal -> شخصی
  - marketplace -> فروشگاه

### has-photo
- **Title**: فقط عکس‌دار
- **Type**: boolean

### price
- **Title**: قیمت
- **Type**: object
 - **Minimum**: 0
 - **Maximum**: N/A

### sort
- **Title**: ترتیب نمایش آگهی‌ها براساس
- **Type**: object
- **Queries**: 
  - quality_and_sort_date -> quality_and_sort_date
  - sort_date -> sort_date
  - cheapest -> cheapest
  - most_expensive -> most_expensive
  - production_year -> production_year
  - usage -> usage
  - most_popular -> most_popular
  - most_relevant -> most_relevant

### status
- **Title**: وضعیت کالا
- **Type**: object
 - **Items Type**: array
- **Queries**: 
  - new -> نو
  - like-new -> در حد نو
  - used -> کارکرده
  - repair-needed -> نیازمند تعمیر

### urgent
- **Title**: فقط فوری‌ها
- **Type**: boolean



---

### Category: crafts



### category
- **Title**: دسته‌بندی
- **Type**: object

### divider
- **Title**: سایر فیلتر‌ها
- **Type**: object

### exchange
- **Title**: نمایش معاوضه‌ها
- **Type**: object
- **Queries**: 
  - only-exchanges -> نمایش فقط معاوضه‌ها
  - exclude-exchanges -> حذف معاوضه‌ها

### goods-business-type
- **Title**: نوع آگهی‌دهنده
- **Type**: object
- **Queries**: 
  - all -> همه
  - personal -> شخصی
  - marketplace -> فروشگاه

### has-photo
- **Title**: فقط عکس‌دار
- **Type**: boolean

### price
- **Title**: قیمت
- **Type**: object
 - **Minimum**: 0
 - **Maximum**: N/A

### sort
- **Title**: ترتیب نمایش آگهی‌ها براساس
- **Type**: object
- **Queries**: 
  - quality_and_sort_date -> quality_and_sort_date
  - sort_date -> sort_date
  - cheapest -> cheapest
  - most_expensive -> most_expensive
  - production_year -> production_year
  - usage -> usage
  - most_popular -> most_popular
  - most_relevant -> most_relevant

### status
- **Title**: وضعیت کالا
- **Type**: object
 - **Items Type**: array
- **Queries**: 
  - new -> نو
  - like-new -> در حد نو
  - used -> کارکرده
  - repair-needed -> نیازمند تعمیر

### urgent
- **Title**: فقط فوری‌ها
- **Type**: boolean



---

### Category: craftsmen



### category
- **Title**: دسته‌بندی
- **Type**: object

### expertises
- **Title**: تخصص
- **Type**: object
 - **Items Type**: array
- **Queries**: 
  - ROOT -> همه تخصص‌ها
  - drain-cleaning -> لوله بازکنی و تخلیه چاه
  - unclog-drain -> لوله بازکنی
  - well-draining -> ترمیم و تخلیه چاه
  - well-digging -> حفر چاه
  - engine-room-services -> اجرای موتورخانه
  - engine-room-construction -> اجرا و تعمیر موتورخانه
  - chiller-fan-coil-repair -> نصب و تعمیر چیلر و فن کویل
  - installing-water-pump -> نصب و تعمیر پمپ آب
  - entilation-cooling-heating-services -> خدمات تهویه، سرمایش و گرمایش
  - water-cooler-installation -> نصب و تعمیر کولر آبی
  - split-air-conditioner-installation -> نصب و تعمیر کولر گازی و اسپیلت
  - water-heater-installation -> نصب و تعمیر آبگرمکن
  - boiler-installation -> نصب و تعمیر پکیج
  - radiators-installation -> نصب و تعمیر رادیاتور
  - fireplace-installation -> نصب و تعمیر بخاری گازی و شومینه
  - air-purifiers-installation -> نصب و تعمیر پنکه و تصفیه‌کنندهٔ هوا
  - wood-furniture-manufacture -> صنایع چوب و مبلمان
  - cabinet-wardrobe-construction -> ساخت و تعمیر کابینت و کمد دیواری
  - furniture-making-repair -> ساخت و تعمیرات مبلمان
  - carpentary -> نجاری لوازم چوبی
  - furniture-cover -> دوخت کاور مبلمان
  - furniture-fabric-repair -> رویه‌کوبی مبلمان
  - wooden-door-construction -> ساخت و تعمیر درب چوبی
  - bedroom-furniture -> ساخت و تعمیر سرویس خواب
  - home-appliances-installation-repair -> راه اندازی و تعمیر لوازم خانگی
  - household-personal-appliances-repair -> تعمیر لوازم برقی خانگی و شخصی
  - refrigerator-freezer-repair -> نصب و تعمیر یخچال و فریزر
  - washing-machine-dishwasher-repair -> نصب و تعمیر ماشین لباس‌شویی و ظرفشویی
  - audio-video-appliance-repair -> نصب و تعمیر لوازم صوتی و تصویری
  - kitchen-hood-repair -> نصب و تعمیر هود
  - stove-repair -> نصب و تعمیر اجاق گاز
  - sports-equipment-repair -> نصب و تعمیر لوازم تناسب اندام و ورزشی
  - faucet-sanitary-services -> خدمات شیرآلات و سرویس بهداشتی
  - faucet-installations -> نصب و تعمیر شیرآلات
  - sanitary-facilities-installation -> نصب و تعمیر سرویس بهداشتی
  - water-purifier-installation -> نصب و تعمیر تصفیه آب
  - interior-decoration -> دکوراسیون داخلی
  - home-decorations-item-painting -> ساخت وسایل دکوری خانگی و تابلو
  - partition-installation -> ساخت و نصب ویترین و پارتیشن
  - curtain-sewing -> دوخت و نصب پرده
  - wallpaper-installation -> نصب و اجرای کاغذ دیواری و دیوار پوش
  - dropped-ceiling -> اجرای کناف و سقف کاذب
  - glass-cutting -> شیشه‌بری و آینه‌کاری
  - parquet-laminate-installation -> نصب پارکت، قرنیز و کفپوش
  - landscape-design -> طراحی و اجرای محوطه و فضای سبز
  - building-painting -> نقاشی ساختمان
  - electrical-wiring-lighting -> سیم‌کشی برق و روشنایی
  - electrical-wiring -> برقکاری ساختمان
  - central-digital-antenna-installation -> نصب و تعمیر آنتن مرکزی و دیجیتال
  - chandelier-lamp-installation -> نصب و تعمیر لوستر، چراغ و نور مخفی
  - electrical-panel-fuse-box -> تابلو برق و جعبه فیوز
  - phone-wiring -> راه اندازی و سیم کشی تلفن
  - advertising-boards-making -> ساخت و تعمیر تابلوی تبلیغاتی
  - building-construction-operations -> عملیات عمرانی ساختمان
  - cooler-ducting -> کانال کشی کولر
  - plastering -> گچکاری
  - tiling-ceramics -> کاشی‌کاری و سرامیک
  - building-facade-repair -> طراحی، اجرا و تعمیر نمای ساختمان
  - scaffolding -> داربست و کفراژ
  - strengthening-cornering-building -> مقاوم‌سازی و نبشی‌کشی
  - waterproofing -> ایزوگام و قیرگونی
  - demolition-excavation -> تخریب، گود برداری و سازهٔ نگهبان
  - doors-windows-making -> ساخت و نصب و تعمیر در و پنجره و توری
  - cementing -> سیمان‌کاری
  - piping -> لوله‌کشی
  - sewage-piping -> لوله کشی فاضلاب
  - swimming-pool-construction -> اجرای استخر، سونا و جکوزی
  - gas-piping -> لوله کشی گاز و آتش نشانی
  - radiator-piping -> لوله کشی پکیج و رادیاتور
  - leak-detection -> نشت یابی و تشخیص ترکیدگی
  - water-piping -> لوله کشی آب سرد و گرم
  - craftsmen-other -> سایر پیشه و مهارت
  - building-safety-security -> ایمنی و امنیت ساختمان
  - locksmithing-keymaking -> قفل و کلید‌سازی
  - door-open-installation -> نصب و تعمیر آیفون صوتی و تصویری
  - cctv-installation -> نصب و تعمیر دوربین مداربسته
  - rollup-door-installation -> نصب و تعمیر کرکرهٔ برقی
  - alarm-security-system-installation -> نصب و تعمیر دزدگیر و سیستم حفاظتی
  - automatic-door-installation -> نصب و تعمیر درب اتوماتیک
  - elevator-installation -> نصب و تعمیر آسانسور و بالابر
  - fire-alarm-system -> اجرا و نصب سیستم اعلام و اطفاء حریق
  - sensor-timer-implementation -> اجرا و نصب سنسور و تایمر مشاعات
  - blacksmithing-welding -> آهنگری و جوشکاری
  - canopy-building -> ساخت و نصب سایه‌بان و آلاچیق
  - cutting-turning -> برشکاری و تراشکاری
  - iron-door-fences -> ساخت و نصب درب آهنی، نرده و حفاظ
  - steel-staircase-construction -> ساخت و نصب پلهٔ استیل
  - conex-building -> ساخت و نصب سوله و کانکس
  - metal-products-manufacture -> ساخت محصولات فلزی
  - welding -> جوشکاری

### services_profile
- **Title**: فقط متخصصان تأیید هویت شده
- **Type**: boolean

### sort
- **Title**: ترتیب نمایش آگهی‌ها براساس
- **Type**: object
- **Queries**: 
  - quality_and_sort_date -> quality_and_sort_date
  - sort_date -> sort_date
  - cheapest -> cheapest
  - most_expensive -> most_expensive
  - production_year -> production_year
  - usage -> usage
  - most_popular -> most_popular
  - most_relevant -> most_relevant

### urgent
- **Title**: فقط فوری‌ها
- **Type**: boolean



---

### Category: curtains-table-cover



### category
- **Title**: دسته‌بندی
- **Type**: object

### divider
- **Title**: سایر فیلتر‌ها
- **Type**: object

### exchange
- **Title**: نمایش معاوضه‌ها
- **Type**: object
- **Queries**: 
  - only-exchanges -> نمایش فقط معاوضه‌ها
  - exclude-exchanges -> حذف معاوضه‌ها

### goods-business-type
- **Title**: نوع آگهی‌دهنده
- **Type**: object
- **Queries**: 
  - all -> همه
  - personal -> شخصی
  - marketplace -> فروشگاه

### has-photo
- **Title**: فقط عکس‌دار
- **Type**: boolean

### price
- **Title**: قیمت
- **Type**: object
 - **Minimum**: 0
 - **Maximum**: N/A

### sort
- **Title**: ترتیب نمایش آگهی‌ها براساس
- **Type**: object
- **Queries**: 
  - quality_and_sort_date -> quality_and_sort_date
  - sort_date -> sort_date
  - cheapest -> cheapest
  - most_expensive -> most_expensive
  - production_year -> production_year
  - usage -> usage
  - most_popular -> most_popular
  - most_relevant -> most_relevant

### status
- **Title**: وضعیت کالا
- **Type**: object
 - **Items Type**: array
- **Queries**: 
  - new -> نو
  - like-new -> در حد نو
  - used -> کارکرده
  - repair-needed -> نیازمند تعمیر

### urgent
- **Title**: فقط فوری‌ها
- **Type**: boolean



---

### Category: decoration



### category
- **Title**: دسته‌بندی
- **Type**: object

### divider
- **Title**: سایر فیلتر‌ها
- **Type**: object

### exchange
- **Title**: نمایش معاوضه‌ها
- **Type**: object
- **Queries**: 
  - only-exchanges -> نمایش فقط معاوضه‌ها
  - exclude-exchanges -> حذف معاوضه‌ها

### goods-business-type
- **Title**: نوع آگهی‌دهنده
- **Type**: object
- **Queries**: 
  - all -> همه
  - personal -> شخصی
  - marketplace -> فروشگاه

### has-photo
- **Title**: فقط عکس‌دار
- **Type**: boolean

### price
- **Title**: قیمت
- **Type**: object
 - **Minimum**: 0
 - **Maximum**: N/A

### sort
- **Title**: ترتیب نمایش آگهی‌ها براساس
- **Type**: object
- **Queries**: 
  - quality_and_sort_date -> quality_and_sort_date
  - sort_date -> sort_date
  - cheapest -> cheapest
  - most_expensive -> most_expensive
  - production_year -> production_year
  - usage -> usage
  - most_popular -> most_popular
  - most_relevant -> most_relevant

### status
- **Title**: وضعیت کالا
- **Type**: object
 - **Items Type**: array
- **Queries**: 
  - new -> نو
  - like-new -> در حد نو
  - used -> کارکرده
  - repair-needed -> نیازمند تعمیر

### urgent
- **Title**: فقط فوری‌ها
- **Type**: boolean



---

### Category: desk



### category
- **Title**: دسته‌بندی
- **Type**: object

### divider
- **Title**: سایر فیلتر‌ها
- **Type**: object

### exchange
- **Title**: نمایش معاوضه‌ها
- **Type**: object
- **Queries**: 
  - only-exchanges -> نمایش فقط معاوضه‌ها
  - exclude-exchanges -> حذف معاوضه‌ها

### goods-business-type
- **Title**: نوع آگهی‌دهنده
- **Type**: object
- **Queries**: 
  - all -> همه
  - personal -> شخصی
  - marketplace -> فروشگاه

### has-photo
- **Title**: فقط عکس‌دار
- **Type**: boolean

### price
- **Title**: قیمت
- **Type**: object
 - **Minimum**: 0
 - **Maximum**: N/A

### sort
- **Title**: ترتیب نمایش آگهی‌ها براساس
- **Type**: object
- **Queries**: 
  - quality_and_sort_date -> quality_and_sort_date
  - sort_date -> sort_date
  - cheapest -> cheapest
  - most_expensive -> most_expensive
  - production_year -> production_year
  - usage -> usage
  - most_popular -> most_popular
  - most_relevant -> most_relevant

### status
- **Title**: وضعیت کالا
- **Type**: object
 - **Items Type**: array
- **Queries**: 
  - new -> نو
  - like-new -> در حد نو
  - used -> کارکرده
  - repair-needed -> نیازمند تعمیر

### urgent
- **Title**: فقط فوری‌ها
- **Type**: boolean



---

### Category: desktops



### category
- **Title**: دسته‌بندی
- **Type**: object

### divider
- **Title**: سایر فیلتر‌ها
- **Type**: object

### exchange
- **Title**: نمایش معاوضه‌ها
- **Type**: object
- **Queries**: 
  - only-exchanges -> نمایش فقط معاوضه‌ها
  - exclude-exchanges -> حذف معاوضه‌ها

### goods-business-type
- **Title**: نوع آگهی‌دهنده
- **Type**: object
- **Queries**: 
  - all -> همه
  - personal -> شخصی
  - marketplace -> فروشگاه

### has-photo
- **Title**: فقط عکس‌دار
- **Type**: boolean

### price
- **Title**: قیمت
- **Type**: object
 - **Minimum**: 0
 - **Maximum**: N/A

### sort
- **Title**: ترتیب نمایش آگهی‌ها براساس
- **Type**: object
- **Queries**: 
  - quality_and_sort_date -> quality_and_sort_date
  - sort_date -> sort_date
  - cheapest -> cheapest
  - most_expensive -> most_expensive
  - production_year -> production_year
  - usage -> usage
  - most_popular -> most_popular
  - most_relevant -> most_relevant

### status
- **Title**: وضعیت کالا
- **Type**: object
 - **Items Type**: array
- **Queries**: 
  - new -> نو
  - like-new -> در حد نو
  - used -> کارکرده
  - repair-needed -> نیازمند تعمیر

### urgent
- **Title**: فقط فوری‌ها
- **Type**: boolean



---

### Category: detergent-tissue



### category
- **Title**: دسته‌بندی
- **Type**: object

### divider
- **Title**: سایر فیلتر‌ها
- **Type**: object

### exchange
- **Title**: نمایش معاوضه‌ها
- **Type**: object
- **Queries**: 
  - only-exchanges -> نمایش فقط معاوضه‌ها
  - exclude-exchanges -> حذف معاوضه‌ها

### goods-business-type
- **Title**: نوع آگهی‌دهنده
- **Type**: object
- **Queries**: 
  - all -> همه
  - personal -> شخصی
  - marketplace -> فروشگاه

### has-photo
- **Title**: فقط عکس‌دار
- **Type**: boolean

### price
- **Title**: قیمت
- **Type**: object
 - **Minimum**: 0
 - **Maximum**: N/A

### sort
- **Title**: ترتیب نمایش آگهی‌ها براساس
- **Type**: object
- **Queries**: 
  - quality_and_sort_date -> quality_and_sort_date
  - sort_date -> sort_date
  - cheapest -> cheapest
  - most_expensive -> most_expensive
  - production_year -> production_year
  - usage -> usage
  - most_popular -> most_popular
  - most_relevant -> most_relevant

### status
- **Title**: وضعیت کالا
- **Type**: object
 - **Items Type**: array
- **Queries**: 
  - new -> نو
  - like-new -> در حد نو
  - used -> کارکرده
  - repair-needed -> نیازمند تعمیر

### urgent
- **Title**: فقط فوری‌ها
- **Type**: boolean



---

### Category: dining-table



### category
- **Title**: دسته‌بندی
- **Type**: object

### divider
- **Title**: سایر فیلتر‌ها
- **Type**: object

### exchange
- **Title**: نمایش معاوضه‌ها
- **Type**: object
- **Queries**: 
  - only-exchanges -> نمایش فقط معاوضه‌ها
  - exclude-exchanges -> حذف معاوضه‌ها

### goods-business-type
- **Title**: نوع آگهی‌دهنده
- **Type**: object
- **Queries**: 
  - all -> همه
  - personal -> شخصی
  - marketplace -> فروشگاه

### has-photo
- **Title**: فقط عکس‌دار
- **Type**: boolean

### price
- **Title**: قیمت
- **Type**: object
 - **Minimum**: 0
 - **Maximum**: N/A

### sort
- **Title**: ترتیب نمایش آگهی‌ها براساس
- **Type**: object
- **Queries**: 
  - quality_and_sort_date -> quality_and_sort_date
  - sort_date -> sort_date
  - cheapest -> cheapest
  - most_expensive -> most_expensive
  - production_year -> production_year
  - usage -> usage
  - most_popular -> most_popular
  - most_relevant -> most_relevant

### status
- **Title**: وضعیت کالا
- **Type**: object
 - **Items Type**: array
- **Queries**: 
  - new -> نو
  - like-new -> در حد نو
  - used -> کارکرده
  - repair-needed -> نیازمند تعمیر

### urgent
- **Title**: فقط فوری‌ها
- **Type**: boolean



---

### Category: dishwasher



### brands
- **Title**: سازنده
- **Type**: object
 - **Items Type**: array
- **Queries**: 
  - آ ا گ -> آ ا گ
  - آروما -> آروما
  - آریستون -> آریستون
  - اسمگ -> اسمگ
  - اسنوا -> اسنوا
  - اکسپریال -> اکسپریال
  - ال جی -> ال جی
  - الگانس -> الگانس
  - ایندزیت -> ایندزیت
  - برتینو -> برتینو
  - بکو -> بکو
  - بلومبرگ -> بلومبرگ
  - بهی -> بهی
  - بوش -> بوش
  - پاکشوما -> پاکشوما
  - تکنوگاز -> تکنوگاز
  - جنرال آدمیرال -> جنرال آدمیرال
  - جنرال هاوس -> جنرال هاوس
  - دکستر -> دکستر
  - ریتون -> ریتون
  - زانوسی -> زانوسی
  - زیرووات -> زیرووات
  - زیمنس -> زیمنس
  - سام -> سام
  - سامسونگ -> سامسونگ
  - سپهر الکتریک -> سپهر الکتریک
  - سینجر -> سینجر
  - شارپ -> شارپ
  - فاستر -> فاستر
  - کرال -> کرال
  - کروپ -> کروپ
  - کندی -> کندی
  - کنوود -> کنوود
  - لوفرا -> لوفرا
  - مایدیا -> مایدیا
  - مجیک -> مجیک
  - هاردستون -> هاردستون
  - وستل -> وستل
  - ویرپول -> ویرپول
  - غیره -> غیره

### category
- **Title**: دسته‌بندی
- **Type**: object

### divider
- **Title**: سایر فیلتر‌ها
- **Type**: object

### exchange
- **Title**: نمایش معاوضه‌ها
- **Type**: object
- **Queries**: 
  - only-exchanges -> نمایش فقط معاوضه‌ها
  - exclude-exchanges -> حذف معاوضه‌ها

### goods-business-type
- **Title**: نوع آگهی‌دهنده
- **Type**: object
- **Queries**: 
  - all -> همه
  - personal -> شخصی
  - marketplace -> فروشگاه

### has-photo
- **Title**: فقط عکس‌دار
- **Type**: boolean

### price
- **Title**: قیمت
- **Type**: object
 - **Minimum**: 0
 - **Maximum**: N/A

### sort
- **Title**: ترتیب نمایش آگهی‌ها براساس
- **Type**: object
- **Queries**: 
  - quality_and_sort_date -> quality_and_sort_date
  - sort_date -> sort_date
  - cheapest -> cheapest
  - most_expensive -> most_expensive
  - production_year -> production_year
  - usage -> usage
  - most_popular -> most_popular
  - most_relevant -> most_relevant

### status
- **Title**: وضعیت کالا
- **Type**: object
 - **Items Type**: array
- **Queries**: 
  - new -> نو
  - like-new -> در حد نو
  - used -> کارکرده
  - repair-needed -> نیازمند تعمیر

### urgent
- **Title**: فقط فوری‌ها
- **Type**: boolean



---

### Category: diving-watersports



### category
- **Title**: دسته‌بندی
- **Type**: object

### divider
- **Title**: سایر فیلتر‌ها
- **Type**: object

### exchange
- **Title**: نمایش معاوضه‌ها
- **Type**: object
- **Queries**: 
  - only-exchanges -> نمایش فقط معاوضه‌ها
  - exclude-exchanges -> حذف معاوضه‌ها

### goods-business-type
- **Title**: نوع آگهی‌دهنده
- **Type**: object
- **Queries**: 
  - all -> همه
  - personal -> شخصی
  - marketplace -> فروشگاه

### has-photo
- **Title**: فقط عکس‌دار
- **Type**: boolean

### price
- **Title**: قیمت
- **Type**: object
 - **Minimum**: 0
 - **Maximum**: N/A

### sort
- **Title**: ترتیب نمایش آگهی‌ها براساس
- **Type**: object
- **Queries**: 
  - quality_and_sort_date -> quality_and_sort_date
  - sort_date -> sort_date
  - cheapest -> cheapest
  - most_expensive -> most_expensive
  - production_year -> production_year
  - usage -> usage
  - most_popular -> most_popular
  - most_relevant -> most_relevant

### status
- **Title**: وضعیت کالا
- **Type**: object
 - **Items Type**: array
- **Queries**: 
  - new -> نو
  - like-new -> در حد نو
  - used -> کارکرده
  - repair-needed -> نیازمند تعمیر

### urgent
- **Title**: فقط فوری‌ها
- **Type**: boolean



---

### Category: dog



### category
- **Title**: دسته‌بندی
- **Type**: object

### divider
- **Title**: سایر فیلتر‌ها
- **Type**: object

### has-photo
- **Title**: فقط عکس‌دار
- **Type**: boolean

### sort
- **Title**: ترتیب نمایش آگهی‌ها براساس
- **Type**: object
- **Queries**: 
  - quality_and_sort_date -> quality_and_sort_date
  - sort_date -> sort_date
  - cheapest -> cheapest
  - most_expensive -> most_expensive
  - production_year -> production_year
  - usage -> usage
  - most_popular -> most_popular
  - most_relevant -> most_relevant

### urgent
- **Title**: فقط فوری‌ها
- **Type**: boolean



---

### Category: drink-maker



### category
- **Title**: دسته‌بندی
- **Type**: object

### divider
- **Title**: سایر فیلتر‌ها
- **Type**: object

### exchange
- **Title**: نمایش معاوضه‌ها
- **Type**: object
- **Queries**: 
  - only-exchanges -> نمایش فقط معاوضه‌ها
  - exclude-exchanges -> حذف معاوضه‌ها

### goods-business-type
- **Title**: نوع آگهی‌دهنده
- **Type**: object
- **Queries**: 
  - all -> همه
  - personal -> شخصی
  - marketplace -> فروشگاه

### has-photo
- **Title**: فقط عکس‌دار
- **Type**: boolean

### price
- **Title**: قیمت
- **Type**: object
 - **Minimum**: 0
 - **Maximum**: N/A

### sort
- **Title**: ترتیب نمایش آگهی‌ها براساس
- **Type**: object
- **Queries**: 
  - quality_and_sort_date -> quality_and_sort_date
  - sort_date -> sort_date
  - cheapest -> cheapest
  - most_expensive -> most_expensive
  - production_year -> production_year
  - usage -> usage
  - most_popular -> most_popular
  - most_relevant -> most_relevant

### status
- **Title**: وضعیت کالا
- **Type**: object
 - **Items Type**: array
- **Queries**: 
  - new -> نو
  - like-new -> در حد نو
  - used -> کارکرده
  - repair-needed -> نیازمند تعمیر

### urgent
- **Title**: فقط فوری‌ها
- **Type**: boolean



---

### Category: drums-percussion



### category
- **Title**: دسته‌بندی
- **Type**: object

### divider
- **Title**: سایر فیلتر‌ها
- **Type**: object

### exchange
- **Title**: نمایش معاوضه‌ها
- **Type**: object
- **Queries**: 
  - only-exchanges -> نمایش فقط معاوضه‌ها
  - exclude-exchanges -> حذف معاوضه‌ها

### goods-business-type
- **Title**: نوع آگهی‌دهنده
- **Type**: object
- **Queries**: 
  - all -> همه
  - personal -> شخصی
  - marketplace -> فروشگاه

### has-photo
- **Title**: فقط عکس‌دار
- **Type**: boolean

### price
- **Title**: قیمت
- **Type**: object
 - **Minimum**: 0
 - **Maximum**: N/A

### sort
- **Title**: ترتیب نمایش آگهی‌ها براساس
- **Type**: object
- **Queries**: 
  - quality_and_sort_date -> quality_and_sort_date
  - sort_date -> sort_date
  - cheapest -> cheapest
  - most_expensive -> most_expensive
  - production_year -> production_year
  - usage -> usage
  - most_popular -> most_popular
  - most_relevant -> most_relevant

### status
- **Title**: وضعیت کالا
- **Type**: object
 - **Items Type**: array
- **Queries**: 
  - new -> نو
  - like-new -> در حد نو
  - used -> کارکرده
  - repair-needed -> نیازمند تعمیر

### urgent
- **Title**: فقط فوری‌ها
- **Type**: boolean



---

### Category: education



### category
- **Title**: دسته‌بندی
- **Type**: object

### divider
- **Title**: سایر فیلتر‌ها
- **Type**: object

### employee_gender
- **Title**: جنسیت کارجو
- **Type**: object
- **Queries**: 
  - female -> زن
  - male -> مرد
  - neutral -> فرقی ندارد

### experience
- **Title**: سابقهٔ مورد نیاز
- **Type**: object
 - **Minimum**: N/A
 - **Maximum**: N/A

### has-photo
- **Title**: فقط عکس‌دار
- **Type**: boolean

### health_insurance
- **Title**: با بیمه
- **Type**: boolean

### job_type
- **Title**: نوع همکاری
- **Type**: object
 - **Items Type**: array
- **Queries**: 
  - full_time -> تمام وقت
  - part_time -> پاره وقت
  - contract -> پیمان‌کاری/پروژه‌ای
  - internship -> کارآموزی
  - adaptive -> توافقی
  - other -> سایر

### military_service_status
- **Title**: پایان خدمت/معافیت
- **Type**: object
- **Queries**: 
  - finish_or_exemption_required -> الزامی
  - finish_not_required -> اختیاری

### no_experience_required
- **Title**: بدون نیاز به سابقه
- **Type**: boolean

### payment_method
- **Title**: شیوهٔ پرداخت
- **Type**: object
 - **Items Type**: array
- **Queries**: 
  - monthly -> ماهانه
  - daily -> روزانه
  - hourly -> ساعتی
  - percentage_commission -> پورسانتی/درصدی
  - adaptive -> توافقی
  - other -> سایر

### remote
- **Title**: با امکان دورکاری
- **Type**: boolean

### sort
- **Title**: ترتیب نمایش آگهی‌ها براساس
- **Type**: object
- **Queries**: 
  - quality_and_sort_date -> quality_and_sort_date
  - sort_date -> sort_date
  - cheapest -> cheapest
  - most_expensive -> most_expensive
  - production_year -> production_year
  - usage -> usage
  - most_popular -> most_popular
  - most_relevant -> most_relevant

### urgent
- **Title**: فقط فوری‌ها
- **Type**: boolean



---

### Category: educational



### category
- **Title**: دسته‌بندی
- **Type**: object

### divider
- **Title**: سایر فیلتر‌ها
- **Type**: object

### exchange
- **Title**: نمایش معاوضه‌ها
- **Type**: object
- **Queries**: 
  - only-exchanges -> نمایش فقط معاوضه‌ها
  - exclude-exchanges -> حذف معاوضه‌ها

### goods-business-type
- **Title**: نوع آگهی‌دهنده
- **Type**: object
- **Queries**: 
  - all -> همه
  - personal -> شخصی
  - marketplace -> فروشگاه

### has-photo
- **Title**: فقط عکس‌دار
- **Type**: boolean

### price
- **Title**: قیمت
- **Type**: object
 - **Minimum**: 0
 - **Maximum**: N/A

### sort
- **Title**: ترتیب نمایش آگهی‌ها براساس
- **Type**: object
- **Queries**: 
  - quality_and_sort_date -> quality_and_sort_date
  - sort_date -> sort_date
  - cheapest -> cheapest
  - most_expensive -> most_expensive
  - production_year -> production_year
  - usage -> usage
  - most_popular -> most_popular
  - most_relevant -> most_relevant

### status
- **Title**: وضعیت کالا
- **Type**: object
 - **Items Type**: array
- **Queries**: 
  - new -> نو
  - like-new -> در حد نو
  - used -> کارکرده
  - repair-needed -> نیازمند تعمیر

### urgent
- **Title**: فقط فوری‌ها
- **Type**: boolean



---

### Category: electronic-devices



### category
- **Title**: دسته‌بندی
- **Type**: object

### divider
- **Title**: سایر فیلتر‌ها
- **Type**: object

### exchange
- **Title**: نمایش معاوضه‌ها
- **Type**: object
- **Queries**: 
  - only-exchanges -> نمایش فقط معاوضه‌ها
  - exclude-exchanges -> حذف معاوضه‌ها

### goods-business-type
- **Title**: نوع آگهی‌دهنده
- **Type**: object
- **Queries**: 
  - all -> همه
  - personal -> شخصی
  - marketplace -> فروشگاه

### has-photo
- **Title**: فقط عکس‌دار
- **Type**: boolean

### price
- **Title**: قیمت
- **Type**: object
 - **Minimum**: 0
 - **Maximum**: N/A

### sort
- **Title**: ترتیب نمایش آگهی‌ها براساس
- **Type**: object
- **Queries**: 
  - quality_and_sort_date -> quality_and_sort_date
  - sort_date -> sort_date
  - cheapest -> cheapest
  - most_expensive -> most_expensive
  - production_year -> production_year
  - usage -> usage
  - most_popular -> most_popular
  - most_relevant -> most_relevant

### status
- **Title**: وضعیت کالا
- **Type**: object
 - **Items Type**: array
- **Queries**: 
  - new -> نو
  - like-new -> در حد نو
  - used -> کارکرده
  - repair-needed -> نیازمند تعمیر

### urgent
- **Title**: فقط فوری‌ها
- **Type**: boolean



---

### Category: event



### category
- **Title**: دسته‌بندی
- **Type**: object

### exchange
- **Title**: نمایش معاوضه‌ها
- **Type**: object
- **Queries**: 
  - only-exchanges -> نمایش فقط معاوضه‌ها
  - exclude-exchanges -> حذف معاوضه‌ها

### has-photo
- **Title**: فقط عکس‌دار
- **Type**: boolean

### non-negotiable
- **Title**: حذف توافقی‌ها
- **Type**: boolean

### price
- **Title**: قیمت
- **Type**: object
 - **Minimum**: 0
 - **Maximum**: N/A

### sort
- **Title**: ترتیب نمایش آگهی‌ها براساس
- **Type**: object
- **Queries**: 
  - quality_and_sort_date -> quality_and_sort_date
  - sort_date -> sort_date
  - cheapest -> cheapest
  - most_expensive -> most_expensive
  - production_year -> production_year
  - usage -> usage
  - most_popular -> most_popular
  - most_relevant -> most_relevant

### urgent
- **Title**: فقط فوری‌ها
- **Type**: boolean



---

### Category: events-sports



### category
- **Title**: دسته‌بندی
- **Type**: object

### divider
- **Title**: سایر فیلتر‌ها
- **Type**: object

### exchange
- **Title**: نمایش معاوضه‌ها
- **Type**: object
- **Queries**: 
  - only-exchanges -> نمایش فقط معاوضه‌ها
  - exclude-exchanges -> حذف معاوضه‌ها

### has-photo
- **Title**: فقط عکس‌دار
- **Type**: boolean

### non-negotiable
- **Title**: حذف توافقی‌ها
- **Type**: boolean

### price
- **Title**: قیمت
- **Type**: object
 - **Minimum**: 0
 - **Maximum**: N/A

### sort
- **Title**: ترتیب نمایش آگهی‌ها براساس
- **Type**: object
- **Queries**: 
  - quality_and_sort_date -> quality_and_sort_date
  - sort_date -> sort_date
  - cheapest -> cheapest
  - most_expensive -> most_expensive
  - production_year -> production_year
  - usage -> usage
  - most_popular -> most_popular
  - most_relevant -> most_relevant

### urgent
- **Title**: فقط فوری‌ها
- **Type**: boolean



---

### Category: fan-ventilator-humidifier



### category
- **Title**: دسته‌بندی
- **Type**: object

### divider
- **Title**: سایر فیلتر‌ها
- **Type**: object

### exchange
- **Title**: نمایش معاوضه‌ها
- **Type**: object
- **Queries**: 
  - only-exchanges -> نمایش فقط معاوضه‌ها
  - exclude-exchanges -> حذف معاوضه‌ها

### goods-business-type
- **Title**: نوع آگهی‌دهنده
- **Type**: object
- **Queries**: 
  - all -> همه
  - personal -> شخصی
  - marketplace -> فروشگاه

### has-photo
- **Title**: فقط عکس‌دار
- **Type**: boolean

### price
- **Title**: قیمت
- **Type**: object
 - **Minimum**: 0
 - **Maximum**: N/A

### sort
- **Title**: ترتیب نمایش آگهی‌ها براساس
- **Type**: object
- **Queries**: 
  - quality_and_sort_date -> quality_and_sort_date
  - sort_date -> sort_date
  - cheapest -> cheapest
  - most_expensive -> most_expensive
  - production_year -> production_year
  - usage -> usage
  - most_popular -> most_popular
  - most_relevant -> most_relevant

### status
- **Title**: وضعیت کالا
- **Type**: object
 - **Items Type**: array
- **Queries**: 
  - new -> نو
  - like-new -> در حد نو
  - used -> کارکرده
  - repair-needed -> نیازمند تعمیر

### urgent
- **Title**: فقط فوری‌ها
- **Type**: boolean



---

### Category: farm-animals



### category
- **Title**: دسته‌بندی
- **Type**: object

### divider
- **Title**: سایر فیلتر‌ها
- **Type**: object

### exchange
- **Title**: نمایش معاوضه‌ها
- **Type**: object
- **Queries**: 
  - only-exchanges -> نمایش فقط معاوضه‌ها
  - exclude-exchanges -> حذف معاوضه‌ها

### has-photo
- **Title**: فقط عکس‌دار
- **Type**: boolean

### price
- **Title**: قیمت
- **Type**: object
 - **Minimum**: 0
 - **Maximum**: N/A

### sort
- **Title**: ترتیب نمایش آگهی‌ها براساس
- **Type**: object
- **Queries**: 
  - quality_and_sort_date -> quality_and_sort_date
  - sort_date -> sort_date
  - cheapest -> cheapest
  - most_expensive -> most_expensive
  - production_year -> production_year
  - usage -> usage
  - most_popular -> most_popular
  - most_relevant -> most_relevant

### urgent
- **Title**: فقط فوری‌ها
- **Type**: boolean



---

### Category: figurines



### category
- **Title**: دسته‌بندی
- **Type**: object

### divider
- **Title**: سایر فیلتر‌ها
- **Type**: object

### exchange
- **Title**: نمایش معاوضه‌ها
- **Type**: object
- **Queries**: 
  - only-exchanges -> نمایش فقط معاوضه‌ها
  - exclude-exchanges -> حذف معاوضه‌ها

### goods-business-type
- **Title**: نوع آگهی‌دهنده
- **Type**: object
- **Queries**: 
  - all -> همه
  - personal -> شخصی
  - marketplace -> فروشگاه

### has-photo
- **Title**: فقط عکس‌دار
- **Type**: boolean

### price
- **Title**: قیمت
- **Type**: object
 - **Minimum**: 0
 - **Maximum**: N/A

### sort
- **Title**: ترتیب نمایش آگهی‌ها براساس
- **Type**: object
- **Queries**: 
  - quality_and_sort_date -> quality_and_sort_date
  - sort_date -> sort_date
  - cheapest -> cheapest
  - most_expensive -> most_expensive
  - production_year -> production_year
  - usage -> usage
  - most_popular -> most_popular
  - most_relevant -> most_relevant

### status
- **Title**: وضعیت کالا
- **Type**: object
 - **Items Type**: array
- **Queries**: 
  - new -> نو
  - like-new -> در حد نو
  - used -> کارکرده
  - repair-needed -> نیازمند تعمیر

### urgent
- **Title**: فقط فوری‌ها
- **Type**: boolean



---

### Category: fish



### category
- **Title**: دسته‌بندی
- **Type**: object

### divider
- **Title**: سایر فیلتر‌ها
- **Type**: object

### exchange
- **Title**: نمایش معاوضه‌ها
- **Type**: object
- **Queries**: 
  - only-exchanges -> نمایش فقط معاوضه‌ها
  - exclude-exchanges -> حذف معاوضه‌ها

### has-photo
- **Title**: فقط عکس‌دار
- **Type**: boolean

### price
- **Title**: قیمت
- **Type**: object
 - **Minimum**: 0
 - **Maximum**: N/A

### sort
- **Title**: ترتیب نمایش آگهی‌ها براساس
- **Type**: object
- **Queries**: 
  - quality_and_sort_date -> quality_and_sort_date
  - sort_date -> sort_date
  - cheapest -> cheapest
  - most_expensive -> most_expensive
  - production_year -> production_year
  - usage -> usage
  - most_popular -> most_popular
  - most_relevant -> most_relevant

### urgent
- **Title**: فقط فوری‌ها
- **Type**: boolean



---

### Category: fishing



### category
- **Title**: دسته‌بندی
- **Type**: object

### divider
- **Title**: سایر فیلتر‌ها
- **Type**: object

### exchange
- **Title**: نمایش معاوضه‌ها
- **Type**: object
- **Queries**: 
  - only-exchanges -> نمایش فقط معاوضه‌ها
  - exclude-exchanges -> حذف معاوضه‌ها

### goods-business-type
- **Title**: نوع آگهی‌دهنده
- **Type**: object
- **Queries**: 
  - all -> همه
  - personal -> شخصی
  - marketplace -> فروشگاه

### has-photo
- **Title**: فقط عکس‌دار
- **Type**: boolean

### price
- **Title**: قیمت
- **Type**: object
 - **Minimum**: 0
 - **Maximum**: N/A

### sort
- **Title**: ترتیب نمایش آگهی‌ها براساس
- **Type**: object
- **Queries**: 
  - quality_and_sort_date -> quality_and_sort_date
  - sort_date -> sort_date
  - cheapest -> cheapest
  - most_expensive -> most_expensive
  - production_year -> production_year
  - usage -> usage
  - most_popular -> most_popular
  - most_relevant -> most_relevant

### status
- **Title**: وضعیت کالا
- **Type**: object
 - **Items Type**: array
- **Queries**: 
  - new -> نو
  - like-new -> در حد نو
  - used -> کارکرده
  - repair-needed -> نیازمند تعمیر

### urgent
- **Title**: فقط فوری‌ها
- **Type**: boolean



---

### Category: food-and-drink



### category
- **Title**: دسته‌بندی
- **Type**: object

### divider
- **Title**: سایر فیلتر‌ها
- **Type**: object

### exchange
- **Title**: نمایش معاوضه‌ها
- **Type**: object
- **Queries**: 
  - only-exchanges -> نمایش فقط معاوضه‌ها
  - exclude-exchanges -> حذف معاوضه‌ها

### goods-business-type
- **Title**: نوع آگهی‌دهنده
- **Type**: object
- **Queries**: 
  - all -> همه
  - personal -> شخصی
  - marketplace -> فروشگاه

### has-photo
- **Title**: فقط عکس‌دار
- **Type**: boolean

### price
- **Title**: قیمت
- **Type**: object
 - **Minimum**: 0
 - **Maximum**: N/A

### sort
- **Title**: ترتیب نمایش آگهی‌ها براساس
- **Type**: object
- **Queries**: 
  - quality_and_sort_date -> quality_and_sort_date
  - sort_date -> sort_date
  - cheapest -> cheapest
  - most_expensive -> most_expensive
  - production_year -> production_year
  - usage -> usage
  - most_popular -> most_popular
  - most_relevant -> most_relevant

### status
- **Title**: وضعیت کالا
- **Type**: object
 - **Items Type**: array
- **Queries**: 
  - new -> نو
  - like-new -> در حد نو
  - used -> کارکرده
  - repair-needed -> نیازمند تعمیر

### urgent
- **Title**: فقط فوری‌ها
- **Type**: boolean



---

### Category: food-mill



### category
- **Title**: دسته‌بندی
- **Type**: object

### divider
- **Title**: سایر فیلتر‌ها
- **Type**: object

### exchange
- **Title**: نمایش معاوضه‌ها
- **Type**: object
- **Queries**: 
  - only-exchanges -> نمایش فقط معاوضه‌ها
  - exclude-exchanges -> حذف معاوضه‌ها

### goods-business-type
- **Title**: نوع آگهی‌دهنده
- **Type**: object
- **Queries**: 
  - all -> همه
  - personal -> شخصی
  - marketplace -> فروشگاه

### has-photo
- **Title**: فقط عکس‌دار
- **Type**: boolean

### price
- **Title**: قیمت
- **Type**: object
 - **Minimum**: 0
 - **Maximum**: N/A

### sort
- **Title**: ترتیب نمایش آگهی‌ها براساس
- **Type**: object
- **Queries**: 
  - quality_and_sort_date -> quality_and_sort_date
  - sort_date -> sort_date
  - cheapest -> cheapest
  - most_expensive -> most_expensive
  - production_year -> production_year
  - usage -> usage
  - most_popular -> most_popular
  - most_relevant -> most_relevant

### status
- **Title**: وضعیت کالا
- **Type**: object
 - **Items Type**: array
- **Queries**: 
  - new -> نو
  - like-new -> در حد نو
  - used -> کارکرده
  - repair-needed -> نیازمند تعمیر

### urgent
- **Title**: فقط فوری‌ها
- **Type**: boolean



---

### Category: for-sale



### category
- **Title**: دسته‌بندی
- **Type**: object

### divider
- **Title**: سایر فیلتر‌ها
- **Type**: object

### exchange
- **Title**: نمایش معاوضه‌ها
- **Type**: object
- **Queries**: 
  - only-exchanges -> نمایش فقط معاوضه‌ها
  - exclude-exchanges -> حذف معاوضه‌ها

### has-photo
- **Title**: فقط عکس‌دار
- **Type**: boolean

### non-negotiable
- **Title**: حذف توافقی‌ها
- **Type**: boolean

### price
- **Title**: قیمت
- **Type**: object
 - **Minimum**: 0
 - **Maximum**: N/A

### sort
- **Title**: ترتیب نمایش آگهی‌ها براساس
- **Type**: object
- **Queries**: 
  - quality_and_sort_date -> quality_and_sort_date
  - sort_date -> sort_date
  - cheapest -> cheapest
  - most_expensive -> most_expensive
  - production_year -> production_year
  - usage -> usage
  - most_popular -> most_popular
  - most_relevant -> most_relevant

### urgent
- **Title**: فقط فوری‌ها
- **Type**: boolean



---

### Category: furniture



### category
- **Title**: دسته‌بندی
- **Type**: object

### divider
- **Title**: سایر فیلتر‌ها
- **Type**: object

### exchange
- **Title**: نمایش معاوضه‌ها
- **Type**: object
- **Queries**: 
  - only-exchanges -> نمایش فقط معاوضه‌ها
  - exclude-exchanges -> حذف معاوضه‌ها

### goods-business-type
- **Title**: نوع آگهی‌دهنده
- **Type**: object
- **Queries**: 
  - all -> همه
  - personal -> شخصی
  - marketplace -> فروشگاه

### has-guarantee
- **Title**: دارای ضمانت
- **Type**: boolean

### has-photo
- **Title**: فقط عکس‌دار
- **Type**: boolean

### merchandise-type
- **Title**: نوع کالا
- **Type**: object
- **Queries**: 
  - sofa -> مبلمان
  - coffee-table -> جلو مبلی و عسلی

### price
- **Title**: قیمت
- **Type**: object
 - **Minimum**: 0
 - **Maximum**: N/A

### sort
- **Title**: ترتیب نمایش آگهی‌ها براساس
- **Type**: object
- **Queries**: 
  - quality_and_sort_date -> quality_and_sort_date
  - sort_date -> sort_date
  - cheapest -> cheapest
  - most_expensive -> most_expensive
  - production_year -> production_year
  - usage -> usage
  - most_popular -> most_popular
  - most_relevant -> most_relevant

### status
- **Title**: وضعیت کالا
- **Type**: object
 - **Items Type**: array
- **Queries**: 
  - new -> نو
  - like-new -> در حد نو
  - used -> کارکرده
  - repair-needed -> نیازمند تعمیر

### urgent
- **Title**: فقط فوری‌ها
- **Type**: boolean



---

### Category: furniture-wood



### category
- **Title**: دسته‌بندی
- **Type**: object

### divider
- **Title**: سایر فیلتر‌ها
- **Type**: object

### exchange
- **Title**: نمایش معاوضه‌ها
- **Type**: object
- **Queries**: 
  - only-exchanges -> نمایش فقط معاوضه‌ها
  - exclude-exchanges -> حذف معاوضه‌ها

### goods-business-type
- **Title**: نوع آگهی‌دهنده
- **Type**: object
- **Queries**: 
  - all -> همه
  - personal -> شخصی
  - marketplace -> فروشگاه

### has-photo
- **Title**: فقط عکس‌دار
- **Type**: boolean

### price
- **Title**: قیمت
- **Type**: object
 - **Minimum**: 0
 - **Maximum**: N/A

### sort
- **Title**: ترتیب نمایش آگهی‌ها براساس
- **Type**: object
- **Queries**: 
  - quality_and_sort_date -> quality_and_sort_date
  - sort_date -> sort_date
  - cheapest -> cheapest
  - most_expensive -> most_expensive
  - production_year -> production_year
  - usage -> usage
  - most_popular -> most_popular
  - most_relevant -> most_relevant

### status
- **Title**: وضعیت کالا
- **Type**: object
 - **Items Type**: array
- **Queries**: 
  - new -> نو
  - like-new -> در حد نو
  - used -> کارکرده
  - repair-needed -> نیازمند تعمیر

### urgent
- **Title**: فقط فوری‌ها
- **Type**: boolean



---

### Category: game-consoles-and-video-games



### accessory_type
- **Title**: تجهیزات بازی
- **Type**: object
 - **Items Type**: array
- **Queries**: 
  - cover-and-shield -> کاور، قاب و محافظ
  - vr-glasses -> عینک واقعیت مجازی
  - steering-wheel -> فرمان بازی
  - others -> سایر

### category
- **Title**: دسته‌بندی
- **Type**: object

### divider
- **Title**: سایر فیلتر‌ها
- **Type**: object

### exchange
- **Title**: نمایش معاوضه‌ها
- **Type**: object
- **Queries**: 
  - only-exchanges -> نمایش فقط معاوضه‌ها
  - exclude-exchanges -> حذف معاوضه‌ها

### gaming_controller_quantity
- **Title**: تعداد دستهٔ همراه
- **Type**: object
- **Queries**: 
  - 0-controller -> بدون دسته
  - 1-controller -> ۱ دسته
  - 2-controllers -> ۲ دسته
  - +2-controllers -> بیشتر از ۲ دسته

### gaming_controller_type
- **Title**: نوع دسته
- **Type**: object
- **Queries**: 
  - console-controller -> دستهٔ کنسول
  - pc-controller -> دستهٔ کامپیوتر

### goods-business-type
- **Title**: نوع آگهی‌دهنده
- **Type**: object
- **Queries**: 
  - all -> همه
  - personal -> شخصی
  - marketplace -> فروشگاه

### has-photo
- **Title**: فقط عکس‌دار
- **Type**: boolean

### model
- **Title**: مدل کنسول
- **Type**: object
 - **Items Type**: array
- **Queries**: 
  - playstation1 -> PlayStation 1
  - playstation2 -> PlayStation 2
  - playstation3 -> PlayStation 3
  - playstation4 -> PlayStation 4
  - playstation5 -> PlayStation 5
  - xbox360 -> Xbox 360
  - xbox-one -> Xbox One
  - xbox-one-s -> Xbox One S
  - xbox-one-x -> Xbox One X
  - xbox-series-s -> Xbox Series S
  - xbox-series-x -> Xbox Series X
  - switch-lite -> Switch Lite
  - switch-normal -> Switch Normal
  - switch-oled -> Switch OLED
  - wii-u -> Wii U
  - others -> سایر

### price
- **Title**: قیمت
- **Type**: object
 - **Minimum**: 0
 - **Maximum**: N/A

### sort
- **Title**: ترتیب نمایش آگهی‌ها براساس
- **Type**: object
- **Queries**: 
  - quality_and_sort_date -> quality_and_sort_date
  - sort_date -> sort_date
  - cheapest -> cheapest
  - most_expensive -> most_expensive
  - production_year -> production_year
  - usage -> usage
  - most_popular -> most_popular
  - most_relevant -> most_relevant

### status
- **Title**: وضعیت کالا
- **Type**: object
 - **Items Type**: array
- **Queries**: 
  - new -> نو
  - like-new -> در حد نو
  - used -> کارکرده
  - repair-needed -> نیازمند تعمیر

### urgent
- **Title**: فقط فوری‌ها
- **Type**: boolean



---

### Category: garden-and-landscaping



### category
- **Title**: دسته‌بندی
- **Type**: object

### expertises
- **Title**: تخصص
- **Type**: object
 - **Items Type**: array
- **Queries**: 
  - ROOT -> همه تخصص‌ها
  - planting-maintaining-plants -> کاشت و نگهداری گیاهان
  - plowing -> شخم زنی
  - planting-flowers -> کاشت گل و گیاه
  - plant-spraying -> سمپاشی گیاه
  - prune -> هرس کردن
  - fertilizing -> کوددهی و تعویض خاک
  - land-irrigation -> آبیاری زمین
  - gardening-others -> سایر باغبانی و درختکاری

### has-photo
- **Title**: فقط عکس‌دار
- **Type**: boolean

### sort
- **Title**: ترتیب نمایش آگهی‌ها براساس
- **Type**: object
- **Queries**: 
  - quality_and_sort_date -> quality_and_sort_date
  - sort_date -> sort_date
  - cheapest -> cheapest
  - most_expensive -> most_expensive
  - production_year -> production_year
  - usage -> usage
  - most_popular -> most_popular
  - most_relevant -> most_relevant

### urgent
- **Title**: فقط فوری‌ها
- **Type**: boolean



---

### Category: gift-certificate



### category
- **Title**: دسته‌بندی
- **Type**: object

### divider
- **Title**: سایر فیلتر‌ها
- **Type**: object

### exchange
- **Title**: نمایش معاوضه‌ها
- **Type**: object
- **Queries**: 
  - only-exchanges -> نمایش فقط معاوضه‌ها
  - exclude-exchanges -> حذف معاوضه‌ها

### has-photo
- **Title**: فقط عکس‌دار
- **Type**: boolean

### price
- **Title**: قیمت
- **Type**: object
 - **Minimum**: 0
 - **Maximum**: N/A

### sort
- **Title**: ترتیب نمایش آگهی‌ها براساس
- **Type**: object
- **Queries**: 
  - quality_and_sort_date -> quality_and_sort_date
  - sort_date -> sort_date
  - cheapest -> cheapest
  - most_expensive -> most_expensive
  - production_year -> production_year
  - usage -> usage
  - most_popular -> most_popular
  - most_relevant -> most_relevant

### urgent
- **Title**: فقط فوری‌ها
- **Type**: boolean



---

### Category: guitar-bass-amplifier



### category
- **Title**: دسته‌بندی
- **Type**: object

### divider
- **Title**: سایر فیلتر‌ها
- **Type**: object

### exchange
- **Title**: نمایش معاوضه‌ها
- **Type**: object
- **Queries**: 
  - only-exchanges -> نمایش فقط معاوضه‌ها
  - exclude-exchanges -> حذف معاوضه‌ها

### goods-business-type
- **Title**: نوع آگهی‌دهنده
- **Type**: object
- **Queries**: 
  - all -> همه
  - personal -> شخصی
  - marketplace -> فروشگاه

### has-photo
- **Title**: فقط عکس‌دار
- **Type**: boolean

### price
- **Title**: قیمت
- **Type**: object
 - **Minimum**: 0
 - **Maximum**: N/A

### sort
- **Title**: ترتیب نمایش آگهی‌ها براساس
- **Type**: object
- **Queries**: 
  - quality_and_sort_date -> quality_and_sort_date
  - sort_date -> sort_date
  - cheapest -> cheapest
  - most_expensive -> most_expensive
  - production_year -> production_year
  - usage -> usage
  - most_popular -> most_popular
  - most_relevant -> most_relevant

### status
- **Title**: وضعیت کالا
- **Type**: object
 - **Items Type**: array
- **Queries**: 
  - new -> نو
  - like-new -> در حد نو
  - used -> کارکرده
  - repair-needed -> نیازمند تعمیر

### urgent
- **Title**: فقط فوری‌ها
- **Type**: boolean



---

### Category: health-beauty



### category
- **Title**: دسته‌بندی
- **Type**: object

### divider
- **Title**: سایر فیلتر‌ها
- **Type**: object

### exchange
- **Title**: نمایش معاوضه‌ها
- **Type**: object
- **Queries**: 
  - only-exchanges -> نمایش فقط معاوضه‌ها
  - exclude-exchanges -> حذف معاوضه‌ها

### goods-business-type
- **Title**: نوع آگهی‌دهنده
- **Type**: object
- **Queries**: 
  - all -> همه
  - personal -> شخصی
  - marketplace -> فروشگاه

### has-photo
- **Title**: فقط عکس‌دار
- **Type**: boolean

### merchandise-type
- **Title**: نوع کالا
- **Type**: object
 - **Items Type**: array
- **Queries**: 
  - لوازم آرایشی و زیبایی -> لوازم آرایشی و زیبایی
  - لوازم طبی و درمانی -> لوازم طبی و درمانی
  - لوازم برقی شخصی -> لوازم برقی شخصی
  - مراقبتی پوست و مو -> مراقبتی پوست و مو
  - عطر و ادکلن -> عطر و ادکلن
  - قرص و ترکیبات گیاهی -> قرص و ترکیبات گیاهی
  - غیره -> غیره

### price
- **Title**: قیمت
- **Type**: object
 - **Minimum**: 0
 - **Maximum**: N/A

### sort
- **Title**: ترتیب نمایش آگهی‌ها براساس
- **Type**: object
- **Queries**: 
  - quality_and_sort_date -> quality_and_sort_date
  - sort_date -> sort_date
  - cheapest -> cheapest
  - most_expensive -> most_expensive
  - production_year -> production_year
  - usage -> usage
  - most_popular -> most_popular
  - most_relevant -> most_relevant

### status
- **Title**: وضعیت کالا
- **Type**: object
 - **Items Type**: array
- **Queries**: 
  - new -> نو
  - like-new -> در حد نو
  - used -> کارکرده
  - repair-needed -> نیازمند تعمیر

### urgent
- **Title**: فقط فوری‌ها
- **Type**: boolean



---

### Category: heavy



### category
- **Title**: دسته‌بندی
- **Type**: object

### divider
- **Title**: سایر فیلتر‌ها
- **Type**: object

### exchange
- **Title**: نمایش معاوضه‌ها
- **Type**: object
- **Queries**: 
  - only-exchanges -> نمایش فقط معاوضه‌ها
  - exclude-exchanges -> حذف معاوضه‌ها

### has-photo
- **Title**: فقط عکس‌دار
- **Type**: boolean

### non-negotiable
- **Title**: حذف توافقی‌ها
- **Type**: boolean

### post-type
- **Title**: نوع آگهی
- **Type**: object
- **Queries**: 
  - فروشی -> فروشی
  - درخواستی -> درخواستی

### price
- **Title**: قیمت
- **Type**: object
 - **Minimum**: 0
 - **Maximum**: N/A

### production-year
- **Title**: مدل (سال تولید)
- **Type**: object
 - **Minimum**: 0
 - **Maximum**: N/A

### sort
- **Title**: ترتیب نمایش آگهی‌ها براساس
- **Type**: object
- **Queries**: 
  - quality_and_sort_date -> quality_and_sort_date
  - sort_date -> sort_date
  - cheapest -> cheapest
  - most_expensive -> most_expensive
  - production_year -> production_year
  - usage -> usage
  - most_popular -> most_popular
  - most_relevant -> most_relevant

### urgent
- **Title**: فقط فوری‌ها
- **Type**: boolean

### usage
- **Title**: کارکرد
- **Type**: object
 - **Minimum**: 0
 - **Maximum**: N/A

### vehicle_type
- **Title**: نوع وسیلهٔ نقلیه
- **Type**: object
- **Queries**: 
  - truck -> کامیون یا کامیونت
  - agricultural -> خودروی کشاورزی
  - bus -> اتوبوس یا مینی‌بوس
  - road-construction -> ماشین‌آلات راه‌سازی



---

### Category: historical



### category
- **Title**: دسته‌بندی
- **Type**: object

### divider
- **Title**: سایر فیلتر‌ها
- **Type**: object

### exchange
- **Title**: نمایش معاوضه‌ها
- **Type**: object
- **Queries**: 
  - only-exchanges -> نمایش فقط معاوضه‌ها
  - exclude-exchanges -> حذف معاوضه‌ها

### goods-business-type
- **Title**: نوع آگهی‌دهنده
- **Type**: object
- **Queries**: 
  - all -> همه
  - personal -> شخصی
  - marketplace -> فروشگاه

### has-photo
- **Title**: فقط عکس‌دار
- **Type**: boolean

### price
- **Title**: قیمت
- **Type**: object
 - **Minimum**: 0
 - **Maximum**: N/A

### sort
- **Title**: ترتیب نمایش آگهی‌ها براساس
- **Type**: object
- **Queries**: 
  - quality_and_sort_date -> quality_and_sort_date
  - sort_date -> sort_date
  - cheapest -> cheapest
  - most_expensive -> most_expensive
  - production_year -> production_year
  - usage -> usage
  - most_popular -> most_popular
  - most_relevant -> most_relevant

### status
- **Title**: وضعیت کالا
- **Type**: object
 - **Items Type**: array
- **Queries**: 
  - new -> نو
  - like-new -> در حد نو
  - used -> کارکرده
  - repair-needed -> نیازمند تعمیر

### urgent
- **Title**: فقط فوری‌ها
- **Type**: boolean



---

### Category: historical-objects



### category
- **Title**: دسته‌بندی
- **Type**: object

### divider
- **Title**: سایر فیلتر‌ها
- **Type**: object

### exchange
- **Title**: نمایش معاوضه‌ها
- **Type**: object
- **Queries**: 
  - only-exchanges -> نمایش فقط معاوضه‌ها
  - exclude-exchanges -> حذف معاوضه‌ها

### has-photo
- **Title**: فقط عکس‌دار
- **Type**: boolean

### price
- **Title**: قیمت
- **Type**: object
 - **Minimum**: 0
 - **Maximum**: N/A

### sort
- **Title**: ترتیب نمایش آگهی‌ها براساس
- **Type**: object
- **Queries**: 
  - quality_and_sort_date -> quality_and_sort_date
  - sort_date -> sort_date
  - cheapest -> cheapest
  - most_expensive -> most_expensive
  - production_year -> production_year
  - usage -> usage
  - most_popular -> most_popular
  - most_relevant -> most_relevant

### urgent
- **Title**: فقط فوری‌ها
- **Type**: boolean



---

### Category: hobby-collectibles



### category
- **Title**: دسته‌بندی
- **Type**: object

### divider
- **Title**: سایر فیلتر‌ها
- **Type**: object

### exchange
- **Title**: نمایش معاوضه‌ها
- **Type**: object
- **Queries**: 
  - only-exchanges -> نمایش فقط معاوضه‌ها
  - exclude-exchanges -> حذف معاوضه‌ها

### has-photo
- **Title**: فقط عکس‌دار
- **Type**: boolean

### price
- **Title**: قیمت
- **Type**: object
 - **Minimum**: 0
 - **Maximum**: N/A

### sort
- **Title**: ترتیب نمایش آگهی‌ها براساس
- **Type**: object
- **Queries**: 
  - quality_and_sort_date -> quality_and_sort_date
  - sort_date -> sort_date
  - cheapest -> cheapest
  - most_expensive -> most_expensive
  - production_year -> production_year
  - usage -> usage
  - most_popular -> most_popular
  - most_relevant -> most_relevant

### urgent
- **Title**: فقط فوری‌ها
- **Type**: boolean



---

### Category: home-catering



### category
- **Title**: دسته‌بندی
- **Type**: object

### divider
- **Title**: سایر فیلتر‌ها
- **Type**: object

### exchange
- **Title**: نمایش معاوضه‌ها
- **Type**: object
- **Queries**: 
  - only-exchanges -> نمایش فقط معاوضه‌ها
  - exclude-exchanges -> حذف معاوضه‌ها

### goods-business-type
- **Title**: نوع آگهی‌دهنده
- **Type**: object
- **Queries**: 
  - all -> همه
  - personal -> شخصی
  - marketplace -> فروشگاه

### has-photo
- **Title**: فقط عکس‌دار
- **Type**: boolean

### price
- **Title**: قیمت
- **Type**: object
 - **Minimum**: 0
 - **Maximum**: N/A

### sort
- **Title**: ترتیب نمایش آگهی‌ها براساس
- **Type**: object
- **Queries**: 
  - quality_and_sort_date -> quality_and_sort_date
  - sort_date -> sort_date
  - cheapest -> cheapest
  - most_expensive -> most_expensive
  - production_year -> production_year
  - usage -> usage
  - most_popular -> most_popular
  - most_relevant -> most_relevant

### status
- **Title**: وضعیت کالا
- **Type**: object
 - **Items Type**: array
- **Queries**: 
  - new -> نو
  - like-new -> در حد نو
  - used -> کارکرده
  - repair-needed -> نیازمند تعمیر

### urgent
- **Title**: فقط فوری‌ها
- **Type**: boolean



---

### Category: home-kitchen



### category
- **Title**: دسته‌بندی
- **Type**: object

### divider
- **Title**: سایر فیلتر‌ها
- **Type**: object

### exchange
- **Title**: نمایش معاوضه‌ها
- **Type**: object
- **Queries**: 
  - only-exchanges -> نمایش فقط معاوضه‌ها
  - exclude-exchanges -> حذف معاوضه‌ها

### goods-business-type
- **Title**: نوع آگهی‌دهنده
- **Type**: object
- **Queries**: 
  - all -> همه
  - personal -> شخصی
  - marketplace -> فروشگاه

### has-photo
- **Title**: فقط عکس‌دار
- **Type**: boolean

### price
- **Title**: قیمت
- **Type**: object
 - **Minimum**: 0
 - **Maximum**: N/A

### sort
- **Title**: ترتیب نمایش آگهی‌ها براساس
- **Type**: object
- **Queries**: 
  - quality_and_sort_date -> quality_and_sort_date
  - sort_date -> sort_date
  - cheapest -> cheapest
  - most_expensive -> most_expensive
  - production_year -> production_year
  - usage -> usage
  - most_popular -> most_popular
  - most_relevant -> most_relevant

### status
- **Title**: وضعیت کالا
- **Type**: object
 - **Items Type**: array
- **Queries**: 
  - new -> نو
  - like-new -> در حد نو
  - used -> کارکرده
  - repair-needed -> نیازمند تعمیر

### urgent
- **Title**: فقط فوری‌ها
- **Type**: boolean



---

### Category: home-lighting



### category
- **Title**: دسته‌بندی
- **Type**: object

### divider
- **Title**: سایر فیلتر‌ها
- **Type**: object

### exchange
- **Title**: نمایش معاوضه‌ها
- **Type**: object
- **Queries**: 
  - only-exchanges -> نمایش فقط معاوضه‌ها
  - exclude-exchanges -> حذف معاوضه‌ها

### goods-business-type
- **Title**: نوع آگهی‌دهنده
- **Type**: object
- **Queries**: 
  - all -> همه
  - personal -> شخصی
  - marketplace -> فروشگاه

### has-photo
- **Title**: فقط عکس‌دار
- **Type**: boolean

### price
- **Title**: قیمت
- **Type**: object
 - **Minimum**: 0
 - **Maximum**: N/A

### sort
- **Title**: ترتیب نمایش آگهی‌ها براساس
- **Type**: object
- **Queries**: 
  - quality_and_sort_date -> quality_and_sort_date
  - sort_date -> sort_date
  - cheapest -> cheapest
  - most_expensive -> most_expensive
  - production_year -> production_year
  - usage -> usage
  - most_popular -> most_popular
  - most_relevant -> most_relevant

### status
- **Title**: وضعیت کالا
- **Type**: object
 - **Items Type**: array
- **Queries**: 
  - new -> نو
  - like-new -> در حد نو
  - used -> کارکرده
  - repair-needed -> نیازمند تعمیر

### urgent
- **Title**: فقط فوری‌ها
- **Type**: boolean



---

### Category: horses-equestrian



### category
- **Title**: دسته‌بندی
- **Type**: object

### divider
- **Title**: سایر فیلتر‌ها
- **Type**: object

### exchange
- **Title**: نمایش معاوضه‌ها
- **Type**: object
- **Queries**: 
  - only-exchanges -> نمایش فقط معاوضه‌ها
  - exclude-exchanges -> حذف معاوضه‌ها

### goods-business-type
- **Title**: نوع آگهی‌دهنده
- **Type**: object
- **Queries**: 
  - all -> همه
  - personal -> شخصی
  - marketplace -> فروشگاه

### has-photo
- **Title**: فقط عکس‌دار
- **Type**: boolean

### price
- **Title**: قیمت
- **Type**: object
 - **Minimum**: 0
 - **Maximum**: N/A

### sort
- **Title**: ترتیب نمایش آگهی‌ها براساس
- **Type**: object
- **Queries**: 
  - quality_and_sort_date -> quality_and_sort_date
  - sort_date -> sort_date
  - cheapest -> cheapest
  - most_expensive -> most_expensive
  - production_year -> production_year
  - usage -> usage
  - most_popular -> most_popular
  - most_relevant -> most_relevant

### status
- **Title**: وضعیت کالا
- **Type**: object
 - **Items Type**: array
- **Queries**: 
  - new -> نو
  - like-new -> در حد نو
  - used -> کارکرده
  - repair-needed -> نیازمند تعمیر

### urgent
- **Title**: فقط فوری‌ها
- **Type**: boolean



---

### Category: house-villa-rent



### balcony
- **Title**: با بالکن
- **Type**: boolean

### building-age
- **Title**: سن بنا
- **Type**: object
- **Queries**: 
  - {"min": 0, "max": 1} -> حداکثر ۱ سال
  - {"min": 0, "max": 2} -> حداکثر ۲ سال
  - {"min": 0, "max": 5} -> حداکثر ۵ سال
  - {"min": 0, "max": 10} -> حداکثر ۱۰ سال
  - {"min": 0, "max": 15} -> حداکثر ۱۵ سال
  - {"min": 0, "max": 20} -> حداکثر ۲۰ سال
  - {"min": 0, "max": 30} -> حداکثر ۳۰ سال
  - {"min": 30} -> بیش از ۳۰ سال

### building_direction
- **Title**: جهت ساختمان
- **Type**: object
 - **Items Type**: array
- **Queries**: 
  - east -> شرقی
  - west -> غربی
  - north -> شمالی
  - south -> جنوبی

### business-type
- **Title**: آگهی‌دهنده
- **Type**: object
- **Queries**: 
  - personal -> شخصی
  - real-estate-business -> مشاور املاک

### category
- **Title**: دسته‌بندی
- **Type**: object

### cooling_system
- **Title**: سرمایش
- **Type**: object
 - **Items Type**: array
- **Queries**: 
  - water_cooler -> کولر آبی
  - air_conditioner -> کولر گازی
  - duct_split -> داکت اسپلیت
  - split -> اسپلیت
  - fan_coil -> فن کوئل

### credit
- **Title**: ودیعه
- **Type**: object
 - **Minimum**: 0
 - **Maximum**: N/A

### floor_type
- **Title**: جنس کف
- **Type**: object
 - **Items Type**: array
- **Queries**: 
  - ceramic -> سرامیک
  - wood_parquet -> پارکت چوب
  - laminate_parquet -> پارکت لمینت
  - stone -> سنگ
  - floor_covering -> کف‌پوش PVC
  - carpet -> موکت
  - mosaic -> موزائیک

### has-photo
- **Title**: عکس‌دار
- **Type**: boolean

### has-video
- **Title**: ویدیو‌دار
- **Type**: boolean

### heating_system
- **Title**: گرمایش
- **Type**: object
 - **Items Type**: array
- **Queries**: 
  - heater -> بخاری
  - shoofaj -> شوفاژ
  - fan_coil -> فن کوئل
  - floor_heating -> از کف
  - duct_split -> داکت اسپلیت
  - split -> اسپلیت
  - fireplace -> شومینه

### parking
- **Title**: با پارکینگ
- **Type**: boolean

### rebuilt
- **Title**: بازسازی شده
- **Type**: boolean

### rent
- **Title**: اجاره
- **Type**: object
 - **Minimum**: 0
 - **Maximum**: N/A

### rent_to_single
- **Title**: مناسب مجرد
- **Type**: boolean

### rooms
- **Title**: تعداد اتاق
- **Type**: object
- **Queries**: 
  - بدون اتاق -> بدون اتاق
  - یک -> ۱
  - دو -> ۲
  - سه -> ۳
  - چهار -> ۴
  - بیشتر -> بیشتر از ۴

### size
- **Title**: متراژ
- **Type**: object
 - **Minimum**: 0
 - **Maximum**: 1000000000

### sort
- **Title**: ترتیب نمایش آگهی‌ها براساس
- **Type**: object
- **Queries**: 
  - quality_and_sort_date -> quality_and_sort_date
  - sort_date -> sort_date
  - cheapest -> cheapest
  - most_expensive -> most_expensive
  - production_year -> production_year
  - usage -> usage
  - most_popular -> most_popular
  - most_relevant -> most_relevant

### toilet
- **Title**: سرویس بهداشتی
- **Type**: object
- **Queries**: 
  - squat -> ایرانی
  - seat -> فرنگی
  - squat_seat -> ایرانی و فرنگی

### urgent
- **Title**: فقط فوری‌ها
- **Type**: boolean

### warehouse
- **Title**: با انباری
- **Type**: boolean

### warm_water_provider
- **Title**: تأمین‌کننده آب گرم
- **Type**: object
 - **Items Type**: array
- **Queries**: 
  - water_heater -> آبگرم‌کن
  - powerhouse -> موتورخانه
  - package -> پکیج



---

### Category: house-villa-sell



### balcony
- **Title**: با بالکن
- **Type**: boolean

### building-age
- **Title**: سن بنا
- **Type**: object
- **Queries**: 
  - {"min": 0, "max": 1} -> حداکثر ۱ سال
  - {"min": 0, "max": 2} -> حداکثر ۲ سال
  - {"min": 0, "max": 5} -> حداکثر ۵ سال
  - {"min": 0, "max": 10} -> حداکثر ۱۰ سال
  - {"min": 0, "max": 15} -> حداکثر ۱۵ سال
  - {"min": 0, "max": 20} -> حداکثر ۲۰ سال
  - {"min": 0, "max": 30} -> حداکثر ۳۰ سال
  - {"min": 30} -> بیش از ۳۰ سال

### building_direction
- **Title**: جهت ساختمان
- **Type**: object
 - **Items Type**: array
- **Queries**: 
  - east -> شرقی
  - west -> غربی
  - north -> شمالی
  - south -> جنوبی

### business-type
- **Title**: آگهی‌دهنده
- **Type**: object
- **Queries**: 
  - personal -> شخصی
  - real-estate-business -> مشاور املاک

### category
- **Title**: دسته‌بندی
- **Type**: object

### cooling_system
- **Title**: سرمایش
- **Type**: object
 - **Items Type**: array
- **Queries**: 
  - water_cooler -> کولر آبی
  - air_conditioner -> کولر گازی
  - duct_split -> داکت اسپلیت
  - split -> اسپلیت
  - fan_coil -> فن کوئل

### deed_type
- **Title**: سند
- **Type**: object
 - **Items Type**: array
- **Queries**: 
  - single_page -> تک‌برگ
  - multi_page -> منگوله‌دار
  - written_agreement -> قول‌نامه‌ای
  - other -> سایر

### floor_type
- **Title**: جنس کف
- **Type**: object
 - **Items Type**: array
- **Queries**: 
  - ceramic -> سرامیک
  - wood_parquet -> پارکت چوب
  - laminate_parquet -> پارکت لمینت
  - stone -> سنگ
  - floor_covering -> کف‌پوش PVC
  - carpet -> موکت
  - mosaic -> موزائیک

### has-photo
- **Title**: عکس‌دار
- **Type**: boolean

### has-video
- **Title**: ویدیو‌دار
- **Type**: boolean

### heating_system
- **Title**: گرمایش
- **Type**: object
 - **Items Type**: array
- **Queries**: 
  - heater -> بخاری
  - shoofaj -> شوفاژ
  - fan_coil -> فن کوئل
  - floor_heating -> از کف
  - duct_split -> داکت اسپلیت
  - split -> اسپلیت
  - fireplace -> شومینه

### parking
- **Title**: با پارکینگ
- **Type**: boolean

### price
- **Title**: قیمت کل
- **Type**: object
 - **Minimum**: 0
 - **Maximum**: N/A

### rebuilt
- **Title**: بازسازی شده
- **Type**: boolean

### rooms
- **Title**: تعداد اتاق
- **Type**: object
- **Queries**: 
  - بدون اتاق -> بدون اتاق
  - یک -> ۱
  - دو -> ۲
  - سه -> ۳
  - چهار -> ۴
  - بیشتر -> بیشتر از ۴

### size
- **Title**: متراژ
- **Type**: object
 - **Minimum**: 0
 - **Maximum**: 1000000000

### sort
- **Title**: ترتیب نمایش آگهی‌ها براساس
- **Type**: object
- **Queries**: 
  - quality_and_sort_date -> quality_and_sort_date
  - sort_date -> sort_date
  - cheapest -> cheapest
  - most_expensive -> most_expensive
  - production_year -> production_year
  - usage -> usage
  - most_popular -> most_popular
  - most_relevant -> most_relevant

### toilet
- **Title**: سرویس بهداشتی
- **Type**: object
- **Queries**: 
  - squat -> ایرانی
  - seat -> فرنگی
  - squat_seat -> ایرانی و فرنگی

### urgent
- **Title**: فقط فوری‌ها
- **Type**: boolean

### warehouse
- **Title**: با انباری
- **Type**: boolean

### warm_water_provider
- **Title**: تأمین‌کننده آب گرم
- **Type**: object
 - **Items Type**: array
- **Queries**: 
  - water_heater -> آبگرم‌کن
  - powerhouse -> موتورخانه
  - package -> پکیج



---

### Category: industrial-machinery



### category
- **Title**: دسته‌بندی
- **Type**: object

### divider
- **Title**: سایر فیلتر‌ها
- **Type**: object

### exchange
- **Title**: نمایش معاوضه‌ها
- **Type**: object
- **Queries**: 
  - only-exchanges -> نمایش فقط معاوضه‌ها
  - exclude-exchanges -> حذف معاوضه‌ها

### goods-business-type
- **Title**: نوع آگهی‌دهنده
- **Type**: object
- **Queries**: 
  - all -> همه
  - personal -> شخصی
  - marketplace -> فروشگاه

### has-photo
- **Title**: فقط عکس‌دار
- **Type**: boolean

### price
- **Title**: قیمت
- **Type**: object
 - **Minimum**: 0
 - **Maximum**: N/A

### sort
- **Title**: ترتیب نمایش آگهی‌ها براساس
- **Type**: object
- **Queries**: 
  - quality_and_sort_date -> quality_and_sort_date
  - sort_date -> sort_date
  - cheapest -> cheapest
  - most_expensive -> most_expensive
  - production_year -> production_year
  - usage -> usage
  - most_popular -> most_popular
  - most_relevant -> most_relevant

### status
- **Title**: وضعیت کالا
- **Type**: object
 - **Items Type**: array
- **Queries**: 
  - new -> نو
  - like-new -> در حد نو
  - used -> کارکرده
  - repair-needed -> نیازمند تعمیر

### urgent
- **Title**: فقط فوری‌ها
- **Type**: boolean



---

### Category: industrial-technology



### category
- **Title**: دسته‌بندی
- **Type**: object

### divider
- **Title**: سایر فیلتر‌ها
- **Type**: object

### employee_gender
- **Title**: جنسیت کارجو
- **Type**: object
- **Queries**: 
  - female -> زن
  - male -> مرد
  - neutral -> فرقی ندارد

### experience
- **Title**: سابقهٔ مورد نیاز
- **Type**: object
 - **Minimum**: N/A
 - **Maximum**: N/A

### has-photo
- **Title**: فقط عکس‌دار
- **Type**: boolean

### health_insurance
- **Title**: با بیمه
- **Type**: boolean

### job_type
- **Title**: نوع همکاری
- **Type**: object
 - **Items Type**: array
- **Queries**: 
  - full_time -> تمام وقت
  - part_time -> پاره وقت
  - contract -> پیمان‌کاری/پروژه‌ای
  - internship -> کارآموزی
  - adaptive -> توافقی
  - other -> سایر

### military_service_status
- **Title**: پایان خدمت/معافیت
- **Type**: object
- **Queries**: 
  - finish_or_exemption_required -> الزامی
  - finish_not_required -> اختیاری

### no_experience_required
- **Title**: بدون نیاز به سابقه
- **Type**: boolean

### payment_method
- **Title**: شیوهٔ پرداخت
- **Type**: object
 - **Items Type**: array
- **Queries**: 
  - monthly -> ماهانه
  - daily -> روزانه
  - hourly -> ساعتی
  - percentage_commission -> پورسانتی/درصدی
  - adaptive -> توافقی
  - other -> سایر

### remote
- **Title**: با امکان دورکاری
- **Type**: boolean

### sort
- **Title**: ترتیب نمایش آگهی‌ها براساس
- **Type**: object
- **Queries**: 
  - quality_and_sort_date -> quality_and_sort_date
  - sort_date -> sort_date
  - cheapest -> cheapest
  - most_expensive -> most_expensive
  - production_year -> production_year
  - usage -> usage
  - most_popular -> most_popular
  - most_relevant -> most_relevant

### urgent
- **Title**: فقط فوری‌ها
- **Type**: boolean



---

### Category: industry-agriculture-business-rent



### building-age
- **Title**: سن بنا
- **Type**: object
- **Queries**: 
  - {"min": 0, "max": 1} -> حداکثر ۱ سال
  - {"min": 0, "max": 2} -> حداکثر ۲ سال
  - {"min": 0, "max": 5} -> حداکثر ۵ سال
  - {"min": 0, "max": 10} -> حداکثر ۱۰ سال
  - {"min": 0, "max": 15} -> حداکثر ۱۵ سال
  - {"min": 0, "max": 20} -> حداکثر ۲۰ سال
  - {"min": 0, "max": 30} -> حداکثر ۳۰ سال
  - {"min": 30} -> بیش از ۳۰ سال

### business-type
- **Title**: آگهی‌دهنده
- **Type**: object
- **Queries**: 
  - personal -> شخصی
  - real-estate-business -> مشاور املاک

### category
- **Title**: دسته‌بندی
- **Type**: object

### credit
- **Title**: ودیعه
- **Type**: object
 - **Minimum**: 0
 - **Maximum**: N/A

### has-photo
- **Title**: عکس‌دار
- **Type**: boolean

### has-video
- **Title**: ویدیو‌دار
- **Type**: boolean

### rent
- **Title**: اجاره
- **Type**: object
 - **Minimum**: 0
 - **Maximum**: N/A

### rooms
- **Title**: تعداد اتاق
- **Type**: object
- **Queries**: 
  - بدون اتاق -> بدون اتاق
  - یک -> ۱
  - دو -> ۲
  - سه -> ۳
  - چهار -> ۴
  - بیشتر -> بیشتر از ۴

### size
- **Title**: متراژ
- **Type**: object
 - **Minimum**: 0
 - **Maximum**: N/A

### sort
- **Title**: ترتیب نمایش آگهی‌ها براساس
- **Type**: object
- **Queries**: 
  - quality_and_sort_date -> quality_and_sort_date
  - sort_date -> sort_date
  - cheapest -> cheapest
  - most_expensive -> most_expensive
  - production_year -> production_year
  - usage -> usage
  - most_popular -> most_popular
  - most_relevant -> most_relevant

### urgent
- **Title**: فقط فوری‌ها
- **Type**: boolean



---

### Category: industry-agriculture-business-sell



### bizzDeed
- **Title**: سند اداری
- **Type**: object
- **Queries**: 
  - True -> دارد
  - False -> ندارد

### building-age
- **Title**: سن بنا
- **Type**: object
- **Queries**: 
  - {"min": 0, "max": 1} -> حداکثر ۱ سال
  - {"min": 0, "max": 2} -> حداکثر ۲ سال
  - {"min": 0, "max": 5} -> حداکثر ۵ سال
  - {"min": 0, "max": 10} -> حداکثر ۱۰ سال
  - {"min": 0, "max": 15} -> حداکثر ۱۵ سال
  - {"min": 0, "max": 20} -> حداکثر ۲۰ سال
  - {"min": 0, "max": 30} -> حداکثر ۳۰ سال
  - {"min": 30} -> بیش از ۳۰ سال

### business-type
- **Title**: آگهی‌دهنده
- **Type**: object
- **Queries**: 
  - personal -> شخصی
  - real-estate-business -> مشاور املاک

### category
- **Title**: دسته‌بندی
- **Type**: object

### has-photo
- **Title**: عکس‌دار
- **Type**: boolean

### has-video
- **Title**: ویدیو‌دار
- **Type**: boolean

### price
- **Title**: قیمت کل
- **Type**: object
 - **Minimum**: 0
 - **Maximum**: N/A

### rooms
- **Title**: تعداد اتاق
- **Type**: object
- **Queries**: 
  - بدون اتاق -> بدون اتاق
  - یک -> ۱
  - دو -> ۲
  - سه -> ۳
  - چهار -> ۴
  - بیشتر -> بیشتر از ۴

### size
- **Title**: متراژ
- **Type**: object
 - **Minimum**: 0
 - **Maximum**: N/A

### sort
- **Title**: ترتیب نمایش آگهی‌ها براساس
- **Type**: object
- **Queries**: 
  - quality_and_sort_date -> quality_and_sort_date
  - sort_date -> sort_date
  - cheapest -> cheapest
  - most_expensive -> most_expensive
  - production_year -> production_year
  - usage -> usage
  - most_popular -> most_popular
  - most_relevant -> most_relevant

### urgent
- **Title**: فقط فوری‌ها
- **Type**: boolean



---

### Category: janitorial-cleaning



### category
- **Title**: دسته‌بندی
- **Type**: object

### divider
- **Title**: سایر فیلتر‌ها
- **Type**: object

### employee_gender
- **Title**: جنسیت کارجو
- **Type**: object
- **Queries**: 
  - female -> زن
  - male -> مرد
  - neutral -> فرقی ندارد

### experience
- **Title**: سابقهٔ مورد نیاز
- **Type**: object
 - **Minimum**: N/A
 - **Maximum**: N/A

### has-photo
- **Title**: فقط عکس‌دار
- **Type**: boolean

### health_insurance
- **Title**: با بیمه
- **Type**: boolean

### job_type
- **Title**: نوع همکاری
- **Type**: object
 - **Items Type**: array
- **Queries**: 
  - full_time -> تمام وقت
  - part_time -> پاره وقت
  - contract -> پیمان‌کاری/پروژه‌ای
  - internship -> کارآموزی
  - adaptive -> توافقی
  - other -> سایر

### military_service_status
- **Title**: پایان خدمت/معافیت
- **Type**: object
- **Queries**: 
  - finish_or_exemption_required -> الزامی
  - finish_not_required -> اختیاری

### no_experience_required
- **Title**: بدون نیاز به سابقه
- **Type**: boolean

### payment_method
- **Title**: شیوهٔ پرداخت
- **Type**: object
 - **Items Type**: array
- **Queries**: 
  - monthly -> ماهانه
  - daily -> روزانه
  - hourly -> ساعتی
  - percentage_commission -> پورسانتی/درصدی
  - adaptive -> توافقی
  - other -> سایر

### remote
- **Title**: با امکان دورکاری
- **Type**: boolean

### sort
- **Title**: ترتیب نمایش آگهی‌ها براساس
- **Type**: object
- **Queries**: 
  - quality_and_sort_date -> quality_and_sort_date
  - sort_date -> sort_date
  - cheapest -> cheapest
  - most_expensive -> most_expensive
  - production_year -> production_year
  - usage -> usage
  - most_popular -> most_popular
  - most_relevant -> most_relevant

### urgent
- **Title**: فقط فوری‌ها
- **Type**: boolean



---

### Category: jewelry



### body-type
- **Title**: جنس
- **Type**: object
 - **Items Type**: array
- **Queries**: 
  - طلا -> طلا
  - نقره -> نقره
  - آبکاری طلا -> آبکاری طلا
  - سنگ قیمتی -> سنگ قیمتی
  - غیره -> غیره

### category
- **Title**: دسته‌بندی
- **Type**: object

### divider
- **Title**: سایر فیلتر‌ها
- **Type**: object

### exchange
- **Title**: نمایش معاوضه‌ها
- **Type**: object
- **Queries**: 
  - only-exchanges -> نمایش فقط معاوضه‌ها
  - exclude-exchanges -> حذف معاوضه‌ها

### goods-business-type
- **Title**: نوع آگهی‌دهنده
- **Type**: object
- **Queries**: 
  - all -> همه
  - personal -> شخصی
  - marketplace -> فروشگاه

### has-photo
- **Title**: فقط عکس‌دار
- **Type**: boolean

### merchandise-type
- **Title**: نوع جواهرات
- **Type**: object
 - **Items Type**: array
- **Queries**: 
  - انگشتر -> انگشتر
  - گوشواره -> گوشواره
  - دست‌بند -> دست‌بند
  - زنجیر و گردن‌بند -> زنجیر و گردن‌بند
  - پابند -> پابند
  - ست و نیم‌ست -> ست و نیم‌ست
  - غیره -> غیره

### price
- **Title**: قیمت
- **Type**: object
 - **Minimum**: 0
 - **Maximum**: N/A

### sort
- **Title**: ترتیب نمایش آگهی‌ها براساس
- **Type**: object
- **Queries**: 
  - quality_and_sort_date -> quality_and_sort_date
  - sort_date -> sort_date
  - cheapest -> cheapest
  - most_expensive -> most_expensive
  - production_year -> production_year
  - usage -> usage
  - most_popular -> most_popular
  - most_relevant -> most_relevant

### status
- **Title**: وضعیت کالا
- **Type**: object
 - **Items Type**: array
- **Queries**: 
  - new -> نو
  - like-new -> در حد نو
  - used -> کارکرده
  - repair-needed -> نیازمند تعمیر

### urgent
- **Title**: فقط فوری‌ها
- **Type**: boolean



---

### Category: jewelry-and-watches



### category
- **Title**: دسته‌بندی
- **Type**: object

### divider
- **Title**: سایر فیلتر‌ها
- **Type**: object

### exchange
- **Title**: نمایش معاوضه‌ها
- **Type**: object
- **Queries**: 
  - only-exchanges -> نمایش فقط معاوضه‌ها
  - exclude-exchanges -> حذف معاوضه‌ها

### goods-business-type
- **Title**: نوع آگهی‌دهنده
- **Type**: object
- **Queries**: 
  - all -> همه
  - personal -> شخصی
  - marketplace -> فروشگاه

### has-photo
- **Title**: فقط عکس‌دار
- **Type**: boolean

### price
- **Title**: قیمت
- **Type**: object
 - **Minimum**: 0
 - **Maximum**: N/A

### sort
- **Title**: ترتیب نمایش آگهی‌ها براساس
- **Type**: object
- **Queries**: 
  - quality_and_sort_date -> quality_and_sort_date
  - sort_date -> sort_date
  - cheapest -> cheapest
  - most_expensive -> most_expensive
  - production_year -> production_year
  - usage -> usage
  - most_popular -> most_popular
  - most_relevant -> most_relevant

### status
- **Title**: وضعیت کالا
- **Type**: object
 - **Items Type**: array
- **Queries**: 
  - new -> نو
  - like-new -> در حد نو
  - used -> کارکرده
  - repair-needed -> نیازمند تعمیر

### urgent
- **Title**: فقط فوری‌ها
- **Type**: boolean



---

### Category: jobs



### category
- **Title**: دسته‌بندی
- **Type**: object

### divider
- **Title**: سایر فیلتر‌ها
- **Type**: object

### employee_gender
- **Title**: جنسیت کارجو
- **Type**: object
- **Queries**: 
  - female -> زن
  - male -> مرد
  - neutral -> فرقی ندارد

### experience
- **Title**: سابقهٔ مورد نیاز
- **Type**: object
 - **Minimum**: N/A
 - **Maximum**: N/A

### has-photo
- **Title**: فقط عکس‌دار
- **Type**: boolean

### health_insurance
- **Title**: با بیمه
- **Type**: boolean

### job_type
- **Title**: نوع همکاری
- **Type**: object
 - **Items Type**: array
- **Queries**: 
  - full_time -> تمام وقت
  - part_time -> پاره وقت
  - contract -> پیمان‌کاری/پروژه‌ای
  - internship -> کارآموزی
  - adaptive -> توافقی
  - other -> سایر

### military_service_status
- **Title**: پایان خدمت/معافیت
- **Type**: object
- **Queries**: 
  - finish_or_exemption_required -> الزامی
  - finish_not_required -> اختیاری

### no_experience_required
- **Title**: بدون نیاز به سابقه
- **Type**: boolean

### payment_method
- **Title**: شیوهٔ پرداخت
- **Type**: object
 - **Items Type**: array
- **Queries**: 
  - monthly -> ماهانه
  - daily -> روزانه
  - hourly -> ساعتی
  - percentage_commission -> پورسانتی/درصدی
  - adaptive -> توافقی
  - other -> سایر

### remote
- **Title**: با امکان دورکاری
- **Type**: boolean

### sort
- **Title**: ترتیب نمایش آگهی‌ها براساس
- **Type**: object
- **Queries**: 
  - quality_and_sort_date -> quality_and_sort_date
  - sort_date -> sort_date
  - cheapest -> cheapest
  - most_expensive -> most_expensive
  - production_year -> production_year
  - usage -> usage
  - most_popular -> most_popular
  - most_relevant -> most_relevant

### urgent
- **Title**: فقط فوری‌ها
- **Type**: boolean



---

### Category: juicers



### category
- **Title**: دسته‌بندی
- **Type**: object

### divider
- **Title**: سایر فیلتر‌ها
- **Type**: object

### exchange
- **Title**: نمایش معاوضه‌ها
- **Type**: object
- **Queries**: 
  - only-exchanges -> نمایش فقط معاوضه‌ها
  - exclude-exchanges -> حذف معاوضه‌ها

### goods-business-type
- **Title**: نوع آگهی‌دهنده
- **Type**: object
- **Queries**: 
  - all -> همه
  - personal -> شخصی
  - marketplace -> فروشگاه

### has-photo
- **Title**: فقط عکس‌دار
- **Type**: boolean

### price
- **Title**: قیمت
- **Type**: object
 - **Minimum**: 0
 - **Maximum**: N/A

### sort
- **Title**: ترتیب نمایش آگهی‌ها براساس
- **Type**: object
- **Queries**: 
  - quality_and_sort_date -> quality_and_sort_date
  - sort_date -> sort_date
  - cheapest -> cheapest
  - most_expensive -> most_expensive
  - production_year -> production_year
  - usage -> usage
  - most_popular -> most_popular
  - most_relevant -> most_relevant

### status
- **Title**: وضعیت کالا
- **Type**: object
 - **Items Type**: array
- **Queries**: 
  - new -> نو
  - like-new -> در حد نو
  - used -> کارکرده
  - repair-needed -> نیازمند تعمیر

### urgent
- **Title**: فقط فوری‌ها
- **Type**: boolean



---

### Category: kitchen-utensils



### category
- **Title**: دسته‌بندی
- **Type**: object

### divider
- **Title**: سایر فیلتر‌ها
- **Type**: object

### exchange
- **Title**: نمایش معاوضه‌ها
- **Type**: object
- **Queries**: 
  - only-exchanges -> نمایش فقط معاوضه‌ها
  - exclude-exchanges -> حذف معاوضه‌ها

### goods-business-type
- **Title**: نوع آگهی‌دهنده
- **Type**: object
- **Queries**: 
  - all -> همه
  - personal -> شخصی
  - marketplace -> فروشگاه

### has-photo
- **Title**: فقط عکس‌دار
- **Type**: boolean

### price
- **Title**: قیمت
- **Type**: object
 - **Minimum**: 0
 - **Maximum**: N/A

### sort
- **Title**: ترتیب نمایش آگهی‌ها براساس
- **Type**: object
- **Queries**: 
  - quality_and_sort_date -> quality_and_sort_date
  - sort_date -> sort_date
  - cheapest -> cheapest
  - most_expensive -> most_expensive
  - production_year -> production_year
  - usage -> usage
  - most_popular -> most_popular
  - most_relevant -> most_relevant

### status
- **Title**: وضعیت کالا
- **Type**: object
 - **Items Type**: array
- **Queries**: 
  - new -> نو
  - like-new -> در حد نو
  - used -> کارکرده
  - repair-needed -> نیازمند تعمیر

### urgent
- **Title**: فقط فوری‌ها
- **Type**: boolean



---

### Category: lamps



### category
- **Title**: دسته‌بندی
- **Type**: object

### divider
- **Title**: سایر فیلتر‌ها
- **Type**: object

### exchange
- **Title**: نمایش معاوضه‌ها
- **Type**: object
- **Queries**: 
  - only-exchanges -> نمایش فقط معاوضه‌ها
  - exclude-exchanges -> حذف معاوضه‌ها

### goods-business-type
- **Title**: نوع آگهی‌دهنده
- **Type**: object
- **Queries**: 
  - all -> همه
  - personal -> شخصی
  - marketplace -> فروشگاه

### has-photo
- **Title**: فقط عکس‌دار
- **Type**: boolean

### price
- **Title**: قیمت
- **Type**: object
 - **Minimum**: 0
 - **Maximum**: N/A

### sort
- **Title**: ترتیب نمایش آگهی‌ها براساس
- **Type**: object
- **Queries**: 
  - quality_and_sort_date -> quality_and_sort_date
  - sort_date -> sort_date
  - cheapest -> cheapest
  - most_expensive -> most_expensive
  - production_year -> production_year
  - usage -> usage
  - most_popular -> most_popular
  - most_relevant -> most_relevant

### status
- **Title**: وضعیت کالا
- **Type**: object
 - **Items Type**: array
- **Queries**: 
  - new -> نو
  - like-new -> در حد نو
  - used -> کارکرده
  - repair-needed -> نیازمند تعمیر

### urgent
- **Title**: فقط فوری‌ها
- **Type**: boolean



---

### Category: lampshade



### category
- **Title**: دسته‌بندی
- **Type**: object

### divider
- **Title**: سایر فیلتر‌ها
- **Type**: object

### exchange
- **Title**: نمایش معاوضه‌ها
- **Type**: object
- **Queries**: 
  - only-exchanges -> نمایش فقط معاوضه‌ها
  - exclude-exchanges -> حذف معاوضه‌ها

### goods-business-type
- **Title**: نوع آگهی‌دهنده
- **Type**: object
- **Queries**: 
  - all -> همه
  - personal -> شخصی
  - marketplace -> فروشگاه

### has-photo
- **Title**: فقط عکس‌دار
- **Type**: boolean

### price
- **Title**: قیمت
- **Type**: object
 - **Minimum**: 0
 - **Maximum**: N/A

### sort
- **Title**: ترتیب نمایش آگهی‌ها براساس
- **Type**: object
- **Queries**: 
  - quality_and_sort_date -> quality_and_sort_date
  - sort_date -> sort_date
  - cheapest -> cheapest
  - most_expensive -> most_expensive
  - production_year -> production_year
  - usage -> usage
  - most_popular -> most_popular
  - most_relevant -> most_relevant

### status
- **Title**: وضعیت کالا
- **Type**: object
 - **Items Type**: array
- **Queries**: 
  - new -> نو
  - like-new -> در حد نو
  - used -> کارکرده
  - repair-needed -> نیازمند تعمیر

### urgent
- **Title**: فقط فوری‌ها
- **Type**: boolean



---

### Category: laptops



### brands
- **Title**: برند
- **Type**: object
 - **Items Type**: array
- **Queries**: 
  - Acer - ایسر -> Acer - ایسر
  - Apple - اپل -> Apple - اپل
  - Asus - ایسوس -> Asus - ایسوس
  - Compaq - کامپک -> Compaq - کامپک
  - Dell - دل -> Dell - دل
  - Fujitsu - فوجیتسو -> Fujitsu - فوجیتسو
  - Gigabyte - گیگابایت -> Gigabyte - گیگابایت
  - HP - اچ‌پی -> HP - اچ‌پی
  - Lenovo - لنوو -> Lenovo - لنوو
  - MSI - ام‌اس‌آی -> MSI - ام‌اس‌آی
  - Samsung - سامسونگ -> Samsung - سامسونگ
  - Sony - سونی -> Sony - سونی
  - Toshiba - توشیبا -> Toshiba - توشیبا
  - Suzuki - سوزوکی -> Suzuki - سوزوکی
  - Razer - ریزر -> Razer - ریزر
  - Alienware - ایلین‌ویر -> Alienware - ایلین‌ویر
  - Microsoft - مایکروسافت -> Microsoft - مایکروسافت
  - غیره -> غیره

### category
- **Title**: دسته‌بندی
- **Type**: object

### divider
- **Title**: سایر فیلتر‌ها
- **Type**: object

### exchange
- **Title**: نمایش معاوضه‌ها
- **Type**: object
- **Queries**: 
  - only-exchanges -> نمایش فقط معاوضه‌ها
  - exclude-exchanges -> حذف معاوضه‌ها

### goods-business-type
- **Title**: نوع آگهی‌دهنده
- **Type**: object
- **Queries**: 
  - all -> همه
  - personal -> شخصی
  - marketplace -> فروشگاه

### has-photo
- **Title**: فقط عکس‌دار
- **Type**: boolean

### has_touch_screen
- **Title**: دارای صفحه‌نمایش لمسی
- **Type**: boolean

### hdmi_port
- **Title**: دارای پورت HDMI
- **Type**: boolean

### price
- **Title**: قیمت
- **Type**: object
 - **Minimum**: 0
 - **Maximum**: N/A

### processor
- **Title**: نوع پردازنده
- **Type**: object
 - **Items Type**: array
- **Queries**: 
  - Core i3 -> Core i3
  - Core i5 -> Core i5
  - Core i7 -> Core i7
  - Core i9 -> Core i9
  - Core 2 Duo -> Core 2 Duo
  - Pentium -> Pentium
  - Celeron -> Celeron
  - Atom -> Atom
  - Ryzen 3 -> Ryzen 3
  - Ryzen 5 -> Ryzen 5
  - Ryzen 7 -> Ryzen 7
  - Apple M1 -> Apple M1
  - غیره -> غیره

### sort
- **Title**: ترتیب نمایش آگهی‌ها براساس
- **Type**: object
- **Queries**: 
  - quality_and_sort_date -> quality_and_sort_date
  - sort_date -> sort_date
  - cheapest -> cheapest
  - most_expensive -> most_expensive
  - production_year -> production_year
  - usage -> usage
  - most_popular -> most_popular
  - most_relevant -> most_relevant

### status
- **Title**: وضعیت کالا
- **Type**: object
 - **Items Type**: array
- **Queries**: 
  - new -> نو
  - like-new -> در حد نو
  - used -> کارکرده
  - repair-needed -> نیازمند تعمیر

### urgent
- **Title**: فقط فوری‌ها
- **Type**: boolean



---

### Category: leisure-hobbies



### category
- **Title**: دسته‌بندی
- **Type**: object

### divider
- **Title**: سایر فیلتر‌ها
- **Type**: object

### exchange
- **Title**: نمایش معاوضه‌ها
- **Type**: object
- **Queries**: 
  - only-exchanges -> نمایش فقط معاوضه‌ها
  - exclude-exchanges -> حذف معاوضه‌ها

### goods-business-type
- **Title**: نوع آگهی‌دهنده
- **Type**: object
- **Queries**: 
  - all -> همه
  - personal -> شخصی
  - marketplace -> فروشگاه

### has-photo
- **Title**: فقط عکس‌دار
- **Type**: boolean

### price
- **Title**: قیمت
- **Type**: object
 - **Minimum**: 0
 - **Maximum**: N/A

### sort
- **Title**: ترتیب نمایش آگهی‌ها براساس
- **Type**: object
- **Queries**: 
  - quality_and_sort_date -> quality_and_sort_date
  - sort_date -> sort_date
  - cheapest -> cheapest
  - most_expensive -> most_expensive
  - production_year -> production_year
  - usage -> usage
  - most_popular -> most_popular
  - most_relevant -> most_relevant

### urgent
- **Title**: فقط فوری‌ها
- **Type**: boolean



---

### Category: leisure-hobbies-toys



### category
- **Title**: دسته‌بندی
- **Type**: object

### divider
- **Title**: سایر فیلتر‌ها
- **Type**: object

### exchange
- **Title**: نمایش معاوضه‌ها
- **Type**: object
- **Queries**: 
  - only-exchanges -> نمایش فقط معاوضه‌ها
  - exclude-exchanges -> حذف معاوضه‌ها

### goods-business-type
- **Title**: نوع آگهی‌دهنده
- **Type**: object
- **Queries**: 
  - all -> همه
  - personal -> شخصی
  - marketplace -> فروشگاه

### has-photo
- **Title**: فقط عکس‌دار
- **Type**: boolean

### price
- **Title**: قیمت
- **Type**: object
 - **Minimum**: 0
 - **Maximum**: N/A

### sort
- **Title**: ترتیب نمایش آگهی‌ها براساس
- **Type**: object
- **Queries**: 
  - quality_and_sort_date -> quality_and_sort_date
  - sort_date -> sort_date
  - cheapest -> cheapest
  - most_expensive -> most_expensive
  - production_year -> production_year
  - usage -> usage
  - most_popular -> most_popular
  - most_relevant -> most_relevant

### status
- **Title**: وضعیت کالا
- **Type**: object
 - **Items Type**: array
- **Queries**: 
  - new -> نو
  - like-new -> در حد نو
  - used -> کارکرده
  - repair-needed -> نیازمند تعمیر

### urgent
- **Title**: فقط فوری‌ها
- **Type**: boolean



---

### Category: light



### body_status
- **Title**: وضعیت بدنه
- **Type**: object
 - **Items Type**: array
- **Queries**: 
  - body_status -> سالم و بی‌خط و خش
  - some-scratches -> خط و خش جزیی
  - paintless-dent-removal -> صافکاری بی‌رنگ
  - one-spot-paint -> رنگ‌شدگی، در ۱ ناحیه
  - two-spots-paint -> رنگ‌شدگی، در ۲ ناحیه
  - some-paint -> رنگ‌شدگی، در چند ناحیه
  - half-paint -> دوررنگ
  - full-paint -> تمام‌رنگ
  - accidental -> تصادفی
  - junk -> اوراقی

### brand_model
- **Title**: برند و تیپ
- **Type**: object
 - **Items Type**: array
- **Queries**: 
  - ROOT -> همه‌ی برند‌ها
  - Audi -> آئودی
  - Audi Q5 -> آئودی Q5
  - Audi TT -> آئودی TT
  - Audi TT convertible -> آئودی TT کروک
  - Audi TT coupe -> آئودی TT کوپه
  - Arisan -> آریسان
  - Ario -> آریو
  - Ario automatic-1600cc -> آریو اتوماتیک 1600cc
  - Ario manual-1500cc -> آریو دنده‌ای 1500cc
  - Ario manual-1600cc -> آریو دنده‌ای 1600cc
  - Alfa Romeo -> آلفارومئو
  - Alfa Romeo 4C -> آلفارومئو 4C
  - Alfa Romeo Giulietta -> آلفارومئو جولیتا
  - Alfa Romeo MiTo -> آلفارومئو میتو
  - Amico -> آمیکو وانت
  - Opel -> اپل
  - Opel Astra Station -> اپل آسترا استیشن
  - Opel Astra -> اپل آسترا سدان
  - Opel Astra new -> اپل آسترا سدان جدید
  - Opel Astra old -> اپل آسترا سدان قدیم
  - Opel Astra Hatchback -> اپل آسترا هاچبک
  - Opel Astra Hatchback 1400cc -> اپل آسترا هاچبک 1400cc
  - Opel Astra Hatchback 1600cc -> اپل آسترا هاچبک 1600cc
  - Opel Omega -> اپل امگا
  - Opel Insignia -> اپل اینسیگنیا
  - Opel Calibra -> اپل کالیبرا
  - Opel Corsa -> اپل کورسا
  - Opel Corsa automatic -> اپل کورسا اتوماتیک
  - Opel Corsa new -> اپل کورسا دنده‌ای اتاق جدید
  - Opel Corsa old -> اپل کورسا دنده‌ای اتاق قدیم
  - Opel Mokka -> اپل موکا
  - Opel Vectra -> اپل وکترا
  - SWM -> اس‌دبلیو‌ام
  - SWM G01 -> اس‌دبلیو‌ام G01
  - SWM G01 F -> اس‌دبلیو‌ام G01 F
  - Smart -> اسمارت
  - Smart Fortwo -> اسمارت فور 2
  - Smart Forfour -> اسمارت فور 4
  - Oldsmobile -> الدزمبیل
  - Oldsmobile Regency -> الدزمبیل ریجنسی
  - Oldsmobile Cutlass -> الدزمبیل کاتلاس
  - MG -> ام‌جی
  - MG 3 -> ام‌جی 3
  - MG 350 -> ام‌جی 350
  - MG 360 -> ام‌جی 360
  - MG 360 automatic -> ام‌جی 360 اتوماتیک
  - MG 360 automatic-turbo -> ام‌جی 360 اتوماتیک توربو
  - MG 360 manual -> ام‌جی 360 دنده‌ای
  - MG 550 -> ام‌جی 550
  - MG 6 -> ام‌جی 6
  - MG 6 Magnette -> ام‌جی 6 مگنت
  - MG 6 New -> ام‌جی 6 نیو
  - MG 6 GT -> ام‌جی 6 GT
  - MG GS -> ام‌جی GS
  - MG GT -> ام‌جی GT
  - MG RX5 -> ام‌جی RX5
  - MVM -> ام‌وی‌ام
  - MVM 110 -> ام‌وی‌ام 110
  - MVM 110 3 cylinder -> ام‌وی‌ام 110 ۳ سیلندر
  - MVM 110 automatic-4 cylinder -> ام‌وی‌ام 110 اتوماتیک ۴ سیلندر
  - MVM 110 manual-4 cylinder -> ام‌وی‌ام 110 دنده‌ای ۴ سیلندر
  - MVM 110S -> ام‌وی‌ام 110S
  - MVM 110S sport-luxury -> ام‌وی‌ام 110S اسپرت لاکچری
  - MVM 110S comfort -> ام‌وی‌ام 110S کامفورت
  - MVM 110S luxury -> ام‌وی‌ام 110S لاکچری
  - MVM 315 Sedan -> ام‌وی‌ام 315 صندوق‌دار
  - MVM 315 Sedan sedan-sport -> ام‌وی‌ام 315 صندوق‌دار اسپرت
  - MVM 315 Sedan basic -> ام‌وی‌ام 315 صندوق‌دار ساده
  - MVM 315 hatchback -> ام‌وی‌ام 315 هاچبک
  - MVM 315 hatchback sport-excellent -> ام‌وی‌ام 315 هاچبک اسپرت اکسلنت
  - MVM 315 hatchback sport-luxury -> ام‌وی‌ام 315 هاچبک اسپرت لاکچری
  - MVM 315 Hatchback Plus -> ام‌وی‌ام 315 هاچبک پلاس
  - MVM 315 hatchback basic -> ام‌وی‌ام 315 هاچبک ساده
  - MVM 530 -> ام‌وی‌ام 530
  - MVM 550 -> ام‌وی‌ام 550
  - MVM 550 automatic -> ام‌وی‌ام 550 اتوماتیک
  - MVM 550 manual -> ام‌وی‌ام 550 دنده‌ای
  - MVM X22 -> ام‌وی‌ام X22
  - MVM X22 automatic-sport -> ام‌وی‌ام X22 اتوماتیک اسپرت
  - MVM X22 automatic-sport-excellent -> ام‌وی‌ام X22 اتوماتیک اسپرت اکسلنت
  - MVM X22 automatic-sport-luxury -> ام‌وی‌ام X22 اتوماتیک اسپرت لاکچری
  - MVM X22 automatic -> ام‌وی‌ام X22 اتوماتیک ساده
  - MVM X22 automatic-luxury -> ام‌وی‌ام X22 اتوماتیک لاکچری
  - MVM X22 manual-sport-excellent -> ام‌وی‌ام X22 دنده‌ای اسپرت اکسلنت
  - MVM X22 manual-sport-luxury -> ام‌وی‌ام X22 دنده‌ای اسپرت لاکچری
  - MVM X22 manual-basic -> ام‌وی‌ام X22 دنده‌ای ساده
  - MVM X22 manual-luxury -> ام‌وی‌ام X22 دنده‌ای لاکچری
  - MVM X22pro -> ام‌وی‌ام X22 Pro
  - MVM X22pro Excellent -> ام‌وی‌ام X22 Pro اکسلنت
  - MVM X22pro IE -> ام‌وی‌ام X22 Pro IE
  - MVM X33 -> ام‌وی‌ام X33
  - MVM X33 automatic -> ام‌وی‌ام X33 اتوماتیک
  - MVM X33 manual -> ام‌وی‌ام X33 دنده‌ای
  - MVM X33S -> ام‌وی‌ام X33 S
  - MVM X33S sport -> ام‌وی‌ام X33 S اسپرت
  - MVM X33S basic -> ام‌وی‌ام X33 S ساده
  - MVM X33S New Face -> ام‌وی‌ام X33 S نیوفیس
  - MVM X55 -> ام‌وی‌ام X55
  - MVM X55 Excellent -> ام‌وی‌ام X55 اکسلنت
  - MVM X55 Excellent-sport -> ام‌وی‌ام X55 اکسلنت اسپرت
  - MVM X55 Pro -> ام‌وی‌ام X55 Pro
  - MVM X55 Pro Excellent -> ام‌وی‌ام X55 Pro اکسلنت
  - MVM X55 Pro Excellent-sport -> ام‌وی‌ام X55 Pro اکسلنت اسپرت
  - MVM X55 Pro IE -> ام‌وی‌ام X55 Pro IE
  - MVM X55 Pro IE Sport -> ام‌وی‌ام X55 Pro IE اسپرت
  - Isuzu -> ایسوزو
  - Isuzu Double Cabin -> ایسوزو دو کابین
  - Isuzu Double Cabin D Max -> ایسوزو دو کابین D MAX
  - inroads -> اینرودز
  - inroads Van C35 -> اینرودز ون C35
  - Iveco -> ایویکو
  - BAIC -> بایک
  - BAIC Sabrina -> بایک سابرینا
  - BAIC Sabrina-ir -> بایک سابرینا مونتاژ
  - BAIC Sabrina-ir hatchback -> بایک سابرینا مونتاژ هاچبک
  - BAIC Sabrina hatchback -> بایک سابرینا هاچبک
  - BAIC Senova -> بایک سنوا
  - BAIC X25 -> بایک X25
  - BAIC X25 Automatic -> بایک X25 اتوماتیک
  - BAIC X25 Manual -> بایک X25 دنده ای
  - Brilliance -> برلیانس
  - Brilliance C3 -> برلیانس کراس
  - Brilliance C3 automatic-1500cc -> برلیانس کراس اتوماتیک 1500cc
  - Brilliance C3 automatic-1650cc -> برلیانس کراس اتوماتیک 1650cc
  - Brilliance H220 -> برلیانس H220
  - Brilliance H220 automatic -> برلیانس H220 اتوماتیک
  - Brilliance H220 manual -> برلیانس H220 دنده ای
  - Brilliance H230 -> برلیانس H230
  - Brilliance H230 automatic -> برلیانس H230 اتوماتیک
  - Brilliance H230 manual -> برلیانس H230 دنده‌ای
  - Brilliance H320 -> برلیانس H320
  - Brilliance H320 automatic-1500cc -> برلیانس H320 اتوماتیک 1500cc
  - Brilliance H320 automatic-1650cc -> برلیانس H320 اتوماتیک 1650cc
  - Brilliance H320 manual-1500cc -> برلیانس H320 دنده‌ای 1500cc
  - Brilliance H320 manual-1650cc -> برلیانس H320 دنده‌ای 1650cc
  - Brilliance H330 -> برلیانس H330
  - Brilliance H330 automatic-1500cc -> برلیانس H330 اتوماتیک 1500cc
  - Brilliance H330 automatic-1650cc -> برلیانس H330 اتوماتیک 1650cc
  - Brilliance H330 manual-1500cc -> برلیانس H330 دنده‌ای 1500cc
  - Brilliance H330 manual-1650cc -> برلیانس H330 دنده‌ای 1650cc
  - Brilliance V5 -> برلیانس V5
  - Besturn -> بسترن
  - Besturn B30 -> بسترن B30
  - Besturn B50 -> بسترن B50
  - Besturn B50F -> بسترن B50F
  - Mercedes-Benz -> بنز
  - Mercedes-Benz A Class -> بنز کلاس A
  - Mercedes-Benz A Class A150 -> بنز کلاس A A150
  - Mercedes-Benz A Class A170 -> بنز کلاس A A170
  - Mercedes-Benz A Class A200 -> بنز کلاس A A200
  - Mercedes-Benz A Class A200-turbo -> بنز کلاس A A200 توربو
  - Mercedes-Benz B Class -> بنز کلاس B
  - Mercedes-Benz B Class B200 -> بنز کلاس B ‌‌B200
  - Mercedes-Benz B Class B200-turbo -> بنز کلاس B B200 توربو
  - Mercedes-Benz C Class -> بنز کلاس C
  - Mercedes-Benz C Class Coupe -> بنز کلاس C کوپه
  - Mercedes-Benz C Class Coupe C230 -> بنز کلاس C کوپه C230
  - Mercedes-Benz C Class Coupe C250 -> بنز کلاس C کوپه C250
  - Mercedes-Benz C Class Coupe C350 -> بنز کلاس C کوپه C350
  - Mercedes-Benz C Class C180 -> بنز کلاس C C180
  - Mercedes-Benz C Class C200 -> بنز کلاس C C200
  - Mercedes-Benz C Class C230 -> بنز کلاس C C230
  - Mercedes-Benz C Class C240-automatic -> بنز کلاس C C240 اتوماتیک
  - Mercedes-Benz C Class C240-manual -> بنز کلاس C C240 دنده‌ای
  - Mercedes-Benz C Class C250 -> بنز کلاس C C250
  - Mercedes-Benz C Class C280 -> بنز کلاس C C280
  - Mercedes-Benz C Class C300 -> بنز کلاس C C300
  - Mercedes-Benz C Class C350 -> بنز کلاس C C350
  - Mercedes-Benz CL Class -> بنز کلاس CL
  - Mercedes-Benz CL Class CL500 -> بنز کلاس CL CL500
  - Mercedes-Benz CLA Class -> بنز کلاس CLA
  - Mercedes-Benz CLA Class CLA45 -> بنز کلاس CLA CLA45
  - Mercedes-Benz CLK Class convertible -> بنز کلاس CLK کروک
  - Mercedes-Benz CLK Class convertible CLK200 -> بنز کلاس CLK کروک CLK200
  - Mercedes-Benz CLK Class convertible CLK240 -> بنز کلاس CLK کروک CLK240
  - Mercedes-Benz CLK Class convertible CLK280 -> بنز کلاس CLK کروک CLK280
  - Mercedes-Benz CLK Class Coupe -> بنز کلاس CLK کوپه
  - Mercedes-Benz CLK Class Coupe CLK200 -> بنز کلاس CLK کوپه CLK200
  - Mercedes-Benz CLS Class -> بنز کلاس CLS
  - Mercedes-Benz CLS Class CLS350 -> بنز کلاس CLS CLS350
  - Mercedes-Benz CLS Class CLS500 -> بنز کلاس CLS CLS500
  - Mercedes-Benz CLS Class CLS550 -> بنز کلاس CLS CLS550
  - Mercedes-Benz E Class -> بنز کلاس E
  - Mercedes-Benz E Class Convertible -> بنز کلاس E کروک
  - Mercedes-Benz E Class Convertible E200 -> بنز کلاس E کروک E200
  - Mercedes-Benz E Class Convertible E250 -> بنز کلاس E کروک E250
  - Mercedes-Benz E Class Convertible E350 -> بنز کلاس E کروک E350
  - Mercedes-Benz E Class Coupe -> بنز کلاس E کوپه
  - Mercedes-Benz E Class Coupe E200 -> بنز کلاس E کوپه E200
  - Mercedes-Benz E Class Coupe E250 -> بنز کلاس E کوپه E250
  - Mercedes-Benz E Class Coupe E350 -> بنز کلاس E کوپه E350
  - Mercedes-Benz E Class-ir -> بنز کلاس E مونتاژ
  - Mercedes-Benz E Class-ir E200 -> بنز کلاس E مونتاژ E200
  - Mercedes-Benz E Class-ir E280 -> بنز کلاس E مونتاژ E280
  - Mercedes-Benz E Class-ir E350 -> بنز کلاس E مونتاژ E350
  - Mercedes-Benz E Class E190 -> بنز کلاس E E190
  - Mercedes-Benz E Class E200 -> بنز کلاس E E200
  - Mercedes-Benz E Class E220 -> بنز کلاس E E220
  - Mercedes-Benz E Class E230 -> بنز کلاس E E230
  - Mercedes-Benz E Class E240-automatic -> بنز کلاس E E240 اتوماتیک
  - Mercedes-Benz E Class E240-manual -> بنز کلاس E E240 دنده‌ای
  - Mercedes-Benz E Class E250 -> بنز کلاس E E250
  - Mercedes-Benz E Class E280 -> بنز کلاس E E280
  - Mercedes-Benz E Class E300 -> بنز کلاس E E300
  - Mercedes-Benz E Class E350 -> بنز کلاس E E350
  - Mercedes-Benz GLA Class -> بنز کلاس GLA
  - Mercedes-Benz GLA Class GLA250 -> بنز کلاس GLA GLA250
  - Mercedes-Benz GLA Class GLA45 -> بنز کلاس GLA GLA45
  - Mercedes-Benz GLK Class -> بنز کلاس GLK
  - Mercedes-Benz GLK Class GLK350 -> بنز کلاس GLK GLK350
  - Mercedes-Benz ML Class -> بنز کلاس ML
  - Mercedes-Benz ML Class ML350 -> بنز کلاس ML ML350
  - Mercedes-Benz S Class -> بنز کلاس S
  - Mercedes-Benz S Class S280 -> بنز کلاس S S280
  - Mercedes-Benz S Class S300 -> بنز کلاس S S300
  - Mercedes-Benz S Class S320 -> بنز کلاس S S320
  - Mercedes-Benz S Class S350 -> بنز کلاس S S350
  - Mercedes-Benz S Class S500 -> بنز کلاس S S500
  - Mercedes-Benz S Class SE -> بنز کلاس S SE
  - Mercedes-Benz SL Class -> بنز کلاس SL
  - Mercedes-Benz SL Class SL350 -> بنز کلاس SL SL350
  - Mercedes-Benz SL Class SL500 -> بنز کلاس SL SL500
  - Mercedes-Benz SLC Class -> بنز کلاس SLC
  - Mercedes-Benz SLK Class -> بنز کلاس SLK
  - Mercedes-Benz SLK Class SLK200 -> بنز کلاس SLK SLK200
  - Mercedes-Benz SLK Class SLK280 -> بنز کلاس SLK SLK280
  - Mercedes-Benz SLK Class SLK350 -> بنز کلاس SLK SLK350
  - Mercedes-Benz Classic -> بنز کلاسیک
  - Borgward -> بورگوارد
  - Borgward BX5 -> بورگوارد BX5
  - Borgward BX5 Ultimate -> بورگوارد BX5 التیمیت
  - Borgward BX7 -> بورگوارد BX7
  - Borgward BX7 Ultimate -> بورگوارد BX7 التیمیت
  - BMW -> بی‌ام‌و
  - BMW 2002 -> بی‌ام‌و 2002
  - BMW 1 Series Convertible -> بی‌ام‌و سری 1 کروک
  - BMW 1 Series Convertible 120i -> بی‌ام‌و سری 1 کروک 120i
  - BMW 1 Series Convertible 125i -> بی‌ام‌و سری 1 کروک 125i
  - BMW 1 Series Coupe -> بی‌ام‌و سری 1 کوپه
  - BMW 1 Series Hatchback -> بی‌ام‌و سری 1 هاچبک
  - BMW 1 Series Hatchback 118i -> بی‌ام‌و سری 1 هاچبک 118i
  - BMW 1 Series Hatchback 120i -> بی‌ام‌و سری 1 هاچبک 120i
  - BMW 1 Series Hatchback 125i -> بی‌ام‌و سری 1 هاچبک 125i
  - BMW 2 Series Activetourer -> بی‌ام‌و سری 2 اکتیوتور
  - BMW 2 Series Activetourer 218i -> بی‌ام‌و سری 2 اکتیوتور 218i
  - BMW 2 Series Convertible -> بی‌ام‌و سری 2 کروک
  - BMW 2 Series Convertible 220i -> بی‌ام‌و سری 2 کروک 220i
  - BMW 2 Series Convertible 230i -> بی‌ام‌و سری 2 کروک 230i
  - BMW 2 Series Coupe -> بی‌ام‌و سری 2 کوپه
  - BMW 2 Series Coupe 220i -> بی‌ام‌و سری 2 کوپه 220i
  - BMW 2 Series Coupe 230i -> بی‌ام‌و سری 2 کوپه 230i
  - BMW 3 Series Sedan -> بی‌ام‌و سری 3 سدان
  - BMW 3 Series Sedan 316i -> بی‌ام‌و سری 3 سدان 316i
  - BMW 3 Series Sedan 318i-automatic -> بی‌ام‌و سری 3 سدان 318i اتوماتیک
  - BMW 3 Series Sedan 318i-manual -> بی‌ام‌و سری 3 سدان 318i دنده‌ای
  - BMW 3 Series Sedan 320i -> بی‌ام‌و سری 3 سدان 320i
  - BMW 3 Series Sedan 325i -> بی‌ام‌و سری 3 سدان 325i
  - BMW 3 Series Sedan 328i -> بی‌ام‌و سری 3 سدان 328i
  - BMW 3 Series Sedan 330i -> بی‌ام‌و سری 3 سدان 330i
  - BMW 3 Series Convertible -> بی‌ام‌و سری 3 کروک
  - BMW 3 Series Convertible 320i -> بی‌ام‌و سری 3 کروک 320i
  - BMW 3 Series Convertible 325i -> بی‌ام‌و سری 3 کروک 325i
  - BMW 3 Series Convertible 330i -> بی‌ام‌و سری 3 کروک 330i
  - BMW 3 Series Convertible 335i -> بی‌ام‌و سری 3 کروک 335i
  - BMW 3 Series Coupe -> بی‌ام‌و سری 3 کوپه
  - BMW 3 Series Coupe 320i -> بی‌ام‌و سری 3 کوپه 320i
  - BMW 3 Series Coupe 325i -> بی‌ام‌و سری 3 کوپه 325i
  - BMW 3 Series Coupe 330i -> بی‌ام‌و سری 3 کوپه 330i
  - BMW 3 Series Coupe 335i -> بی‌ام‌و سری 3 کوپه 335i
  - BMW 3 Series GT -> بی‌ام‌و سری 3 GT
  - BMW 3 Series GT 328i -> بی‌ام‌و سری 3 GT 328i
  - BMW 4 Series Convertible -> بی‌ام‌و سری 4 کروک
  - BMW 4 Series Convertible 428i -> بی‌ام‌و سری 4 کروک 428i
  - BMW 4 Series Coupe -> بی‌ام‌و سری 4 کوپه
  - BMW 4 Series Coupe 420i -> بی‌ام‌و سری 4 کوپه 420i
  - BMW 4 Series Coupe 428i -> بی‌ام‌و سری 4 کوپه 428i
  - BMW 4 Series Grancoupe -> بی‌ام‌و سری 4 گرن کوپه
  - BMW 4 Series Grancoupe 420i -> بی‌ام‌و سری 4 گرن کوپه 420i
  - BMW 4 Series Grancoupe 428i -> بی‌ام‌و سری 4 گرن کوپه 428i
  - BMW 5 Series Sedan -> بی‌ام‌و سری 5 سدان
  - BMW 5 Series Sedan 518 -> بی‌ام‌و سری 5 سدان 518
  - BMW 5 Series Sedan 520i -> بی‌ام‌و سری 5 سدان 520i
  - BMW 5 Series Sedan 523i -> بی‌ام‌و سری 5 سدان 523i
  - BMW 5 Series Sedan 525i -> بی‌ام‌و سری 5 سدان 525i
  - BMW 5 Series Sedan 528i -> بی‌ام‌و سری 5 سدان 528i
  - BMW 5 Series Sedan 530i -> بی‌ام‌و سری 5 سدان 530i
  - BMW 5 Series Sedan 530xi -> بی‌ام‌و سری 5 سدان 530xi
  - BMW 5 Series Sedan 535i -> بی‌ام‌و سری 5 سدان 535i
  - BMW 5 Series Sedan 540i -> بی‌ام‌و سری 5 سدان 540i
  - BMW 5 Series Sedan 550i -> بی‌ام‌و سری 5 سدان 550i
  - BMW 5 Series GT -> بی‌ام‌و سری 5 GT
  - BMW 5 Series GT 528i -> بی‌ام‌و سری 5 GT 528i
  - BMW 5 Series GT 535i -> بی‌ام‌و سری 5 GT 535i
  - BMW 6 Series Convertible -> بی‌ام‌و سری 6 کروک
  - BMW 6 Series Convertible 630i -> بی‌ام‌و سری 6 کروک 630i
  - BMW 6 Series Convertible 650i -> بی‌ام‌و سری 6 کروک 650i
  - BMW 6 Series Convertible M6 -> بی‌ام‌و سری 6 کروک M6
  - BMW 6 Series Coupe -> بی‌ام‌و سری 6 کوپه
  - BMW 6 Series Coupe 630i -> بی‌ام‌و سری 6 کوپه 630i
  - BMW 6 Series Coupe 640i -> بی‌ام‌و سری 6 کوپه 640i
  - BMW 6 Series Coupe 650i -> بی‌ام‌و سری 6 کوپه 650i
  - BMW 6 Series Grancoupe -> بی‌ام‌و سری 6 گرن کوپه
  - BMW 6 Series Grancoupe 640i -> بی‌ام‌و سری 6 گرن کوپه 640i
  - BMW 6 Series Grancoupe 650i -> بی‌ام‌و سری 6 گرن کوپه 650i
  - BMW 6 Series Grancoupe M6 -> بی‌ام‌و سری 6 گرن کوپه M6
  - BMW 7 Series -> بی‌ام‌و سری 7
  - BMW 7 Series 730i -> بی‌ام‌و سری 7 730i
  - BMW 7 Series 730li -> بی‌ام‌و سری 7 730li
  - BMW 7 Series 740li -> بی‌ام‌و سری 7 740li
  - BMW 7 Series 750li -> بی‌ام‌و سری 7 750li
  - BMW Classic -> بی‌ام‌و کلاسیک
  - BMW i8 -> بی‌ام‌و i8
  - BMW X1 -> بی‌ام‌و X1
  - BMW X1 18i -> بی‌ام‌و X1 18i
  - BMW X1 20i -> بی‌ام‌و X1 20i
  - BMW X1 25i -> بی‌ام‌و X1 25i
  - BMW X1 28i -> بی‌ام‌و X1 28i
  - BMW X3 -> بی‌ام‌و X3
  - BMW X3 25i -> بی‌ام‌و X3 25i
  - BMW X3 28i -> بی‌ام‌و X3 28i
  - BMW X3 30i -> بی‌ام‌و X3 30i
  - BMW X3 35i -> بی‌ام‌و X3 35i
  - BMW X4 -> بی‌ام‌و X4
  - BMW X4 28i -> بی‌ام‌و X4 28i
  - BMW X5 -> بی‌ام‌و X5
  - BMW X5 50i -> بی‌ام‌و X5 50i
  - BMW X6 -> بی‌ام‌و X6
  - BMW X6 35i -> بی‌ام‌و X6 35i
  - BMW X6 50i -> بی‌ام‌و X6 50i
  - BMW Z3 -> بی‌ام‌و z3
  - BMW Z4 -> بی‌ام‌و Z4
  - BMW Z4 20i -> بی‌ام‌و Z4 20i
  - BMW Z4 23i -> بی‌ام‌و Z4 23i
  - BMW Z4 28i -> بی‌ام‌و Z4 28i
  - BMW Z4 30i -> بی‌ام‌و Z4 30i
  - BMW Z4 35i -> بی‌ام‌و Z4 35i
  - BISU -> بیسو
  - BISU T3 -> بیسو T3
  - BISU T5 -> بیسو T5
  - BYD -> بی‌‌وای‌دی
  - BYD F3 -> بی‌‌وای‌دی F3
  - BYD S6 -> بی‌‌وای‌دی S6
  - BYD S7 -> بی‌‌وای‌دی S7
  - Buick -> بیوک
  - Buick B2 -> بیوک B2
  - Buick B3 -> بیوک B3
  - Buick B3-ir -> بیوک B3 مونتاژ
  - Pazhan -> پاژن
  - Pazhan 2 door -> پاژن 2 در
  - Pazhan 4 door -> پاژن 4 در
  - Pazhan 4 door 4 cylinder-4 door -> پاژن 4 در 4 سیلندر
  - Pazhan 4 door 6 cylinder-4 door -> پاژن 4 در 6 سیلندر
  - Pazhan Herour -> پاژن هرور
  - Pride -> پراید
  - Pride 111 -> پراید 111
  - Pride 111 EX -> پراید 111 EX
  - Pride 111 SE -> پراید 111 SE
  - Pride 111 SL -> پراید 111 SL
  - Pride 111 SX -> پراید 111 SX
  - Pride 131 -> پراید 131
  - Pride 131 Bi-fuel -> پراید 131 دوگانه سوز
  - Pride 131 EX -> پراید 131 EX
  - Pride 131 LE -> پراید 131 LE
  - Pride 131 SE -> پراید 131 SE
  - Pride 131 SL -> پراید 131 SL
  - Pride 131 SX -> پراید 131 SX
  - Pride 131 TL -> پراید 131 TL
  - Pride 132 -> پراید 132
  - Pride 132 Bi-fuel -> پراید 132 دوگانه سوز
  - Pride 132 basic -> پراید 132 ساده
  - Pride 132 EX -> پراید 132 EX
  - Pride 132 SE -> پراید 132 SE
  - Pride 132 SL -> پراید 132 SL
  - Pride 132 SX -> پراید 132 SX
  - Pride 141 -> پراید 141
  - Pride 141 Bi-fuel -> پراید 141 دوگانه سوز
  - Pride 141 basic -> پراید 141 ساده
  - Pride 141 EX -> پراید 141 EX
  - Pride 141 SE -> پراید 141 SE
  - Pride 141 SL -> پراید 141 SL
  - Pride 141 SX -> پراید 141 SX
  - Pride Automatic -> پراید اتوماتیک
  - Pride Station -> پراید سفری
  - Pride Sedan -> پراید صندوق‌دار
  - Pride Sedan petrol -> پراید صندوق‌دار بنزینی
  - Pride Sedan CNG -> پراید صندوق‌دار CNG
  - Pride Sedan LPG -> پراید صندوق‌دار LPG
  - Pride Hatchback -> پراید هاچبک
  - Proton -> پروتون
  - Proton Impian -> پروتون ایمپین
  - Proton Gen-2 -> پروتون جن تو
  - Proton Gen-2 automatic -> پروتون جن تو اتوماتیک
  - Proton Gen-2 manual -> پروتون جن تو دنده‌ای
  - Proton Viera -> پروتون ویرا
  - Proton Viera automatic -> پروتون ویرا اتوماتیک
  - Proton Viera manual -> پروتون ویرا دنده‌ای
  - Peugeot -> پژو
  - Peugeot 2008 -> پژو 2008
  - Peugeot 205 -> پژو 205
  - Peugeot 206 -> پژو 206
  - Peugeot 206 1 -> پژو 206 تیپ ۱
  - Peugeot 206 2 -> پژو 206 تیپ ۲
  - Peugeot 206 3 -> پژو 206 تیپ ۳
  - Peugeot 206 3P -> پژو 206 تیپ ۳ پانوراما
  - Peugeot 206 4 -> پژو 206 تیپ ۴
  - Peugeot 206 5 -> پژو 206 تیپ ۵
  - Peugeot 206 6 -> پژو 206 تیپ ۶
  - Peugeot 206 SD -> پژو 206 SD
  - Peugeot 206 SD V1 -> پژو 206 SD V1
  - Peugeot 206 SD V10 -> پژو 206 SD V10
  - Peugeot 206 SD V19 -> پژو 206 SD V19
  - Peugeot 206 SD V2 -> پژو 206 SD V2
  - Peugeot 206 SD V20 -> پژو 206 SD V20
  - Peugeot 206 SD V6 -> پژو 206 SD V6
  - Peugeot 206 SD V8 -> پژو 206 SD V8
  - Peugeot 206 SD V9 -> پژو 206 SD V9
  - Peugeot 207i -> پژو 207i
  - Peugeot 207i automatic -> پژو 207i اتوماتیک
  - Peugeot 207i automatic MC -> پژو 207i اتوماتیک MC
  - Peugeot 207i Automatic TU5P -> پژو 207i اتوماتیک TU5P
  - Peugeot 207i Automatic P -> پژو 207i پانوراما اتوماتیک
  - Peugeot 207i Automatic P TU5P -> پژو 207i پانوراما اتوماتیک TU5P
  - Peugeot 207i Manual P -> پژو 207i پانوراما دنده‌ای
  - Peugeot 207i manual -> پژو 207i دنده‌ای
  - Peugeot 207i SD -> پژو 207i SD
  - Peugeot 207i SD automatic -> پژو 207i SD اتوماتیک
  - Peugeot 207i SD manual -> پژو 207i SD دنده‌ای
  - Peugeot 301 -> پژو 301
  - Peugeot 404 -> پژو 404
  - Peugeot 405 -> پژو 405
  - Peugeot 405 station -> پژو 405 استیشن
  - Peugeot 405 GLX-TU5-Petrol -> پژو 405 بنزینی GLX - TU5
  - Peugeot 405 GLX-TU5-Bi-fuel -> پژو 405 دوگانه سوز GLX - TU5
  - Peugeot 405 GL-Bi-fuel(CNG) -> پژو 405 GL - دوگانه سوز CNG
  - Peugeot 405 GL-Bi-fuel(LPG) -> پژو 405 GL - دوگانه سوز LPG
  - Peugeot 405 GL-petrol -> پژو 405 GL بنزینی
  - Peugeot 405 GLi-Bi-fuel(CNG) -> پژو 405 GLi - دوگانه سوز CNG
  - Peugeot 405 GLi-Bi-fuel(LPG) -> پژو 405 GLi - دوگانه سوز LPG
  - Peugeot 405 GLi-petrol -> پژو 405 GLi بنزینی
  - Peugeot 405 GLX-Bi-fuel(CNG) -> پژو 405 GLX - دوگانه سوز CNG
  - Peugeot 405 GLX-Bi-fuel(LPG) -> پژو 405 GLX - دوگانه سوز LPG
  - Peugeot 405 GLX-petrol -> پژو 405 GLX بنزینی
  - Peugeot 405 SLX -> پژو 405 SLX بنزینی
  - Peugeot 405 SLX-Bi-fuel -> پژو 405 SLX دوگانه سوز
  - Peugeot 406 -> پژو 406
  - Peugeot 407 -> پژو 407
  - Peugeot 504 -> پژو 504
  - Peugeot 508 -> پژو 508
  - Peugeot 508 GT -> پژو 508 GT
  - Peugeot Pars -> پژو پارس
  - Peugeot Pars automatic-TU5 -> پژو پارس اتوماتیک TU5
  - Peugeot Pars Bi-fuel -> پژو پارس دوگانه سوز
  - Peugeot Pars basic -> پژو پارس ساده
  - Peugeot Pars latest -> پژو پارس سال
  - Peugeot Limousine -> پژو پارس لیموزین
  - Peugeot Pars XU7P -> پژو پارس موتور جدید XU7P
  - Peugeot Pars XU7P-ELX -> پژو پارس موتور جدید XU7P (سفارشی)
  - Peugeot Pars ELX -> پژو پارس ELX
  - Peugeot Pars ELX-TU5 -> پژو پارس ELX (سفارشی) TU5
  - Peugeot Pars ELX XUM -> پژو پارس ELX XUM
  - Peugeot Pars LX-TU5 -> پژو پارس LX TU5
  - Peugeot Roa -> پژو روآ
  - Peugeot Roa Petrol -> پژو روآ بنزینی
  - Peugeot Roa Bi-fuel -> پژو روآ دوگانه سوز
  - Peugeot Roa Sal -> پژو روآ سال
  - Peugeot Roa Sal petrol -> پژو روآ سال بنزینی
  - Peugeot Roa Sal Bi-fuel -> پژو روآ سال دوگانه سوز
  - Peugeot RD -> پژو RD
  - Peugeot RD petrol -> پژو RD بنزینی
  - Peugeot RD Bi-fuel(CNG) -> پژو RD دوگانه سوز CNG
  - Peugeot RD Bi-fuel(LPG) -> پژو RD دوگانه سوز LPG
  - Peugeot RDI -> پژو RDI
  - Peugeot RDI petrol -> پژو RDI بنزینی
  - Porsche -> پورشه
  - Porsche 911 -> پورشه 911
  - Porsche 911 Carrera 4 -> پورشه 911 کررا 4
  - Porsche 911 Carrera S -> پورشه 911 کررا s
  - Porsche Boxster -> پورشه باکستر
  - Porsche Boxster 718 -> پورشه باکستر 718
  - Porsche Boxster 718 S -> پورشه باکستر 718 S
  - Porsche Boxster V6 -> پورشه باکستر V6
  - Porsche Boxster V6 S -> پورشه باکستر V6 S
  - Porsche Panamera -> پورشه پانامرا
  - Porsche Panamera 4S -> پورشه پانامرا 4S
  - Porsche Panamera 4S turbo -> پورشه پانامرا 4S توربو
  - Porsche Panamera V6 -> پورشه پانامرا V6
  - Porsche Cayenne -> پورشه کاین
  - Porsche Cayenne GTS -> پورشه کاین GTS
  - Porsche Cayenne S -> پورشه کاین S
  - Porsche Cayenne S turbo -> پورشه کاین S توربو
  - Porsche Cayenne V6 -> پورشه کاین V6
  - Porsche Cayman -> پورشه کیمن
  - Porsche Cayman S -> پورشه کیمن S
  - Porsche Macan -> پورشه ماکان
  - Pontiac -> پونتیاک
  - Pontiac Parisienne -> پونتیاک پاریزین
  - Pontiac Grandprix -> پونتیاک گرند پریکس
  - Rich Rich -> پیکاپ ریچ دوکابین
  - Paykan -> پیکان
  - Paykan Petrol -> پیکان بنزینی
  - Paykan Bi-fuel(CNG) -> پیکان دوگانه سوز CNG
  - Paykan Bi-fuel(LPG) -> پیکان دوگانه سوز LPG
  - Paykan Pickup -> پیکان وانت
  - Paykan Pickup Petrol -> پیکان وانت بنزینی
  - Paykan Pickup CNG -> پیکان وانت CNG
  - Paykan Pickup LPG -> پیکان وانت LPG
  - Tara -> تارا
  - Tara Automatic -> تارا اتوماتیک
  - Tara Manual -> تارا دنده‌ای
  - Toyota -> تویوتا
  - Toyota Aurion -> تویوتا آریون
  - Toyota Aurion sport -> تویوتا آریون اسپرت
  - Toyota Aurion grand -> تویوتا آریون گرند
  - Toyota FJ Cruiser -> تویوتا اف جی کروزر
  - Toyota Echo -> تویوتا اکو
  - Toyota Prado 2door -> تویوتا پرادو ۲ در
  - Toyota Prado 2door 4 cylinder -> تویوتا پرادو ۲ در ۴ سلیندر
  - Toyota Prado 2door 6 cylinder -> تویوتا پرادو ۲ در ۶ سلیندر
  - Toyota Prado 4door -> تویوتا پرادو ۴ در
  - Toyota Prado 4door 4 cylinder -> تویوتا پرادو ۴ در ۴ سلیندر
  - Toyota Prado 4door 6 cylinder -> تویوتا پرادو ۴ در ۶ سلیندر
  - Toyota Prado 4door 6 cylinder-off road -> تویوتا پرادو ۴ در ۶ سلیندر آفرود
  - Toyota Prado 4door 6 cylinder-on road -> تویوتا پرادو ۴ در ۶ سلیندر آنرود
  - Toyota Prius -> تویوتا پریوس
  - Toyota Prius 2 -> تویوتا پریوس 2
  - Toyota Prius 3 -> تویوتا پریوس 3
  - Toyota Prius A -> تویوتا پریوس A
  - Toyota Prius B -> تویوتا پریوس B
  - Toyota Prius C -> تویوتا پریوس C
  - Toyota Rav4 -> تویوتا راوفور
  - Toyota Celica -> تویوتا سلیکا
  - Toyota Supra -> تویوتا سوپرا
  - Toyota Solara -> تویوتا سولارا
  - Toyota 4runner -> تویوتا فررانر
  - Toyota Furtuner -> تویوتا فورچونر
  - Toyota Carina -> تویوتا کارینا
  - Toyota Crown -> تویوتا کراون
  - Toyota Corolla -> تویوتا کرولا
  - Toyota Corolla GLI-automatic-1800cc -> تویوتا کرولا اتوماتیک GLI - 1800cc
  - Toyota Corolla XLI-automatic-1800cc -> تویوتا کرولا اتوماتیک XLI - 1800cc
  - Toyota Corolla GLI-manual-1800cc -> تویوتا کرولا دنده‌ای GLI - 1800cc
  - Toyota Corolla XLI-manual-1800cc -> تویوتا کرولا دنده‌ای XLI - 1800cc
  - Toyota Corolla GLI-2000cc -> تویوتا کرولا GLI 2000cc
  - Toyota Corolla SE-1600cc -> تویوتا کرولا SE 1600cc
  - Toyota Corolla XLI-2000cc -> تویوتا کرولا XLI 2000cc
  - Toyota Corona -> تویوتا کرونا
  - Toyota Cressida -> تویوتا کریسیدا
  - Toyota Camry -> تویوتا کمری
  - Toyota Camry Aurion -> تویوتا کمری اتاق آریون
  - Toyota Camry manual -> تویوتا کمری دنده‌ای
  - Toyota Camry Grand-4 cylinder -> تویوتا کمری گرند 4 سیلندر
  - Toyota Camry Grand-6 cylinder -> تویوتا کمری گرند 6 سیلندر
  - Toyota Camry GL -> تویوتا کمری GL
  - Toyota Camry GLX -> تویوتا کمری GLX
  - Toyota Camry LE -> تویوتا کمری LE
  - Toyota Camry hybrid-LE -> تویوتا کمری LE هیبرید
  - Toyota Camry SE -> تویوتا کمری SE
  - Toyota Camry hybrid-XLE -> تویوتا کمری XLE هیبرید
  - Toyota Landcruiser 2door -> تویوتا لندکروزر ۲ در
  - Toyota Landcruiser 2door 2F -> تویوتا لندکروزر ۲ در 2F
  - Toyota Landcruiser 2door 3F -> تویوتا لندکروزر ۲ در 3F
  - Toyota Landcruiser 4door -> تویوتا لندکروزر ۴ در
  - Toyota Landcruiser 4door 4000cc -> تویوتا لندکروزر ۴ در 4000cc
  - Toyota Landcruiser 4door 4500cc -> تویوتا لندکروزر ۴ در 4500cc
  - Toyota Landcruiser 4door 4700cc -> تویوتا لندکروزر ۴ در 4700cc
  - Toyota Landcruiser 4door 5700cc -> تویوتا لندکروزر ۴ در 5700cc
  - Toyota Hilux single cabin -> تویوتا هایلوکس تک کابین
  - Toyota Hilux double cabin -> تویوتا هایلوکس دو کابین
  - Toyota Hilux double cabin automatic -> تویوتا هایلوکس دو کابین اتوماتیک
  - Toyota Hilux double cabin high -> تویوتا هایلوکس دو کابین بلند
  - Toyota Hilux double cabin high automatic -> تویوتا هایلوکس دو کابین بلند اتوماتیک
  - Toyota Hilux double cabin high manual -> تویوتا هایلوکس دو کابین بلند دنده‌ای
  - Toyota Hilux double cabin manual -> تویوتا هایلوکس دو کابین دنده‌ای
  - Toyota Yaris Sedan -> تویوتا یاریس صندوق دار
  - Toyota Yaris Sedan 1300cc -> تویوتا یاریس صندوق دار 1300cc
  - Toyota Yaris Sedan 1500cc -> تویوتا یاریس صندوق دار 1500cc
  - Toyota Yaris Hatchback -> تویوتا یاریس هاچبک
  - Toyota Yaris Hatchback 1300cc -> تویوتا یاریس هاچبک 1300cc
  - Toyota Yaris Hatchback 1500cc -> تویوتا یاریس هاچبک 1500cc
  - Toyota Yaris Hatchback Hybrid -> تویوتا یاریس هاچبک هیبرید
  - Toyota C-HR -> تویوتا C-HR
  - Toyota C-HR Petrol Singledifferential -> تویوتا C-HR بنزینی تک دیفرانسیل
  - Toyota C-HR Petrol doubledifferential -> تویوتا C-HR بنزینی دو دیفرانسیل
  - Toyota C-HR hybrid -> تویوتا C-HR هیبرید
  - Toyota GT86 -> تویوتا GT 86
  - Toyota GT86 automatic -> تویوتا GT 86 اتوماتیک
  - Toyota GT86 manual -> تویوتا GT 86 دنده‌ای
  - Tiba -> تیبا
  - Tiba Sedan -> تیبا صندوق‌دار
  - Tiba Sedan Plus -> تیبا صندوق‌دار پلاس
  - Tiba Sedan EX -> تیبا صندوق‌دار EX
  - Tiba Sedan EX Bi-fuel -> تیبا صندوق‌دار EX دوگانه سوز
  - Tiba Sedan SL -> تیبا صندوق‌دار LX
  - Tiba Sedan LX Bi-fuel -> تیبا صندوق‌دار LX دوگانه سوز
  - Tiba Sedan SX -> تیبا صندوق‌دار SX
  - Tiba Sedan SX Bi-fuel -> تیبا صندوق‌دار SX دوگانه سوز
  - Tiba Hatchback -> تیبا هاچبک
  - Tiba Hatchback Plus -> تیبا هاچبک پلاس
  - Tiba Hatchback EX -> تیبا هاچبک EX
  - Tiba Hatchback SX -> تیبا هاچبک SX
  - Tigard -> تیگارد
  - JAC -> جک
  - JAC J3 Sedan -> جک J3 سدان
  - JAC J3 Hatchback -> جک J3 هاچبک
  - JAC J4 -> جک J4
  - JAC J5 -> جک J5
  - JAC J5 automatic-1500cc -> جک J5 اتوماتیک 1800cc
  - JAC J5 manual-1500cc -> جک J5 دنده‌ای 1500cc
  - JAC S3 -> جک S3
  - JAC S3 automatic -> جک S3 اتوماتیک
  - JAC S5 -> جک S5
  - JAC S5 automatic -> جک S5 اتوماتیک
  - JAC S5 manual -> جک S5 دنده‌ای
  - JAC S5 New Face -> جک S5 نیوفیس
  - Jaguar -> جگوار
  - Jaguar XJ -> جگوار XJ
  - Joylong -> جوی لانگ
  - JMC -> جی‌ام‌سی
  - JMC S350 -> جی‌ام‌سی S350
  - GAC Gonow -> جی‌ای‌سی گونو
  - GAC Gonow G5 -> جی‌ای‌سی گونو G5
  - GAC Gonow GA3S -> جی‌ای‌سی گونو GA3S
  - GAC Gonow GS5 -> جی‌ای‌سی گونو GS5
  - Jeep -> جیپ
  - Jeep Ahoo -> جیپ آهو
  - Jeep Cherokee -> جیپ چروکی
  - Jeep Wrangler -> جیپ رنگلر
  - Jeep Renegade -> جیپ رنه گید
  - Jeep Shahbaz -> جیپ شهباز
  - Jeep Sahra -> جیپ صحرا
  - Jeep Mute -> جیپ میوت
  - Jeep Wagoneer -> جیپ واگونیر
  - Jeep KM -> جیپ KM
  - Geely -> جیلی
  - Geely Emgrand 7 -> جیلی Emgrand 7
  - Geely Emgrand 7 automatic -> جیلی Emgrand 7 اتوماتیک
  - Geely Emgrand 7 manual -> جیلی Emgrand 7 دنده‌ای
  - Geely Emgrand 7_RV -> جیلی Emgrand 7_RV
  - Geely Emgrand 7_RV automatic -> جیلی Emgrand 7_RV اتوماتیک
  - Geely Emgrand 7_RV manual -> جیلی Emgrand 7_RV دنده‌ای
  - Geely Emgrand X7 -> جیلی Emgrand X7
  - Geely GC6 -> جیلی GC6
  - Geely GC6 excellent -> جیلی GC6 اکسلنت
  - Geely GC6 elite -> جیلی GC6 الیت
  - Changan -> چانگان
  - Changan CS35 -> چانگان CS35
  - Changan CS35-ir -> چانگان CS35 مونتاژ
  - Changan EADO -> چانگان EADO
  - Chery -> چری
  - Chery Arrizo 5 -> چری آریزو 5
  - Chery Arrizo 5 automatic-excellent -> چری آریزو 5 اتوماتیک اکسلنت
  - Chery Arrizo 5 automati-luxury -> چری آریزو 5 اتوماتیک لاکچری
  - Chery Arrizo 5 manual-luxury -> چری آریزو 5 دنده‌ای لاکچری
  - Chery Arrizo 5IE New -> چری آریزو 5IE جدید
  - Chery Arrizo 5IE New Turbo -> چری آریزو 5IE جدید توربو
  - Chery Arrizo 5TE -> چری آریزو 5TE
  - Chery Arrizo 5TE turbo-excellent -> چری آریزو 5TE اکسلنت توربو
  - Chery Arrizo 6 -> چری آریزو 6
  - Chery Arrizo 6 excellent -> چری آریزو 6 اکسلنت
  - Chery Tiggo 5 -> چری تیگو 5
  - Chery Tiggo 5 excellent -> چری تیگو 5 اکسلنت
  - Chery Tiggo 5 luxury -> چری تیگو 5 لاکچری
  - Chery Tiggo 5 luxury-sport -> چری تیگو 5 لاکچری اسپرت
  - Chery Tiggo 5 IE -> چری تیگو 5 IE
  - Chery Tiggo 5 IL -> چری تیگو 5 IL
  - Chery Tiggo 5 TE -> چری تیگو 5 TE توربو
  - Chery Tiggo 7 -> چری تیگو 7
  - Chery Tiggo 7 excellent -> چری تیگو 7 اکسلنت
  - Chery Tiggo 7 IE -> چری تیگو 7 IE
  - Chery Viana A15 -> چری ویانا A15
  - Datsun -> داتسون
  - Domy -> دامای
  - Domy X7 -> دامای X7
  - Dongfeng -> دانگ فنگ
  - Dongfeng H30 -> دانگ فنگ H30 کراس
  - Dongfeng S30 -> دانگ فنگ S30
  - Dayun -> دایون
  - Dayun Y5 -> دایون Y5
  - Dayun Y5 Plus -> دایون Y5 پلاس
  - Daihatsu -> دایهاتسو
  - Delica -> دلیکا
  - Dena -> دنا
  - Dena plus -> دنا پلاس
  - Dena plus Manual 6 Turbo -> دنا پلاس 6 دنده توربو
  - Dena plus 1700cc Automatic -> دنا پلاس اتوماتیک
  - Dena plus Turbo 1 -> دنا پلاس تیپ ۱ توربو
  - Dena plus Manual 1 -> دنا پلاس تیپ ۱ دنده‌ای
  - Dena plus 1700cc-turbo -> دنا پلاس تیپ ۲ توربو
  - Dena plus 1700cc Manual -> دنا پلاس تیپ ۲ دنده‌ای
  - Dena basic -> دنا معمولی
  - Dena basic 1700cc -> دنا معمولی تیپ ۱
  - Dena basic 2 -> دنا معمولی تیپ ۲
  - Dodge -> دوج
  - Dodge Coronet -> دوج کرنت
  - Daewoo -> دوو
  - Daewoo Espero -> دوو اسپرو
  - Daewoo Espero automatic -> دوو اسپرو اتوماتیک
  - Daewoo Espero manual -> دوو اسپرو دنده‌ای
  - Daewoo Racer -> دوو ریسر
  - Daewoo Racer hatchback -> دوو ریسر هاچبک
  - Daewoo Racer GTE -> دوو ریسر GTE
  - Daewoo Racer GTI -> دوو ریسر GTI
  - Daewoo Cielo -> دوو سی یلو
  - Daewoo Cielo sedan -> دوو سی یلو سدان
  - Daewoo Cielo hatchback -> دوو سی یلو هاچبک
  - Daewoo Matiz -> دوو ماتیز
  - DS -> دی‌اس
  - DS 3 -> دی‌اس 3
  - DS 5 -> دی‌اس 5
  - DS 5LS -> دی‌اس 5LS
  - DS 6 -> دی‌اس 6
  - DS Crossback-4 -> دی‌اس کراس بک 4
  - DS crossback-7 -> دی‌اس کراس بک 7
  - DS crossback-7 opera -> دی‌اس کراس بک 7 اپرا
  - DS crossback-7 rivoli -> دی‌اس کراس بک 7 ریولی
  - Dignity -> دیگنیتی
  - Deer -> دییر
  - Runna -> رانا
  - Runna Plus -> رانا پلاس
  - Runna Plus P -> رانا پلاس پانوراما
  - Runna EL -> رانا EL
  - Runna LX -> رانا LX
  - Rayen -> راین
  - Rayen R3 -> راین R3
  - Rayen V5 -> راین V5
  - Rayen V5 automatic -> راین V5 اتوماتیک
  - Rayen V5 manual -> راین V5 دنده‌ای
  - Renault -> رنو
  - Renault 21 -> رنو 21
  - Renault 5 -> رنو 5
  - Renault 5-ir -> رنو 5 مونتاژ
  - Renault Scala -> رنو اسکالا
  - Renault Scala 1600cc -> رنو اسکالا 1600cc
  - Renault Scala convertible -> رنو اسکالا کروک
  - Renault Scala E2 -> رنو اسکالا E2
  - Renault Scala E4 -> رنو اسکالا E4
  - Renault Pars Tondar -> رنو پارس تندر
  - Renault Pars Tondar manual -> رنو پارس تندر دنده‌ای
  - Renault PK -> رنو پی کی
  - Renault Talisman -> رنو تلیسمان
  - Renault Talisman E2 -> رنو تلیسمان E2
  - Renault Talisman E3 -> رنو تلیسمان E3
  - Renault Tondar 90 -> رنو تندر 90
  - Renault Tondar 90 automatic -> رنو تندر 90 اتوماتیک
  - Renault Tondar 90 station -> رنو تندر 90 استیشن (لوگان)
  - Renault Tondar 90 plus -> رنو تندر 90 پلاس
  - Renault Tondar 90 plus automatic -> رنو تندر 90 پلاس اتوماتیک
  - Renault Tondar 90 plus manual -> رنو تندر 90 پلاس دنده‌ای
  - Renault Tondar 90 E0-petrol -> رنو تندر 90 E0 بنزینی
  - Renault Tondar 90 E0-Bi-fuel -> رنو تندر 90 E0 دوگانه سوز
  - Renault Tondar 90 E1-petrol -> رنو تندر 90 E1 بنزینی
  - Renault Tondar 90 E1-Bi-fuel -> رنو تندر 90 E1 دوگانه سوز
  - Renault Tondar 90 E2-petrol -> رنو تندر 90 E2 بنزینی
  - Renault Tondar 90 E2-Bi-fuel -> رنو تندر 90 E2 دوگانه سوز
  - Renault Duster -> رنو داستر
  - Renault Duster PE Singledifferential -> رنو داستر PE تک دیفرانسیل
  - Renault Duster PE doubledifferential -> رنو داستر PE دو دیفرانسیل
  - Renault Duster SE Singledifferential -> رنو داستر SE تک دیفرانسیل
  - Renault Duster SE doubledifferential -> رنو داستر SE دو دیفرانسیل
  - Renault Sandero -> رنو ساندرو
  - Renault Sandero automatic -> رنو ساندرو اتوماتیک
  - Renault Sandero-Stepway -> رنو ساندرو استپ‌وی
  - Renault Sandero-Stepway automatic -> رنو ساندرو استپ‌وی اتوماتیک
  - Renault Sandero-Stepway manual -> رنو ساندرو استپ‌وی دنده‌ای
  - Renault Sandero manual -> رنو ساندرو دنده‌ای
  - Renault Sepand -> رنو سپند
  - Renault Safrane -> رنو سفران
  - Renault Safrane LE-2500cc -> رنو سفران LE 2500cc
  - Renault Safrane PE-2000cc -> رنو سفران PE 2000cc
  - Renault Safrane PE-2500cc -> رنو سفران PE 2500cc
  - Renault Safrane SE-2000cc -> رنو سفران SE 2000cc
  - Renault Symbol -> رنو سیمبل
  - Renault Symbol LE -> رنو سیمبل LE
  - Renault Symbol PE -> رنو سیمبل PE
  - Renault Symbol SE -> رنو سیمبل SE
  - Renault Fluence -> رنو فلوئنس
  - Renault Fluence manual -> رنو فلوئنس دنده‌ای
  - Renault Fluence E2 -> رنو فلوئنس E2
  - Renault Fluence E4 -> رنو فلوئنس E4
  - Renault Captur -> رنو کپچر
  - Renault Koleos -> رنو کوليوس
  - Renault Koleos first generation -> رنو کوليوس نسل اول
  - Renault Koleos second generation -> رنو کوليوس نسل دوم
  - Renault Laguna -> رنو لاگونا
  - Renault Laguna coupe -> رنو لاگونا کوپه
  - Renault Latitude -> رنو لتیتود
  - Renault Megan -> رنو مگان
  - Renault Megan 1600cc -> رنو مگان 1600cc
  - Renault Megan 2000cc -> رنو مگان 2000cc
  - Renault Megan convertible -> رنو مگان کروک
  - Renault Megan-ir -> رنو مگان مونتاژ
  - Renault Megan-ir 2000cc -> رنو مگان مونتاژ 2000cc
  - Renault Megan-ir E1-1600cc -> رنو مگان مونتاژ E1 1600cc
  - Renault Megan-ir E2-1600cc -> رنو مگان مونتاژ E2 1600cc
  - Renault Megan hatchback -> رنو مگان هاچبک
  - Rollsroyce -> رولزرویس
  - Rich -> ریچ
  - Respect -> ریسپکت
  - Respect Prime -> ریسپکت پرایم
  - Rigan -> ریگان
  - Rigan Coupa -> ریگان کوپا
  - Rigan Coupa exclusive -> ریگان کوپا اکسکلوسیو
  - Rigan Coupa royal -> ریگان کوپا رویال
  - Rigan Coupa flagship -> ریگان کوپا فلگ شیپ
  - Zamyad -> زامیاد
  - Zamyad Padra -> زامیاد پادرا
  - Zamyad Padra Plus -> زامیاد پادرا پلاس
  - Zamyad Dorka -> زامیاد درکا
  - Zamyad Shooka -> زامیاد شوکا
  - Zamyad Karoon -> زامیاد کارون
  - Zamyad Z 24 -> زامیاد Z 24
  - Zamyad Z 24 Petrol -> زامیاد Z 24 بنزینی
  - Zamyad Z 24 Petrol Optional -> زامیاد Z 24 بنزینی آپشنال
  - Zamyad Z 24 Bi-fuel -> زامیاد Z 24 دوگانه سوز
  - Zamyad Z 24 Bi-fuel Optional -> زامیاد Z 24 دوگانه سوز آپشنال
  - Zamyad Z 24 diesel -> زامیاد Z 24 دیزلی
  - Zotye -> زوتی
  - Zotye Z300-im -> زوتی Z300 وارداتی
  - SsangYong -> سانگ یانگ
  - SsangYong Actyon -> سانگ یانگ اکتیون
  - SsangYong Tivoli -> سانگ یانگ تیوولی
  - SsangYong Tivoli armour -> سانگ یانگ تیوولی ارمور
  - SsangYong Tivoli sport -> سانگ یانگ تیوولی اسپرت
  - SsangYong Tivoli elite -> سانگ یانگ تیوولی الیت
  - SsangYong Tivoli-IR -> سانگ یانگ تیوولی مونتاژ
  - SsangYong Tivoli-IR Special -> سانگ یانگ تیوولی مونتاژ اسپشیال توربو
  - SsangYong Tivoli-IR Solar -> سانگ یانگ تیوولی مونتاژ سولار
  - SsangYong Tivoli-IR Fighter -> سانگ یانگ تیوولی مونتاژ فایتر توربو
  - SsangYong Tivoli-IR Armour -> سانگ یانگ تیوولی مونتاژ فیس ۲۰۱۸
  - SsangYong Chairman -> سانگ یانگ چیرمن
  - SsangYong Rexton -> سانگ یانگ رکستون
  - SsangYong Rexton basic -> سانگ یانگ رکستون ساده
  - SsangYong Rexton-ir -> سانگ یانگ رکستون مونتاژ
  - SsangYong Rexton-ir Emperor -> سانگ یانگ رکستون مونتاژ امپرور
  - SsangYong Rexton-ir G4 -> سانگ یانگ رکستون مونتاژ G4
  - SsangYong Rexton G4 -> سانگ یانگ رکستون G4
  - SsangYong Rodius -> سانگ یانگ رودیوس
  - SsangYong Kyron -> سانگ یانگ کایرون
  - SsangYong Korando -> سانگ یانگ کوراندو
  - SsangYong Korando 2300cc -> سانگ یانگ کوراندو 2300cc
  - SsangYong Korando 3200cc -> سانگ یانگ کوراندو 3200cc
  - SsangYong Musso -> سانگ یانگ موسو
  - SsangYong Musso E23M1 -> سانگ یانگ موسو 2300cc دنده ای
  - SsangYong Musso E32M3 -> سانگ یانگ موسو 3200cc اتوماتیک
  - SsangYong Musso E32M1 -> سانگ یانگ موسو 3200cc دنده ای
  - SsangYong new actyon -> سانگ یانگ نیو اکتیون
  - SsangYong new actyon prestige -> سانگ یانگ نیو اکتیون پرستیژ
  - SsangYong new actyon comfort -> سانگ یانگ نیو اکتیون کامفورت
  - SsangYong new actyon luxury -> سانگ یانگ نیو اکتیون لاکچری
  - SsangYong new-korando -> سانگ یانگ نیو کوراندو
  - SsangYong new-korando Optimum -> سانگ یانگ نیو کوراندو اپتیموم
  - SsangYong new-korando Premium -> سانگ یانگ نیو کوراندو پرمیوم
  - SsangYong new-korando Premium Plus -> سانگ یانگ نیو کوراندو پرمیوم پلاس
  - Saina -> ساینا
  - Saina automatic -> ساینا اتوماتیک
  - Saina manual -> ساینا دنده‌ای
  - Saina manual Plus -> ساینا دنده‌ای پلاس
  - Saina manual EX -> ساینا دنده‌ای EX
  - Saina manual G -> ساینا دنده‌ای G
  - Saina manual S -> ساینا دنده‌ای S
  - Saina manual SX -> ساینا دنده‌ای SX
  - Seat -> سئات
  - Seat Leon -> سئات لئون
  - Samand -> سمند
  - Samand Sarir -> سمند سریر
  - Samand Soren -> سمند سورن
  - Samand Soren Plus -> سمند سورن پلاس
  - Samand Soren basic -> سمند سورن معمولی
  - Samand Soren ELX -> سمند سورن ELX
  - Samand Soren ELX turbo -> سمند سورن ELX توربو شارژ
  - Samand EL -> سمند EL
  - Samand EL petrol -> سمند EL بنزینی
  - Samand EL Bi-fuel -> سمند EL دوگانه سوز
  - Samand LX -> سمند LX
  - Samand LX basic -> سمند LX ساده
  - Samand LX EF7-petrol -> سمند LX EF7 بنزینی
  - Samand LX EF7 -> سمند LX EF7 گازسوز
  - Samand SE -> سمند SE
  - Samand X7 -> سمند X7
  - Samand X7 petrol -> سمند X7 بنزینی
  - Samand X7 Bi-fuel -> سمند X7 دوگانه سوز
  - Datsun Car -> سواری داتسون
  - Soueast -> سوئیست
  - Soueast DX-3 -> سوئیست DX 3
  - Subaru -> سوبارو
  - Subaru Forester -> سوبارو فارستر
  - Subaru Legacy -> سوبارو لگاسی
  - Subaru Way Wave -> سوبارو وی ویو
  - Subaru X7 -> سوبارو X7
  - Suzuki -> سوزوکی
  - Suzuki Kizashi -> سوزوکی کیزاشی
  - Suzuki Kizashi automatic -> سوزوکی کیزاشی اتوماتیک
  - Suzuki Kizashi manual -> سوزوکی کیزاشی دنده‌ای
  - Suzuki Grand-Vitara -> سوزوکی گرند ویتارا
  - Suzuki Grand-Vitara automatic-2000cc -> سوزوکی گرند ویتارا اتوماتیک 2000cc
  - Suzuki Grand-Vitara manual-2000cc -> سوزوکی گرند ویتارا دنده‌ای 2000cc
  - Suzuki Grand-Vitara-ir -> سوزوکی گرند ویتارا مونتاژ
  - Suzuki Grand-Vitara-ir automatic-2000cc -> سوزوکی گرند ویتارا مونتاژ اتوماتیک 2000cc
  - Suzuki Grand-Vitara-ir automatic-2400cc -> سوزوکی گرند ویتارا مونتاژ اتوماتیک 2400cc
  - Suzuki Grand-Vitara-ir manual-2000cc -> سوزوکی گرند ویتارا مونتاژ دنده‌ای 2000cc
  - Suzuki Grand-Vitara-ir manual-2400cc -> سوزوکی گرند ویتارا مونتاژ دنده‌ای 2400cc
  - Citroen -> سیتروئن
  - Citroen Xantia -> سیتروئن زانتیا
  - Citroen Xantia 1800cc -> سیتروئن زانتیا 1800cc
  - Citroen Xantia2 -> سیتروئن زانتیا 2 (فیس لیفت)
  - Citroen Xantia 2000cc -> سیتروئن زانتیا 2000cc
  - Citroen Jian -> سیتروئن ژیان
  - Citroen C3 -> سیتروئن C3 مونتاژ
  - Citroen C3 wo-warmer -> سیتروئن C3 مونتاژ بدون گرمکن صندلی
  - Citroen C3 wt-warmer -> سیتروئن C3 مونتاژ گرمکن صندلی
  - Citroen C5 -> سیتروئن C5
  - Citroen New C5 -> سیتروئن C5 جدید
  - Sinad -> سیناد
  - Shahin -> شاهین
  - Shahin G -> شاهین G
  - Chevrolet -> شورولت
  - Chevrolet Impala -> شورولت ایمپالا
  - Chevrolet Bel Air -> شورولت بلر
  - Chevrolet Blazer -> شورولت بلیزر
  - Chevrolet Royal-ir -> شورولت رویال مونتاژ
  - Chevrolet Suburban -> شورولت سابربن
  - Chevrolet Fleetmaster -> شورولت فلیت مستر
  - Chevrolet Caprice -> شورولت کاپریس
  - Chevrolet Camaro -> شورولت کامارو
  - Chevrolet Monte Carlo -> شورولت مونت کارلو
  - Chevrolet Nova -> شورولت نوا
  - Chevrolet Nova-ir -> شورولت نوا مونتاژ
  - Farda -> فردا
  - Farda 511 -> فردا 511
  - Farda Sx5 -> فردا Sx5
  - Farda Sx6 -> فردا Sx6
  - Farda T5 -> فردا T5
  - Foton -> فوتون
  - Foton Tunland G7 -> فوتون تونلند G7
  - Foton Sauvana -> فوتون ساوانا
  - Ford -> فورد
  - Ford Taurus -> فورد تاروس
  - Ford Mustang -> فورد موستانگ
  - Ford F150 -> فورد F150
  - Volkswagen -> فولکس
  - Volkswagen Beetle -> فولکس بیتل
  - Volkswagen Beetle convertible -> فولکس بیتل کروک
  - Volkswagen Beetle Coupe -> فولکس بیتل کوپه
  - Volkswagen Passat -> فولکس پاسات
  - Volkswagen Tiguan -> فولکس تیگوان
  - Volkswagen Caddy -> فولکس کدی
  - Volkswagen Gol -> فولکس گل
  - Volkswagen Golf -> فولکس گلف
  - Volkswagen Golf basic -> فولکس گلف ساده
  - Volkswagen Golf GTI -> فولکس گلف GTI
  - Fownix -> فونیکس
  - Fownix Arrizo 6 pro -> فونیکس آریزو 6 پرو
  - Fownix Tiggo 7 pro -> فونیکس تیگو 7 پرو
  - Fownix Tiggo 8 pro -> فونیکس تیگو 8 پرو
  - Fownix Fx -> فونیکس FX
  - Fownix Fx Excellent -> فونیکس FX اکسلنت
  - Fownix Fx Premium -> فونیکس FX پرمیوم
  - Fiat -> فیات
  - Fiat 500 -> فیات 500
  - Fiat Siena -> فیات سی ینا
  - Fidelity -> فیدلیتی
  - Fidelity Prime -> فیدلیتی پرایم
  - Fidelity Prime 5seater -> فیدلیتی پرایم ۵ نفره
  - Fidelity Prime 7seater -> فیدلیتی پرایم ۷ نفره
  - Capra -> کاپرا
  - Capra Capra 2 -> کاپرا 2
  - Capra Single-cabin -> کاپرا تک کابین
  - Capra Single-cabin singledifferential -> کاپرا تک کابین تک دیفرانسیل
  - Capra Double Cabin -> کاپرا دو کابین
  - Capra Double Cabin singledifferential -> کاپرا دو کابین تک دیفرانسیل
  - Capra Double Cabin doubledifferential -> کاپرا دو کابین دو دیفرانسیل
  - Chrysler -> کرایسلر
  - Quick -> کوییک
  - Quick Automatic -> کوییک اتوماتیک
  - Quick automatic-full -> کوییک اتوماتیک فول
  - Quick automatic-full plus -> کوییک اتوماتیک فول پلاس
  - Quick Automatic P Plus -> کوییک اتوماتیک R پلاس
  - Quick Automatic S -> کوییک اتوماتیک S
  - Quick manual -> کوییک دنده‌ای
  - Quick manual basic -> کوییک دنده‌ای ساده
  - Quick manual G -> کوییک دنده‌ای G
  - Quick manual R -> کوییک دنده‌ای R
  - Quick manual R Plus -> کوییک دنده‌ای R Plus
  - Quick manual S -> کوییک دنده‌ای S
  - Kia -> کیا
  - Kia Optima -> کیا اپتیما
  - Kia Optima 2400cc -> کیا اپتیما 2400cc
  - Kia Optima 2700cc -> کیا اپتیما 2700cc
  - Kia Optima-hybrid -> کیا اپتیما هیبرید
  - Kia Optima GT Line 2400cc -> کیا اپتیما GT Line 2400cc
  - Kia Opirus -> کیا اپیروس
  - Kia Sportage -> کیا اسپورتیج
  - Kia Sportage 2000cc turbo -> کیا اسپورتیج 2000cc توربو
  - Kia Sportage 2400cc -> کیا اسپورتیج 2400cc
  - Kia Sportage 2700cc -> کیا اسپورتیج 2700cc
  - Kia Sportage GT Line-2400cc -> کیا اسپورتیج GT Line 2400cc
  - Kia Picanto -> کیا پیکانتو
  - Kia Rio -> کیا ریو
  - Kia Rio sedan -> کیا ریو سدان
  - Kia Rio-ir -> کیا ریو مونتاژ
  - Kia Rio-ir automatic -> کیا ریو مونتاژ اتوماتیک
  - Kia Rio-ir manual -> کیا ریو مونتاژ دنده‌ای
  - Kia Rio hatchback -> کیا ریو هاچبک
  - Kia Cerato -> کیا سراتو
  - Kia Cerato automatic-1600cc -> کیا سراتو اتوماتیک 1600cc
  - Kia Cerato automatic-2000cc -> کیا سراتو اتوماتیک 2000cc
  - Kia Cerato Coupe -> کیا سراتو کوپه
  - Kia Cerato Coupe 1600cc -> کیا سراتو کوپه 1600cc
  - Kia Cerato Coupe 2000cc -> کیا سراتو کوپه 2000cc
  - Kia Cerato-ir -> کیا سراتو مونتاژ
  - Kia Cerato-ir automatic-2000cc -> کیا سراتو مونتاژ اتوماتیک 2000cc
  - Kia Cerato-ir optional-automatic-2000cc -> کیا سراتو مونتاژ اتوماتیک آپشنال 2000cc
  - Kia Cerato-ir manual-1600cc -> کیا سراتو مونتاژ دنده‌ای 1600cc
  - Kia Cerato-ir manual-optional-1600cc -> کیا سراتو مونتاژ دنده‌ای آپشنال 1600cc
  - Kia Sorento -> کیا سورنتو
  - Kia Sorento first generation-(2002-2009) -> کیا سورنتو نسل اول
  - Kia Sorento second generation -> کیا سورنتو نسل دوم
  - Kia Sorento third generation-(2016-present) -> کیا سورنتو نسل سوم
  - Kia Sorento GT Line-third generation -> کیا سورنتو GT Line نسل سوم
  - Kia soul -> کیا سول
  - Kia cadenza -> کیا کادنزا
  - Kia carnival -> کیا کارناوال
  - Kia carens -> کیا کارنز
  - Kia mohave -> کیا موهاوی
  - Kia mohave 6 cylinder -> کیا موهاوی 6 سیلندر
  - Kia mohave 8 cylinder -> کیا موهاوی 8 سیلندر
  - KMC -> کی‌ام‌سی
  - KMC J7 -> کی‌ام‌سی J7
  - KMC K7 -> کی‌ام‌سی K7
  - KMC T8 -> کی‌ام‌سی T8
  - Great-Wall -> گریت وال
  - Great-Wall Pickup Wingle 5-single cabin -> گریت وال وینگل 5 تک کابین
  - Great-Wall Pickup Wingle 5-single cabin singledifferential -> گریت وال وینگل 5 تک کابین تک دیفرانسیل
  - Great-Wall Pickup Wingle 5-single cabin doubledifferential -> گریت وال وینگل 5 تک کابین دو دیفرانسیل
  - Great-Wall Pickup Wingle 5-double cabin -> گریت وال وینگل 5 دو کابین
  - Great-Wall Pickup Wingle 5-double cabin singledifferential -> گریت وال وینگل 5 دو کابین تک دیفرانسیل
  - Great-Wall Pickup Wingle 5-double cabin doubledifferential -> گریت وال وینگل 5 دو کابین دو دیفرانسیل
  - Great-Wall C30 -> گریت وال C30
  - Great-Wall C30 automatic -> گریت وال C30 اتوماتیک
  - Great-Wall C30 manual -> گریت وال C30 دنده‌ای
  - Lada -> لادا
  - Lada Niva -> لادا نیوا
  - Lamari -> لاماری
  - Lamari Eama -> لاماری ایما
  - Lamborghini -> لامبورگینی
  - Lexus -> لکسوس
  - Lexus CT -> لکسوس CT
  - Lexus CT 200-hybrid -> لکسوس CT 200 H
  - Lexus CT 200-hybrid-F-sport -> لکسوس CT 200H F
  - Lexus ES -> لکسوس ES
  - Lexus ES 250 -> لکسوس ES 250
  - Lexus ES 350 -> لکسوس ES 350
  - Lexus GS -> لکسوس GS
  - Lexus GS 250 -> لکسوس GS 250
  - Lexus GS 250-F-sport -> لکسوس GS 250 F
  - Lexus GS 430 -> لکسوس GS 430
  - Lexus GS 460 -> لکسوس GS 460
  - Lexus IS -> لکسوس IS
  - Lexus IS 250 -> لکسوس IS 250
  - Lexus IS 250-F-sport -> لکسوس IS 250 F
  - Lexus IS 300 -> لکسوس IS 300
  - Lexus IS convertible -> لکسوس IS کروک
  - Lexus IS convertible 300 -> لکسوس IS کروک 300
  - Lexus LS -> لکسوس LS
  - Lexus LS 460L -> لکسوس LS 460L
  - Lexus LX -> لکسوس LX
  - Lexus LX 570 -> لکسوس LX 570
  - Lexus NX 200t -> لکسوس NX 200t
  - Lexus NX 200t premium -> لکسوس NX 200t پرمیوم
  - Lexus NX 200t paltinum -> لکسوس NX 200t پلاتینیوم
  - Lexus NX 200t F -> لکسوس NX 200t F
  - Lexus NX 300 H -> لکسوس NX 300 H
  - Lexus NX 300 H 300-hybrid -> لکسوس NX 300 H 300
  - Lexus NX 300 H 300-hybrid-F-sport -> لکسوس NX 300 H 300 F
  - Lexus RX -> لکسوس RX
  - Lexus RX 200t-luxury -> لکسوس RX 200T لاکچری
  - Lexus RX 200T-F-sport -> لکسوس RX 200T F
  - Lexus RX 350 -> لکسوس RX 350
  - Lexus RX 350-F-sport -> لکسوس RX 350 F
  - Land Rover -> لندرور
  - Land Rover Discovery -> لندرور دیسکاوری
  - Land Rover Defender -> لندرور دیفندر
  - Land Rover Range Rover -> لندرور رنجرور
  - Land Rover Range Rover-Evoque -> لندرور رنجرور ایووک
  - Land Rover ir -> لندرور سری مونتاژ
  - Land Rover Freelander -> لندرور فریلندر
  - Landmark -> لندمارک
  - Landmark V7 -> لندمارک V7
  - Lotus -> لوتوس
  - Lotus Elise -> لوتوس الیزه
  - Lotus Elise 220 cup -> لوتوس الیزه Cup 220
  - Lotus Elise S -> لوتوس الیزه S
  - Luxgen -> لوکسژن
  - Luxgen U6 -> لوکسژن U6
  - Lifan -> لیفان
  - Lifan 520 -> لیفان 520
  - Lifan 520i -> لیفان 520i
  - Lifan 620 -> لیفان 620
  - Lifan 620 1600cc -> لیفان 620 1600cc
  - Lifan 620 1800cc -> لیفان 620 1800cc
  - Lifan 820 -> لیفان 820
  - Lifan X50 -> لیفان X50
  - Lifan X50 automatic -> لیفان X50 اتوماتیک
  - Lifan X50 manual -> لیفان X50 دنده‌ای
  - Lifan X60 -> لیفان X60
  - Lifan X60 automatic -> لیفان X60 اتوماتیک
  - Lifan X60 manual -> لیفان X60 دنده‌ای
  - Lifan X70 -> لیفان X70
  - Maserati -> مازراتی
  - Maserati Quattroporte -> مازراتی کواتروپورته
  - Maserati Quattroporte basic -> مازراتی کواتروپورته ساده
  - Maserati Quattroporte GTS -> مازراتی کواتروپورته GTS
  - Maserati Quattroporte S -> مازراتی کواتروپورته S
  - Maserati Granturismo -> مازراتی گرن توریسمو
  - Maserati Granturismo basic -> مازراتی گرن توریسمو ساده
  - Maserati Granturismo MC -> مازراتی گرن توریسمو MC
  - Maserati Granturismo S -> مازراتی گرن توریسمو S
  - Maserati Grancabrio -> مازراتی گرن کبریو
  - Maserati Grancabrio basic -> مازراتی گرن کبریو ساده
  - Maserati Grancabrio MC -> مازراتی گرن کبریو MC
  - Maserati Grancabrio S -> مازراتی گرن کبریو S
  - Maserati Ghibli -> مازراتی گیبلی
  - Mazda -> مزدا
  - Mazda 2-ir -> مزدا 2 مونتاژ
  - Mazda 2-ir 2 -> مزدا 2 مونتاژ تیپ 2
  - Mazda 3-ir -> مزدا 3 مونتاژ
  - Mazda 3-ir 1 -> مزدا 3 مونتاژ تیپ 1
  - Mazda 3-ir 2 -> مزدا 3 مونتاژ تیپ 2
  - Mazda 3-ir 3 -> مزدا 3 مونتاژ تیپ 3
  - Mazda 323 -> مزدا 323
  - Mazda 323 automatic -> مزدا 323 اتوماتیک
  - Mazda 323 manual -> مزدا 323 دنده‌ای
  - Mazda 323 F -> مزدا 323 F
  - Mazda 3N Sedan-ir -> مزدا 3N صندوق‌دار مونتاژ
  - Mazda 3N Sedan-ir 1 -> مزدا 3N صندوق‌دار مونتاژ تیپ 1
  - Mazda 3N Sedan-ir 2 -> مزدا 3N صندوق‌دار مونتاژ تیپ 2
  - Mazda 3N Sedan-ir 3 -> مزدا 3N صندوق‌دار مونتاژ تیپ 3
  - Mazda 3N Sedan-ir 4 -> مزدا 3N صندوق‌دار مونتاژ تیپ 4
  - Mazda 3N Hatchback-ir -> مزدا 3N هاچبک مونتاژ
  - Mazda 3N Hatchback-ir 1 -> مزدا 3N هاچبک مونتاژ تیپ 1
  - Mazda 3N Hatchback-ir 3 -> مزدا 3N هاچبک مونتاژ تیپ 3
  - Mazda 6 -> مزدا 6
  - Maxmotor -> مکث موتور
  - Maxmotor Tiara -> مکث موتور تیارا
  - Maxmotor Kalut -> مکث موتور کلوت
  - Maxmotor Kalut Automatic -> مکث موتور کلوت اتوماتیک
  - Maxmotor Kalut manual -> مکث موتور کلوت دنده‌ای
  - Maxus -> مکسوس
  - Mitsubishi -> میتسوبیشی
  - Mitsubishi Outlander -> میتسوبیشی اوتلندر
  - Mitsubishi Outlander 3 -> میتسوبیشی اوتلندر تیپ 3
  - Mitsubishi Outlander 4 -> میتسوبیشی اوتلندر تیپ 4
  - Mitsubishi Outlander 5 -> میتسوبیشی اوتلندر تیپ 5
  - Mitsubishi Outlander PHEV -> میتسوبیشی اوتلندر PHEV
  - Mitsubishi Pajero 2 door -> میتسوبیشی پاجرو 2 در
  - Mitsubishi Pajero 2 door 4 cylinder -> میتسوبیشی پاجرو 2 در 4 سیلندر
  - Mitsubishi Pajero 2 door 6 cylinder -> میتسوبیشی پاجرو 2 در 6 سیلندر
  - Mitsubishi Pajero 4 door -> میتسوبیشی پاجرو 4 در
  - Mitsubishi Pajero 4 door 4 cylinder -> میتسوبیشی پاجرو 4 در 4 سیلندر
  - Mitsubishi Pajero 4 door 6 cylinder -> میتسوبیشی پاجرو 4 در 6 سیلندر
  - Mitsubishi Pajero-ir -> میتسوبیشی پاجرو مونتاژ
  - Mitsubishi Pajero-ir automatic -> میتسوبیشی پاجرو مونتاژ اتوماتیک
  - Mitsubishi Pajero-ir manual -> میتسوبیشی پاجرو مونتاژ دنده‌ای
  - Mitsubishi Galant -> میتسوبیشی گالانت
  - Mitsubishi Lancer -> میتسوبیشی لنسر
  - Mitsubishi Lancer 1800cc -> میتسوبیشی لنسر 1800cc
  - Mitsubishi Lancer automatic-1600cc -> میتسوبیشی لنسر اتوماتیک 1600cc
  - Mitsubishi Lancer manual-1600cc -> میتسوبیشی لنسر دنده‌ای 1600cc
  - Mitsubishi Mirage -> میتسوبیشی میراژ
  - Mitsubishi ASX -> میتسوبیشی ASX
  - Mitsubishi ASX 4 -> میتسوبیشی ASX تیپ 4
  - Mitsubishi ASX midline -> میتسوبیشی ASX مید لاین
  - Mitsubishi ASX highline -> میتسوبیشی ASX های لاین
  - MINI -> مینی
  - MINI Countryman -> مینی کانتری من
  - MINI Countryman S -> مینی کانتری من S
  - MINI Clubman -> مینی کلاب من
  - MINI Clubman S -> مینی کلاب من S
  - MINI Classic -> مینی کلاسیک
  - MINI Cooper S -> مینی کوپر S
  - MINI Cooper S 3 door -> مینی کوپر S 3 در
  - MINI Cooper S 5 door -> مینی کوپر S 5 در
  - Nissan -> نیسان
  - Nissan Altima -> نیسان آلتیما
  - Nissan X-Trail -> نیسان ایکس تریل
  - Nissan X-Trail automatic -> نیسان ایکس تریل اتوماتیک
  - Nissan X-Trail manual -> نیسان ایکس تریل دنده ای
  - Nissan Patrol 2 door -> نیسان پاترول 2 در
  - Nissan Patrol 2 door 4 cylinder -> نیسان پاترول 2 در 4 سیلندر
  - Nissan Patrol 4 door -> نیسان پاترول 4 در
  - Nissan Patrol 4 door 4 cylinder -> نیسان پاترول 4 در 4 سیلندر
  - Nissan Patrol 4 door 6 cylinder -> نیسان پاترول 4 در 6 سیلندر
  - Nissan Pathfinder -> نیسان پت فایندر
  - Nissan Pickup Double-Cabin -> نیسان پیکاپ دو کابین
  - Nissan Pickup double-cabin petrol -> نیسان پیکاپ دو کابین بنزینی
  - Nissan Pickup double-cabin Bi-fuel -> نیسان پیکاپ دو کابین دوگانه سوز
  - Nissan Teana-ir -> نیسان تی ینا مونتاژ
  - Nissan Teana-ir HI -> نیسان تی ینا مونتاژ HI
  - Nissan Teana-ir MID -> نیسان تی ینا مونتاژ MID
  - Nissan Teana-im -> نیسان تی ینا وارداتی
  - Nissan Tiida -> نیسان تیدا
  - Nissan Juke -> نیسان جوک
  - Nissan Juke sport -> نیسان جوک اسپرت
  - Nissan Juke skypack -> نیسان جوک اسکای پک
  - Nissan Juke platinum -> نیسان جوک پلاتینیوم
  - Nissan Roniz -> نیسان رونیز
  - Nissan Sunny -> نیسان سانی
  - Nissan Seranza -> نیسان سرانزا
  - Nissan Qashqai -> نیسان قشقایی
  - Nissan Qashqai-ir -> نیسان قشقایی مونتاژ
  - Nissan Maxima-ir -> نیسان ماکسیما مونتاژ
  - Nissan Maxima-ir automatic -> نیسان ماکسیما مونتاژ اتوماتیک
  - Nissan Maxima-ir manual -> نیسان ماکسیما مونتاژ دنده‌ای
  - Nissan Maxima-im -> نیسان ماکسیما وارداتی
  - Nissan Murano -> نیسان مورانو
  - Nissan Murano LE -> نیسان مورانو LE
  - Nissan Murano SE -> نیسان مورانو SE
  - Nissan Murano SL -> نیسان مورانو SL
  - Arisan Arisan -> وانت آریسان
  - Arisan Arisun 2 -> وانت آریسان 2
  - Arisan Arisan petrol -> وانت آریسان بنزینی
  - Arisan Arisan Bi-fuel -> وانت آریسان دوگانه سوز
  - Amico Araz -> وانت آمیکو آراز
  - Amico Araz singledifferential -> وانت آمیکو آراز تک دیفرانسیل
  - Amico Araz doubledifferential -> وانت آمیکو آراز دو دیفرانسیل
  - Amico Asna -> وانت آمیکو آسنا
  - Amico Asna petrol -> وانت آمیکو آسنا بنزینی
  - Amico Asna Bi-fuel -> وانت آمیکو آسنا دوگانه سوز
  - Pride Pickup -> وانت پراید 151
  - Pride Pickup Plus -> وانت پراید 151 پلاس
  - Pride Pickup 151 Bi-fuel -> وانت پراید 151 دوگانه سوز
  - Pride Pickup 151 SE -> وانت پراید 151 SE
  - Pride Pickup 151 SL -> وانت پراید 151 SL
  - GAC Gonow Pickup -> وانت جی‌ای‌سی گونو
  - GAC Gonow Pickup Troy -> وانت جی‌ای‌سی گونو تروی
  - Jeep Pickup -> وانت جیپ
  - Jeep Pickup Simorgh -> وانت جیپ سیمرغ
  - Datsun Pickup -> وانت داتسون
  - Deer Deer -> وانت دییر
  - Renault Pickup -> وانت رنو
  - Renault Pickup Tondar 90 -> وانت رنو تندر 90
  - Subaru Pickup -> وانت سوبارو
  - Chevrolet Pickup -> وانت شورولت
  - Foton Pickup -> وانت فوتون
  - Foton Pickup Tunland Petrol doubledifferential -> وانت فوتون تونلند دو دیفرانسیل بنزینی
  - Foton Pickup Tunland diesel doubledifferential -> وانت فوتون تونلند دو دیفرانسیل دیزلی
  - Volkswagen Pickup -> وانت فولکس
  - Great-Wall Pickup Wingle 3 -> وانت گریت وال وینگل 3
  - Toyota Pickup -> وانت لندکروزر
  - Toyota Pickup Land Cruiser-Pickup-single cabin 2F -> وانت لندکروزر تک کابین 2F
  - Toyota Pickup Land Cruiser-Pickup-single cabin 3F -> وانت لندکروزر تک کابین 3F
  - Toyota Pickup Land Cruiser-Pickup-Single cabin 4.5F -> وانت لندکروزر تک کابین 4.5F
  - Toyota Pickup Land Cruiser-Pickup-Double cabin 3F -> وانت لندکروزر دو کابین 3F
  - Toyota Pickup Land Cruiser-Pickup-Double cabin 4.5F -> وانت لندکروزر دو کابین 4.5F
  - Mazda Pickup -> وانت مزدا
  - Mazda Pickup 1000 -> وانت مزدا 1000
  - Mazda Pickup 1600 -> وانت مزدا 1600
  - Mazda Pickup injector 2000-single cabin petrol -> وانت مزدا 2000 تک کابین بنزینی
  - Mazda Pickup injector 2000-single cabin Bi-fuel -> وانت مزدا 2000 تک کابین دوگانه سوز
  - Mazda Pickup injector 2000-double cabin petrol -> وانت مزدا 2000 دو کابین بنزینی
  - Mazda Pickup injector 2000-double cabin Bi-fuel -> وانت مزدا 2000 دو کابین دوگانه سوز
  - Mazda Pickup 2600 -> وانت مزدا 2600
  - Mazda Pickup Cara-single cabin 1700cc -> وانت مزدا کارا تک کابین 1700cc
  - Mazda Pickup Cara-single cabin 2000cc -> وانت مزدا کارا تک کابین 2000cc
  - Mazda Pickup Cara-double cabin 1700cc -> وانت مزدا کارا دو کابین 1700cc
  - Mazda Pickup Cara-double cabin 2000cc -> وانت مزدا کارا دو کابین 2000cc
  - Mitsubishi Pickup -> وانت میتسوبیشی
  - Nissan Pickup -> وانت نیسان
  - Nissan Pickup Patrol -> وانت نیسان پاترول
  - Nissan Pickup single-cabin -> وانت نیسان پیکاپ تک کابین
  - Hyosow T205 Pickup -> وانت هیوسو T205
  - Volvo -> ولوو
  - Volvo C30 -> ولوو C30
  - Volvo C70 -> ولوو C70
  - Volvo C70 convertible -> ولوو C70 کروک
  - Volvo V40 -> ولوو V40
  - Volvo V40 R-Design -> ولوو V40 R دیزاین
  - Volvo V40 R-Design-Plus -> ولوو V40 R دیزاین پلاس
  - Volvo XC60 -> ولوو XC60
  - Volvo XC60 R-Design -> ولوو XC60 R دیزاین
  - Volvo XC60 T5 -> ولوو XC60 T5
  - Volvo XC90 -> ولوو XC90
  - Volvo XC90 Inscription -> ولوو XC90 اینسکریپشن
  - Volvo XC90 Momentum -> ولوو XC90 مومنتوم
  - Volvo XC90 R-Design -> ولوو XC90 R دیزاین
  - IranKhodro Van -> ون ایران خودرو
  - IranKhodro Van Ghazal -> ون ایران خودرو غزال‌
  - IranKhodro Van Vana -> ون ایران خودرو وانا
  - Iveco Van -> ون ایویکو
  - Iveco Van A36 -> ون ایویکو A36
  - Brilliance Van -> ون برلیانس
  - Brilliance Van H2L -> ون برلیانس H2L
  - Mercedes-Benz Van -> ون بنز
  - Mercedes-Benz Van Vito -> ون بنز ویتو
  - Mercedes-Benz Van MB140 -> ون بنز MB140
  - Toyota Van -> ون تویوتا
  - Toyota Van Previa -> ون تویوتا پرویا
  - Toyota Van Hiace -> ون تویوتا هایس
  - JAC Van -> ون جک
  - JAC Van Refine -> ون جک ریفاین
  - JAC Van Sunray -> ون جک سانری
  - Joylong Van -> ون جوی لانگ
  - Delica Van -> ون دلیکا
  - Delica Van Taxi -> ون دلیکا تاکسی
  - Delica Van Personal -> ون دلیکا شخصی
  - Dodge Van -> ون دوج
  - Renault Van -> ون رنو
  - Renault Van Traffic -> ون رنو ترافیک
  - Saipa -> ون سایپا
  - Saipa Karvan Saipa -> ون سایپا کاروان
  - Chevrolet Van -> ون شورولت
  - Chevrolet Van Vandura -> ون شورولت وندورا
  - Faw -> ون فاو
  - Faw Siba -> ون فاو سیبا
  - Foton Van -> ون فوتون
  - Volkswagen Van -> ون فولکس
  - Volkswagen Van Transporter -> ون فولکس ترنسپورتر
  - Volkswagen Van Caddy -> ون فولکس کدی
  - Volkswagen Van T2 -> ون فولکس T2
  - Volkswagen Van T2 Camper -> ون فولکس T2 کمبی
  - Volkswagen Van T3 -> ون فولکس T3
  - Kia Van -> ون کیا
  - Great-Wall Van -> ون گریت وال
  - Great-Wall Van 13 Seater -> ون گریت وال 13 نفره
  - Great-Wall Van 9 Seater -> ون گریت وال 9 نفره
  - Maxus Van -> ون مکسوس
  - Mitsubishi Van -> ون میتسوبیشی
  - Mitsubishi Van Caspian -> ون میتسوبیشی کاسپین
  - Narvan -> ون نارون
  - Narvan Taxi -> ون نارون تاکسی
  - Narvan Personal -> ون نارون شخصی
  - Hyundai Van -> ون هیوندای
  - Hyundai Van H1 -> ون هیوندای H1
  - Hyundai Van H350 -> ون هیوندای H350
  - Hafei Lobo -> هافی لوبو
  - Hafei Lobo Lobo -> هافی لوبو لوبو
  - Hummer -> هامر
  - Hummer H2 -> هامر H2
  - Haval -> هاوال
  - Haval H2-ir -> هاوال H2 مونتاژ
  - Haval H6 -> هاوال H6
  - Haval H6-ir -> هاوال H6 مونتاژ
  - Haval H9 -> هاوال H9
  - Haval M4 -> هاوال M4
  - Haval M4-ir -> هاوال M4 مونتاژ
  - Haima -> هایما
  - Haima S5 -> هایما S5
  - Haima S5 6 AT -> هایما S5 اتوماتیک ۶ سرعته
  - Haima S5 AT CVT -> هایما S5 اتوماتیک CVT
  - Haima S7 -> هایما S7
  - Haima S7 automatic-2000cc -> هایما S7 2000cc
  - Haima S7 Plus -> هایما S7 پلاس
  - Haima S7 automatic-turbo-1800cc -> هایما S7 توربو1800cc
  - Haima S8 -> هایما S8
  - Hanteng -> هن تنگ
  - Hanteng X5-ir -> هن تنگ X5 مونتاژ
  - Hanteng X7-ir -> هن تنگ X7 مونتاژ
  - Honda -> هوندا
  - Honda Accord -> هوندا آکورد
  - Honda Accord DX -> هوندا آکورد DX
  - Honda Accord EX -> هوندا آکورد EX
  - Honda Accord EXA -> هوندا آکورد EXA
  - Honda Accord EXB -> هوندا آکورد EXB
  - Honda Accord EXL -> هوندا آکورد EXL
  - Honda Accord LXB -> هوندا آکورد LXB
  - Honda Civic -> هوندا سیویک
  - Honda Legend -> هوندا لجند
  - Honda CR-V -> هوندا CR-V
  - Honda CR-V Touring -> هوندا CR-V تورینگ
  - Honda CR-V EX-L -> هوندا CR-V EXL
  - Honda CR-X -> هوندا CR-X
  - Hillman -> هیلمن
  - Hyosow -> هیوسو
  - Hyundai -> هیوندای
  - Hyundai Azera Grandeur -> هیوندای آزرا گرنجور
  - Hyundai Azera Grandeur 2400cc -> هیوندای آزرا گرنجور 2400cc
  - Hyundai Azera Grandeur 3000cc -> هیوندای آزرا گرنجور 3000cc
  - Hyundai Azera Grandeur 3300cc -> هیوندای آزرا گرنجور 3300cc
  - Hyundai Avante -> هیوندای آوانته
  - Hyundai Avante automatic -> هیوندای آوانته اتوماتیک
  - Hyundai Avante manual -> هیوندای آوانته دنده‌ای
  - Hyundai Scoupe -> هیوندای اسکوپ
  - Hyundai Excel -> هیوندای اکسل
  - Hyundai Accent -> هیوندای اکسنت
  - Hyundai Accent blue -> هیوندای اکسنت بلو
  - Hyundai Accent basic -> هیوندای اکسنت ساده
  - Hyundai Accent-ir -> هیوندای اکسنت مونتاژ
  - Hyundai Elantra -> هیوندای النترا
  - Hyundai Elantra 1600cc -> هیوندای النترا 1600cc
  - Hyundai Elantra 1800cc -> هیوندای النترا 1800cc
  - Hyundai Elantra 2000cc -> هیوندای النترا 2000cc
  - Hyundai Elantra-ir -> هیوندای النترا مونتاژ
  - Hyundai Trajet -> هیوندای تراجت
  - Hyundai Tucson-ix35 -> هیوندای توسان ix 35
  - Hyundai Tucson-ix35 2000cc -> هیوندای توسان ix 35 2000cc
  - Hyundai Tucson-ix35 2400cc -> هیوندای توسان ix 35 2400cc
  - Hyundai Tucson-ix35 2700cc -> هیوندای توسان ix 35 2700cc
  - Hyundai Genesis Sedan -> هیوندای جنسیس سدان
  - Hyundai Genesis Coupe -> هیوندای جنسیس کوپه
  - Hyundai Santafe ix45 -> هیوندای سانتافه ix 45
  - Hyundai Santafe ix45 2400cc -> هیوندای سانتافه ix 45 2400cc
  - Hyundai Santafe ix45 2700cc -> هیوندای سانتافه ix 45 2700cc
  - Hyundai Santafe ix45 3500cc -> هیوندای سانتافه ix 45 3500cc
  - Hyundai Centennial -> هیوندای سنتنیال
  - Hyundai Sonata-LF -> هیوندای سوناتا LF
  - Hyundai Sonata-LF-hybrid -> هیوندای سوناتا LF هیبرید
  - Hyundai Sonata-LF-hybrid GL -> هیوندای سوناتا LF هیبرید gl
  - Hyundai Sonata-LF-hybrid GLS -> هیوندای سوناتا LF هیبرید gls
  - Hyundai Sonata-LF-hybrid GLS-Plus -> هیوندای سوناتا LF هیبرید gls plus
  - Hyundai Sonata-NF -> هیوندای سوناتا NF
  - Hyundai Sonata-NF NF-3300cc -> هیوندای سوناتا NF 3300cc
  - Hyundai Sonata-NF automatic-2400cc -> هیوندای سوناتا NF اتوماتیک 2400cc
  - Hyundai Sonata-NF manual-2400cc -> هیوندای سوناتا NF دنده‌ای 2400cc
  - Hyundai Sonata-YF -> هیوندای سوناتا YF
  - Hyundai Veracruz-ix55 -> هیوندای وراکروز ix55
  - Hyundai Verna -> هیوندای ورنا
  - Hyundai Verna automatic -> هیوندای ورنا اتوماتیک
  - Hyundai Verna manual -> هیوندای ورنا دنده‌ای
  - Hyundai Veloster -> هیوندای ولستر
  - Hyundai FX Coupe -> هیوندای FX کوپه
  - Hyundai FX Coupe automatic -> هیوندای FX کوپه اتوماتیک
  - Hyundai FX Coupe manual -> هیوندای FX کوپه دنده‌ای
  - Hyundai i10-ir -> هیوندای i10 مونتاژ
  - Hyundai i20 -> هیوندای i20
  - Hyundai i20-ir -> هیوندای i20 مونتاژ
  - Hyundai i20-ir optional -> هیوندای i20 مونتاژ آپشنال
  - Hyundai i20-ir basic -> هیوندای i20 مونتاژ ساده
  - Hyundai i30 -> هیوندای i30
  - Hyundai i40 -> هیوندای i40
  - Hyundai i40 Station -> هیوندای i40 استیشن
  - Uaz -> یوآز
  - Uaz Patriot -> یوآز پاتریوت
  - Uaz Pickup -> یوآز پیکاپ
  - other -> سایر

### brand_model_manufacturer_origin
- **Title**: داخلی/خارجی
- **Type**: object
- **Queries**: 
  - domestic -> داخلی
  - foreign -> وارداتی و مونتاژ

### business-type
- **Title**: نوع آگهی‌دهنده
- **Type**: object
- **Queries**: 
  - personal -> شخصی
  - car-business -> نمایشگاه

### category
- **Title**: دسته‌بندی
- **Type**: object

### chassis_status
- **Title**: وضعیت شاسی‌ها
- **Type**: object
- **Queries**: 
  - both-healthy -> هر دو سالم و پلمب
  - back-damage -> عقب ضربه‌خورده
  - back-paint -> عقب رنگ‌شده
  - front-damage -> جلو ضربه‌خورده
  - front-paint -> جلو رنگ‌شده
  - back-damage-front-paint -> عقب ضربه‌خورده، جلو رنگ‌شده
  - front-damage-back-paint -> عقب رنگ‌شده، جلو ضربه‌خورده
  - both-damage -> هردو ضربه‌خورده
  - both-paint -> هردو رنگ‌شده

### color
- **Title**: رنگ
- **Type**: object
 - **Items Type**: array
- **Queries**: 
  - ROOT -> همهٔ رنگ‌ها
  - POPULAR_COLORS -> رنگ‌های پر بازدید
  - بژ -> بژ
  - مشکی -> مشکی
  - نقرآبی -> نقرآبی
  - برنز -> برنز
  - قهوه‌ای -> قهوه‌ای
  - کربن‌بلک -> کربن‌بلک
  - ذغالی -> ذغالی
  - آلبالویی -> آلبالویی
  - مسی -> مسی
  - کرم -> کرم
  - زرشکی -> زرشکی
  - گیلاسی -> گیلاسی
  - نوک‌مدادی -> نوک‌مدادی
  - بادمجانی -> بادمجانی
  - طلایی -> طلایی
  - خاکستری -> خاکستری
  - سبز -> سبز
  - آبی -> آبی
  - یشمی -> یشمی
  - عنابی -> عنابی
  - خاکی -> خاکی
  - طوسی -> طوسی
  - سربی -> سربی
  - موکا -> موکا
  - سرمه‌ای -> سرمه‌ای
  - زیتونی -> زیتونی
  - پوست‌پیازی -> پوست‌پیازی
  - نارنجی -> نارنجی
  - سفید صدفی -> سفید صدفی
  - اطلسی -> اطلسی
  - بنفش -> بنفش
  - قرمز -> قرمز
  - نقره‌ای -> نقره‌ای
  - دلفینی -> دلفینی
  - تیتانیوم -> تیتانیوم
  - عدسی -> عدسی
  - سفید -> سفید
  - زرد -> زرد

### divider
- **Title**: سایر فیلتر‌ها
- **Type**: object

### exchange
- **Title**: نمایش معاوضه‌ها
- **Type**: object
- **Queries**: 
  - only-exchanges -> نمایش فقط معاوضه‌ها
  - exclude-exchanges -> حذف معاوضه‌ها

### fuel_type
- **Title**: نوع سوخت
- **Type**: object
 - **Items Type**: array
- **Queries**: 
  - benzine -> بنزین
  - company-hybrid -> دوگانه‌سوز شرکتی
  - manual-hybrid -> دوگانه‌سوز دستی
  - gasoline -> گازوئیل

### gearbox
- **Title**: نوع گیربکس
- **Type**: object
- **Queries**: 
  - manual -> دنده‌ای
  - automatic -> اتوماتیک

### has-photo
- **Title**: فقط عکس‌دار
- **Type**: boolean

### installment_sale
- **Title**: نوع فروش
- **Type**: object
- **Queries**: 
  - cash -> نقدی
  - instalment -> اقساطی

### motor_status
- **Title**: وضعیت موتور
- **Type**: object
- **Queries**: 
  - healthy -> سالم
  - needs-repair -> نیاز به تعمیر
  - replaced -> تعویض شده

### price
- **Title**: قیمت
- **Type**: object
 - **Minimum**: 0
 - **Maximum**: N/A

### production-year
- **Title**: مدل (سال تولید)
- **Type**: object
 - **Minimum**: 0
 - **Maximum**: N/A

### sort
- **Title**: ترتیب نمایش آگهی‌ها براساس
- **Type**: object
- **Queries**: 
  - quality_and_sort_date -> quality_and_sort_date
  - sort_date -> sort_date
  - cheapest -> cheapest
  - most_expensive -> most_expensive
  - production_year -> production_year
  - usage -> usage
  - most_popular -> most_popular
  - most_relevant -> most_relevant

### third_party_insurance_deadline
- **Title**: مهلت بیمهٔ شخص ثالث
- **Type**: object
 - **Minimum**: 0
 - **Maximum**: 12

### urgent
- **Title**: فقط فوری‌ها
- **Type**: boolean

### usage
- **Title**: کارکرد
- **Type**: object
 - **Minimum**: 0
 - **Maximum**: N/A



---

### Category: literary



### category
- **Title**: دسته‌بندی
- **Type**: object

### divider
- **Title**: سایر فیلتر‌ها
- **Type**: object

### exchange
- **Title**: نمایش معاوضه‌ها
- **Type**: object
- **Queries**: 
  - only-exchanges -> نمایش فقط معاوضه‌ها
  - exclude-exchanges -> حذف معاوضه‌ها

### goods-business-type
- **Title**: نوع آگهی‌دهنده
- **Type**: object
- **Queries**: 
  - all -> همه
  - personal -> شخصی
  - marketplace -> فروشگاه

### has-photo
- **Title**: فقط عکس‌دار
- **Type**: boolean

### price
- **Title**: قیمت
- **Type**: object
 - **Minimum**: 0
 - **Maximum**: N/A

### sort
- **Title**: ترتیب نمایش آگهی‌ها براساس
- **Type**: object
- **Queries**: 
  - quality_and_sort_date -> quality_and_sort_date
  - sort_date -> sort_date
  - cheapest -> cheapest
  - most_expensive -> most_expensive
  - production_year -> production_year
  - usage -> usage
  - most_popular -> most_popular
  - most_relevant -> most_relevant

### status
- **Title**: وضعیت کالا
- **Type**: object
 - **Items Type**: array
- **Queries**: 
  - new -> نو
  - like-new -> در حد نو
  - used -> کارکرده
  - repair-needed -> نیازمند تعمیر

### urgent
- **Title**: فقط فوری‌ها
- **Type**: boolean



---

### Category: lost-and-found



### category
- **Title**: دسته‌بندی
- **Type**: object

### divider
- **Title**: سایر فیلتر‌ها
- **Type**: object

### exchange
- **Title**: نمایش معاوضه‌ها
- **Type**: object
- **Queries**: 
  - only-exchanges -> نمایش فقط معاوضه‌ها
  - exclude-exchanges -> حذف معاوضه‌ها

### has-photo
- **Title**: فقط عکس‌دار
- **Type**: boolean

### non-negotiable
- **Title**: حذف توافقی‌ها
- **Type**: boolean

### price
- **Title**: قیمت
- **Type**: object
 - **Minimum**: 0
 - **Maximum**: N/A

### sort
- **Title**: ترتیب نمایش آگهی‌ها براساس
- **Type**: object
- **Queries**: 
  - quality_and_sort_date -> quality_and_sort_date
  - sort_date -> sort_date
  - cheapest -> cheapest
  - most_expensive -> most_expensive
  - production_year -> production_year
  - usage -> usage
  - most_popular -> most_popular
  - most_relevant -> most_relevant

### urgent
- **Title**: فقط فوری‌ها
- **Type**: boolean



---

### Category: lost-animals



### category
- **Title**: دسته‌بندی
- **Type**: object

### divider
- **Title**: سایر فیلتر‌ها
- **Type**: object

### exchange
- **Title**: نمایش معاوضه‌ها
- **Type**: object
- **Queries**: 
  - only-exchanges -> نمایش فقط معاوضه‌ها
  - exclude-exchanges -> حذف معاوضه‌ها

### has-photo
- **Title**: فقط عکس‌دار
- **Type**: boolean

### non-negotiable
- **Title**: حذف توافقی‌ها
- **Type**: boolean

### price
- **Title**: قیمت
- **Type**: object
 - **Minimum**: 0
 - **Maximum**: N/A

### sort
- **Title**: ترتیب نمایش آگهی‌ها براساس
- **Type**: object
- **Queries**: 
  - quality_and_sort_date -> quality_and_sort_date
  - sort_date -> sort_date
  - cheapest -> cheapest
  - most_expensive -> most_expensive
  - production_year -> production_year
  - usage -> usage
  - most_popular -> most_popular
  - most_relevant -> most_relevant

### urgent
- **Title**: فقط فوری‌ها
- **Type**: boolean



---

### Category: lost-things



### category
- **Title**: دسته‌بندی
- **Type**: object

### divider
- **Title**: سایر فیلتر‌ها
- **Type**: object

### exchange
- **Title**: نمایش معاوضه‌ها
- **Type**: object
- **Queries**: 
  - only-exchanges -> نمایش فقط معاوضه‌ها
  - exclude-exchanges -> حذف معاوضه‌ها

### has-photo
- **Title**: فقط عکس‌دار
- **Type**: boolean

### non-negotiable
- **Title**: حذف توافقی‌ها
- **Type**: boolean

### price
- **Title**: قیمت
- **Type**: object
 - **Minimum**: 0
 - **Maximum**: N/A

### sort
- **Title**: ترتیب نمایش آگهی‌ها براساس
- **Type**: object
- **Queries**: 
  - quality_and_sort_date -> quality_and_sort_date
  - sort_date -> sort_date
  - cheapest -> cheapest
  - most_expensive -> most_expensive
  - production_year -> production_year
  - usage -> usage
  - most_popular -> most_popular
  - most_relevant -> most_relevant

### urgent
- **Title**: فقط فوری‌ها
- **Type**: boolean



---

### Category: lumbar-pillow



### category
- **Title**: دسته‌بندی
- **Type**: object

### divider
- **Title**: سایر فیلتر‌ها
- **Type**: object

### exchange
- **Title**: نمایش معاوضه‌ها
- **Type**: object
- **Queries**: 
  - only-exchanges -> نمایش فقط معاوضه‌ها
  - exclude-exchanges -> حذف معاوضه‌ها

### goods-business-type
- **Title**: نوع آگهی‌دهنده
- **Type**: object
- **Queries**: 
  - all -> همه
  - personal -> شخصی
  - marketplace -> فروشگاه

### has-photo
- **Title**: فقط عکس‌دار
- **Type**: boolean

### price
- **Title**: قیمت
- **Type**: object
 - **Minimum**: 0
 - **Maximum**: N/A

### sort
- **Title**: ترتیب نمایش آگهی‌ها براساس
- **Type**: object
- **Queries**: 
  - quality_and_sort_date -> quality_and_sort_date
  - sort_date -> sort_date
  - cheapest -> cheapest
  - most_expensive -> most_expensive
  - production_year -> production_year
  - usage -> usage
  - most_popular -> most_popular
  - most_relevant -> most_relevant

### status
- **Title**: وضعیت کالا
- **Type**: object
 - **Items Type**: array
- **Queries**: 
  - new -> نو
  - like-new -> در حد نو
  - used -> کارکرده
  - repair-needed -> نیازمند تعمیر

### urgent
- **Title**: فقط فوری‌ها
- **Type**: boolean



---

### Category: magazines



### category
- **Title**: دسته‌بندی
- **Type**: object

### divider
- **Title**: سایر فیلتر‌ها
- **Type**: object

### exchange
- **Title**: نمایش معاوضه‌ها
- **Type**: object
- **Queries**: 
  - only-exchanges -> نمایش فقط معاوضه‌ها
  - exclude-exchanges -> حذف معاوضه‌ها

### goods-business-type
- **Title**: نوع آگهی‌دهنده
- **Type**: object
- **Queries**: 
  - all -> همه
  - personal -> شخصی
  - marketplace -> فروشگاه

### has-photo
- **Title**: فقط عکس‌دار
- **Type**: boolean

### price
- **Title**: قیمت
- **Type**: object
 - **Minimum**: 0
 - **Maximum**: N/A

### sort
- **Title**: ترتیب نمایش آگهی‌ها براساس
- **Type**: object
- **Queries**: 
  - quality_and_sort_date -> quality_and_sort_date
  - sort_date -> sort_date
  - cheapest -> cheapest
  - most_expensive -> most_expensive
  - production_year -> production_year
  - usage -> usage
  - most_popular -> most_popular
  - most_relevant -> most_relevant

### status
- **Title**: وضعیت کالا
- **Type**: object
 - **Items Type**: array
- **Queries**: 
  - new -> نو
  - like-new -> در حد نو
  - used -> کارکرده
  - repair-needed -> نیازمند تعمیر

### urgent
- **Title**: فقط فوری‌ها
- **Type**: boolean



---

### Category: mat



### category
- **Title**: دسته‌بندی
- **Type**: object

### divider
- **Title**: سایر فیلتر‌ها
- **Type**: object

### exchange
- **Title**: نمایش معاوضه‌ها
- **Type**: object
- **Queries**: 
  - only-exchanges -> نمایش فقط معاوضه‌ها
  - exclude-exchanges -> حذف معاوضه‌ها

### goods-business-type
- **Title**: نوع آگهی‌دهنده
- **Type**: object
- **Queries**: 
  - all -> همه
  - personal -> شخصی
  - marketplace -> فروشگاه

### has-photo
- **Title**: فقط عکس‌دار
- **Type**: boolean

### price
- **Title**: قیمت
- **Type**: object
 - **Minimum**: 0
 - **Maximum**: N/A

### sort
- **Title**: ترتیب نمایش آگهی‌ها براساس
- **Type**: object
- **Queries**: 
  - quality_and_sort_date -> quality_and_sort_date
  - sort_date -> sort_date
  - cheapest -> cheapest
  - most_expensive -> most_expensive
  - production_year -> production_year
  - usage -> usage
  - most_popular -> most_popular
  - most_relevant -> most_relevant

### status
- **Title**: وضعیت کالا
- **Type**: object
 - **Items Type**: array
- **Queries**: 
  - new -> نو
  - like-new -> در حد نو
  - used -> کارکرده
  - repair-needed -> نیازمند تعمیر

### urgent
- **Title**: فقط فوری‌ها
- **Type**: boolean



---

### Category: mattress



### category
- **Title**: دسته‌بندی
- **Type**: object

### divider
- **Title**: سایر فیلتر‌ها
- **Type**: object

### exchange
- **Title**: نمایش معاوضه‌ها
- **Type**: object
- **Queries**: 
  - only-exchanges -> نمایش فقط معاوضه‌ها
  - exclude-exchanges -> حذف معاوضه‌ها

### goods-business-type
- **Title**: نوع آگهی‌دهنده
- **Type**: object
- **Queries**: 
  - all -> همه
  - personal -> شخصی
  - marketplace -> فروشگاه

### has-photo
- **Title**: فقط عکس‌دار
- **Type**: boolean

### price
- **Title**: قیمت
- **Type**: object
 - **Minimum**: 0
 - **Maximum**: N/A

### sort
- **Title**: ترتیب نمایش آگهی‌ها براساس
- **Type**: object
- **Queries**: 
  - quality_and_sort_date -> quality_and_sort_date
  - sort_date -> sort_date
  - cheapest -> cheapest
  - most_expensive -> most_expensive
  - production_year -> production_year
  - usage -> usage
  - most_popular -> most_popular
  - most_relevant -> most_relevant

### status
- **Title**: وضعیت کالا
- **Type**: object
 - **Items Type**: array
- **Queries**: 
  - new -> نو
  - like-new -> در حد نو
  - used -> کارکرده
  - repair-needed -> نیازمند تعمیر

### urgent
- **Title**: فقط فوری‌ها
- **Type**: boolean



---

### Category: media-advertising



### category
- **Title**: دسته‌بندی
- **Type**: object

### divider
- **Title**: سایر فیلتر‌ها
- **Type**: object

### employee_gender
- **Title**: جنسیت کارجو
- **Type**: object
- **Queries**: 
  - female -> زن
  - male -> مرد
  - neutral -> فرقی ندارد

### experience
- **Title**: سابقهٔ مورد نیاز
- **Type**: object
 - **Minimum**: N/A
 - **Maximum**: N/A

### has-photo
- **Title**: فقط عکس‌دار
- **Type**: boolean

### health_insurance
- **Title**: با بیمه
- **Type**: boolean

### job_type
- **Title**: نوع همکاری
- **Type**: object
 - **Items Type**: array
- **Queries**: 
  - full_time -> تمام وقت
  - part_time -> پاره وقت
  - contract -> پیمان‌کاری/پروژه‌ای
  - internship -> کارآموزی
  - adaptive -> توافقی
  - other -> سایر

### military_service_status
- **Title**: پایان خدمت/معافیت
- **Type**: object
- **Queries**: 
  - finish_or_exemption_required -> الزامی
  - finish_not_required -> اختیاری

### no_experience_required
- **Title**: بدون نیاز به سابقه
- **Type**: boolean

### payment_method
- **Title**: شیوهٔ پرداخت
- **Type**: object
 - **Items Type**: array
- **Queries**: 
  - monthly -> ماهانه
  - daily -> روزانه
  - hourly -> ساعتی
  - percentage_commission -> پورسانتی/درصدی
  - adaptive -> توافقی
  - other -> سایر

### remote
- **Title**: با امکان دورکاری
- **Type**: boolean

### sort
- **Title**: ترتیب نمایش آگهی‌ها براساس
- **Type**: object
- **Queries**: 
  - quality_and_sort_date -> quality_and_sort_date
  - sort_date -> sort_date
  - cheapest -> cheapest
  - most_expensive -> most_expensive
  - production_year -> production_year
  - usage -> usage
  - most_popular -> most_popular
  - most_relevant -> most_relevant

### urgent
- **Title**: فقط فوری‌ها
- **Type**: boolean



---

### Category: medical-equipment



### category
- **Title**: دسته‌بندی
- **Type**: object

### divider
- **Title**: سایر فیلتر‌ها
- **Type**: object

### exchange
- **Title**: نمایش معاوضه‌ها
- **Type**: object
- **Queries**: 
  - only-exchanges -> نمایش فقط معاوضه‌ها
  - exclude-exchanges -> حذف معاوضه‌ها

### goods-business-type
- **Title**: نوع آگهی‌دهنده
- **Type**: object
- **Queries**: 
  - all -> همه
  - personal -> شخصی
  - marketplace -> فروشگاه

### has-photo
- **Title**: فقط عکس‌دار
- **Type**: boolean

### price
- **Title**: قیمت
- **Type**: object
 - **Minimum**: 0
 - **Maximum**: N/A

### sort
- **Title**: ترتیب نمایش آگهی‌ها براساس
- **Type**: object
- **Queries**: 
  - quality_and_sort_date -> quality_and_sort_date
  - sort_date -> sort_date
  - cheapest -> cheapest
  - most_expensive -> most_expensive
  - production_year -> production_year
  - usage -> usage
  - most_popular -> most_popular
  - most_relevant -> most_relevant

### status
- **Title**: وضعیت کالا
- **Type**: object
 - **Items Type**: array
- **Queries**: 
  - new -> نو
  - like-new -> در حد نو
  - used -> کارکرده
  - repair-needed -> نیازمند تعمیر

### urgent
- **Title**: فقط فوری‌ها
- **Type**: boolean



---

### Category: mirror



### category
- **Title**: دسته‌بندی
- **Type**: object

### divider
- **Title**: سایر فیلتر‌ها
- **Type**: object

### exchange
- **Title**: نمایش معاوضه‌ها
- **Type**: object
- **Queries**: 
  - only-exchanges -> نمایش فقط معاوضه‌ها
  - exclude-exchanges -> حذف معاوضه‌ها

### goods-business-type
- **Title**: نوع آگهی‌دهنده
- **Type**: object
- **Queries**: 
  - all -> همه
  - personal -> شخصی
  - marketplace -> فروشگاه

### has-photo
- **Title**: فقط عکس‌دار
- **Type**: boolean

### price
- **Title**: قیمت
- **Type**: object
 - **Minimum**: 0
 - **Maximum**: N/A

### sort
- **Title**: ترتیب نمایش آگهی‌ها براساس
- **Type**: object
- **Queries**: 
  - quality_and_sort_date -> quality_and_sort_date
  - sort_date -> sort_date
  - cheapest -> cheapest
  - most_expensive -> most_expensive
  - production_year -> production_year
  - usage -> usage
  - most_popular -> most_popular
  - most_relevant -> most_relevant

### status
- **Title**: وضعیت کالا
- **Type**: object
 - **Items Type**: array
- **Queries**: 
  - new -> نو
  - like-new -> در حد نو
  - used -> کارکرده
  - repair-needed -> نیازمند تعمیر

### urgent
- **Title**: فقط فوری‌ها
- **Type**: boolean



---

### Category: mobile-phones



### base_color
- **Title**: رنگ
- **Type**: object
 - **Items Type**: array
- **Queries**: 
  - black -> مشکی
  - white -> سفید
  - green -> سبز
  - red -> قرمز
  - pink -> صورتی
  - gray -> خاکستری
  - gold -> طلایی
  - blue -> آبی
  - yellow -> زرد
  - silver -> نقره‌ای
  - orange -> نارنجی
  - purple -> بنفش
  - brown -> قهوه‌ای
  - آبی -> آبی
  - grey -> خاکستری

### brand_model
- **Title**: برند و مدل
- **Type**: object
 - **Items Type**: array
- **Queries**: 
  - ROOT -> همه‌ی برند‌ها
  - acer -> ایسر
  - acer liquid glow e330 -> ایسر Liquid Glow E330
  - acer liquid gallant e350 -> ایسر Liquid Gallant E350
  - acer liquid z110 -> ایسر Liquid Z110
  - acer liquid c1 -> ایسر Liquid C1
  - acer liquid e1 -> ایسر Liquid E1
  - acer liquid z2 -> ایسر Liquid Z2
  - acer liquid e2 -> ایسر Liquid E2
  - acer liquid s1 -> ایسر Liquid S1
  - acer liquid s2 -> ایسر Liquid S2
  - acer liquid z3 -> ایسر Liquid Z3
  - acer liquid e3 duo plus -> ایسر Liquid E3 Duo Plus
  - acer liquid z5 -> ایسر Liquid Z5
  - acer liquid e3 -> ایسر Liquid E3
  - acer liquid z4 -> ایسر Liquid Z4
  - acer liquid e600 -> ایسر Liquid E600
  - acer liquid e700 -> ایسر Liquid E700
  - acer liquid jade -> ایسر Liquid Jade
  - acer liquid x1 -> ایسر Liquid X1
  - acer liquid z200 -> ایسر Liquid Z200
  - acer liquid z500 -> ایسر Liquid Z500
  - acer liquid jade s -> ایسر Liquid Jade S
  - acer liquid z410 -> ایسر Liquid Z410
  - acer liquid z220 -> ایسر Liquid Z220
  - acer liquid z520 -> ایسر Liquid Z520
  - acer liquid x2 -> ایسر Liquid X2
  - acer liquid jade primo -> ایسر Liquid Jade Primo
  - acer liquid m320 -> ایسر Liquid M320
  - acer liquid m330 -> ایسر Liquid M330
  - acer liquid z320 -> ایسر Liquid Z320
  - acer liquid z330 -> ایسر Liquid Z330
  - acer liquid z530 -> ایسر Liquid Z530
  - acer liquid z530s -> ایسر Liquid Z530S
  - acer liquid z630 -> ایسر Liquid Z630
  - acer liquid z630s -> ایسر Liquid Z630S
  - acer liquid jade 2 -> ایسر Liquid Jade 2
  - acer liquid zest -> ایسر Liquid Zest
  - acer liquid zest plus -> ایسر Liquid Zest Plus
  - acer liquid z6 -> ایسر Liquid Z6
  - acer liquid z6 plus -> ایسر Liquid Z6 Plus
  - alcatel -> آلکاتل
  - alcatel fire s -> آلکاتل Fire S
  - alcatel ot-992d -> آلکاتل OT-992D
  - alcatel ot-995 -> آلکاتل OT-995
  - alcatel ot-997d -> آلکاتل OT-997D
  - alcatel ot-997 -> آلکاتل OT-997
  - alcatel ot-988 shockwave -> آلکاتل OT-988 Shockwave
  - alcatel ot-983 -> آلکاتل OT-983
  - alcatel one touch m'pop -> آلکاتل One Touch M'Pop
  - alcatel one touch t'pop -> آلکاتل One Touch T'Pop
  - alcatel one touch x'pop -> آلکاتل One Touch X'Pop
  - alcatel one touch evo 7 -> آلکاتل One Touch Evo 7
  - alcatel one touch idol -> آلکاتل One Touch Idol
  - alcatel one touch idol ultra -> آلکاتل One Touch Idol Ultra
  - alcatel one touch scribe hd -> آلکاتل One Touch Scribe HD
  - alcatel one touch scribe hd-lte -> آلکاتل One Touch Scribe HD-LTE
  - alcatel one touch scribe x -> آلکاتل One Touch Scribe X
  - alcatel idol x -> آلکاتل Idol X
  - alcatel one touch scribe easy -> آلکاتل One Touch Scribe Easy
  - alcatel one touch snap -> آلکاتل One Touch Snap
  - alcatel one touch star -> آلکاتل One Touch Star
  - alcatel idol s -> آلکاتل Idol S
  - alcatel one touch pixi -> آلکاتل One Touch Pixi
  - alcatel evolve -> آلکاتل Evolve
  - alcatel fierce -> آلکاتل Fierce
  - alcatel hero -> آلکاتل Hero
  - alcatel idol alpha -> آلکاتل Idol Alpha
  - alcatel pop c1 -> آلکاتل Pop C1
  - alcatel pop c3 -> آلکاتل Pop C3
  - alcatel pop c5 -> آلکاتل Pop C5
  - alcatel idol x+ -> آلکاتل Idol X+
  - alcatel pop 7 -> آلکاتل Pop 7
  - alcatel pop c9 -> آلکاتل Pop C9
  - alcatel pop fit -> آلکاتل Pop Fit
  - alcatel fire c -> آلکاتل Fire C
  - alcatel fire e -> آلکاتل Fire E
  - alcatel idol 2 s -> آلکاتل Idol 2 S
  - alcatel pop s3 -> آلکاتل Pop S3
  - alcatel pop s7 -> آلکاتل Pop S7
  - alcatel pop s9 -> آلکاتل Pop S9
  - alcatel pixi 2 -> آلکاتل Pixi 2
  - alcatel pop c2 -> آلکاتل Pop C2
  - alcatel fierce 2 -> آلکاتل Fierce 2
  - alcatel pop d1 -> آلکاتل Pop D1
  - alcatel pop d3 -> آلکاتل Pop D3
  - alcatel pop d5 -> آلکاتل Pop D5
  - alcatel flash -> آلکاتل Flash
  - alcatel hero 2 -> آلکاتل Hero 2
  - alcatel hero 8 -> آلکاتل Hero 8
  - alcatel pop 2 (4.5) -> آلکاتل Pop 2 (4.5)
  - alcatel pop 2 (4.5) dual sim -> آلکاتل Pop 2 (4.5) Dual SIM
  - alcatel pop 2 (5) -> آلکاتل Pop 2 (5)
  - alcatel pop 2 (5) premium -> آلکاتل Pop 2 (5) Premium
  - alcatel pop icon -> آلکاتل Pop Icon
  - alcatel evolve 2 -> آلکاتل Evolve 2
  - alcatel pixi 3 (3.5) -> آلکاتل Pixi 3 (3.5)
  - alcatel pixi 3 (3.5) firefox -> آلکاتل Pixi 3 (3.5) Firefox
  - alcatel pixi 3 (4) -> آلکاتل Pixi 3 (4)
  - alcatel pop 3 (5) -> آلکاتل Pop 3 (5)
  - alcatel orange klif -> آلکاتل Orange Klif
  - alcatel pixi 3 (5.5) -> آلکاتل Pixi 3 (5.5)
  - alcatel pixi 3 (5.5) lte -> آلکاتل Pixi 3 (5.5) LTE
  - alcatel pop astro -> آلکاتل Pop Astro
  - alcatel flash plus -> آلکاتل Flash Plus
  - alcatel flash 2 -> آلکاتل Flash 2
  - alcatel go play -> آلکاتل Go Play
  - alcatel idol 3c -> آلکاتل Idol 3C
  - alcatel pixi first -> آلکاتل Pixi First
  - alcatel pop star -> آلکاتل Pop Star
  - alcatel pop star lte -> آلکاتل Pop Star LTE
  - alcatel pop up -> آلکاتل Pop Up
  - alcatel fierce xl -> آلکاتل Fierce XL
  - alcatel x1 -> آلکاتل X1
  - alcatel fierce xl (windows) -> آلکاتل Fierce XL (Windows)
  - alcatel idol 4s windows -> آلکاتل Idol 4s Windows
  - alcatel pixi 3 (8) lte -> آلکاتل Pixi 3 8 LTE
  - alcatel pixi 4 (3.5) -> آلکاتل Pixi 4 (3.5)
  - alcatel pixi 4 (4) -> آلکاتل Pixi 4 (4)
  - alcatel pixi 4 (6) -> آلکاتل Pixi 4 (6)
  - alcatel idol 4s -> آلکاتل Idol 4s
  - alcatel pop 3 (5.5) -> آلکاتل Pop 3 (5.5)
  - alcatel pop 4 -> آلکاتل Pop 4
  - alcatel pop 4+ -> آلکاتل Pop 4+
  - alcatel pop 4s -> آلکاتل Pop 4S
  - alcatel pop 7 lte -> آلکاتل Pop 7 LTE
  - alcatel flash plus 2 -> آلکاتل Flash Plus 2
  - alcatel pixi 4 (5) -> آلکاتل Pixi 4 (5)
  - alcatel pixi 4 (6) 3g -> آلکاتل Pixi 4 (6) 3G
  - alcatel fierce 4 -> آلکاتل Fierce 4
  - alcatel pixi 4 plus power -> آلکاتل Pixi 4 Plus Power
  - alcatel shine lite -> آلکاتل Shine Lite
  - alcatel a3 xl -> آلکاتل A3 XL
  - alcatel a3 -> آلکاتل A3
  - alcatel a5 led -> آلکاتل A5 LED
  - alcatel u5 -> آلکاتل U5
  - alcatel flash (2017) -> آلکاتل Flash (2017)
  - alcatel idol 5s (usa) -> آلکاتل Idol 5s (USA)
  - alcatel pulsemix -> آلکاتل Pulsemix
  - alcatel u5 hd -> آلکاتل U5 HD
  - alcatel a7 -> آلکاتل A7
  - alcatel a7 xl -> آلکاتل A7 XL
  - alcatel idol 5 -> آلکاتل Idol 5
  - alcatel idol 5s -> آلکاتل Idol 5s
  - alcatel 1t 10 -> آلکاتل 1T 10
  - alcatel 1t 7 -> آلکاتل 1T 7
  - alcatel 3 -> آلکاتل 3
  - alcatel 3c -> آلکاتل 3c
  - alcatel 3x (2018) -> آلکاتل 3x (2018)
  - alcatel 1x -> آلکاتل 1x
  - alcatel 3v -> آلکاتل 3v
  - alcatel 5 -> آلکاتل 5
  - alcatel 1 -> آلکاتل 1
  - alcatel 5v -> آلکاتل 5v
  - alcatel 7 -> آلکاتل 7
  - alcatel tetra -> آلکاتل Tetra
  - alcatel 3t 8 -> آلکاتل 3T 8
  - alcatel 1c (2019) -> آلکاتل 1c (2019)
  - alcatel go flip v -> آلکاتل Go Flip V
  - alcatel 1s -> آلکاتل 1s
  - alcatel 1x (2019) -> آلکاتل 1x (2019)
  - alcatel 3088 -> آلکاتل 3088
  - alcatel 3 (2019) -> آلکاتل 3 (2019)
  - alcatel 3l -> آلکاتل 3L
  - alcatel 3v (2019) -> آلکاتل 3v (2019)
  - alcatel 3t 10 -> آلکاتل 3T 10
  - alcatel 1v (2019) -> آلکاتل 1v (2019)
  - alcatel 3x (2019) -> آلکاتل 3x (2019)
  - alcatel go flip 3 -> آلکاتل Go Flip 3
  - alcatel 1b (2020) -> آلکاتل 1B (2020)
  - alcatel 1s (2020) -> آلکاتل وان 1S 2020
  - alcatel 1v (2020) -> آلکاتل 1V 2020
  - alcatel 3l (2020) -> آلکاتل 3L (2020)
  - alcatel 3x (2020) -> آلکاتل 3X (2020)
  - alcatel 1se (2020) -> آلکاتل 1SE (2020)
  - alcatel 1 (2021) -> آلکاتل وان 2021
  - alcatel 1l (2021) -> آلکاتل 1L (2021)
  - alcatel 1l pro (2021) -> آلکاتل 1L Pro 2021
  - alcatel 1s (2021) -> آلکاتل 1S 2020
  - alcatel 1v (2021) -> آلکاتل 1V (2021)
  - alcatel 3l (2021) -> آلکاتل 3L (2021)
  - alcatel 1b (2022) -> آلکاتل 1B (2022)
  - allview -> آلویو
  - allview x4 soul infinity l -> آلویو X4 Soul Infinity L
  - allview x4 soul infinity n -> آلویو X4 Soul Infinity N
  - allview x4 soul infinity plus -> آلویو X4 Soul Infinity Plus
  - allview x4 soul infinity s -> آلویو X4 Soul Infinity S
  - allview x4 soul infinity z -> آلویو X4 Soul Infinity Z
  - allview x4 soul vision -> آلویو X4 Soul Vision
  - allview p8 pro -> آلویو P8 Pro
  - allview v3 viper -> آلویو V3 Viper
  - allview soul x5 pro -> آلویو Soul X5 Pro
  - allview soul x5 mini -> آلویو Soul X5 Mini
  - allview x5 soul -> آلویو X5 Soul
  - allview a10 lite 2019 -> آلویو A10 Lite 2019
  - allview p10 style -> آلویو P10 Style
  - allview a10 plus -> آلویو A10 Plus
  - allview soul x5 style -> آلویو Soul X5 Style
  - allview p10 life -> آلویو P10 Life
  - allview p10 max -> آلویو P10 Max
  - allview p10 mini -> آلویو P10 Mini
  - allview p10 pro -> آلویو P10 Pro
  - allview soul x6 xtreme -> آلویو Soul X6 Xtreme
  - allview soul x6 mini -> آلویو Soul X6 Mini
  - allview viva home -> آلویو Viva Home
  - allview viva 1003g -> آلویو Viva 1003G
  - allview v4 viper -> آلویو V4 Viper
  - allview viva 1003g lite -> آلویو Viva 1003G Lite
  - allview viva c703 -> آلویو Viva C703
  - allview soul x7 pro -> آلویو Soul X7 Pro
  - allview v4 viper pro -> آلویو V4 Viper Pro
  - allview viva 803g -> آلویو Viva 803G
  - amazon -> آمازون
  - amazon fire phone -> آمازون Fire Phone
  - amazon fire hd 10 (2019) -> آمازون فایر HD 10 2019
  - amazon fire hd 8 (2020) -> آمازون Fire HD 8 (2020)
  - amazon fire hd 8 plus (2020) -> آمازون Fire HD 8 Plus (2020)
  - amazon fire hd 10 (2021) -> آمازون فایر HD 10 2021
  - amazon fire hd 10 plus (2021) -> آمازون فایر HD 10 پلاس 2021
  - apple -> اپل
  - apple iphone 4 -> اپل iPhone 4
  - apple iphone 4 cdma -> اپل iPhone 4 CDMA
  - apple iphone 4s -> اپل iPhone 4s
  - apple iphone 5 -> اپل iPhone 5
  - apple iphone 5c -> اپل iPhone 5c
  - apple iphone 5s -> اپل iPhone 5s
  - apple iphone 6 -> اپل iPhone 6
  - apple iphone 6 plus -> اپل iPhone 6 Plus
  - apple iphone 6s -> اپل iPhone 6s
  - apple iphone 6s plus -> اپل iPhone 6s Plus
  - apple iphone se -> اپل iPhone SE
  - apple iphone 7 -> اپل iPhone 7
  - apple iphone 7 plus -> اپل iPhone 7 Plus
  - apple iphone 8 -> اپل iPhone 8
  - apple iphone 8 plus -> اپل iPhone 8 Plus
  - apple iphone x -> اپل iPhone X
  - apple iphone xr -> اپل iPhone XR
  - apple iphone xs -> اپل iPhone XS
  - apple iphone xs max -> اپل iPhone XS Max
  - apple iphone 11 -> اپل iPhone 11
  - apple iphone 11 pro -> اپل iPhone 11 Pro
  - apple iphone 11 pro max -> اپل iPhone 11 Pro Max
  - apple iphone se (2020) -> اپل iPhone SE (2020)
  - apple ipad 10.2 (2020) -> اپل iPad 10.2 (2020)
  - apple ipad air (2020) -> اپل iPad Air (2020)
  - apple iphone 12 -> اپل iPhone 12
  - apple iphone 12 mini -> اپل iPhone 12 mini
  - apple iphone 12 pro -> اپل iPhone 12 Pro
  - apple iphone 12 pro max -> اپل iPhone 12 Pro Max
  - apple iphone 13 -> اپل iPhone 13
  - apple iphone 13 mini -> اپل iPhone 13 mini
  - apple iphone 13 pro -> اپل iPhone 13 Pro
  - apple iphone 13 pro max -> اپل iPhone 13 Pro Max
  - apple iphone 14 -> اپل آیفون 14
  - apple iphone 14 plus -> اپل آیفون 14 پلاس
  - apple iphone 14 pro -> اپل آیفون 14 پرو
  - apple iphone 14 pro max -> اپل آیفون 14 پرو مکس
  - apple iphone se (2022) -> اپل iPhone SE (2022)
  - archos -> آرکاس
  - archos 40 titanium -> آرکاس 40 Titanium
  - archos 45 platinum -> آرکاس 45 Platinum
  - archos 45 titanium -> آرکاس 45 Titanium
  - archos 50 oxygen -> آرکاس 50 Oxygen
  - archos 50 platinum -> آرکاس 50 Platinum
  - archos 50 titanium -> آرکاس 50 Titanium
  - archos 53 platinum -> آرکاس 53 Platinum
  - archos 53 titanium -> آرکاس 53 Titanium
  - archos 45 helium 4g -> آرکاس 45 Helium 4G
  - archos 50 helium 4g -> آرکاس 50 Helium 4G
  - archos 40b titanium -> آرکاس 40b Titanium
  - archos 40c titanium -> آرکاس 40c Titanium
  - archos 50c oxygen -> آرکاس 50c Oxygen
  - archos 64 xenon -> آرکاس 64 Xenon
  - archos 50b platinum -> آرکاس 50b Platinum
  - archos 50b helium 4g -> آرکاس 50b Helium 4G
  - archos 50 diamond -> آرکاس 50 Diamond
  - archos 50d helium 4g -> آرکاس 50d Helium 4G
  - archos diamond plus -> آرکاس Diamond Plus
  - archos diamond s -> آرکاس Diamond S
  - archos 50 cobalt -> آرکاس 50 Cobalt
  - archos 55 cobalt plus -> آرکاس 55 Cobalt Plus
  - archos diamond 2 plus -> آرکاس Diamond 2 Plus
  - archos 50b cobalt -> آرکاس 50b Cobalt
  - archos 55b cobalt -> آرکاس 55b Cobalt
  - archos 50 graphite -> آرکاس 50 Graphite
  - archos 50 saphir -> آرکاس 50 Saphir
  - archos 55 graphite -> آرکاس 55 Graphite
  - archos diamond alpha -> آرکاس Diamond Alpha
  - archos diamond gamma -> آرکاس Diamond Gamma
  - archos sense 50x -> آرکاس Sense 50x
  - archos sense 55s -> آرکاس Sense 55s
  - archos diamond alpha + -> آرکاس Diamond Alpha +
  - archos diamond omega -> آرکاس Diamond Omega
  - archos saphir 50x -> آرکاس Saphir 50X
  - archos diamond -> آرکاس Diamond
  - archos oxygen 57 -> آرکاس Oxygen 57
  - archos oxygen 63 -> آرکاس Oxygen 63
  - archos oxygen 68xl -> آرکاس Oxygen 68XL
  - asus -> ایسوس
  - asus zenfone pegasus 3s -> ایسوس Zenfone Pegasus 3s
  - asus padfone 2 -> ایسوس PadFone 2
  - asus padfone infinity -> ایسوس PadFone Infinity
  - asus fonepad note fhd6 -> ایسوس Fonepad Note FHD6
  - asus padfone infinity 2 -> ایسوس PadFone Infinity 2
  - asus padfone mini -> ایسوس PadFone mini
  - asus padfone mini (intel) -> ایسوس PadFone mini (Intel)
  - asus zenfone 4 (2014) -> ایسوس Zenfone 4 (2014)
  - asus zenfone 5 a500cg (2014) -> ایسوس Zenfone 5 A500CG (2014)
  - asus zenfone 6 a600cg (2014) -> ایسوس Zenfone 6 A600CG (2014)
  - asus zenfone 6 a601cg (2014) -> ایسوس Zenfone 6 A601CG (2014)
  - asus padfone infinity lite -> ایسوس PadFone Infinity Lite
  - asus padfone s -> ایسوس PadFone S
  - asus padfone x -> ایسوس PadFone X
  - asus zenfone 4 a450cg (2014) -> ایسوس Zenfone 4 A450CG (2014)
  - asus zenfone 5 a500kl (2014) -> ایسوس Zenfone 5 A500KL (2014)
  - asus padfone mini 4g (intel) -> ایسوس PadFone mini 4G (Intel)
  - asus padfone x mini -> ایسوس PadFone X mini
  - asus pegasus -> ایسوس Pegasus
  - asus zenfone 2 ze551ml -> ایسوس Zenfone 2 ZE551ML
  - asus zenfone 5 a501cg (2015) -> ایسوس Zenfone 5 A501CG (2015)
  - asus zenfone c zc451cg -> ایسوس Zenfone C ZC451CG
  - asus zenfone zoom zx550 -> ایسوس Zenfone Zoom ZX550
  - asus zenfone 2 ze550ml -> ایسوس Zenfone 2 ZE550ML
  - asus zenfone selfie zd551kl -> ایسوس Zenfone Selfie ZD551KL
  - asus pegasus 2 plus -> ایسوس Pegasus 2 Plus
  - asus zenfone 2e -> ایسوس Zenfone 2E
  - asus zenfone 2 deluxe ze551ml -> ایسوس Zenfone 2 Deluxe ZE551ML
  - asus zenfone 2 laser ze601kl -> ایسوس Zenfone 2 Laser ZE601KL
  - asus zenfone go zc500tg -> ایسوس Zenfone Go ZC500TG
  - asus zenfone max zc550kl -> ایسوس Zenfone Max ZC550KL
  - asus zenfone zoom zx551ml -> ایسوس Zenfone Zoom ZX551ML
  - asus zenfone go zc451tg -> ایسوس Zenfone Go ZC451TG
  - asus zenfone go t500 -> ایسوس Zenfone Go T500
  - asus zenfone go zb452kg -> ایسوس Zenfone Go ZB452KG
  - asus zenfone go zb551kl -> ایسوس Zenfone Go ZB551KL
  - asus zenfone 3 deluxe zs570kl -> ایسوس Zenfone 3 Deluxe ZS570KL
  - asus zenfone 3 ultra zu680kl -> ایسوس Zenfone 3 Ultra ZU680KL
  - asus zenfone 3 ze552kl -> ایسوس Zenfone 3 ZE552KL
  - asus zenfone max zc550kl (2016) -> ایسوس Zenfone Max ZC550KL (2016)
  - asus zenfone pegasus 3 -> ایسوس Zenfone Pegasus 3
  - asus zenfone 3 laser zc551kl -> ایسوس Zenfone 3 Laser ZC551KL
  - asus zenfone go zb450kl -> ایسوس Zenfone Go ZB450KL
  - asus zenfone 3 deluxe 5.5 zs550kl -> ایسوس Zenfone 3 Deluxe 5.5 ZS550KL
  - asus zenfone go zb500kl -> ایسوس Zenfone Go ZB500KL
  - asus zenfone 3 max zc553kl -> ایسوس Zenfone 3 Max ZC553KL
  - asus zenfone go zb690kg -> ایسوس Zenfone Go ZB690KG
  - asus zenfone 3s max zc521tl -> ایسوس Zenfone 3s Max ZC521TL
  - asus zenfone 3 zoom ze553kl -> ایسوس Zenfone 3 Zoom ZE553KL
  - asus zenfone ar zs571kl -> ایسوس Zenfone AR ZS571KL
  - asus zenfone live zb501kl -> ایسوس Zenfone Live ZB501KL
  - asus zenfone go zb552kl -> ایسوس Zenfone Go ZB552KL
  - asus zenfone 4 max zc554kl -> ایسوس ذن فون 4 مکس ZC554KL
  - asus zenfone 4 max plus zc554kl -> ایسوس Zenfone 4 Max Plus ZC554KL
  - asus zenfone 4 max pro zc554kl -> ایسوس Zenfone 4 Max Pro ZC554KL
  - asus zenfone 4 max zc520kl -> ایسوس Zenfone 4 Max ZC520KL
  - asus zenfone 4 pro zs551kl -> ایسوس Zenfone 4 Pro ZS551KL
  - asus zenfone 4 selfie pro zd552kl -> ایسوس Zenfone 4 Selfie Pro ZD552KL
  - asus zenfone 4 selfie zd553kl -> ایسوس Zenfone 4 Selfie ZD553KL
  - asus zenfone 4 ze554kl -> ایسوس Zenfone 4 ZE554KL
  - asus zenfone v v520kl -> ایسوس Zenfone V V520KL
  - asus zenfone 4 selfie zb553kl -> ایسوس Zenfone 4 Selfie ZB553KL
  - asus zenfone 4 selfie lite zb553kl -> ایسوس Zenfone 4 Selfie Lite ZB553KL
  - asus zenfone max plus (m1) zb570tl -> ایسوس Zenfone Max Plus (M1) ZB570TL
  - asus zenfone 5 lite zc600kl -> ایسوس Zenfone 5 Lite ZC600KL
  - asus zenfone 5 ze620kl -> ایسوس Zenfone 5 ZE620KL
  - asus zenfone 5z zs620kl -> ایسوس Zenfone 5z ZS620KL
  - asus zenfone max (m1) zb555kl -> ایسوس Zenfone Max (M1) ZB555KL
  - asus zenfone max pro (m1) zb601kl/zb602k -> ایسوس Zenfone Max Pro (M1) ZB601KL/ZB602K
  - asus zenfone live (l1) za550kl -> ایسوس ZenFone Live (L1) ZA550KL
  - asus rog phone zs600kl -> ایسوس ROG Phone ZS600KL
  - asus zenfone lite (l1) za551kl -> ایسوس ZenFone Lite (L1) ZA551KL
  - asus zenfone max (m1) zb556kl -> ایسوس Zenfone Max (M1) ZB556KL
  - asus zenfone max (m2) zb633kl -> ایسوس Zenfone Max (M2) ZB633KL
  - asus zenfone max pro (m2) zb631kl -> ایسوس Zenfone Max Pro (M2) ZB631KL
  - asus zenfone max plus (m2) zb634kl -> ایسوس Zenfone Max Plus (M2) ZB634KL
  - asus zenfone max shot zb634kl -> ایسوس Zenfone Max Shot ZB634KL
  - asus zenfone live (l2) -> ایسوس ZenFone Live (L2)
  - asus zenfone 6 zs630kl -> ایسوس Zenfone 6 ZS630KL
  - asus rog phone ii zs660kl -> ایسوس ROG Phone II ZS660KL
  - asus rog phone 3 -> ایسوس ROG فون 3
  - asus zenfone 7 -> ایسوس Zenfone 7
  - asus zenfone 7 pro -> ایسوس Zenfone 7 Pro
  - asus rog phone 3 strix -> ایسوس ROG Phone 3 Strix
  - asus rog phone 3 zs661ks -> ایسوس ROG Phone 3 ZS661KS
  - asus zenfone 7 pro zs671ks -> ایسوس Zenfone 7 Pro ZS671KS
  - asus zenfone 7 zs670ks -> ایسوس Zenfone 7 ZS670KS
  - asus rog phone 5 -> ایسوس ROG Phone 5
  - asus rog phone 5 pro -> ایسوس ROG Phone 5 Pro
  - asus rog phone 5 ultimate -> ایسوس ROG Phone 5 Ultimate
  - asus zenfone 8 -> ایسوس Zenfone 8
  - asus zenfone 8 flip -> ایسوس Zenfone 8 Flip
  - asus smartphone for snapdragon insiders -> ایسوس Smartphone for Snapdragon Insiders
  - asus rog phone 5s -> ایسوس ROG Phone 5s
  - asus rog phone 5s pro -> ایسوس ROG Phone 5s Pro
  - asus rog phone 6 -> ایسوس ROG فون 6
  - asus rog phone 6 batman edition -> ایسوس ROG Phone 6 Batman Edition
  - asus rog phone 6d -> ایسوس ROG Phone 6D
  - asus rog phone 6d ultimate -> ایسوس ROG فون 6D Ultimate
  - asus rog phone 6 pro -> ایسوس ROG فون 6 پرو
  - asus zenfone 9 -> ایسوس ذن فون 9
  - blackberry -> بلک‌بری
  - blackberry a10 -> بلک‌بری A10
  - blackberry porsche design p'9531 -> بلک‌بری Porsche Design P'9531
  - blackberry porsche design p'9981 -> بلک‌بری Porsche Design P'9981
  - blackberry q10 -> بلک‌بری Q10
  - blackberry z10 -> بلک‌بری Z10
  - blackberry q5 -> بلک‌بری Q5
  - blackberry 9720 -> بلک‌بری 9720
  - blackberry z30 -> بلک‌بری Z30
  - blackberry porsche design p'9982 -> بلک‌بری Porsche Design P'9982
  - blackberry z3 -> بلک‌بری Z3
  - blackberry classic -> بلک‌بری Classic
  - blackberry passport -> بلک‌بری Passport
  - blackberry porsche design p'9983 -> بلک‌بری Porsche Design P'9983
  - blackberry classic non camera -> بلک‌بری Classic Non Camera
  - blackberry leap -> بلک‌بری Leap
  - blackberry priv -> بلک‌بری Priv
  - blackberry dtek50 -> بلک‌بری DTEK50
  - blackberry dtek60 -> بلک‌بری DTEK60
  - blackberry keyone -> بلک‌بری Keyone
  - blackberry aurora -> بلک‌بری Aurora
  - blackberry motion -> بلک‌بری Motion
  - blackberry key2 -> بلک‌بری KEY2
  - blackberry evolve -> بلک‌بری Evolve
  - blackberry evolve x -> بلک‌بری Evolve X
  - blackberry key2 le -> بلک‌بری KEY2 LE
  - blu -> بلو
  - blu studio 5.3 -> بلو Studio 5.3
  - blu elite 3.8 -> بلو Elite 3.8
  - blu dash 3.5 -> بلو Dash 3.5
  - blu dash 3.2 -> بلو Dash 3.2
  - blu dash 4.0 -> بلو Dash 4.0
  - blu vivo 4.65 hd -> بلو Vivo 4.65 HD
  - blu quattro 4.5 -> بلو Quattro 4.5
  - blu quattro 4.5 hd -> بلو Quattro 4.5 HD
  - blu quattro 5.7 hd -> بلو Quattro 5.7 HD
  - blu studio 5.3 ii -> بلو Studio 5.3 II
  - blu tank 4.5 -> بلو Tank 4.5
  - blu life one -> بلو Life One
  - blu life play -> بلو Life Play
  - blu life view -> بلو Life View
  - blu dash music -> بلو Dash Music
  - blu studio 5.0 -> بلو Studio 5.0
  - blu studio 5.0 s -> بلو Studio 5.0 S
  - blu studio 5.3 s -> بلو Studio 5.3 S
  - blu amour -> بلو Amour
  - blu dash 4.5 -> بلو Dash 4.5
  - blu dash 5.0 -> بلو Dash 5.0
  - blu dash jr -> بلو Dash JR
  - blu dash music 4.0 -> بلو Dash Music 4.0
  - blu zoey -> بلو Zoey
  - blu studio 5.5 -> بلو Studio 5.5
  - blu life pro -> بلو Life Pro
  - blu advance 4.0 -> بلو Advance 4.0
  - blu life play x -> بلو Life Play X
  - blu life pure -> بلو Life Pure
  - blu studio 5.0 ii -> بلو Studio 5.0 II
  - blu life one m -> بلو Life One M
  - blu life one x -> بلو Life One X
  - blu life play s -> بلو Life Play S
  - blu studio 5.0 e -> بلو Studio 5.0 E
  - blu studio 5.0 s ii -> بلو Studio 5.0 S II
  - blu studio 5.5 s -> بلو Studio 5.5 S
  - blu vivo 4.8 hd -> بلو Vivo 4.8 HD
  - blu life pure mini -> بلو Life Pure Mini
  - blu neo 3.5 -> بلو Neo 3.5
  - blu neo 4.5 -> بلو Neo 4.5
  - blu studio 5.0 lte -> بلو Studio 5.0 LTE
  - blu studio 6.0 hd -> بلو Studio 6.0 HD
  - blu life 8 -> بلو Life 8
  - blu vivo iv -> بلو Vivo IV
  - blu studio 5.0 c -> بلو Studio 5.0 C
  - blu studio 5.0 ce -> بلو Studio 5.0 CE
  - blu studio 5.0 c hd -> بلو Studio 5.0 C HD
  - blu studio c mini -> بلو Studio C Mini
  - blu win hd -> بلو Win HD
  - blu win jr -> بلو Win JR
  - blu life play mini -> بلو Life Play Mini
  - blu sport 4.5 -> بلو Sport 4.5
  - blu dash c music -> بلو Dash C Music
  - blu dash music jr -> بلو Dash Music JR
  - blu studio mini lte -> بلو Studio Mini LTE
  - blu studio 5.0 hd lte -> بلو Studio 5.0 HD LTE
  - blu studio 6.0 lte -> بلو Studio 6.0 LTE
  - blu life one (2015) -> بلو Life One (2015)
  - blu life one xl -> بلو Life One XL
  - blu studio energy -> بلو Studio Energy
  - blu studio g -> بلو Studio G
  - blu studio x -> بلو Studio X
  - blu studio x plus -> بلو Studio X Plus
  - blu vivo air -> بلو Vivo Air
  - blu selfie -> بلو Selfie
  - blu win hd lte -> بلو Win HD LTE
  - blu win jr lte -> بلو Win JR LTE
  - blu advance 4.0 l -> بلو Advance 4.0 L
  - blu life 8 xl -> بلو Life 8 XL
  - blu studio 5.5c -> بلو Studio 5.5C
  - blu studio c -> بلو Studio C
  - blu energy x plus -> بلو Energy X Plus
  - blu life x8 -> بلو Life X8
  - blu studio c 5 + 5 -> بلو Studio C 5 + 5
  - blu studio c 5 + 5 lte -> بلو Studio C 5 + 5 LTE
  - blu vivo selfie -> بلو Vivo Selfie
  - blu studio c super camera -> بلو Studio C Super Camera
  - blu studio xl -> بلو Studio XL
  - blu energy x -> بلو Energy X
  - blu pure xl -> بلو Pure XL
  - blu vivo air lte -> بلو Vivo Air LTE
  - blu dash l -> بلو Dash L
  - blu dash m -> بلو Dash M
  - blu dash x -> بلو Dash X
  - blu dash x plus -> بلو Dash X Plus
  - blu studio energy 2 -> بلو Studio Energy 2
  - blu studio g lte -> بلو Studio G LTE
  - blu dash x lte -> بلو Dash X LTE
  - blu studio g plus -> بلو Studio G Plus
  - blu life one x (2016) -> بلو Life One X (2016)
  - blu life xl -> بلو Life XL
  - blu studio c hd -> بلو Studio C HD
  - blu vivo 5 -> بلو Vivo 5
  - blu vivo xl -> بلو Vivo XL
  - blu energy x 2 -> بلو Energy X 2
  - blu neo x plus -> بلو Neo X Plus
  - blu studio g hd -> بلو Studio G HD
  - blu studio m hd -> بلو Studio M HD
  - blu studio one -> بلو Studio One
  - blu studio one plus -> بلو Studio One Plus
  - blu dash x plus lte -> بلو Dash X Plus LTE
  - blu energy x lte -> بلو Energy X LTE
  - blu life mark -> بلو Life Mark
  - blu neo xl -> بلو Neo XL
  - blu studio 5.5 hd -> بلو Studio 5.5 HD
  - blu studio x mini -> بلو Studio X Mini
  - blu advance 4.0 l2 -> بلو Advance 4.0 L2
  - blu dash m2 -> بلو Dash M2
  - blu dash x2 -> بلو Dash X2
  - blu neo x -> بلو Neo X
  - blu studio selfie 2 -> بلو Studio Selfie 2
  - blu studio x8 hd -> بلو Studio X8 HD
  - blu dash l2 -> بلو Dash L2
  - blu energy jr -> بلو Energy JR
  - blu r1 hd -> بلو R1 HD
  - blu studio touch -> بلو Studio Touch
  - blu dash 4.5 (2016) -> بلو Dash 4.5 (2016)
  - blu energy diamond mini -> بلو Energy Diamond Mini
  - blu energy xl -> بلو Energy XL
  - blu grand 5.5 hd -> بلو Grand 5.5 HD
  - blu neo x mini -> بلو Neo X Mini
  - blu diamond m -> بلو Diamond M
  - blu energy diamond -> بلو Energy Diamond
  - blu energy m -> بلو Energy M
  - blu neo x lte -> بلو Neo X LTE
  - blu pure xr -> بلو Pure XR
  - blu studio c 8+8 -> بلو Studio C 8+8
  - blu studio c 8+8 lte -> بلو Studio C 8+8 LTE
  - blu studio g2 -> بلو Studio G2
  - blu studio g hd lte -> بلو Studio G HD LTE
  - blu studio m lte -> بلو Studio M LTE
  - blu life one x2 -> بلو Life One X2
  - blu vivo 5r -> بلو Vivo 5R
  - blu advance 4.0 m -> بلو Advance 4.0 M
  - blu dash g -> بلو Dash G
  - blu dash xl -> بلو Dash XL
  - blu energy x plus 2 -> بلو Energy X Plus 2
  - blu life max -> بلو Life Max
  - blu studio g max -> بلو Studio G Max
  - blu studio g plus hd -> بلو Studio G Plus HD
  - blu studio j5 -> بلو Studio J5
  - blu studio max -> بلو Studio Max
  - blu studio xl2 -> بلو Studio XL2
  - blu vivo 6 -> بلو Vivo 6
  - blu studio g2 hd -> بلو Studio G2 HD
  - blu advance 4.0 l3 -> بلو Advance 4.0 L3
  - blu dash l3 -> بلو Dash L3
  - blu grand energy -> بلو Grand Energy
  - blu grand m -> بلو Grand M
  - blu grand max -> بلو Grand Max
  - blu grand x -> بلو Grand X
  - blu life one x2 mini -> بلو Life One X2 Mini
  - blu tank xtreme 4.0 -> بلو Tank Xtreme 4.0
  - blu tank xtreme 5.0 -> بلو Tank Xtreme 5.0
  - blu vivo 5 mini -> بلو Vivo 5 Mini
  - blu vivo xl2 -> بلو Vivo XL2
  - blu studio selfie lte -> بلو Studio Selfie LTE
  - blu r1 plus -> بلو R1 Plus
  - blu studio j2 -> بلو Studio J2
  - blu grand xl -> بلو Grand XL
  - blu grand x lte -> بلو Grand X LTE
  - blu studio j1 -> بلو Studio J1
  - blu studio mega -> بلو Studio Mega
  - blu r2 -> بلو R2
  - blu r2 lte -> بلو R2 LTE
  - blu studio j8 -> بلو Studio J8
  - blu studio j8 lte -> بلو Studio J8 LTE
  - blu tank xtreme pro -> بلو Tank Xtreme Pro
  - blu grand mini -> بلو Grand Mini
  - blu grand xl lte -> بلو Grand XL LTE
  - blu studio g mini -> بلو Studio G Mini
  - blu studio pro -> بلو Studio Pro
  - blu vivo 8 -> بلو Vivo 8
  - blu s1 -> بلو S1
  - blu c5 (2017) -> بلو C5 (2017)
  - blu grand m2 -> بلو Grand M2
  - blu grand m2 lte -> بلو Grand M2 LTE
  - blu studio g3 -> بلو Studio G3
  - blu c5 lte -> بلو C5 LTE
  - blu dash l5 lte -> بلو Dash L5 LTE
  - blu grand 5.5 hd ii -> بلو Grand 5.5 HD II
  - blu life one x3 -> بلو Life One X3
  - blu r2 plus -> بلو R2 Plus
  - blu dash l4 -> بلو Dash L4
  - blu dash l4 lte -> بلو Dash L4 LTE
  - blu studio view -> بلو Studio View
  - blu pure view -> بلو Pure View
  - blu studio view xl -> بلو Studio View XL
  - blu vivo one -> بلو Vivo One
  - blu vivo x -> بلو Vivo X
  - blu studio j8m lte -> بلو Studio J8M LTE
  - blu vivo xl3 -> بلو Vivo XL3
  - blu x link -> بلو X Link
  - blu vivo xl3 plus -> بلو Vivo XL3 Plus
  - blu vivo one plus -> بلو Vivo One Plus
  - blu c6 -> بلو C6
  - blu grand m3 -> بلو Grand M3
  - blu c4 -> بلو C4
  - blu studio g4 -> بلو Studio G4
  - blu vivo xi+ -> بلو Vivo XI+
  - blu c5 -> بلو C5
  - blu vivo xi -> بلو Vivo XI
  - blu advance l4 -> بلو Advance L4
  - blu grand m2 (2018) -> بلو Grand M2 (2018)
  - blu studio mega (2018) -> بلو Studio Mega (2018)
  - blu vivo go -> بلو Vivo Go
  - blu c6l -> بلو C6L
  - blu vivo xl4 -> بلو Vivo XL4
  - blu vivo one plus (2019) -> بلو Vivo One Plus (2019)
  - blu c5l -> بلو C5L
  - blu studio x8 hd (2019) -> بلو Studio X8 HD (2019)
  - blu g9 -> بلو G9
  - blu g5 -> بلو G5
  - blu g5 plus -> بلو G5 Plus
  - blu g6 -> بلو G6
  - blu g8 -> بلو G8
  - blu vivo xl5 -> بلو Vivo XL5
  - blu g9 pro -> بلو G9 Pro
  - blu studio mini -> بلو Studio Mini
  - blu vivo x5 -> بلو X5 ویوو
  - blu advance l5 -> بلو Advance L5
  - blu bold n1 -> بلو Bold N1
  - blu j4 -> بلو J4
  - blu studio mega 2019 -> بلو Studio Mega 2019
  - blu c5 2019 -> بلو C5 2019
  - blu c5 plus -> بلو C5 Plus
  - blu c6 2019 -> بلو C6 2019
  - blu j2 -> بلو J2
  - blu j6 -> بلو J6
  - blu view 1 -> بلو View 1
  - blu tank xtreme -> بلو Tank Xtreme
  - blu g60 -> بلو G60
  - blu g70 -> بلو G70
  - blu studio x9 hd -> بلو Studio X9 HD
  - blu view mega -> بلو View Mega
  - blu g80 -> بلو G80
  - blu g90 -> بلو G90
  - blu m8l -> بلو M8L
  - blu m8l plus -> بلو M8L Plus
  - blu studio x10l -> بلو Studio X10L
  - blu g90 pro -> بلو G90 Pro
  - blu studio x10 -> بلو Studio X10
  - blu c6 2020 -> بلو C6 2020
  - blu c6l 2020 -> بلو C6L 2020
  - blu g50 -> بلو G50
  - blu g50 plus -> بلو G50 Plus
  - blu j5l -> بلو J5L
  - blu j6 2020 -> بلو J6 2020
  - blu j7l -> بلو J7L
  - blu c5l 2020 -> بلو C5L 2020
  - blu view 2 -> بلو View 2
  - blu g50 mega -> بلو G50 Mega
  - blu a5l -> بلو A5L
  - blu c7 -> بلو C7
  - blu g51 plus -> بلو G51 Plus
  - blu g71 -> بلو G71
  - blu g91s -> بلو G91s
  - blu m7l -> بلو M7L
  - blu g61 -> بلو G61
  - blu g91 -> بلو G91
  - blu studio x10+ -> بلو Studio X10+
  - blu studio x12 -> بلو Studio X12
  - blu j9l -> بلو J9L
  - blu g91 pro -> بلو G91 Pro
  - blu view 3 -> بلو View 3
  - blu c5l max -> بلو C5L Max
  - blu bold n2 -> بلو Bold N2
  - blu c5 max -> بلو C5 Max
  - blu c7x -> بلو C7X
  - blu g51 -> بلو G51
  - blu g51s -> بلو G51S
  - blu g71+ -> بلو G71+
  - blu g71l -> بلو G71L
  - blu j6s -> بلو J6S
  - blu s91 -> بلو S91
  - blu s91 pro -> بلو S91 Pro
  - blu studio x10 2022 -> بلو Studio X10 2022
  - blu m8l 2022 -> بلو M8L 2022
  - blu g91 max -> بلو G91 Max
  - blu g50 mega 2022 -> بلو G50 Mega 2022
  - blu g61s -> بلو G61s
  - blu f91 -> بلو F91
  - blu g40 -> بلو G40
  - blu studio x10l 2022 -> بلو Studio X10L 2022
  - blu studio x5 -> بلو Studio X5
  - blu studio x5 max -> بلو Studio X5 Max
  - bq -> بی کیو
  - bq aquaris u2 -> بی کیو Aquaris U2
  - bq aquaris u2 lite -> بی کیو Aquaris U2 Lite
  - bq aquaris v -> بی کیو Aquaris V
  - bq aquaris v plus -> بی کیو Aquaris V Plus
  - bq aquaris vs -> بی کیو Aquaris VS
  - bq aquaris vs plus -> بی کیو Aquaris VS Plus
  - bq aquaris x2 -> بی کیو Aquaris X2
  - bq aquaris x2 pro -> بی کیو Aquaris X2 Pro
  - cat -> کت
  - cat b100 -> کت B100
  - cat b15 -> کت B15
  - cat b15 q -> کت B15 Q
  - cat s50 -> کت S50
  - cat s40 -> کت S40
  - cat s30 -> کت S30
  - cat s60 -> کت S60
  - cat s31 -> کت S31
  - cat b35 -> کت B35
  - cat s52 -> کت S52
  - cat s42 -> کت S42
  - cat s62 pro -> کت S62 Pro
  - cat s42 h+ -> کت S42 H+
  - cat s22 flip -> کت S22 Flip
  - energizer -> انرجیزایر
  - energizer energy 200 -> انرجیزایر Energy 200
  - energizer energy 240 -> انرجیزایر Energy 240
  - energizer energy 400 -> انرجیزایر Energy 400
  - energizer energy 500 -> انرجیزایر Energy 500
  - energizer energy 100 -> انرجیزایر Energy 100
  - energizer energy 400 lte -> انرجیزایر Energy 400 LTE
  - energizer energy e520 lte -> انرجیزایر Energy E520 LTE
  - energizer energy s500e -> انرجیزایر Energy S500E
  - energizer energy s550 -> انرجیزایر Energy S550
  - energizer power max p550s -> انرجیزایر Power Max P550S
  - energizer hardcase h240s -> انرجیزایر Hardcase H240S
  - energizer hardcase h550s -> انرجیزایر Hardcase H550S
  - energizer power max p600s -> انرجیزایر Power Max P600S
  - energizer power max p16k pro -> انرجیزایر Power Max P16K Pro
  - energizer hardcase h500s -> انرجیزایر Hardcase H500S
  - energizer power max p20 -> انرجیزایر Power Max P20
  - energizer power max p490 -> انرجیزایر Power Max P490
  - energizer power max p490s -> انرجیزایر Power Max P490S
  - energizer energy e10+ -> انرجیزایر Energy E10+
  - energizer energy e11 -> انرجیزایر Energy E11
  - energizer energy e500 -> انرجیزایر Energy E500
  - energizer energy e500s -> انرجیزایر Energy E500S
  - energizer ultimate u570s -> انرجیزایر Ultimate U570S
  - energizer ultimate u620s -> انرجیزایر Ultimate U620S
  - energizer ultimate u620s pop -> انرجیزایر Ultimate U620S Pop
  - energizer ultimate u630s pop -> انرجیزایر Ultimate U630S Pop
  - energizer ultimate u650s -> انرجیزایر Ultimate U650S
  - energizer energy e220 -> انرجیزایر Energy E220
  - energizer energy e220s -> انرجیزایر Energy E220s
  - energizer energy e241 -> انرجیزایر Energy E241
  - energizer energy e401 -> انرجیزایر Energy E401
  - energizer energy e551s -> انرجیزایر Energy E551S
  - energizer hardcase h241 -> انرجیزایر Hardcase H241
  - energizer hardcase h242 -> انرجیزایر Hardcase H242
  - energizer hardcase h242s -> انرجیزایر Hardcase H242S
  - energizer hardcase h280s -> انرجیزایر Hardcase H280S
  - energizer hardcase h501s -> انرجیزایر Hardcase H501S
  - energizer hardcase h570s -> انرجیزایر Hardcase H570S
  - energizer hardcase h591s -> انرجیزایر Hardcase H591S
  - energizer power max p18k pop -> انرجیزایر Power Max P18K Pop
  - energizer power max p8100s -> انرجیزایر Power Max P8100S
  - energizer energy e241s -> انرجیزایر Energy E241s
  - energizer hardcase h10 -> انرجیزایر Hardcase H10
  - energizer energy e12 -> انرجیزایر Energy E12
  - energizer ultimate u710s -> انرجیزایر Ultimate U710S
  - energizer hardcase h620s -> انرجیزایر Hardcase H620S
  - energizer e280s -> انرجیزایر E280s
  - energizer hard case g5 -> انرجیزایر Hard Case G5
  - energizer u680s -> انرجیزایر U680S
  - energizer e282sc -> انرجیزایر E282SC
  - energizer e284s -> انرجیزایر E284S
  - energizer e242s -> انرجیزایر E242s
  - energizer ultimate u505s -> انرجیزایر Ultimate U505s
  - energizer ultimate u608s -> انرجیزایر Ultimate U608s
  - gigabyte -> گیگابایت
  - gigabyte gsmart g1362 -> گیگابایت GSmart G1362
  - gigabyte gsmart gs202 -> گیگابایت GSmart GS202
  - gigabyte gsmart maya m1 -> گیگابایت GSmart Maya M1
  - gigabyte gsmart rio r1 -> گیگابایت GSmart Rio R1
  - gigabyte gsmart maya m1 v2 -> گیگابایت GSmart Maya M1 v2
  - gigabyte gsmart sierra s1 -> گیگابایت GSmart Sierra S1
  - gigabyte gsmart simba sx1 -> گیگابایت GSmart Simba SX1
  - gigabyte gsmart aku a1 -> گیگابایت GSmart Aku A1
  - gigabyte gsmart tuku t2 -> گیگابایت GSmart Tuku T2
  - gigabyte gsmart alto a2 -> گیگابایت GSmart Alto A2
  - gigabyte gsmart roma r2 -> گیگابایت GSmart Roma R2
  - gigabyte gsmart rey r3 -> گیگابایت GSmart Rey R3
  - gigabyte gsmart saga s3 -> گیگابایت GSmart Saga S3
  - gigabyte gsmart t4 -> گیگابایت GSmart T4
  - gigabyte gsmart mika m2 -> گیگابایت GSmart Mika M2
  - gigabyte gsmart arty a3 -> گیگابایت GSmart Arty A3
  - gigabyte gsmart t4 (lite edition) -> گیگابایت GSmart T4 (Lite Edition)
  - gigabyte gsmart gx2 -> گیگابایت GSmart GX2
  - gigabyte gsmart mika m3 -> گیگابایت GSmart Mika M3
  - gigabyte gsmart akta a4 -> گیگابایت GSmart Akta A4
  - gigabyte gsmart guru gx -> گیگابایت GSmart Guru GX
  - gigabyte gsmart mika mx -> گیگابایت GSmart Mika MX
  - gigabyte gsmart roma rx -> گیگابایت GSmart Roma RX
  - gigabyte gsmart classic -> گیگابایت GSmart Classic
  - gigabyte gsmart classic lite -> گیگابایت GSmart Classic Lite
  - gigabyte gsmart essence -> گیگابایت GSmart Essence
  - gigabyte gsmart essence 4 -> گیگابایت GSmart Essence 4
  - gionee -> جیونی
  - gionee ctrl v1 -> جیونی Ctrl V1
  - gionee ctrl v2 -> جیونی Ctrl V2
  - gionee ctrl v3 -> جیونی Ctrl V3
  - gionee ctrl v4 -> جیونی Ctrl V4
  - gionee dream d1 -> جیونی Dream D1
  - gionee elife e3 -> جیونی Elife E3
  - gionee elife e5 -> جیونی Elife E5
  - gionee elife e6 -> جیونی Elife E6
  - gionee elife e7 -> جیونی Elife E7
  - gionee gpad g1 -> جیونی Gpad G1
  - gionee gpad g3 -> جیونی Gpad G3
  - gionee pioneer p1 -> جیونی Pioneer P1
  - gionee pioneer p2 -> جیونی Pioneer P2
  - gionee pioneer p3 -> جیونی Pioneer P3
  - gionee gpad g2 -> جیونی Gpad G2
  - gionee ctrl v4s -> جیونی Ctrl V4s
  - gionee ctrl v5 -> جیونی Ctrl V5
  - gionee gpad g4 -> جیونی Gpad G4
  - gionee gpad g5 -> جیونی Gpad G5
  - gionee m2 -> جیونی M2
  - gionee elife s5.5 -> جیونی Elife S5.5
  - gionee pioneer p2s -> جیونی Pioneer P2S
  - gionee pioneer p4 -> جیونی Pioneer P4
  - gionee elife s5.1 -> جیونی Elife S5.1
  - gionee ctrl v6l -> جیونی Ctrl V6L
  - gionee marathon m3 -> جیونی Marathon M3
  - gionee pioneer p5l -> جیونی Pioneer P5L
  - gionee pioneer p6 -> جیونی Pioneer P6
  - gionee elife s7 -> جیونی Elife S7
  - gionee pioneer p4s -> جیونی Pioneer P4S
  - gionee elife e8 -> جیونی Elife E8
  - gionee marathon m5 -> جیونی Marathon M5
  - gionee pioneer p2m -> جیونی Pioneer P2M
  - gionee marathon m4 -> جیونی Marathon M4
  - gionee f103 -> جیونی F103
  - gionee pioneer p3s -> جیونی Pioneer P3S
  - gionee s5.1 pro -> جیونی S5.1 Pro
  - gionee elife s plus -> جیونی Elife S Plus
  - gionee s6 -> جیونی S6
  - gionee marathon m5 enjoy -> جیونی Marathon M5 enjoy
  - gionee marathon m5 lite -> جیونی Marathon M5 lite
  - gionee marathon m5 plus -> جیونی Marathon M5 Plus
  - gionee pioneer p5w -> جیونی Pioneer P5W
  - gionee marathon m5 mini -> جیونی Marathon M5 mini
  - gionee s8 -> جیونی S8
  - gionee p5 mini -> جیونی P5 Mini
  - gionee w909 -> جیونی W909
  - gionee s6 pro -> جیونی S6 Pro
  - gionee m6 -> جیونی M6
  - gionee m6 plus -> جیونی M6 Plus
  - gionee s6s -> جیونی S6s
  - gionee f103 pro -> جیونی F103 Pro
  - gionee p7 max -> جیونی P7 Max
  - gionee s9 -> جیونی S9
  - gionee m2017 -> جیونی M2017
  - gionee p7 -> جیونی P7
  - gionee steel 2 -> جیونی Steel 2
  - gionee f5 -> جیونی F5
  - gionee a1 -> جیونی A1
  - gionee a1 plus -> جیونی A1 Plus
  - gionee m6s plus -> جیونی M6s Plus
  - gionee s10 -> جیونی S10
  - gionee s10b -> جیونی S10B
  - gionee s10c -> جیونی S10C
  - gionee a1 lite -> جیونی A1 Lite
  - gionee p8 max -> جیونی P8 Max
  - gionee x1 -> جیونی X1
  - gionee m7 -> جیونی M7
  - gionee x1s -> جیونی X1s
  - gionee m7 power -> جیونی M7 Power
  - gionee m7 plus -> جیونی M7 Plus
  - gionee s11 -> جیونی S11
  - gionee s11 lite -> جیونی S11 lite
  - gionee s11s -> جیونی S11S
  - gionee f205 -> جیونی F205
  - gionee k30 pro -> جیونی K30 Pro
  - gionee k3 pro -> جیونی K3 Pro
  - gionee k6 -> جیونی K6
  - gionee m12 -> جیونی M12
  - gionee m30 -> جیونی M30
  - gionee max -> جیونی Max
  - gionee p12 -> جیونی P12
  - gionee s12 lite -> جیونی S12 Lite
  - gionee s12 -> جیونی S12
  - gionee m3 -> جیونی M3
  - gionee max pro -> جیونی Max Pro
  - gionee p15 -> جیونی P15
  - gionee p15 pro -> جیونی P15 Pro
  - gionee m15 -> جیونی M15
  - gionee g13 pro -> جیونی G13 Pro
  - glx -> جی‌‌ال‌ایکس
  - glx arya -> جی‌‌ال‌ایکس Arya
  - glx c6000 -> جی‌‌ال‌ایکس C6000
  - glx e51 -> جی‌‌ال‌ایکس E51
  - glx shahab -> جی‌‌ال‌ایکس Shahab
  - glx x -> جی‌‌ال‌ایکس X
  - glx zoom me c58 -> جی‌‌ال‌ایکس Zoom me C58
  - google -> گوگل
  - google pixel -> گوگل Pixel
  - google pixel xl -> گوگل Pixel XL
  - google pixel 2 -> گوگل Pixel 2
  - google pixel 2 xl -> گوگل Pixel 2 XL
  - google pixel 3 -> گوگل Pixel 3
  - google pixel 3 xl -> گوگل Pixel 3 XL
  - google pixel 3a -> گوگل Pixel 3a
  - google pixel 3a xl -> گوگل Pixel 3a XL
  - google pixel 4 -> گوگل Pixel 4
  - google pixel 4 xl -> گوگل Pixel 4 XL
  - google pixel 4a -> گوگل Pixel 4a
  - google pixel 4a 5g -> گوگل Pixel 4a 5G
  - google pixel 5 -> گوگل Pixel 5
  - google pixel 6 -> گوگل پیکسل 6
  - google pixel 6 pro -> گوگل پیکسل 6 پرو
  - google pixel 5a 5g -> گوگل Pixel 5a 5G
  - google pixel 6a -> گوگل پیکسل 6a
  - gplus -> جی‌پلاس
  - gplus p10 -> جی‌پلاس P10
  - gplus q10 -> جی‌پلاس Q10
  - gplus t10 -> جی‌پلاس T10
  - gplus x10 -> جی‌پلاس X10
  - honor -> آنر
  - honor 3c -> آنر 3C
  - honor 3x g750 -> آنر 3X G750
  - honor 3c 4g -> آنر 3C 4G
  - honor 3x pro -> آنر 3X Pro
  - honor 6 -> آنر 6
  - honor 3c play -> آنر 3C Play
  - honor 4 play -> آنر 4 Play
  - honor 4x -> آنر 4X
  - honor holly -> آنر Holly
  - honor 6 plus -> آنر 6 Plus
  - honor 4c -> آنر 4C
  - honor bee -> آنر Bee
  - honor 7 -> آنر 7
  - honor 5x -> آنر 5X
  - honor holly 2 plus -> آنر Holly 2 Plus
  - honor 5c -> آنر 5c
  - honor 5a -> آنر 5A
  - honor 8 -> آنر 8
  - honor note 8 -> آنر Note 8
  - honor 6x -> آنر 6X
  - honor holly 3 -> آنر Holly 3
  - honor magic -> آنر Magic
  - honor 8 pro -> آنر 8 Pro
  - honor 6a (pro) -> آنر 6A (Pro)
  - honor 9 -> آنر 9
  - honor 6c pro -> آنر 6C Pro
  - honor 7x -> آنر 7X
  - honor 9 lite -> آنر 9 Lite
  - honor view 10 -> آنر View 10
  - honor 7a -> آنر 7A
  - honor 10 -> آنر 10
  - honor 7c -> آنر 7C
  - honor 7s -> آنر 7S
  - honor 9n (9i) -> آنر 9N (9i)
  - honor note 10 -> آنر Note 10
  - honor play -> آنر Play
  - honor 8x -> آنر 8X
  - honor 8x max -> آنر 8X Max
  - honor 8c -> آنر 8C
  - honor magic 2 -> آنر Magic 2
  - honor 10 lite -> آنر 10 Lite
  - honor view 20 -> آنر View 20
  - honor play 8a -> آنر Play 8A
  - honor magic 2 3d -> آنر Magic 2 3D
  - honor 20i -> آنر 20i
  - honor 20 lite -> آنر 20 lite
  - honor 8a pro -> آنر 8A Pro
  - honor 8s -> آنر 8S
  - honor 20 -> آنر 20
  - honor 20 pro -> آنر 20 Pro
  - honor 9x (china) -> آنر 9X (China)
  - honor pad 5 10.1 -> آنر Pad 5 10.1
  - honor 9x pro -> آنر 9X Pro
  - honor 20s -> آنر 20S
  - honor play 3 -> آنر Play 3
  - honor play 3e -> آنر Play 3e
  - honor 20 lite (china) -> آنر 20 lite (China)
  - honor 9x -> آنر 9X
  - honor v30 -> آنر V30 (ویو 30)
  - honor v30 pro -> آنر V30 Pro
  - honor 8a prime -> آنر 8A Prime
  - honor v6 -> آنر V6
  - honor view30 -> آنر View30
  - honor view30 pro -> آنر View30 Pro
  - honor 30s -> آنر 30S
  - honor play 9a -> آنر Play 9A
  - honor 20e -> آنر 20e
  - honor 30 -> آنر 30
  - honor 30 pro -> آنر 30 Pro
  - honor 30 pro+ -> آنر 30 Pro+
  - honor 8a 2020 -> آنر 8A 2020
  - honor 9a -> آنر 9A
  - honor 9c -> آنر 9C
  - honor 9s -> آنر 9S
  - honor 9x lite -> آنر 9X Lite
  - honor play 4t -> آنر Play 4T
  - honor play 4t pro -> آنر Play 4T Pro
  - honor 8s 2020 -> آنر 8S 2020
  - honor x10 5g -> آنر X10 5G
  - honor play4 -> آنر Play4
  - honor play4 pro -> آنر Play4 Pro
  - honor 30 youth -> آنر 30 Youth
  - honor pad 6 -> آنر Pad 6
  - honor x10 max 5g -> آنر X10 Max 5G
  - honor 30i -> آنر 30i
  - honor 10x lite -> آنر 10X Lite
  - honor play 20 -> آنر 20 پلی
  - honor play5 5g -> آنر Play5 5G
  - honor play 5t youth -> آنر Play 5T Youth
  - honor v40 5g -> آنر V40 (ویو 40)
  - honor view40 -> آنر View40
  - honor v40 lite -> آنر V40 Lite
  - honor 50 -> آنر 50
  - honor 50 pro -> آنر 50 Pro
  - honor 50 se -> آنر 50 SE
  - honor x20 se -> آنر X20 SE
  - honor magic3 -> آنر Magic3
  - honor magic3 pro -> آنر Magic3 Pro
  - honor magic3 pro+ -> آنر Magic3 Pro+
  - honor play 5t pro -> آنر Play 5T Pro
  - honor x20 -> آنر X20
  - honor 50 lite -> آنر 50 Lite
  - honor play5 youth -> آنر Play5 Youth
  - honor x30i -> آنر X30i
  - honor x30 max -> آنر X30 Max
  - honor 60 -> آنر 60
  - honor 60 pro -> آنر 60 Pro
  - honor magic4 lite -> آنر مجیک 4 لایت
  - honor play 30 -> آنر پلی 30
  - honor play 30 plus -> آنر Play 30 Plus
  - honor x30 -> آنر X30
  - honor x40 -> آنر X40
  - honor x8 5g -> آنر X8 5G
  - honor magic v -> آنر Magic V
  - honor 60 se -> آنر 60 SE
  - honor magic4 -> آنر Magic4
  - honor magic4 pro -> آنر Magic4 Pro
  - honor magic4 ultimate -> آنر Magic4 Ultimate
  - honor x7 -> آنر X7
  - honor x8 -> آنر X8
  - honor x9 -> آنر X9
  - honor x9 5g -> آنر X9 5G
  - honor play6t -> آنر Play6T
  - honor play6t pro -> آنر Play6T Pro
  - honor 70 -> آنر 70
  - honor 70 pro -> آنر 70 Pro
  - honor 70 pro+ -> آنر 70 Pro+
  - htc -> اچ‌تی‌سی
  - htc a12 -> اچ‌تی‌سی A12
  - htc one (m8i) -> اچ‌تی‌سی One (M8i)
  - htc one m8 prime -> اچ‌تی‌سی One M8 Prime
  - htc tiara -> اچ‌تی‌سی Tiara
  - htc wildfire r70 -> اچ‌تی‌سی Wildfire R70
  - htc evo 4g -> اچ‌تی‌سی Evo 4G
  - htc evo 4g+ -> اچ‌تی‌سی Evo 4G+
  - htc evo shift 4g -> اچ‌تی‌سی EVO Shift 4G
  - htc evo 3d cdma -> اچ‌تی‌سی EVO 3D CDMA
  - htc evo view 4g -> اچ‌تی‌سی EVO View 4G
  - htc jetstream -> اچ‌تی‌سی Jetstream
  - htc evo design 4g -> اچ‌تی‌سی EVO Design 4G
  - htc one x -> اچ‌تی‌سی One X
  - htc one x at&t -> اچ‌تی‌سی One X AT&T
  - htc one xl -> اچ‌تی‌سی One XL
  - htc evo 4g lte -> اچ‌تی‌سی Evo 4G LTE
  - htc j -> اچ‌تی‌سی J
  - htc one xc -> اچ‌تی‌سی One XC
  - htc desire x -> اچ‌تی‌سی Desire X
  - htc one sc -> اچ‌تی‌سی One SC
  - htc one st -> اچ‌تی‌سی One ST
  - htc windows phone 8s -> اچ‌تی‌سی Windows Phone 8S
  - htc windows phone 8x -> اچ‌تی‌سی Windows Phone 8X
  - htc one vx -> اچ‌تی‌سی One VX
  - htc one x+ -> اچ‌تی‌سی One X+
  - htc desire sv -> اچ‌تی‌سی Desire SV
  - htc droid dna -> اچ‌تی‌سی DROID DNA
  - htc one sv -> اچ‌تی‌سی One SV
  - htc one sv cdma -> اچ‌تی‌سی One SV CDMA
  - htc windows phone 8x cdma -> اچ‌تی‌سی Windows Phone 8X CDMA
  - htc butterfly -> اچ‌تی‌سی Butterfly
  - htc desire 400 dual sim -> اچ‌تی‌سی Desire 400 dual sim
  - htc desire u -> اچ‌تی‌سی Desire U
  - htc one -> اچ‌تی‌سی One
  - htc desire l -> اچ‌تی‌سی Desire L
  - htc desire p -> اچ‌تی‌سی Desire P
  - htc first -> اچ‌تی‌سی First
  - htc desire 600 dual sim -> اچ‌تی‌سی Desire 600 dual sim
  - htc 8xt -> اچ‌تی‌سی 8XT
  - htc butterfly s -> اچ‌تی‌سی Butterfly S
  - htc desire 200 -> اچ‌تی‌سی Desire 200
  - htc one dual sim -> اچ‌تی‌سی One Dual Sim
  - htc desire xc -> اچ‌تی‌سی Desire XC
  - htc one mini -> اچ‌تی‌سی One mini
  - htc desire 500 -> اچ‌تی‌سی Desire 500
  - htc desire 300 -> اچ‌تی‌سی Desire 300
  - htc desire 601 -> اچ‌تی‌سی Desire 601
  - htc one max -> اچ‌تی‌سی One Max
  - htc desire 501 -> اچ‌تی‌سی Desire 501
  - htc desire 601 dual sim -> اچ‌تی‌سی Desire 601 dual sim
  - htc desire 700 dual sim -> اچ‌تی‌سی Desire 700 dual sim
  - htc desire 501 dual sim -> اچ‌تی‌سی Desire 501 dual sim
  - htc desire 310 -> اچ‌تی‌سی Desire 310
  - htc desire 700 -> اچ‌تی‌سی Desire 700
  - htc desire 610 -> اچ‌تی‌سی Desire 610
  - htc desire 626 -> اچ‌تی‌سی Desire 626
  - htc desire 816 -> اچ‌تی‌سی Desire 816
  - htc one (m8) -> اچ‌تی‌سی One (M8)
  - htc one (m8) cdma -> اچ‌تی‌سی One (M8) CDMA
  - htc desire 210 dual sim -> اچ‌تی‌سی Desire 210 dual sim
  - htc desire 310 dual sim -> اچ‌تی‌سی Desire 310 dual sim
  - htc desire 616 dual sim -> اچ‌تی‌سی Desire 616 dual sim
  - htc desire 816 dual sim -> اچ‌تی‌سی Desire 816 dual sim
  - htc one mini 2 -> اچ‌تی‌سی One mini 2
  - htc desire 516 dual sim -> اچ‌تی‌سی Desire 516 dual sim
  - htc one (e8) -> اچ‌تی‌سی One (E8)
  - htc one (m8) dual sim -> اچ‌تی‌سی One (M8) dual sim
  - htc one remix -> اچ‌تی‌سی One Remix
  - htc butterfly 2 -> اچ‌تی‌سی Butterfly 2
  - htc desire 510 -> اچ‌تی‌سی Desire 510
  - htc one (e8) cdma -> اچ‌تی‌سی One (E8) CDMA
  - htc one (m8) for windows -> اچ‌تی‌سی One (M8) for Windows
  - htc one (m8) for windows (cdma) -> اچ‌تی‌سی One (M8) for Windows (CDMA)
  - htc desire 820 -> اچ‌تی‌سی Desire 820
  - htc desire 820 dual sim -> اچ‌تی‌سی Desire 820 dual sim
  - htc desire 612 -> اچ‌تی‌سی Desire 612
  - htc desire 820q dual sim -> اچ‌تی‌سی Desire 820q dual sim
  - htc desire eye -> اچ‌تی‌سی Desire Eye
  - htc one (m8 eye) -> اچ‌تی‌سی One (M8 Eye)
  - htc desire 620 -> اچ‌تی‌سی Desire 620
  - htc desire 620g dual sim -> اچ‌تی‌سی Desire 620G dual sim
  - htc desire 826 dual sim -> اچ‌تی‌سی Desire 826 dual sim
  - htc desire 820s dual sim -> اچ‌تی‌سی Desire 820s dual sim
  - htc one e9+ -> اچ‌تی‌سی One E9+
  - htc one m9 -> اچ‌تی‌سی One M9
  - htc desire 326g dual sim -> اچ‌تی‌سی Desire 326G dual sim
  - htc desire 626g+ -> اچ‌تی‌سی Desire 626G+
  - htc one m8s -> اچ‌تی‌سی One M8s
  - htc one m9+ -> اچ‌تی‌سی One M9+
  - htc desire 820g+ dual sim -> اچ‌تی‌سی Desire 820G+ dual sim
  - htc one e9 -> اچ‌تی‌سی One E9
  - htc one me -> اچ‌تی‌سی One ME
  - htc desire 526 -> اچ‌تی‌سی Desire 526
  - htc desire 626 (usa) -> اچ‌تی‌سی Desire 626 (USA)
  - htc desire 520 -> اچ‌تی‌سی Desire 520
  - htc butterfly 3 -> اچ‌تی‌سی Butterfly 3
  - htc one a9 -> اچ‌تی‌سی One A9
  - htc one m9+ supreme camera -> اچ‌تی‌سی One M9+ Supreme Camera
  - htc one e9s dual sim -> اچ‌تی‌سی One E9s dual sim
  - htc desire 828 dual sim -> اچ‌تی‌سی Desire 828 dual sim
  - htc one m9s -> اچ‌تی‌سی One M9s
  - htc one x9 -> اچ‌تی‌سی One X9
  - htc desire 530 -> اچ‌تی‌سی Desire 530
  - htc desire 630 -> اچ‌تی‌سی Desire 630
  - htc desire 825 -> اچ‌تی‌سی Desire 825
  - htc 10 -> اچ‌تی‌سی 10
  - htc 10 lifestyle -> اچ‌تی‌سی 10 Lifestyle
  - htc one s9 -> اچ‌تی‌سی One S9
  - htc desire 628 -> اچ‌تی‌سی Desire 628
  - htc desire 830 -> اچ‌تی‌سی Desire 830
  - htc one m9 prime camera -> اچ‌تی‌سی One M9 Prime Camera
  - htc desire 625 -> اچ‌تی‌سی Desire 625
  - htc desire 728 ultra -> اچ‌تی‌سی Desire 728 Ultra
  - htc desire 10 pro -> اچ‌تی‌سی Desire 10 Pro
  - htc one a9s -> اچ‌تی‌سی One A9s
  - htc 10 evo -> اچ‌تی‌سی 10 evo
  - htc desire 650 -> اچ‌تی‌سی Desire 650
  - htc desire 10 compact -> اچ‌تی‌سی Desire 10 Compact
  - htc u play -> اچ‌تی‌سی U Play
  - htc u ultra -> اچ‌تی‌سی U Ultra
  - htc one x10 -> اچ‌تی‌سی One X10
  - htc u11 -> اچ‌تی‌سی U11
  - htc u11+ -> اچ‌تی‌سی U11+
  - htc u11 life -> اچ‌تی‌سی U11 Life
  - htc u11 eyes -> اچ‌تی‌سی U11 Eyes
  - htc desire 12 -> اچ‌تی‌سی Desire 12
  - htc desire 12+ -> اچ‌تی‌سی Desire 12+
  - htc u12+ -> اچ‌تی‌سی U12+
  - htc u12 life -> اچ‌تی‌سی U12 life
  - htc exodus 1 -> اچ‌تی‌سی Exodus 1
  - htc desire 12s -> اچ‌تی‌سی Desire 12s
  - htc wildfire e -> اچ‌تی‌سی Wildfire E
  - htc wildfire e1 -> اچ‌تی‌سی Wildfire E1
  - htc wildfire e1 plus -> اچ‌تی‌سی Wildfire E1 plus
  - htc desire 19+ -> اچ‌تی‌سی Desire 19+
  - htc u19e -> اچ‌تی‌سی U19e
  - htc wildfire x -> اچ‌تی‌سی Wildfire X
  - htc exodus 1s -> اچ‌تی‌سی Exodus 1s
  - htc desire 19s -> اچ‌تی‌سی Desire 19s
  - htc wildfire e1 lite -> اچ‌تی‌سی Wildfire E1 lite
  - htc desire 20 pro -> اچ‌تی‌سی Desire 20 Pro
  - htc u20 5g -> اچ‌تی‌سی U20 5G
  - htc wildfire e2 -> اچ‌تی‌سی Wildfire E2
  - htc desire 20+ -> اچ‌تی‌سی Desire 20+
  - htc desire 21 pro 5g -> اچ‌تی‌سی Desire 21 Pro 5G
  - htc wildfire e3 -> اچ‌تی‌سی Wildfire E3
  - htc wildfire e2 plus -> اچ‌تی‌سی Wildfire E2 Plus
  - htc desire 22 pro -> اچ‌تی‌سی Desire 22 Pro
  - huawei -> هواوی
  - huawei ascend g628 -> هواوی Ascend G628
  - huawei g10 -> هواوی G10
  - huawei mate 30 lite -> هواوی Mate 30 Lite
  - huawei p8 max -> هواوی P8 max
  - huawei ascend d1 xl u9500e -> هواوی Ascend D1 XL U9500E
  - huawei ascend g312 -> هواوی Ascend G312
  - huawei ascend g330d u8825d -> هواوی Ascend G330D U8825D
  - huawei ascend p1 xl u9200e -> هواوی Ascend P1 XL U9200E
  - huawei ascend g330 -> هواوی Ascend G330
  - huawei ascend g600 -> هواوی Ascend G600
  - huawei ascend p1 lte -> هواوی Ascend P1 LTE
  - huawei fusion 2 u8665 -> هواوی Fusion 2 U8665
  - huawei summit -> هواوی Summit
  - huawei ascend g500 -> هواوی Ascend G500
  - huawei ascend d2 -> هواوی Ascend D2
  - huawei ascend g510 -> هواوی Ascend G510
  - huawei ascend g525 -> هواوی Ascend G525
  - huawei ascend g615 -> هواوی Ascend G615
  - huawei ascend g700 -> هواوی Ascend G700
  - huawei ascend mate -> هواوی Ascend Mate
  - huawei ascend w1 -> هواوی Ascend W1
  - huawei ascend g350 -> هواوی Ascend G350
  - huawei ascend g526 -> هواوی Ascend G526
  - huawei ascend p2 -> هواوی Ascend P2
  - huawei ascend y210d -> هواوی Ascend Y210D
  - huawei ascend y300 -> هواوی Ascend Y300
  - huawei premia 4g m931 -> هواوی Premia 4G M931
  - huawei ascend p6 -> هواوی Ascend P6
  - huawei g610s -> هواوی G610s
  - huawei ascend g740 -> هواوی Ascend G740
  - huawei ascend y320 -> هواوی Ascend Y320
  - huawei ascend y511 -> هواوی Ascend Y511
  - huawei u8687 cronos -> هواوی U8687 Cronos
  - huawei ascend g535 -> هواوی Ascend G535
  - huawei ascend mate2 4g -> هواوی Ascend Mate2 4G
  - huawei ascend p6 s -> هواوی Ascend P6 S
  - huawei y300ii -> هواوی Y300II
  - huawei ascend g6 -> هواوی Ascend G6
  - huawei ascend g6 4g -> هواوی Ascend G6 4G
  - huawei ascend g730 -> هواوی Ascend G730
  - huawei ascend y530 -> هواوی Ascend Y530
  - huawei ascend g630 -> هواوی Ascend G630
  - huawei ascend y330 -> هواوی Ascend Y330
  - huawei ascend y600 -> هواوی Ascend Y600
  - huawei ascend p7 mini -> هواوی Ascend P7 mini
  - huawei ascend p7 -> هواوی Ascend P7
  - huawei ascend p7 sapphire edition -> هواوی Ascend P7 Sapphire Edition
  - huawei ascend g620s -> هواوی Ascend G620s
  - huawei ascend g7 -> هواوی Ascend G7
  - huawei ascend mate7 -> هواوی Ascend Mate7
  - huawei ascend y550 -> هواوی Ascend Y550
  - huawei ascend gx1 -> هواوی Ascend GX1
  - huawei ascend mate7 monarch -> هواوی Ascend Mate7 Monarch
  - huawei ascend y221 -> هواوی Ascend Y221
  - huawei ascend y520 -> هواوی Ascend Y520
  - huawei ascend y540 -> هواوی Ascend Y540
  - huawei y360 -> هواوی Y360
  - huawei y635 -> هواوی Y635
  - huawei p8 -> هواوی P8
  - huawei p8lite -> هواوی P8lite
  - huawei p8lite ale-l04 -> هواوی P8lite ALE-L04
  - huawei snapto -> هواوی SnapTo
  - huawei y625 -> هواوی Y625
  - huawei y560 -> هواوی Y560
  - huawei g8 -> هواوی G8
  - huawei y6 -> هواوی Y6
  - huawei mate s -> هواوی Mate S
  - huawei nexus 6p -> هواوی Nexus 6P
  - huawei y6 pro -> هواوی Y6 Pro
  - huawei g7 plus -> هواوی G7 Plus
  - huawei enjoy 5s -> هواوی Enjoy 5s
  - huawei p9 lite -> هواوی P9 lite
  - huawei p9 plus -> هواوی P9 Plus
  - huawei y3ii -> هواوی Y3II
  - huawei y5ii -> هواوی Y5II
  - huawei g9 plus -> هواوی G9 Plus
  - huawei nova plus -> هواوی nova plus
  - huawei y6ii compact -> هواوی Y6II Compact
  - huawei enjoy 6 -> هواوی Enjoy 6
  - huawei mate 9 -> هواوی Mate 9
  - huawei mate 9 porsche design -> هواوی Mate 9 Porsche Design
  - huawei mate 9 pro -> هواوی Mate 9 Pro
  - huawei p8 lite (2017) -> هواوی P8 Lite (2017)
  - huawei p10 -> هواوی P10
  - huawei p10 lite -> هواوی P10 Lite
  - huawei p10 plus -> هواوی P10 Plus
  - huawei y5 (2017) -> هواوی Y5 2017
  - huawei nova 2 -> هواوی nova 2
  - huawei nova 2 plus -> هواوی nova 2 plus
  - huawei y3 (2017) -> هواوی Y3 (2017)
  - huawei y6 (2017) -> هواوی Y6 (2017)
  - huawei y7 -> هواوی Y7
  - huawei y7 prime -> هواوی Y7 Prime
  - huawei p9 lite mini -> هواوی P9 lite mini
  - huawei mate 10 -> هواوی Mate 10
  - huawei mate 10 lite -> هواوی Mate 10 Lite
  - huawei mate 10 porsche design -> هواوی Mate 10 Porsche Design
  - huawei mate 10 pro -> هواوی Mate 10 Pro
  - huawei nova 2s -> هواوی nova 2s
  - huawei p smart -> هواوی P smart
  - huawei mate rs porsche design -> هواوی Mate RS Porsche Design
  - huawei p20 -> هواوی P20
  - huawei p20 lite -> هواوی P20 lite
  - huawei p20 pro -> هواوی P20 Pro
  - huawei y7 (2018) -> هواوی Y7 (2018)
  - huawei y7 prime (2018) -> هواوی Y7 Prime (2018)
  - huawei y7 pro (2018) -> هواوی Y7 Pro (2018)
  - huawei y9 (2018) -> هواوی Y9 (2018)
  - huawei y6 (2018) -> هواوی Y6 (2018)
  - huawei y6 prime (2018) -> هواوی Y6 Prime (2018)
  - huawei y3 (2018) -> هواوی Y3 (2018)
  - huawei y5 prime (2018) -> هواوی Y5 Prime (2018)
  - huawei nova 3 -> هواوی nova 3
  - huawei nova 3i -> هواوی nova 3i
  - huawei p smart+ 2019 -> هواوی P Smart+ 2019
  - huawei mate 20 lite -> هواوی Mate 20 lite
  - huawei mate 20 -> هواوی Mate 20
  - huawei mate 20 pro -> هواوی Mate 20 Pro
  - huawei mate 20 rs porsche design -> هواوی Mate 20 RS Porsche Design
  - huawei mate 20 x -> هواوی Mate 20 X
  - huawei y9 (2019) -> هواوی Y9 (2019)
  - huawei y max -> هواوی Y Max
  - huawei enjoy 9 -> هواوی Enjoy 9
  - huawei nova 4 -> هواوی nova 4
  - huawei p smart 2019 -> هواوی P smart 2019
  - huawei y5 lite (2018) -> هواوی Y5 lite (2018)
  - huawei y7 prime (2019) -> هواوی Y7 Prime (2019)
  - huawei y7 pro (2019) -> هواوی Y7 Pro (2019)
  - huawei mate x -> هواوی Mate X
  - huawei y6 pro (2019) -> هواوی Y6 Pro (2019)
  - huawei enjoy 9e -> هواوی Enjoy 9e
  - huawei enjoy 9s -> هواوی Enjoy 9s
  - huawei nova 4e -> هواوی nova 4e
  - huawei p30 -> هواوی P30
  - huawei p30 lite -> هواوی P30 lite
  - huawei p30 pro -> هواوی P30 Pro
  - huawei y6 (2019) -> هواوی Y6 (2019)
  - huawei y7 (2019) -> هواوی Y7 (2019)
  - huawei y5 (2019) -> هواوی Y5 (2019)
  - huawei mate 20 x (5g) -> هواوی Mate 20 X (5G)
  - huawei p smart z -> هواوی P Smart Z
  - huawei nova 5 -> هواوی nova 5
  - huawei nova 5i -> هواوی nova 5i
  - huawei nova 5 pro -> هواوی nova 5 Pro
  - huawei p20 lite (2019) -> هواوی P20 lite (2019)
  - huawei nova 5i pro -> هواوی nova 5i Pro
  - huawei nova 5t -> هواوی nova 5T
  - huawei y9 prime (2019) -> هواوی Y9 Prime (2019)
  - huawei enjoy 10 plus -> هواوی Enjoy 10 Plus
  - huawei mate 30 -> هواوی Mate 30
  - huawei mate 30 5g -> هواوی Mate 30 5G
  - huawei mate 30 pro -> هواوی Mate 30 Pro
  - huawei mate 30 pro 5g -> هواوی Mate 30 Pro 5G
  - huawei mate 30 rs porsche design -> هواوی Mate 30 RS Porsche Design
  - huawei mediapad m6 turbo 8.4 -> هواوی MediaPad M6 Turbo 8.4
  - huawei enjoy 10 -> هواوی Enjoy 10
  - huawei enjoy 10s -> هواوی Enjoy 10s
  - huawei nova 5z -> هواوی nova 5z
  - huawei nova 6 5g -> هواوی نوا 6 5G
  - huawei y9s -> هواوی Y9s
  - huawei enjoy 10e -> هواوی Enjoy 10e
  - huawei mate 40 rs porsche design -> هواوی میت 40 RS پورشه دیزاین
  - huawei nova 6 -> هواوی nova 6
  - huawei nova 6 se -> هواوی nova 6 SE
  - huawei p40 lite e -> هواوی P40 lite E
  - huawei p smart pro 2019 -> هواوی P smart Pro 2019
  - huawei nova 7i -> هواوی nova 7i
  - huawei p30 lite new edition -> هواوی P30 lite New Edition
  - huawei y6s (2019) -> هواوی Y6s (2019)
  - huawei mate xs -> هواوی Mate Xs
  - huawei p40 lite -> هواوی P40 lite
  - huawei y7p -> هواوی Y7p
  - huawei p40 -> هواوی P40
  - huawei p40 pro -> هواوی P40 Pro
  - huawei p40 pro+ -> هواوی P40 Pro+
  - huawei matepad 10.4 -> هواوی MatePad 10.4
  - huawei nova 7 5g -> هواوی nova 7 5G
  - huawei nova 7 pro 5g -> هواوی nova 7 Pro 5G
  - huawei nova 7 se -> هواوی nova 7 SE
  - huawei p smart 2020 -> هواوی P smart 2020
  - huawei enjoy z 5g -> هواوی Enjoy Z 5G
  - huawei matepad t8 -> هواوی MatePad T8
  - huawei p30 pro new edition -> هواوی P30 Pro New Edition
  - huawei p40 lite 5g -> هواوی P40 lite 5G
  - huawei y5p -> هواوی Y5p
  - huawei y6p -> هواوی Y6p
  - huawei y8p -> هواوی Y8p
  - huawei y8s -> هواوی Y8s
  - huawei enjoy 20 pro -> هواوی Enjoy 20 Pro
  - huawei p smart s -> هواوی P Smart S
  - huawei matepad 10.8 -> هواوی MatePad 10.8
  - huawei enjoy 20 5g -> هواوی Enjoy 20 5G
  - huawei enjoy 20 plus 5g -> هواوی Enjoy 20 Plus 5G
  - huawei matepad t 10s -> هواوی MatePad T 10s
  - huawei p smart 2021 -> هواوی P smart 2021
  - huawei y9a -> هواوی Y9a
  - huawei mate 30e pro 5g -> هواوی Mate 30E Pro 5G
  - huawei mate 40 -> هواوی Mate 40
  - huawei mate 40 pro -> هواوی Mate 40 Pro
  - huawei mate 40 pro+ -> هواوی Mate 40 Pro+
  - huawei nova 7 se 5g youth -> هواوی nova 7 SE 5G Youth
  - huawei y7a -> هواوی Y7a
  - huawei nova 8 se -> هواوی nova 8 SE
  - huawei enjoy 20 se -> هواوی Enjoy 20 SE
  - huawei nova 8 -> هواوی نوا 8
  - huawei nova 8 5g -> هواوی nova 8 5G
  - huawei nova 8 pro 4g -> هواوی نوا 8 پرو 4G
  - huawei nova 8 pro 5g -> هواوی nova 8 Pro 5G
  - huawei nova y60 -> هواوی نوا Y60
  - huawei mate x2 -> هواوی Mate X2
  - huawei p40 4g -> هواوی P40 4G
  - huawei mate 40e -> هواوی Mate 40E
  - huawei mate 40e 4g -> هواوی Mate 40E 4G
  - huawei mate 40 pro 4g -> هواوی Mate 40 Pro 4G
  - huawei mate x2 4g -> هواوی Mate X2 4G
  - huawei nova 8i -> هواوی nova 8i
  - huawei nova 8 se youth -> هواوی nova 8 SE Youth
  - huawei p50 -> هواوی P50
  - huawei p50 pro -> هواوی P50 Pro
  - huawei nova 9 -> هواوی nova 9
  - huawei nova 9 pro -> هواوی nova 9 Pro
  - huawei enjoy 20e -> هواوی Enjoy 20e
  - huawei nova 8 se 4g -> هواوی nova 8 SE 4G
  - huawei mate 50 -> هواوی میت 50
  - huawei mate 50e -> هواوی Mate 50E
  - huawei mate 50 pro -> هواوی میت 50 پرو
  - huawei mate 50 rs porsche design -> هواوی میت 50 RS پورشه دیزاین
  - huawei nova 9 se -> هواوی نوا 9 SE
  - huawei p50 pocket -> هواوی P50 Pocket
  - huawei p50e -> هواوی P50E
  - huawei mate xs 2 -> هواوی Mate Xs 2
  - huawei nova 9 se 5g -> هواوی nova 9 SE 5G
  - huawei nova y70 plus -> هواوی nova Y70 Plus
  - huawei nova y90 -> هواوی nova Y90
  - huawei nova 10 -> هواوی nova 10
  - huawei nova 10 pro -> هواوی nova 10 Pro
  - infinix -> اینفینیکس
  - infinix hot s -> اینفینیکس Hot S
  - infinix hot 4 -> اینفینیکس Hot 4
  - infinix note 3 -> اینفینیکس Note 3
  - infinix note 3 pro -> اینفینیکس Note 3 Pro
  - infinix hot 4 pro -> اینفینیکس Hot 4 Pro
  - infinix zero 4 -> اینفینیکس Zero 4
  - infinix zero 4 plus -> اینفینیکس Zero 4 Plus
  - infinix note 4 pro -> اینفینیکس Note 4 Pro
  - infinix smart 2 hd -> اینفینیکس Smart 2 HD
  - infinix hot 7 -> اینفینیکس Hot 7
  - infinix hot 8 -> اینفینیکس Hot 8
  - infinix s5 -> اینفینیکس S5
  - infinix hot 7 pro -> اینفینیکس Hot 7 Pro
  - infinix zero 6 -> اینفینیکس Zero 6
  - infinix zero 6 pro -> اینفینیکس Zero 6 Pro
  - infinix s4 -> اینفینیکس S4
  - infinix smart3 plus -> اینفینیکس Smart3 Plus
  - infinix note 6 -> اینفینیکس Note 6
  - infinix hot 8 lite -> اینفینیکس Hot 8 Lite
  - infinix smart 4 -> اینفینیکس Smart 4
  - infinix s5 lite -> اینفینیکس S5 lite
  - infinix smart 4c -> اینفینیکس Smart 4c
  - infinix hot 10 -> اینفینیکس Hot 10
  - infinix hot 10 lite -> اینفینیکس Hot 10 لایت
  - infinix hot 9 -> اینفینیکس Hot 9
  - infinix hot 9 play -> اینفینیکس Hot 9 Play
  - infinix hot 9 pro -> اینفینیکس Hot 9 Pro
  - infinix note 7 -> اینفینیکس Note 7
  - infinix note 7 lite -> اینفینیکس Note 7 Lite
  - infinix note 8 -> اینفینیکس نوت 8
  - infinix note 8i -> اینفینیکس نوت 8i
  - infinix s5 pro -> اینفینیکس S5 Pro
  - infinix s5 pro (16+32) -> اینفینیکس S5 Pro (16+32)
  - infinix s5 pro (48+40) -> اینفینیکس S5 Pro (48+40)
  - infinix smart 5 -> اینفینیکس اسمارت 5
  - infinix smart hd 2021 -> اینفینیکس اسمارت اچ دی 2021
  - infinix zero 8 -> اینفینیکس Zero 8
  - infinix zero 8i -> اینفینیکس Zero 8i
  - infinix hot 10i -> اینفینیکس Hot 10i
  - infinix hot 10 play -> اینفینیکس Hot 10 پلی
  - infinix hot 10s -> اینفینیکس Hot 10s
  - infinix hot 10s nfc -> اینفینیکس Hot 10s NFC
  - infinix hot 10t -> اینفینیکس Hot 10T
  - infinix note 10 -> اینفینیکس نوت 10
  - infinix note 10 pro -> اینفینیکس نوت 10 پرو
  - infinix note 10 pro nfc -> اینفینیکس Note 10 Pro NFC
  - infinix note 11 -> اینفینیکس نوت 11
  - infinix note 11s -> اینفینیکس نوت 11 اس
  - infinix smart 5 (india) -> اینفینیکس Smart 5 (India)
  - infinix smart 5 pro -> اینفینیکس اسمارت 5 پرو
  - infinix hot 11 -> اینفینیکس Hot 11
  - infinix hot 11s -> اینفینیکس Hot 11s
  - infinix zero x -> اینفینیکس Zero X
  - infinix zero x neo -> اینفینیکس Zero X Neo
  - infinix zero x pro -> اینفینیکس Zero X Pro
  - infinix note 11 pro -> اینفینیکس Note 11 Pro
  - infinix smart 6 -> اینفینیکس Smart 6
  - infinix hot 11 play -> اینفینیکس Hot 11 Play
  - infinix note 11i -> اینفینیکس Note 11i
  - infinix hot 12 play -> اینفینیکس Hot 12 پلی
  - infinix hot 12 play nfc -> اینفینیکس Hot 12 Play NFC
  - infinix hot 12 pro -> اینفینیکس Hot 12 پرو
  - infinix note 12 -> اینفینیکس نوت 12
  - infinix note 12 5g -> اینفینیکس نوت 12 5G
  - infinix note 12 g96 -> اینفینیکس نوت 12 G96
  - infinix note 12 pro -> اینفینیکس نوت 12 پرو
  - infinix note 12 pro 5g -> اینفینیکس نوت 12 پرو 5G
  - infinix smart 6 hd -> اینفینیکس اسمارت 6 HD
  - infinix hot 11s nfc -> اینفینیکس Hot 11s NFC
  - infinix zero 5g -> اینفینیکس Zero 5G
  - infinix hot 11 2022 -> اینفینیکس Hot 11 2022
  - infinix hot 12 -> اینفینیکس Hot 12
  - infinix hot 12i -> اینفینیکس Hot 12i
  - infinix note 12i -> اینفینیکس Note 12i
  - infinix note 12 vip -> اینفینیکس Note 12 VIP
  - lava -> لاوا
  - lava z50 -> لاوا Z50
  - lava z91 -> لاوا Z91
  - lava z61 -> لاوا Z61
  - lava z91 (2gb) -> لاوا Z91 (2GB)
  - lava z60s -> لاوا Z60s
  - lava z81 -> لاوا Z81
  - lava z92 -> لاوا Z92
  - lava z40 -> لاوا Z40
  - lava z61 pro -> لاوا Z61 Pro
  - lava z71 -> لاوا Z71
  - lava agni 5g -> لاوا Agni 5G
  - lava z1 -> لاوا Z1
  - lava z2 -> لاوا Z2
  - lava z2 max -> لاوا Z2 Max
  - lava z2s -> لاوا Z2s
  - lava z4 -> لاوا Z4
  - lava z6 -> لاوا Z6
  - lava blaze -> لاوا Blaze
  - lava x2 -> لاوا X2
  - lava z3 -> لاوا Z3
  - lenovo -> لنوو
  - lenovo a5860 -> لنوو A5860
  - lenovo vibe z3 pro -> لنوو Vibe Z3 Pro
  - lenovo zuk z1 mini -> لنوو ZUK Z1 mini
  - lenovo k800 -> لنوو K800
  - lenovo p700i -> لنوو P700i
  - lenovo s560 -> لنوو S560
  - lenovo a789 -> لنوو A789
  - lenovo k860 -> لنوو K860
  - lenovo s880 -> لنوو S880
  - lenovo a660 -> لنوو A660
  - lenovo p770 -> لنوو P770
  - lenovo a369i -> لنوو A369i
  - lenovo a516 -> لنوو A516
  - lenovo a706 -> لنوو A706
  - lenovo a800 -> لنوو A800
  - lenovo a820 -> لنوو A820
  - lenovo a830 -> لنوو A830
  - lenovo k900 -> لنوو K900
  - lenovo s720 -> لنوو S720
  - lenovo s890 -> لنوو S890
  - lenovo s920 -> لنوو S920
  - lenovo a390 -> لنوو A390
  - lenovo s820 -> لنوو S820
  - lenovo p780 -> لنوو P780
  - lenovo a850 -> لنوو A850
  - lenovo a269i -> لنوو A269i
  - lenovo a630 -> لنوو A630
  - lenovo s5000 -> لنوو S5000
  - lenovo vibe x s960 -> لنوو Vibe X S960
  - lenovo vibe z k910 -> لنوو Vibe Z K910
  - lenovo s650 -> لنوو S650
  - lenovo s930 -> لنوو S930
  - lenovo a328 -> لنوو A328
  - lenovo a536 -> لنوو A536
  - lenovo a859 -> لنوو A859
  - lenovo a880 -> لنوو A880
  - lenovo s750 -> لنوو S750
  - lenovo s850 -> لنوو S850
  - lenovo a850+ -> لنوو A850+
  - lenovo a316i -> لنوو A316i
  - lenovo a526 -> لنوو A526
  - lenovo a8-50 a5500 -> لنوو A8-50 A5500
  - lenovo a680 -> لنوو A680
  - lenovo a889 -> لنوو A889
  - lenovo s939 -> لنوو S939
  - lenovo golden warrior a8 -> لنوو Golden Warrior A8
  - lenovo vibe z2 pro -> لنوو Vibe Z2 Pro
  - lenovo a606 -> لنوو A606
  - lenovo s580 -> لنوو S580
  - lenovo vibe x2 -> لنوو Vibe X2
  - lenovo vibe z2 -> لنوو Vibe Z2
  - lenovo a319 -> لنوو A319
  - lenovo s856 -> لنوو S856
  - lenovo a916 -> لنوو A916
  - lenovo s90 sisley -> لنوو S90 Sisley
  - lenovo golden warrior note 8 -> لنوو Golden Warrior Note 8
  - lenovo k3 -> لنوو K3
  - lenovo a6000 -> لنوو A6000
  - lenovo a616 -> لنوو A616
  - lenovo p70 -> لنوو P70
  - lenovo p90 -> لنوو P90
  - lenovo s60 -> لنوو S60
  - lenovo vibe x2 pro -> لنوو Vibe X2 Pro
  - lenovo a5000 -> لنوو A5000
  - lenovo a7000 -> لنوو A7000
  - lenovo k3 note -> لنوو K3 Note
  - lenovo vibe shot -> لنوو Vibe Shot
  - lenovo a1900 -> لنوو A1900
  - lenovo a6000 plus -> لنوو A6000 Plus
  - lenovo k80 -> لنوو K80
  - lenovo a3900 -> لنوو A3900
  - lenovo a2010 -> لنوو A2010
  - lenovo zuk z1 -> لنوو ZUK Z1
  - lenovo a1000 -> لنوو A1000
  - lenovo a6010 -> لنوو A6010
  - lenovo a6010 plus -> لنوو A6010 Plus
  - lenovo a7000 plus -> لنوو A7000 Plus
  - lenovo phab -> لنوو Phab
  - lenovo phab plus -> لنوو Phab Plus
  - lenovo vibe p1 -> لنوو Vibe P1
  - lenovo vibe p1m -> لنوو Vibe P1m
  - lenovo vibe s1 -> لنوو Vibe S1
  - lenovo a3690 -> لنوو A3690
  - lenovo vibe x3 -> لنوو Vibe X3
  - lenovo vibe x3 c78 -> لنوو Vibe X3 c78
  - lenovo a7000 turbo -> لنوو A7000 Turbo
  - lenovo k5 note -> لنوو K5 Note
  - lenovo lemon 3 -> لنوو Lemon 3
  - lenovo vibe s1 lite -> لنوو Vibe S1 Lite
  - lenovo vibe k5 -> لنوو Vibe K5
  - lenovo vibe k5 plus -> لنوو Vibe K5 Plus
  - lenovo vibe p1 turbo -> لنوو Vibe P1 Turbo
  - lenovo zuk z2 pro -> لنوو ZUK Z2 Pro
  - lenovo vibe c -> لنوو Vibe C
  - lenovo zuk z2 -> لنوو ZUK Z2
  - lenovo phab2 -> لنوو Phab2
  - lenovo phab2 plus -> لنوو Phab2 Plus
  - lenovo phab2 pro -> لنوو Phab2 Pro
  - lenovo c2 -> لنوو C2
  - lenovo vibe a -> لنوو Vibe A
  - lenovo a6600 -> لنوو A6600
  - lenovo a6600 plus -> لنوو A6600 Plus
  - lenovo a plus -> لنوو A Plus
  - lenovo c2 power -> لنوو C2 Power
  - lenovo k6 -> لنوو K6
  - lenovo k6 note -> لنوو K6 Note
  - lenovo k6 power -> لنوو K6 Power
  - lenovo p2 -> لنوو P2
  - lenovo b -> لنوو B
  - lenovo zuk edge -> لنوو ZUK Edge
  - lenovo k8 -> لنوو K8
  - lenovo k8 note -> لنوو K8 Note
  - lenovo k8 plus -> لنوو K8 Plus
  - lenovo k320t -> لنوو K320t
  - lenovo k5 -> لنوو K5
  - lenovo k5 play -> لنوو K5 play
  - lenovo s5 -> لنوو S5
  - lenovo a5 -> لنوو A5
  - lenovo k5 note (2018) -> لنوو K5 Note (2018)
  - lenovo z5 -> لنوو Z5
  - lenovo k5 pro -> لنوو K5 Pro
  - lenovo k9 -> لنوو K9
  - lenovo s5 pro -> لنوو S5 Pro
  - lenovo z5 pro -> لنوو Z5 Pro
  - lenovo a7 -> لنوو A7
  - lenovo s5 pro gt -> لنوو S5 Pro GT
  - lenovo z5 pro gt -> لنوو Z5 Pro GT
  - lenovo z5s -> لنوو Z5s
  - lenovo k6 enjoy -> لنوو K6 Enjoy
  - lenovo z6 pro -> لنوو Z6 Pro
  - lenovo z6 youth -> لنوو Z6 Youth
  - lenovo z6 pro 5g -> لنوو Z6 Pro 5G
  - lenovo z6 -> لنوو Z6
  - lenovo a6 note -> لنوو A6 Note
  - lenovo k10 note -> لنوو K10 Note
  - lenovo k10 plus -> لنوو K10 Plus
  - lenovo a8 2020 -> لنوو A8 2020
  - lenovo k12 (china) -> لنوو K12 (China)
  - lenovo k12 pro -> لنوو K12 Pro
  - lenovo m10 plus -> لنوو M10 پلاس
  - lenovo legion duel -> لنوو Legion Duel
  - lenovo legion pro -> لنوو Legion Pro
  - lenovo legion 2 pro -> لنوو Legion 2 Pro
  - lenovo legion duel 2 -> لنوو Legion Duel 2
  - lenovo k13 note -> لنوو K13 Note
  - lenovo k13 -> لنوو K13
  - lenovo k13 pro -> لنوو K13 پرو
  - lenovo legion y70 -> لنوو Legion Y70
  - lenovo legion y90 -> لنوو Legion Y90
  - lg -> ال‌جی
  - lg g4 pro -> ال‌جی G4 Pro
  - lg optimus l5 ii -> ال‌جی Optimus L5 II
  - lg optimus vu ii -> ال‌جی Optimus Vu II
  - lg w11 -> ال‌جی W11
  - lg t385 -> ال‌جی T385
  - lg motion 4g ms770 -> ال‌جی Motion 4G MS770
  - lg optimus g e975 -> ال‌جی Optimus G E975
  - lg optimus l5 dual e615 -> ال‌جی Optimus L5 Dual E615
  - lg optimus l9 p760 -> ال‌جی Optimus L9 P760
  - lg optimus vu p895 -> ال‌جی Optimus Vu P895
  - lg escape p870 -> ال‌جی Escape P870
  - lg intuition vs950 -> ال‌جی Intuition VS950
  - lg optimus g e970 -> ال‌جی Optimus G E970
  - lg splendor us730 -> ال‌جی Splendor US730
  - lg mach ls860 -> ال‌جی Mach LS860
  - lg nexus 4 e960 -> ال‌جی Nexus 4 E960
  - lg optimus l9 p769 -> ال‌جی Optimus L9 P769
  - lg spectrum ii 4g vs930 -> ال‌جی Spectrum II 4G VS930
  - lg optimus f7 -> ال‌جی Optimus F7
  - lg optimus g pro e985 -> ال‌جی Optimus G Pro E985
  - lg optimus l1 ii e410 -> ال‌جی Optimus L1 II E410
  - lg optimus l3 ii dual e435 -> ال‌جی Optimus L3 II Dual E435
  - lg optimus l3 ii e430 -> ال‌جی Optimus L3 II E430
  - lg optimus l7 ii dual p715 -> ال‌جی Optimus L7 II Dual P715
  - lg optimus l7 ii p710 -> ال‌جی Optimus L7 II P710
  - lg lucid2 vs870 -> ال‌جی Lucid2 VS870
  - lg optimus gj e975w -> ال‌جی Optimus GJ E975W
  - lg optimus f3 -> ال‌جی Optimus F3
  - lg optimus l4 ii dual e445 -> ال‌جی Optimus L4 II Dual E445
  - lg optimus l4 ii e440 -> ال‌جی Optimus L4 II E440
  - lg g2 -> ال‌جی G2
  - lg optimus l9 ii -> ال‌جی Optimus L9 II
  - lg vu 3 f300l -> ال‌جی Vu 3 F300L
  - lg g flex -> ال‌جی G Flex
  - lg g pro lite -> ال‌جی G Pro Lite
  - lg g pro lite dual -> ال‌جی G Pro Lite Dual
  - lg nexus 5 -> ال‌جی Nexus 5
  - lg optimus l2 ii e435 -> ال‌جی Optimus L2 II E435
  - lg gx f310l -> ال‌جی GX F310L
  - lg 450 -> ال‌جی 450
  - lg l45 dual x132 -> ال‌جی L45 Dual X132
  - lg l80 -> ال‌جی L80
  - lg optimus f3q -> ال‌جی Optimus F3Q
  - lg f70 d315 -> ال‌جی F70 D315
  - lg g2 mini -> ال‌جی G2 mini
  - lg g2 mini lte -> ال‌جی G2 mini LTE
  - lg g2 mini lte (tegra) -> ال‌جی G2 mini LTE (Tegra)
  - lg g pro 2 -> ال‌جی G Pro 2
  - lg l40 d160 -> ال‌جی L40 D160
  - lg l40 dual d170 -> ال‌جی L40 Dual D170
  - lg l70 d320n -> ال‌جی L70 D320N
  - lg l70 dual d325 -> ال‌جی L70 Dual D325
  - lg l90 d405 -> ال‌جی L90 D405
  - lg l90 dual d410 -> ال‌جی L90 Dual D410
  - lg l65 dual d285 -> ال‌جی L65 Dual D285
  - lg l80 dual -> ال‌جی L80 Dual
  - lg lucid 3 vs876 -> ال‌جی Lucid 3 VS876
  - lg g3 -> ال‌جی G3
  - lg l35 -> ال‌جی L35
  - lg volt -> ال‌جی Volt
  - lg l30 -> ال‌جی L30
  - lg l65 d280 -> ال‌جی L65 D280
  - lg g3 s -> ال‌جی G3 S
  - lg g3 s dual -> ال‌جی G3 S Dual
  - lg l20 -> ال‌جی L20
  - lg l50 -> ال‌جی L50
  - lg g3 stylus -> ال‌جی G3 Stylus
  - lg g vista -> ال‌جی G Vista
  - lg l60 -> ال‌جی L60
  - lg l60 dual -> ال‌جی L60 Dual
  - lg l bello -> ال‌جی L Bello
  - lg l fino -> ال‌جی L Fino
  - lg f60 -> ال‌جی F60
  - lg tribute -> ال‌جی Tribute
  - lg g3 screen -> ال‌جی G3 Screen
  - lg g2 lite -> ال‌جی G2 Lite
  - lg l prime -> ال‌جی L Prime
  - lg g flex2 -> ال‌جی G Flex2
  - lg joy -> ال‌جی Joy
  - lg leon -> ال‌جی Leon
  - lg magna -> ال‌جی Magna
  - lg spirit -> ال‌جی Spirit
  - lg aka -> ال‌جی AKA
  - lg g4 -> ال‌جی G4
  - lg g4c -> ال‌جی G4c
  - lg g4 dual -> ال‌جی G4 Dual
  - lg g stylo -> ال‌جی G Stylo
  - lg g360 -> ال‌جی G360
  - lg bello ii -> ال‌جی Bello II
  - lg g4 beat -> ال‌جی G4 Beat
  - lg tribute 2 -> ال‌جی Tribute 2
  - lg nexus 5x -> ال‌جی Nexus 5X
  - lg g vista 2 -> ال‌جی G Vista 2
  - lg v10 -> ال‌جی V10
  - lg ray -> ال‌جی Ray
  - lg k4 -> ال‌جی K4
  - lg g5 -> ال‌جی G5
  - lg k8 -> ال‌جی K8
  - lg x cam -> ال‌جی X cam
  - lg x screen -> ال‌جی X screen
  - lg k5 -> ال‌جی K5
  - lg g5 se -> ال‌جی G5 SE
  - lg stylo 2 -> ال‌جی Stylo 2
  - lg stylus 2 plus -> ال‌جی Stylus 2 Plus
  - lg x power -> ال‌جی X power
  - lg x style -> ال‌جی X style
  - lg x mach -> ال‌جی X mach
  - lg x max -> ال‌جی X max
  - lg x5 -> ال‌جی X5
  - lg x skin -> ال‌جی X Skin
  - lg k3 -> ال‌جی K3
  - lg v20 -> ال‌جی V20
  - lg u -> ال‌جی U
  - lg k10 (2017) -> ال‌جی K10 (2017)
  - lg k20 plus -> ال‌جی K20 plus
  - lg k3 (2017) -> ال‌جی K3 (2017)
  - lg k4 (2017) -> ال‌جی K4 (2017)
  - lg k8 (2017) -> ال‌جی K8 (2017)
  - lg stylus 3 -> ال‌جی Stylus 3
  - lg g6 -> ال‌جی G6
  - lg x power2 -> ال‌جی X power2
  - lg harmony -> ال‌جی Harmony
  - lg k7 (2017) -> ال‌جی K7 (2017)
  - lg stylo 3 plus -> ال‌جی استایلو 3 پلاس
  - lg x venture -> ال‌جی X venture
  - lg q8 (2017) -> ال‌جی Q8 (2017)
  - lg q6 -> ال‌جی Q6
  - lg v30 -> ال‌جی V30
  - lg aristo 2 -> ال‌جی Aristo 2
  - lg x4+ -> ال‌جی X4+
  - lg k10 (2018) -> ال‌جی K10 (2018)
  - lg k8 (2018) -> ال‌جی K8 (2018)
  - lg v30s thinq -> ال‌جی V30S ThinQ
  - lg zone 4 -> ال‌جی Zone 4
  - lg g7 thinq -> ال‌جی G7 ThinQ
  - lg k30 -> ال‌جی K30
  - lg q7 -> ال‌جی Q7
  - lg v35 thinq -> ال‌جی V35 ThinQ
  - lg q stylo 4 -> ال‌جی Q Stylo 4
  - lg q stylus -> ال‌جی Q Stylus
  - lg candy -> ال‌جی Candy
  - lg k11 plus -> ال‌جی K11 Plus
  - lg x power 3 -> ال‌جی X power 3
  - lg g7 fit -> ال‌جی G7 Fit
  - lg g7 one -> ال‌جی G7 One
  - lg q8 (2018) -> ال‌جی Q8 (2018)
  - lg v40 thinq -> ال‌جی V40 ThinQ
  - lg q9 -> ال‌جی Q9
  - lg tribute empire -> ال‌جی Tribute Empire
  - lg g8s thinq -> ال‌جی G8S ThinQ
  - lg g8 thinq -> ال‌جی G8 ThinQ
  - lg k40 -> ال‌جی K40
  - lg k50 -> ال‌جی K50
  - lg q60 -> ال‌جی Q60
  - lg v50 thinq 5g -> ال‌جی V50 ThinQ 5G
  - lg stylo 5 -> ال‌جی Stylo 5
  - lg w10 -> ال‌جی W10
  - lg w30 -> ال‌جی W30
  - lg w30 pro -> ال‌جی W30 Pro
  - lg k20 (2019) -> ال‌جی K20 (2019)
  - lg k30 (2019) -> ال‌جی K30 (2019)
  - lg k40s -> ال‌جی K40S
  - lg k50s -> ال‌جی K50S
  - lg g8x thinq -> ال‌جی G8X ThinQ
  - lg q70 -> ال‌جی Q70
  - lg v50s thinq 5g -> ال‌جی V50S ThinQ 5G
  - lg q51 -> ال‌جی Q51
  - lg stylo 6 -> ال‌جی Stylo 6
  - lg velvet 5g uw -> ال‌جی Velvet 5G UW
  - lg k41s -> ال‌جی K41S
  - lg k51s -> ال‌جی K51S
  - lg k61 -> ال‌جی K61
  - lg v60 thinq 5g -> ال‌جی V60 ThinQ 5G
  - lg v60 thinq 5g uw -> ال‌جی V60 ThinQ 5G UW
  - lg w10 alpha -> ال‌جی W10 Alpha
  - lg folder 2 -> ال‌جی Folder 2
  - lg q61 -> ال‌جی Q61
  - lg velvet 5g -> ال‌جی Velvet 5G
  - lg velvet -> ال‌جی Velvet
  - lg k31 -> ال‌جی K31
  - lg q92 5g -> ال‌جی Q92 5G
  - lg k22 -> ال‌جی K22
  - lg k42 -> ال‌جی K42
  - lg k52 -> ال‌جی K52
  - lg k62 -> ال‌جی K62
  - lg k71 -> ال‌جی K71
  - lg k92 5g -> ال‌جی K92 5G
  - lg q31 -> ال‌جی Q31
  - lg q52 -> ال‌جی Q52
  - lg wing 5g -> ال‌جی Wing 5G
  - lg w31 -> ال‌جی W31
  - lg w31+ -> ال‌جی W31+
  - lg w41 -> ال‌جی W41
  - lg w41+ -> ال‌جی W41+
  - lg w41 pro -> ال‌جی W41 Pro
  - meizu -> میزو
  - meizu pro 5 mini -> میزو PRO 5 mini
  - meizu mx2 -> میزو MX2
  - meizu mx4 -> میزو MX4
  - meizu mx4 pro -> میزو MX4 Pro
  - meizu m1 note -> میزو M1 Note
  - meizu m1 -> میزو M1
  - meizu m2 note -> میزو M2 Note
  - meizu mx5 -> میزو MX5
  - meizu m2 -> میزو M2
  - meizu pro 5 -> میزو PRO 5
  - meizu m1 metal -> میزو M1 Metal
  - meizu m3 -> میزو M3
  - meizu m3 note -> میزو M3 Note
  - meizu mx5e -> میزو MX5e
  - meizu pro 6 -> میزو Pro 6
  - meizu m3s -> میزو M3s
  - meizu mx6 -> میزو MX6
  - meizu m3e -> میزو M3e
  - meizu u10 -> میزو U10
  - meizu u20 -> میزو U20
  - meizu m3 max -> میزو M3 Max
  - meizu m5 -> میزو M5
  - meizu m3x -> میزو M3x
  - meizu pro 6 plus -> میزو Pro 6 Plus
  - meizu pro 6s -> میزو Pro 6s
  - meizu m5 note -> میزو M5 Note
  - meizu m5s -> میزو M5s
  - meizu e2 -> میزو E2
  - meizu m5c -> میزو M5c
  - meizu pro 7 -> میزو Pro 7
  - meizu pro 7 plus -> میزو Pro 7 Plus
  - meizu m6 note -> میزو M6 Note
  - meizu m6 -> میزو M6
  - meizu m6s -> میزو M6s
  - meizu 15 -> میزو 15
  - meizu 15 lite -> میزو 15 Lite
  - meizu 15 plus -> میزو 15 پلاس
  - meizu e3 -> میزو E3
  - meizu m6t -> میزو M6T
  - meizu m8c -> میزو M8c
  - meizu 16 -> میزو 16
  - meizu 16 plus -> میزو 16 Plus
  - meizu 16x -> میزو 16X
  - meizu v8 -> میزو V8
  - meizu v8 pro -> میزو V8 Pro
  - meizu x8 -> میزو X8
  - meizu note 8 -> میزو Note 8
  - meizu c9 -> میزو C9
  - meizu c9 pro -> میزو C9 Pro
  - meizu zero -> میزو Zero
  - meizu note 9 -> میزو Note 9
  - meizu 16s -> میزو 16s
  - meizu 16xs -> میزو 16Xs
  - meizu 16s pro -> میزو 16s Pro
  - meizu m10 -> میزو M10
  - meizu 16t -> میزو 16T
  - meizu 17 -> میزو 17
  - meizu 17 pro -> میزو 17 Pro
  - meizu 18 -> میزو 18
  - meizu 18 pro -> میزو 18 Pro
  - meizu 18s -> میزو 18s
  - meizu 18s pro -> میزو 18s Pro
  - meizu 18x -> میزو 18x
  - micromax -> مایکرومکس
  - micromax vdeo 3 -> مایکرومکس Vdeo 3
  - micromax bharat 5 -> مایکرومکس Bharat 5
  - micromax bharat 5 plus -> مایکرومکس Bharat 5 Plus
  - micromax bharat 5 pro -> مایکرومکس Bharat 5 Pro
  - micromax canvas infinity life -> مایکرومکس Canvas Infinity Life
  - micromax canvas 1 2018 -> مایکرومکس Canvas 1 2018
  - micromax bharat go -> مایکرومکس Bharat Go
  - micromax bharat 5 infinity -> مایکرومکس Bharat 5 Infinity
  - micromax infinity n11 -> مایکرومکس Infinity N11
  - micromax infinity n12 -> مایکرومکس Infinity N12
  - micromax in 1b -> مایکرومکس In 1b
  - micromax in note 1 -> مایکرومکس In note 1
  - micromax in 1 -> مایکرومکس In 1
  - micromax in 2b -> مایکرومکس In 2b
  - micromax in 2c -> مایکرومکس In 2c
  - micromax in note 2 -> مایکرومکس In note 2
  - microsoft -> مایکروسافت
  - microsoft lumia 1030 -> مایکروسافت Lumia 1030
  - microsoft lumia 1330 -> مایکروسافت Lumia 1330
  - microsoft lumia 850 -> مایکروسافت Lumia 850
  - microsoft lumia 535 -> مایکروسافت Lumia 535
  - microsoft lumia 535 dual sim -> مایکروسافت Lumia 535 Dual SIM
  - microsoft lumia 435 -> مایکروسافت Lumia 435
  - microsoft lumia 435 dual sim -> مایکروسافت Lumia 435 Dual SIM
  - microsoft lumia 532 -> مایکروسافت Lumia 532
  - microsoft lumia 532 dual sim -> مایکروسافت Lumia 532 Dual SIM
  - microsoft lumia 430 dual sim -> مایکروسافت Lumia 430 Dual SIM
  - microsoft lumia 640 lte -> مایکروسافت Lumia 640 LTE
  - microsoft lumia 640 xl -> مایکروسافت Lumia 640 XL
  - microsoft lumia 540 dual sim -> مایکروسافت Lumia 540 Dual SIM
  - microsoft lumia 550 -> مایکروسافت Lumia 550
  - microsoft lumia 950 -> مایکروسافت Lumia 950
  - microsoft lumia 950 dual sim -> مایکروسافت Lumia 950 Dual SIM
  - microsoft lumia 950 xl -> مایکروسافت Lumia 950 XL
  - microsoft lumia 950 xl dual sim -> مایکروسافت Lumia 950 XL Dual SIM
  - microsoft lumia 650 -> مایکروسافت Lumia 650
  - microsoft surface duo -> مایکروسافت Surface Duo
  - microsoft surface duo 2 -> مایکروسافت Surface Duo 2
  - motorola -> موتورولا
  - motorola moto g60 -> موتورولا Moto G60
  - motorola moto x5 -> موتورولا Moto X5
  - motorola moto z4 force -> موتورولا Moto Z4 Force
  - motorola moto z4 play -> موتورولا Moto Z4 Play
  - motorola p40 -> موتورولا P40
  - motorola droid razr xt912 -> موتورولا DROID RAZR XT912
  - motorola xt319 -> موتورولا XT319
  - motorola droid razr maxx -> موتورولا DROID RAZR MAXX
  - motorola motosmart me xt303 -> موتورولا Motosmart Me XT303
  - motorola razr maxx -> موتورولا RAZR MAXX
  - motorola razr v xt885 -> موتورولا RAZR V XT885
  - motorola droid razr hd -> موتورولا DROID RAZR HD
  - motorola droid razr m -> موتورولا DROID RAZR M
  - motorola droid razr maxx hd -> موتورولا DROID RAZR MAXX HD
  - motorola razr hd xt925 -> موتورولا RAZR HD XT925
  - motorola razr i xt890 -> موتورولا RAZR i XT890
  - motorola razr m xt905 -> موتورولا RAZR M XT905
  - motorola electrify m xt905 -> موتورولا Electrify M XT905
  - motorola razr d1 -> موتورولا RAZR D1
  - motorola razr d3 xt919 -> موتورولا RAZR D3 XT919
  - motorola droid maxx -> موتورولا DROID Maxx
  - motorola droid mini -> موتورولا DROID Mini
  - motorola droid ultra -> موتورولا DROID Ultra
  - motorola moto x -> موتورولا Moto X
  - motorola moto g -> موتورولا Moto G
  - motorola moto g dual sim -> موتورولا Moto G Dual SIM
  - motorola moto e -> موتورولا Moto E
  - motorola moto e dual sim -> موتورولا Moto E Dual SIM
  - motorola moto g 4g -> موتورولا Moto G 4G
  - motorola luge -> موتورولا Luge
  - motorola moto g (2nd gen) -> موتورولا Moto G (2nd gen)
  - motorola moto g dual sim (2nd gen) -> موتورولا Moto G Dual SIM (2nd gen)
  - motorola droid turbo -> موتورولا DROID Turbo
  - motorola nexus 6 -> موتورولا Nexus 6
  - motorola moto maxx -> موتورولا Moto Maxx
  - motorola moto g 4g dual sim (2nd gen) -> موتورولا Moto G 4G Dual SIM (2nd gen)
  - motorola moto g 4g (2nd gen) -> موتورولا Moto G 4G (2nd gen)
  - motorola moto g (3rd gen) -> موتورولا Moto G (3rd gen)
  - motorola moto g dual sim (3rd gen) -> موتورولا Moto G Dual SIM (3rd gen)
  - motorola moto x play -> موتورولا Moto X Play
  - motorola moto x play dual sim -> موتورولا Moto X Play Dual SIM
  - motorola droid maxx 2 -> موتورولا Droid Maxx 2
  - motorola moto x force -> موتورولا Moto X Force
  - motorola moto g4 -> موتورولا Moto G4
  - motorola moto g4 play -> موتورولا Moto G4 Play
  - motorola moto g4 plus -> موتورولا Moto G4 Plus
  - motorola moto z -> موتورولا Moto Z
  - motorola moto z force -> موتورولا Moto Z Force
  - motorola moto e3 -> موتورولا Moto E3
  - motorola moto e3 power -> موتورولا Moto E3 Power
  - motorola moto g5 -> موتورولا Moto G5
  - motorola moto g5 plus -> موتورولا Moto G5 Plus
  - motorola moto c -> موتورولا Moto C
  - motorola moto c plus -> موتورولا Moto C Plus
  - motorola moto e4 -> موتورولا Moto E4
  - motorola moto e4 plus -> موتورولا Moto E4 Plus
  - motorola moto e4 plus (usa) -> موتورولا Moto E4 Plus (USA)
  - motorola moto e4 (usa) -> موتورولا Moto E4 (USA)
  - motorola moto z2 play -> موتورولا Moto Z2 Play
  - motorola moto z2 force -> موتورولا Moto Z2 Force
  - motorola moto g5s -> موتورولا Moto G5S
  - motorola moto g5s plus -> موتورولا Moto G5S Plus
  - motorola moto x4 -> موتورولا Moto X4
  - motorola moto e5 -> موتورولا Moto E5
  - motorola moto e5 play -> موتورولا Moto E5 Play
  - motorola moto e5 plus -> موتورولا Moto E5 Plus
  - motorola moto g6 -> موتورولا Moto G6
  - motorola moto g6 play -> موتورولا Moto G6 Play
  - motorola moto g6 plus -> موتورولا Moto G6 Plus
  - motorola moto e5 cruise -> موتورولا Moto E5 Cruise
  - motorola moto z3 play -> موتورولا Moto Z3 Play
  - motorola moto e5 play go -> موتورولا Moto E5 Play Go
  - motorola moto z3 -> موتورولا Moto Z3
  - motorola one (p30 play) -> موتورولا One (P30 Play)
  - motorola one power (p30 note) -> موتورولا One Power (P30 Note)
  - motorola p30 -> موتورولا P30
  - motorola razr 2019 -> موتورولا ریزر 2019
  - motorola moto g7 -> موتورولا Moto G7
  - motorola moto g7 play -> موتورولا Moto G7 Play
  - motorola moto g7 plus -> موتورولا Moto G7 Plus
  - motorola moto g7 power -> موتورولا Moto G7 Power
  - motorola moto z4 -> موتورولا Moto Z4
  - motorola moto e6 -> موتورولا Moto E6
  - motorola one action -> موتورولا One Action
  - motorola moto e6 plus -> موتورولا Moto E6 Plus
  - motorola one zoom -> موتورولا One Zoom
  - motorola moto e6 play -> موتورولا Moto E6 Play
  - motorola moto g8 play -> موتورولا Moto G8 Play
  - motorola moto g8 plus -> موتورولا Moto G8 Plus
  - motorola one macro -> موتورولا One Macro
  - motorola edge+ (2020) -> موتورولا Edge+ (2020)
  - motorola moto g9 (india) -> موتورولا Moto G9 (India)
  - motorola moto g pro -> موتورولا موتو G پرو
  - motorola moto g stylus -> موتورولا موتو G استایلوس
  - motorola one hyper -> موتورولا One Hyper
  - motorola moto g8 power -> موتورولا Moto G8 Power
  - motorola moto g power -> موتورولا Moto G Power
  - motorola moto e6s (2020) -> موتورولا Moto E6s (2020)
  - motorola moto g8 -> موتورولا Moto G8
  - motorola edge -> موتورولا Edge
  - motorola edge+ -> موتورولا Edge+
  - motorola moto g8 power lite -> موتورولا Moto G8 Power Lite
  - motorola moto e (2020) -> موتورولا Moto E (2020)
  - motorola moto g fast -> موتورولا Moto G Fast
  - motorola one fusion+ -> موتورولا One Fusion+
  - motorola moto g 5g plus -> موتورولا Moto G 5G Plus
  - motorola one fusion -> موتورولا One Fusion
  - motorola one vision plus -> موتورولا One Vision Plus
  - motorola moto g9 play -> موتورولا Moto G9 Play
  - motorola moto e7 plus -> موتورولا Moto E7 Plus
  - motorola moto g9 plus -> موتورولا Moto G9 Plus
  - motorola one 5g -> موتورولا One 5G
  - motorola razr 5g -> موتورولا Razr 5G
  - motorola one 5g uw -> موتورولا One 5G UW
  - motorola moto e7 -> موتورولا Moto E7
  - motorola moto g 5g -> موتورولا Moto G 5G
  - motorola moto g9 power -> موتورولا Moto G9 Power
  - motorola edge (2021) -> موتورولا اج 2021
  - motorola edge 5g uw (2021) -> موتورولا Edge 5G UW (2021)
  - motorola g pure -> موتورولا G Pure
  - motorola moto e40 -> موتورولا موتو E40
  - motorola moto e7i power -> موتورولا موتو E7i Power
  - motorola moto g40 fusion -> موتورولا موتو G40 Fusion
  - motorola moto g51 5g -> موتورولا Moto G51 5G
  - motorola moto g play (2021) -> موتورولا موتو G Play 2021
  - motorola moto g power (2022) -> موتورولا موتو جی پاور 2022
  - motorola one 5g uw ace -> موتورولا one 5G UW ace
  - motorola edge s -> موتورولا Edge S
  - motorola moto g power (2021) -> موتورولا Moto G Power (2021)
  - motorola moto g stylus (2021) -> موتورولا Moto G Stylus (2021)
  - motorola one 5g ace -> موتورولا One 5G Ace
  - motorola moto e6i -> موتورولا Moto E6i
  - motorola moto e7 power -> موتورولا Moto E7 Power
  - motorola moto g10 -> موتورولا Moto G10
  - motorola moto g30 -> موتورولا Moto G30
  - motorola moto g100 -> موتورولا Moto G100
  - motorola moto g10 power -> موتورولا Moto G10 Power
  - motorola moto g50 -> موتورولا Moto G50
  - motorola moto g20 -> موتورولا Moto G20
  - motorola defy (2021) -> موتورولا Defy (2021)
  - motorola moto g stylus 5g -> موتورولا Moto G Stylus 5G
  - motorola edge 20 -> موتورولا Edge 20
  - motorola edge 20 lite -> موتورولا Edge 20 Lite
  - motorola edge 20 pro -> موتورولا Edge 20 Pro
  - motorola edge 20 fusion -> موتورولا Edge 20 Fusion
  - motorola moto g50 5g -> موتورولا Moto G50 5G
  - motorola moto g60s -> موتورولا Moto G60S
  - motorola moto e20 -> موتورولا Moto E20
  - motorola moto e30 -> موتورولا Moto E30
  - motorola moto g200 5g -> موتورولا Moto G200 5G
  - motorola moto g31 -> موتورولا Moto G31
  - motorola moto g41 -> موتورولا Moto G41
  - motorola moto g51 -> موتورولا Moto G51
  - motorola moto g71 5g -> موتورولا Moto G71 5G
  - motorola edge (2022) -> موتورولا اج 2022
  - motorola edge 30 fusion -> موتورولا اج 30 فیوژن
  - motorola edge 30 pro -> موتورولا اج 30 پرو
  - motorola edge 30 ultra -> موتورولا اج 30 اولترا
  - motorola edge+ 5g uw (2022) -> موتورولا Edge+ 5G UW (2022)
  - motorola edge s30 -> موتورولا Edge S30
  - motorola edge x30 -> موتورولا Edge X30
  - motorola moto e22 -> موتورولا Moto E22
  - motorola moto e22s -> موتورولا موتو E22s
  - motorola moto e32 -> موتورولا موتو E32
  - motorola moto g22 -> موتورولا موتو G22
  - motorola moto g32 -> موتورولا موتو G32
  - motorola moto g42 -> موتورولا موتو G42
  - motorola moto g52 -> موتورولا موتو G52
  - motorola moto g62 5g -> موتورولا Moto G62 5G
  - motorola moto g62 (india) -> موتورولا موتو G62 هند
  - motorola moto g82 -> موتورولا موتو G82
  - motorola moto g stylus (2022) -> موتورولا موتو G استایلوس 2022
  - motorola moto g stylus 5g (2022) -> موتورولا موتو G استایلوس 5G 2022
  - motorola moto razr 2022 -> موتورولا موتو ریزر 2022
  - motorola moto s30 pro -> موتورولا موتو S30 پرو
  - motorola moto x30 pro -> موتورولا موتو X30 پرو
  - motorola edge 30 -> موتورولا Edge 30
  - motorola moto g (2022) -> موتورولا Moto G (2022)
  - motorola moto e32s -> موتورولا Moto E32s
  - motorola moto g71s -> موتورولا Moto G71s
  - nokia -> نوکیا
  - nokia 5800 xpressmusic -> نوکیا 5800 XpressMusic
  - nokia 8.1 plus -> نوکیا 8.1 Plus
  - nokia 9.3 pureview -> نوکیا 9.3 PureView
  - nokia n95 8gb -> نوکیا N95 8GB
  - nokia 808 pureview -> نوکیا 808 PureView
  - nokia lumia 820 -> نوکیا Lumia 820
  - nokia lumia 920 -> نوکیا Lumia 920
  - nokia lumia 510 -> نوکیا Lumia 510
  - nokia lumia 810 -> نوکیا Lumia 810
  - nokia lumia 822 -> نوکیا Lumia 822
  - nokia lumia 505 -> نوکیا Lumia 505
  - nokia lumia 620 -> نوکیا Lumia 620
  - nokia lumia 520 -> نوکیا Lumia 520
  - nokia lumia 720 -> نوکیا Lumia 720
  - nokia asha 210 -> نوکیا Asha 210
  - nokia lumia 928 -> نوکیا Lumia 928
  - nokia lumia 925 -> نوکیا Lumia 925
  - nokia lumia 625 -> نوکیا Lumia 625
  - nokia 515 -> نوکیا 515
  - nokia lumia 1320 -> نوکیا Lumia 1320
  - nokia lumia 1520 -> نوکیا Lumia 1520
  - nokia lumia 525 -> نوکیا Lumia 525
  - nokia lumia icon -> نوکیا Lumia Icon
  - nokia x -> نوکیا X
  - nokia xl -> نوکیا XL
  - nokia lumia 630 -> نوکیا Lumia 630
  - nokia lumia 630 dual sim -> نوکیا Lumia 630 Dual SIM
  - nokia lumia 930 -> نوکیا Lumia 930
  - nokia x2 dual sim -> نوکیا X2 Dual SIM
  - nokia lumia 530 -> نوکیا Lumia 530
  - nokia lumia 530 dual sim -> نوکیا Lumia 530 Dual SIM
  - nokia lumia 730 dual sim -> نوکیا Lumia 730 Dual SIM
  - nokia lumia 735 -> نوکیا Lumia 735
  - nokia lumia 830 -> نوکیا Lumia 830
  - nokia lumia 638 -> نوکیا Lumia 638
  - nokia 6 -> نوکیا 6
  - nokia 3 -> نوکیا 3
  - nokia 5 -> نوکیا 5
  - nokia 105 (2017) -> نوکیا 105 2017
  - nokia 130 (2017) -> نوکیا 130 2017
  - nokia 8 -> نوکیا 8
  - nokia 2 -> نوکیا 2
  - nokia 7 -> نوکیا 7
  - nokia 3310 4g -> نوکیا 3310 4G
  - nokia 6.1 -> نوکیا 6.1
  - nokia 1 -> نوکیا 1
  - nokia 7 plus -> نوکیا 7 plus
  - nokia 8110 4g -> نوکیا 8110 4G
  - nokia 8 sirocco -> نوکیا 8 Sirocco
  - nokia 2.1 -> نوکیا 2.1
  - nokia 3.1 -> نوکیا 3.1
  - nokia 5.1 -> نوکیا 5.1
  - nokia 5.1 plus (nokia x5) -> نوکیا 5.1 Plus (Nokia X5)
  - nokia 6.1 plus (nokia x6) -> نوکیا 6.1 Plus (Nokia X6)
  - nokia 106 (2018) -> نوکیا 106 2018
  - nokia 3.1 plus -> نوکیا 3.1 Plus
  - nokia 7.1 -> نوکیا 7.1
  - nokia 8.1 (nokia x7) -> نوکیا 8.1 (Nokia X7)
  - nokia 1 plus -> نوکیا 1 Plus
  - nokia 3.2 -> نوکیا 3.2
  - nokia 4.2 -> نوکیا 4.2
  - nokia 9 pureview -> نوکیا 9 PureView
  - nokia x71 -> نوکیا X71
  - nokia 105 (2019) -> نوکیا 105 2019
  - nokia 2.2 -> نوکیا 2.2
  - nokia 3.1 a -> نوکیا 3.1 A
  - nokia 3.1 c -> نوکیا 3.1 C
  - nokia 220 4g -> نوکیا 220 4G
  - nokia 2720 flip -> نوکیا 2720 Flip
  - nokia 6.2 -> نوکیا 6.2
  - nokia 7.2 -> نوکیا 7.2
  - nokia 800 tough -> نوکیا 800 Tough
  - nokia 215 4g -> نوکیا 215
  - nokia 2.3 -> نوکیا 2.3
  - nokia 2 v tella -> نوکیا 2 V Tella
  - nokia 3 v -> نوکیا 3 V
  - nokia c1 -> نوکیا C1
  - nokia 1.3 -> نوکیا 1.3
  - nokia 5.3 -> نوکیا 5.3
  - nokia 5310 (2020) -> نوکیا 5310 (2020)
  - nokia 8.3 5g -> نوکیا 8.3 5G
  - nokia c2 -> نوکیا C2
  - nokia c2 tava -> نوکیا C2 Tava
  - nokia c2 tennen -> نوکیا C2 Tennen
  - nokia c5 endi -> نوکیا C5 Endi
  - nokia c3 -> نوکیا C3
  - nokia 2.4 -> نوکیا 2.4
  - nokia 3.4 -> نوکیا 3.4
  - nokia 225 4g -> نوکیا 225 4G
  - nokia 6300 4g -> نوکیا 6300 4G
  - nokia 8000 4g -> نوکیا 8000 4G
  - nokia 8 v 5g uw -> نوکیا 8 V 5G UW
  - nokia 2720 v flip -> نوکیا 2720 V Flip
  - nokia 5.4 -> نوکیا 5.4
  - nokia 6310 (2021) -> نوکیا 6310 2021
  - nokia c1 plus -> نوکیا C1 Plus
  - nokia g20 -> نوکیا G20
  - nokia g300 -> نوکیا G300
  - nokia t20 -> نوکیا T20
  - nokia 1.4 -> نوکیا 1.4
  - nokia c10 -> نوکیا C10
  - nokia c20 -> نوکیا C20
  - nokia g10 -> نوکیا G10
  - nokia x10 -> نوکیا X10
  - nokia x20 -> نوکیا X20
  - nokia 105 4g -> نوکیا 105 4G
  - nokia 110 4g -> نوکیا 110 4G
  - nokia c01 plus -> نوکیا C01 Plus
  - nokia c20 plus -> نوکیا C20 Plus
  - nokia c1 2nd edition -> نوکیا C1 2nd Edition
  - nokia c30 -> نوکیا C30
  - nokia xr20 -> نوکیا XR20
  - nokia g50 -> نوکیا G50
  - nokia x100 -> نوکیا X100
  - nokia 105 (2022) -> نوکیا 105 2022
  - nokia 105+ (2022) -> نوکیا 105+ (2022)
  - nokia 110 (2022) -> نوکیا 110 2022
  - nokia 2660 flip -> نوکیا 2660 Flip
  - nokia 2760 flip -> نوکیا 2760 Flip
  - nokia 5710 xpressaudio -> نوکیا 5710 XpressAudio
  - nokia 8210 4g -> نوکیا 8210 4G
  - nokia c21 plus -> نوکیا C21 پلاس
  - nokia c31 -> نوکیا C31
  - nokia g400 -> نوکیا G400
  - nokia g60 -> نوکیا G60
  - nokia t10 -> نوکیا T10
  - nokia t21 -> نوکیا T21
  - nokia x30 -> نوکیا X30
  - nokia c100 -> نوکیا C100
  - nokia c200 -> نوکیا C200
  - nokia c21 -> نوکیا C21
  - nokia c2 2nd edition -> نوکیا C2 2nd Edition
  - nokia g11 -> نوکیا G11
  - nokia g21 -> نوکیا G21
  - nokia g11 plus -> نوکیا G11 Plus
  - oneplus -> وان پلاس
  - oneplus 9e -> وان پلاس 9E
  - oneplus 2 -> وان پلاس 2
  - oneplus x -> وان پلاس X
  - oneplus 3 -> وان پلاس 3
  - oneplus 3t -> وان پلاس 3T
  - oneplus 5 -> وان پلاس 5
  - oneplus 5t -> وان پلاس 5T
  - oneplus 6 -> وان پلاس 6
  - oneplus 6t -> وان پلاس 6T
  - oneplus 6t mclaren -> وان پلاس 6T McLaren
  - oneplus 7 -> وان پلاس 7
  - oneplus 7 pro -> وان پلاس 7 Pro
  - oneplus 7 pro 5g -> وان پلاس 7 Pro 5G
  - oneplus 7t -> وان پلاس 7T
  - oneplus 7t pro -> وان پلاس 7T Pro
  - oneplus 7t pro 5g mclaren -> وان پلاس 7T Pro 5G McLaren
  - oneplus 8 5g (t-mobile) -> وان پلاس 8 5G (T-Mobile)
  - oneplus 8 5g uw (verizon) -> وان پلاس 8 5G UW (Verizon)
  - oneplus 8 -> وان پلاس 8
  - oneplus 8 pro -> وان پلاس 8 Pro
  - oneplus nord -> وان پلاس Nord
  - oneplus 8t -> وان پلاس 8T
  - oneplus 8t+ 5g -> وان پلاس 8T+ 5G
  - oneplus nord n100 -> وان پلاس Nord N100
  - oneplus nord n10 5g -> وان پلاس Nord N10 5G
  - oneplus 9 -> وان پلاس 9
  - oneplus 9 pro -> وان پلاس 9 Pro
  - oneplus 9r -> وان پلاس 9R
  - oneplus nord ce 5g -> وان پلاس Nord CE 5G
  - oneplus nord n200 5g -> وان پلاس Nord N200 5G
  - oneplus nord 2 5g -> وان پلاس Nord 2 5G
  - oneplus 9rt 5g -> وان پلاس 9RT 5G
  - oneplus 10 pro -> وان پلاس 10 پرو
  - oneplus 10r -> وان پلاس 10R
  - oneplus 10r 150w -> وان پلاس 10R 150W
  - oneplus 10t -> وان پلاس 10T
  - oneplus ace pro -> وان پلاس Ace پرو
  - oneplus nord 2t -> وان پلاس نورد 2T
  - oneplus nord ce 2 lite 5g -> وان پلاس Nord CE 2 Lite 5G
  - oneplus nord n20 5g -> وان پلاس نورد N20 5G
  - oneplus nord n20 se -> وان پلاس نورد N20 SE
  - oneplus nord ce 2 5g -> وان پلاس Nord CE 2 5G
  - oneplus ace -> وان پلاس Ace
  - oneplus ace racing -> وان پلاس Ace Racing
  - oppo -> اوپو
  - oppo a95 5g -> اوپو A95 5G
  - oppo r811 real -> اوپو R811 Real
  - oppo r817 real -> اوپو R817 Real
  - oppo u705t ulike 2 -> اوپو U705T Ulike 2
  - oppo find 5 -> اوپو Find 5
  - oppo r821t find muse -> اوپو R821T FInd Muse
  - oppo r815t clover -> اوپو R815T Clover
  - oppo r819 -> اوپو R819
  - oppo n1 -> اوپو N1
  - oppo r1 r829t -> اوپو R1 R829T
  - oppo find 5 mini -> اوپو Find 5 Mini
  - oppo neo -> اوپو Neo
  - oppo find 7 -> اوپو Find 7
  - oppo find 7a -> اوپو Find 7a
  - oppo r1s -> اوپو R1S
  - oppo r1001 joy -> اوپو R1001 Joy
  - oppo r2001 yoyo -> اوپو R2001 Yoyo
  - oppo r3 -> اوپو R3
  - oppo n1 mini -> اوپو N1 mini
  - oppo neo 3 -> اوپو Neo 3
  - oppo neo 5 -> اوپو Neo 5
  - oppo n3 -> اوپو N3
  - oppo r5 -> اوپو R5
  - oppo mirror 3 -> اوپو Mirror 3
  - oppo r1x -> اوپو R1x
  - oppo u3 -> اوپو U3
  - oppo a31 (2015) -> اوپو A31 (2015)
  - oppo joy plus -> اوپو Joy Plus
  - oppo neo 5s -> اوپو Neo 5s
  - oppo r7 -> اوپو R7
  - oppo r7 plus -> اوپو R7 Plus
  - oppo joy 3 -> اوپو Joy 3
  - oppo neo 5 (2015) -> اوپو Neo 5 (2015)
  - oppo mirror 5 -> اوپو Mirror 5
  - oppo mirror 5s -> اوپو Mirror 5s
  - oppo r5s -> اوپو R5s
  - oppo r7 lite -> اوپو R7 lite
  - oppo neo 7 -> اوپو Neo 7
  - oppo a33 (2015) -> اوپو A33 (2015)
  - oppo a53 (2015) -> اوپو A53 (2015)
  - oppo f1 -> اوپو F1
  - oppo f1 plus -> اوپو F1 Plus
  - oppo r9 plus -> اوپو R9 Plus
  - oppo a37 -> اوپو A37
  - oppo a59 -> اوپو A59
  - oppo f1s -> اوپو F1s
  - oppo a57 (2016) -> اوپو A57 (2016)
  - oppo r9s -> اوپو R9s
  - oppo r9s plus -> اوپو R9s Plus
  - oppo a57 -> اوپو A57
  - oppo a39 -> اوپو A39
  - oppo f3 plus -> اوپو F3 Plus
  - oppo a77 (mediatek) -> اوپو A77 (Mediatek)
  - oppo f3 -> اوپو F3
  - oppo a77 (2017) -> اوپو A77 (2017)
  - oppo r11 -> اوپو R11
  - oppo r11 plus -> اوپو R11 Plus
  - oppo a77 -> اوپو A77
  - oppo a71 -> اوپو A71
  - oppo f5 -> اوپو F5
  - oppo r11s -> اوپو R11s
  - oppo f5 youth -> اوپو F5 Youth
  - oppo r11s plus -> اوپو R11s Plus
  - oppo a83 -> اوپو A83
  - oppo a71 (2018) -> اوپو A71 (2018)
  - oppo a1 -> اوپو A1
  - oppo f7 -> اوپو F7
  - oppo r15 -> اوپو R15
  - oppo r15 pro -> اوپو R15 Pro
  - oppo a3 -> اوپو A3
  - oppo f7 youth -> اوپو F7 Youth
  - oppo find x -> اوپو Find X
  - oppo find x lamborghini -> اوپو Find X Lamborghini
  - oppo a3s -> اوپو A3s
  - oppo a5 (ax5) -> اوپو A5 (AX5)
  - oppo f9 (f9 pro) -> اوپو F9 (F9 Pro)
  - oppo r17 -> اوپو R17
  - oppo rx17 pro -> اوپو RX17 Pro
  - oppo a7x -> اوپو A7x
  - oppo k1 -> اوپو K1
  - oppo r15x -> اوپو R15x
  - oppo a7 -> اوپو A7
  - oppo rx17 neo -> اوپو RX17 Neo
  - oppo a5s (ax5s) -> اوپو A5s (AX5s)
  - oppo f11 -> اوپو F11
  - oppo f11 pro -> اوپو F11 Pro
  - oppo reno -> اوپو Reno
  - oppo a1k -> اوپو A1k
  - oppo a7n -> اوپو A7n
  - oppo a9 -> اوپو A9
  - oppo a9x -> اوپو A9x
  - oppo reno 10x zoom -> اوپو Reno 10x zoom
  - oppo reno 5g -> اوپو Reno 5G
  - oppo reno z -> اوپو Reno Z
  - oppo k3 -> اوپو K3
  - oppo reno2 -> اوپو Reno2
  - oppo reno2 f -> اوپو Reno2 F
  - oppo reno2 z -> اوپو Reno2 Z
  - oppo a5 (2020) -> اوپو A5 (2020)
  - oppo a9 (2020) -> اوپو A9 (2020)
  - oppo k5 -> اوپو K5
  - oppo reno a -> اوپو Reno A
  - oppo a11 -> اوپو A11
  - oppo reno ace -> اوپو Reno Ace
  - oppo a8 -> اوپو A8
  - oppo a72 5g -> اوپو A72 5G
  - oppo a73 5g -> اوپو A73 5G
  - oppo a91 -> اوپو A91
  - oppo k7x -> اوپو K7x
  - oppo reno3 -> اوپو Reno3 5G
  - oppo reno3 5g -> اوپو Reno3 5G
  - oppo reno3 pro 5g -> اوپو Reno3 Pro 5G
  - oppo reno3 youth -> اوپو Reno3 Youth
  - oppo reno4 f -> اوپو Reno4 F
  - oppo reno4 lite -> اوپو Reno4 Lite
  - oppo reno4 pro -> اوپو Reno4 پرو
  - oppo reno5 4g -> اوپو Reno5 4G
  - oppo f15 -> اوپو F15
  - oppo a31 -> اوپو A31
  - oppo find x2 -> اوپو Find X2
  - oppo find x2 pro -> اوپو Find X2 Pro
  - oppo reno3 pro -> اوپو Reno3 Pro
  - oppo a12 -> اوپو A12
  - oppo a12e -> اوپو A12e
  - oppo a52 -> اوپو A52
  - oppo a72 -> اوپو A72
  - oppo a92s -> اوپو A92s
  - oppo ace2 -> اوپو Ace2
  - oppo find x2 lite -> اوپو Find X2 Lite
  - oppo find x2 neo -> اوپو Find X2 Neo
  - oppo a92 -> اوپو A92
  - oppo a11k -> اوپو A11k
  - oppo reno4 5g -> اوپو Reno4 5G
  - oppo reno4 pro 5g -> اوپو Reno4 Pro 5G
  - oppo a12s -> اوپو A12s
  - oppo reno4 -> اوپو Reno4
  - oppo a53 -> اوپو A53
  - oppo k7 5g -> اوپو K7 5G
  - oppo a32 -> اوپو A32
  - oppo a33 (2020) -> اوپو A33 (2020)
  - oppo f17 -> اوپو F17
  - oppo f17 pro -> اوپو F17 Pro
  - oppo reno4 se -> اوپو Reno4 SE
  - oppo reno4 z 5g -> اوپو Reno4 Z 5G
  - oppo a15 -> اوپو A15
  - oppo a53s -> اوپو A53s
  - oppo a73 -> اوپو A73
  - oppo a93 -> اوپو A93
  - oppo a15s -> اوپو A15s
  - oppo a16s -> اوپو A16s
  - oppo a53 5g -> اوپو A53 5G
  - oppo a53s 5g -> اوپو A53s 5G
  - oppo a54 5g -> اوپو A54 5G
  - oppo a54s -> اوپو A54s
  - oppo a55 -> اوپو A55
  - oppo a95 -> اوپو A95
  - oppo find n -> اوپو Find N
  - oppo k9 -> اوپو K9
  - oppo k9x -> اوپو K9x
  - oppo reno5 5g -> اوپو Reno5 5G
  - oppo reno5 k -> اوپو Reno5 K
  - oppo reno5 lite -> اوپو Reno5 Lite
  - oppo reno5 pro 5g -> اوپو Reno5 Pro 5G
  - oppo reno5 pro+ 5g -> اوپو Reno5 Pro+ 5G
  - oppo reno7 pro 5g -> اوپو Reno7 پرو 5G
  - oppo reno7 se 5g -> اوپو Reno7 SE 5G
  - oppo a55 5g -> اوپو A55 5G
  - oppo a93 5g -> اوپو A93 5G
  - oppo a54 -> اوپو A54
  - oppo a94 -> اوپو A94
  - oppo f19 pro -> اوپو F19 Pro
  - oppo f19 pro+ 5g -> اوپو F19 Pro+ 5G
  - oppo find x3 -> اوپو Find X3
  - oppo find x3 lite -> اوپو Find X3 Lite
  - oppo find x3 neo -> اوپو Find X3 Neo
  - oppo find x3 pro -> اوپو Find X3 Pro
  - oppo reno5 f -> اوپو Reno5 F
  - oppo a35 -> اوپو A35
  - oppo a74 -> اوپو A74
  - oppo a74 5g -> اوپو A74 5G
  - oppo a94 5g -> اوپو A94 5G
  - oppo f19 -> اوپو F19
  - oppo reno5 z -> اوپو Reno5 Z
  - oppo reno6 5g -> اوپو Reno6 5G
  - oppo reno6 pro 5g -> اوپو Reno6 Pro 5G
  - oppo reno6 pro+ 5g -> اوپو Reno6 Pro+ 5G
  - oppo a16 -> اوپو A16
  - oppo a93s 5g -> اوپو A93s 5G
  - oppo reno6 -> اوپو Reno6
  - oppo reno6 z -> اوپو Reno6 Z
  - oppo f19s -> اوپو F19s
  - oppo k9 pro -> اوپو K9 Pro
  - oppo reno6 pro 5g (snapdragon) -> اوپو Reno6 Pro 5G (Snapdragon)
  - oppo a56 5g -> اوپو A56 5G
  - oppo k9s -> اوپو K9s
  - oppo a16k -> اوپو A16K
  - oppo reno7 5g (china) -> اوپو Reno7 5G (China)
  - oppo a11s -> اوپو A11s
  - oppo a57e -> اوپو A57e
  - oppo a57s -> اوپو A57s
  - oppo a77 4g -> اوپو A77 4G
  - oppo a96 (china) -> اوپو A96 (China)
  - oppo a97 -> اوپو A97
  - oppo f21 pro -> اوپو F21 پرو
  - oppo f21 pro 5g -> اوپو F21 پرو 5G
  - oppo find x5 lite -> اوپو فایند X5 لایت
  - oppo find x5 pro -> اوپو فایند X5 پرو
  - oppo k10 5g -> اوپو K10 5G
  - oppo k10 5g (china) -> اوپو K10 5G (China)
  - oppo k10 pro -> اوپو K10 پرو
  - oppo k10x -> اوپو K10x
  - oppo reno6 lite -> اوپو Reno6 لایت
  - oppo reno7 lite -> اوپو Reno7 لایت
  - oppo reno7 z 5g -> اوپو Reno7 Z 5G
  - oppo reno8 4g -> اوپو Reno8 4G
  - oppo reno8 (china) -> اوپو Reno8 (China)
  - oppo reno8 lite -> اوپو Reno8 لایت
  - oppo reno8 pro (china) -> اوپو Reno8 Pro (China)
  - oppo reno8 z -> اوپو Reno8 Z
  - oppo a36 -> اوپو A36
  - oppo a96 -> اوپو A96
  - oppo a76 -> اوپو A76
  - oppo find x5 -> اوپو Find X5
  - oppo reno7 5g -> اوپو Reno7 5G
  - oppo a16e -> اوپو A16e
  - oppo k10 -> اوپو K10
  - oppo reno7 -> اوپو Reno7
  - oppo a55s -> اوپو A55s
  - oppo a57 4g -> اوپو A57 4G
  - oppo reno8 -> اوپو Reno8
  - oppo reno8 pro -> اوپو Reno8 Pro
  - oppo reno8 pro+ -> اوپو Reno8 Pro+
  - panasonic -> پاناسونیک
  - panasonic p11 -> پاناسونیک P11
  - panasonic t11 -> پاناسونیک T11
  - panasonic t21 -> پاناسونیک T21
  - panasonic p51 -> پاناسونیک P51
  - panasonic t31 -> پاناسونیک T31
  - panasonic p81 -> پاناسونیک P81
  - panasonic eluga u -> پاناسونیک Eluga U
  - panasonic p61 -> پاناسونیک P61
  - panasonic t41 -> پاناسونیک T41
  - panasonic eluga a -> پاناسونیک Eluga A
  - panasonic p41 -> پاناسونیک P41
  - panasonic lumix smart camera cm1 -> پاناسونیک Lumix Smart Camera CM1
  - panasonic t40 -> پاناسونیک T40
  - panasonic eluga i -> پاناسونیک Eluga I
  - panasonic eluga s -> پاناسونیک Eluga S
  - panasonic p55 -> پاناسونیک P55
  - panasonic eluga u2 -> پاناسونیک Eluga U2
  - panasonic eluga l 4g -> پاناسونیک Eluga L 4G
  - panasonic eluga s mini -> پاناسونیک Eluga S mini
  - panasonic eluga z -> پاناسونیک Eluga Z
  - panasonic eluga i2 -> پاناسونیک Eluga I2
  - panasonic eluga icon -> پاناسونیک Eluga Icon
  - panasonic eluga l2 -> پاناسونیک Eluga L2
  - panasonic t45 -> پاناسونیک T45
  - panasonic eluga switch -> پاناسونیک Eluga Switch
  - panasonic eluga mark -> پاناسونیک Eluga Mark
  - panasonic eluga turbo -> پاناسونیک Eluga Turbo
  - panasonic t50 -> پاناسونیک T50
  - panasonic eluga a2 -> پاناسونیک Eluga A2
  - panasonic eluga arc -> پاناسونیک Eluga Arc
  - panasonic eluga i3 -> پاناسونیک Eluga I3
  - panasonic eluga i2 (2016) -> پاناسونیک Eluga I2 (2016)
  - panasonic eluga note -> پاناسونیک Eluga Note
  - panasonic eluga arc 2 -> پاناسونیک Eluga Arc 2
  - panasonic p77 -> پاناسونیک P77
  - panasonic eluga tapp -> پاناسونیک Eluga Tapp
  - panasonic eluga mark 2 -> پاناسونیک Eluga Mark 2
  - panasonic p88 -> پاناسونیک P88
  - panasonic eluga pulse -> پاناسونیک Eluga Pulse
  - panasonic eluga pulse x -> پاناسونیک Eluga Pulse X
  - panasonic eluga ray max -> پاناسونیک Eluga Ray Max
  - panasonic eluga ray x -> پاناسونیک Eluga Ray X
  - panasonic eluga i3 mega -> پاناسونیک Eluga i3 Mega
  - panasonic eluga ray -> پاناسونیک Eluga Ray
  - panasonic p85 -> پاناسونیک P85
  - panasonic p55 max -> پاناسونیک P55 Max
  - panasonic eluga a3 -> پاناسونیک Eluga A3
  - panasonic eluga a3 pro -> پاناسونیک Eluga A3 Pro
  - panasonic eluga i2 activ -> پاناسونیک Eluga I2 Activ
  - panasonic eluga i4 -> پاناسونیک Eluga I4
  - panasonic eluga ray 500 -> پاناسونیک Eluga Ray 500
  - panasonic eluga ray 700 -> پاناسونیک Eluga Ray 700
  - panasonic p9 -> پاناسونیک P9
  - panasonic p99 -> پاناسونیک P99
  - panasonic eluga c -> پاناسونیک Eluga C
  - panasonic eluga a4 -> پاناسونیک Eluga A4
  - panasonic eluga i5 -> پاناسونیک Eluga I5
  - panasonic p91 -> پاناسونیک P91
  - panasonic eluga i9 -> پاناسونیک Eluga I9
  - panasonic p100 -> پاناسونیک P100
  - panasonic p101 -> پاناسونیک P101
  - panasonic eluga i7 -> پاناسونیک Eluga I7
  - panasonic eluga ray 550 -> پاناسونیک Eluga Ray 550
  - panasonic p95 -> پاناسونیک P95
  - panasonic p90 -> پاناسونیک P90
  - panasonic eluga x1 pro -> پاناسونیک Eluga X1 Pro
  - panasonic eluga ray 530 -> پاناسونیک Eluga Ray 530
  - panasonic eluga ray 600 -> پاناسونیک Eluga Ray 600
  - panasonic eluga z1 pro -> پاناسونیک Eluga Z1 Pro
  - panasonic p85 nxt -> پاناسونیک P85 Nxt
  - panasonic eluga ray 800 -> پاناسونیک Eluga Ray 800
  - panasonic eluga i7 (2019) -> پاناسونیک Eluga I7 (2019)
  - philips -> فیلیپس
  - philips w8355 -> فیلیپس W8355
  - philips t939 -> فیلیپس T939
  - philips w8560 -> فیلیپس W8560
  - philips w8568 -> فیلیپس W8568
  - philips w8555 -> فیلیپس W8555
  - philips w7555 -> فیلیپس W7555
  - philips w9588 -> فیلیپس W9588
  - philips w8578 -> فیلیپس W8578
  - philips s308 -> فیلیپس S308
  - philips w6610 -> فیلیپس W6610
  - philips s396 -> فیلیپس S396
  - philips s309 -> فیلیپس S309
  - philips i908 -> فیلیپس I908
  - philips v526 -> فیلیپس V526
  - philips i928 -> فیلیپس I928
  - philips s337 -> فیلیپس S337
  - philips s616 -> فیلیپس S616
  - philips v377 -> فیلیپس V377
  - philips v787 -> فیلیپس V787
  - philips ph1 -> فیلیپس PH1
  - philips ph2 -> فیلیپس PH2
  - prestigio -> پرستیژ
  - prestigio multiphone 3400 duo -> پرستیژ MultiPhone 3400 Duo
  - prestigio multiphone 3540 duo -> پرستیژ MultiPhone 3540 Duo
  - prestigio multiphone 4040 duo -> پرستیژ MultiPhone 4040 Duo
  - prestigio multiphone 4044 duo -> پرستیژ MultiPhone 4044 Duo
  - prestigio multiphone 4055 duo -> پرستیژ MultiPhone 4055 Duo
  - prestigio multiphone 4300 duo -> پرستیژ MultiPhone 4300 Duo
  - prestigio multiphone 4322 duo -> پرستیژ MultiPhone 4322 Duo
  - prestigio multiphone 4500 duo -> پرستیژ MultiPhone 4500 Duo
  - prestigio multiphone 4505 duo -> پرستیژ MultiPhone 4505 Duo
  - prestigio multiphone 5000 duo -> پرستیژ MultiPhone 5000 Duo
  - prestigio multiphone 5044 duo -> پرستیژ MultiPhone 5044 Duo
  - prestigio multiphone 5300 duo -> پرستیژ MultiPhone 5300 Duo
  - prestigio multiphone 5400 duo -> پرستیژ MultiPhone 5400 Duo
  - prestigio multiphone 5430 duo -> پرستیژ MultiPhone 5430 Duo
  - prestigio multiphone 5450 duo -> پرستیژ MultiPhone 5450 Duo
  - prestigio multiphone 5451 duo -> پرستیژ MultiPhone 5451 Duo
  - prestigio multiphone 5500 duo -> پرستیژ MultiPhone 5500 Duo
  - prestigio multiphone 5501 duo -> پرستیژ MultiPhone 5501 Duo
  - prestigio multiphone 5503 duo -> پرستیژ MultiPhone 5503 Duo
  - prestigio multiphone 5504 duo -> پرستیژ MultiPhone 5504 Duo
  - prestigio multiphone 5508 duo -> پرستیژ MultiPhone 5508 Duo
  - prestigio multiphone 7500 -> پرستیژ MultiPhone 7500
  - prestigio multiphone 7600 duo -> پرستیژ MultiPhone 7600 Duo
  - prestigio multiphone 8400 duo -> پرستیژ MultiPhone 8400 Duo
  - prestigio multiphone 8500 duo -> پرستیژ MultiPhone 8500 Duo
  - razer -> ریزر
  - razer phone -> ریزر Phone
  - razer phone 2 -> ریزر Phone 2
  - realme -> ریلمی
  - realme 8 5g -> ریلمی 8 5G
  - realme x9 -> ریلمی X9
  - realme 1 -> ریلمی 1
  - realme 2 -> ریلمی 2
  - realme 2 pro -> ریلمی 2 Pro
  - realme c1 -> ریلمی C1
  - realme u1 -> ریلمی U1
  - realme 3 pro -> ریلمی 3 Pro
  - realme 5 -> ریلمی 5
  - realme 5 pro -> ریلمی 5 Pro
  - realme 5s -> ریلمی 5s
  - realme c1 (2019) -> ریلمی C1 (2019)
  - realme c2 -> ریلمی C2
  - realme x2 -> ریلمی X2
  - realme x2 pro -> ریلمی X2 Pro
  - realme xt -> ریلمی XT
  - realme 3 -> ریلمی 3
  - realme x -> ریلمی X
  - realme 3i -> ریلمی 3i
  - realme q -> ریلمی Q
  - realme c2 2020 -> ریلمی C2 2020
  - realme 5i -> ریلمی 5i
  - realme 6 -> ریلمی 6
  - realme 6i -> ریلمی 6i
  - realme 6i (india) -> ریلمی 6i (India)
  - realme 6 pro -> ریلمی 6 Pro
  - realme 6s -> ریلمی 6S
  - realme 7 (asia) -> ریلمی 7 (Asia)
  - realme 7i -> ریلمی 7i
  - realme 7i (global) -> ریلمی 7i گلوبال
  - realme 7 pro -> ریلمی 7 Pro
  - realme c11 -> ریلمی C11
  - realme c12 -> ریلمی C12
  - realme c15 -> ریلمی C15
  - realme c15 qualcomm edition -> ریلمی C15 Qualcomm Edition
  - realme c17 -> ریلمی C17
  - realme c2s -> ریلمی C2s
  - realme c3 -> ریلمی C3
  - realme c3 (3 cameras) -> ریلمی C3 (3 cameras)
  - realme c3i -> ریلمی C3i
  - realme narzo -> ریلمی Narzo
  - realme narzo 10 -> ریلمی Narzo 10
  - realme narzo 10a -> ریلمی Narzo 10A
  - realme narzo 20 -> ریلمی Narzo 20
  - realme narzo 20a -> ریلمی Narzo 20A
  - realme narzo 20 pro -> ریلمی Narzo 20 پرو
  - realme q2 -> ریلمی Q2
  - realme q2i -> ریلمی Q2i
  - realme q2 pro -> ریلمی Q2 Pro
  - realme v3 -> ریلمی V3
  - realme v5 5g -> ریلمی V5 5G
  - realme x3 -> ریلمی X3
  - realme x3 superzoom -> ریلمی X3 SuperZoom
  - realme x50 5g -> ریلمی X50 5G
  - realme x50 5g (china) -> ریلمی X50 5G (China)
  - realme x50m 5g -> ریلمی X50m 5G
  - realme x50 pro 5g -> ریلمی X50 Pro 5G
  - realme x50 pro player -> ریلمی X50 پرو Player
  - realme x7 -> ریلمی X7
  - realme x7 pro -> ریلمی X7 Pro
  - realme 7 (global) -> ریلمی 7 (Global)
  - realme 7 5g -> ریلمی 7 5G
  - realme c20a -> ریلمی C20A
  - realme gt neo flash -> ریلمی GT Neo Flash
  - realme q3 5g -> ریلمی Q3 5G
  - realme q3i 5g -> ریلمی Q3i 5G
  - realme q3 pro 5g -> ریلمی Q3 پرو 5G
  - realme v11 5g -> ریلمی V11 5G
  - realme v15 5g -> ریلمی V15 5G
  - realme x7 (india) -> ریلمی X7 (India)
  - realme x7 max 5g -> ریلمی X7 مکس 5G
  - realme c20 -> ریلمی C20
  - realme narzo 30a -> ریلمی Narzo 30A
  - realme narzo 30 pro 5g -> ریلمی Narzo 30 Pro 5G
  - realme 8 -> ریلمی 8
  - realme 8 pro -> ریلمی 8 Pro
  - realme c21 -> ریلمی C21
  - realme c25 -> ریلمی C25
  - realme gt 5g -> ریلمی GT 5G
  - realme gt neo -> ریلمی GT Neo
  - realme v13 5g -> ریلمی V13 5G
  - realme x7 pro ultra -> ریلمی X7 Pro Ultra
  - realme narzo 30 -> ریلمی Narzo 30
  - realme narzo 30 5g -> ریلمی Narzo 30 5G
  - realme q3 pro carnival -> ریلمی Q3 Pro Carnival
  - realme c11 (2021) -> ریلمی C11 (2021)
  - realme c21y -> ریلمی C21Y
  - realme c25s -> ریلمی C25s
  - realme gt explorer master -> ریلمی GT Explorer Master
  - realme gt master -> ریلمی GT Master
  - realme 8i -> ریلمی 8i
  - realme 8s 5g -> ریلمی 8s 5G
  - realme c25y -> ریلمی C25Y
  - realme gt neo2 -> ریلمی GT Neo2
  - realme narzo 50a -> ریلمی Narzo 50A
  - realme narzo 50i -> ریلمی Narzo 50i
  - realme v11s 5g -> ریلمی V11s 5G
  - realme gt neo2t -> ریلمی GT Neo2T
  - realme q3s -> ریلمی Q3s
  - realme q3t -> ریلمی Q3t
  - realme 9 5g (india) -> ریلمی 9 5G (India)
  - realme 9 5g speed -> ریلمی 9 5G اسپید
  - realme 9 pro -> ریلمی 9 Pro
  - realme 9 pro+ -> ریلمی 9 Pro+
  - realme c30s -> ریلمی C30s
  - realme c33 -> ریلمی C33
  - realme gt2 explorer master -> ریلمی GT2 Explorer Master
  - realme gt neo 3 -> ریلمی GT Neo 3
  - realme narzo 50 5g -> ریلمی Narzo 50 5G
  - realme v23 -> ریلمی V23
  - realme 9i -> ریلمی 9i
  - realme gt2 -> ریلمی GT2
  - realme gt2 pro -> ریلمی GT2 Pro
  - realme c35 -> ریلمی C35
  - realme narzo 50 -> ریلمی Narzo 50
  - realme 9 5g -> ریلمی 9 5G
  - realme c31 -> ریلمی C31
  - realme gt neo3 -> ریلمی GT Neo3
  - realme narzo 50a prime -> ریلمی Narzo 50A Prime
  - realme v25 -> ریلمی V25
  - realme 9 -> ریلمی 9
  - realme q5 -> ریلمی Q5
  - realme q5i -> ریلمی Q5i
  - realme q5 pro -> ریلمی Q5 Pro
  - realme narzo 50 pro -> ریلمی Narzo 50 Pro
  - realme c30 -> ریلمی C30
  - realme gt neo 3t -> ریلمی GT Neo 3T
  - realme narzo 50i prime -> ریلمی Narzo 50i Prime
  - samsung -> سامسونگ
  - samsung galaxy a72 5g -> سامسونگ گلکسی A72 5G
  - samsung galaxy a91 -> سامسونگ Galaxy A91
  - samsung galaxy c10 -> سامسونگ Galaxy C10
  - samsung galaxy grand 3 -> سامسونگ Galaxy Grand 3
  - samsung galaxy j5 prime (2017) -> سامسونگ Galaxy J5 Prime (2017)
  - samsung galaxy m42 5g -> سامسونگ Galaxy M42 5G
  - samsung galaxy on5 (2016) -> سامسونگ Galaxy On5 (2016)
  - samsung galaxy s21 -> سامسونگ Galaxy S21
  - samsung galaxy s6 plus -> سامسونگ Galaxy S6 Plus
  - samsung galaxy s9 active -> سامسونگ Galaxy S9 Active
  - samsung galaxy z fold 2 5g -> سامسونگ Galaxy Z Fold 2 5G
  - samsung i9000 galaxy s -> سامسونگ I9000 Galaxy S
  - samsung galaxy ace s5830 -> سامسونگ Galaxy Ace S5830
  - samsung galaxy mini s5570 -> سامسونگ Galaxy Mini S5570
  - samsung m220l galaxy neo -> سامسونگ M220L Galaxy Neo
  - samsung galaxy reverb m950 -> سامسونگ Galaxy Reverb M950
  - samsung galaxy s ii skyrocket hd i757 -> سامسونگ Galaxy S II Skyrocket HD I757
  - samsung galaxy ace ii x s7560m -> سامسونگ Galaxy Ace II X S7560M
  - samsung galaxy note ii cdma -> سامسونگ Galaxy Note II CDMA
  - samsung galaxy pocket plus s5301 -> سامسونگ Galaxy Pocket plus S5301
  - samsung galaxy pop plus s5570i -> سامسونگ Galaxy Pop Plus S5570i
  - samsung galaxy note t879 -> سامسونگ Galaxy Note T879
  - samsung i9500 fraser -> سامسونگ I9500 Fraser
  - samsung galaxy ace advance s6800 -> سامسونگ Galaxy Ace Advance S6800
  - samsung galaxy ace duos s6802 -> سامسونگ Galaxy Ace Duos S6802
  - samsung galaxy s duos s7562 -> سامسونگ Galaxy S Duos S7562
  - samsung ativ s i8750 -> سامسونگ Ativ S I8750
  - samsung galaxy camera gc100 -> سامسونگ Galaxy Camera GC100
  - samsung galaxy rush m830 -> سامسونگ Galaxy Rush M830
  - samsung galaxy stellar 4g i200 -> سامسونگ Galaxy Stellar 4G I200
  - samsung galaxy s relay 4g t699 -> سامسونگ Galaxy S Relay 4G T699
  - samsung galaxy victory 4g lte l300 -> سامسونگ Galaxy Victory 4G LTE L300
  - samsung i9305 galaxy s iii -> سامسونگ I9305 Galaxy S III
  - samsung galaxy express i437 -> سامسونگ Galaxy Express I437
  - samsung galaxy music duos s6012 -> سامسونگ Galaxy Music Duos S6012
  - samsung galaxy music s6010 -> سامسونگ Galaxy Music S6010
  - samsung galaxy rugby pro i547 -> سامسونگ Galaxy Rugby Pro I547
  - samsung i8190 galaxy s iii mini -> سامسونگ I8190 Galaxy S III mini
  - samsung a997 rugby iii -> سامسونگ A997 Rugby III
  - samsung galaxy axiom r830 -> سامسونگ Galaxy Axiom R830
  - samsung galaxy discover s730m -> سامسونگ Galaxy Discover S730M
  - samsung galaxy premier i9260 -> سامسونگ Galaxy Premier I9260
  - samsung galaxy stratosphere ii i415 -> سامسونگ Galaxy Stratosphere II I415
  - samsung galaxy grand i9080 -> سامسونگ Galaxy Grand I9080
  - samsung galaxy grand i9082 -> سامسونگ Galaxy Grand I9082
  - samsung ativ odyssey i930 -> سامسونگ Ativ Odyssey I930
  - samsung e1272 -> سامسونگ E1272
  - samsung galaxy express i8730 -> سامسونگ Galaxy Express I8730
  - samsung galaxy pop shv-e220 -> سامسونگ Galaxy Pop SHV-E220
  - samsung galaxy s ii tv -> سامسونگ Galaxy S II TV
  - samsung i9105 galaxy s ii plus -> سامسونگ I9105 Galaxy S II Plus
  - samsung i9506 galaxy s4 -> سامسونگ I9506 Galaxy S4
  - samsung s7710 galaxy xcover 2 -> سامسونگ S7710 Galaxy Xcover 2
  - samsung galaxy fame s6810 -> سامسونگ Galaxy Fame S6810
  - samsung galaxy note 8.0 -> سامسونگ Galaxy Note 8.0
  - samsung galaxy young s6310 -> سامسونگ Galaxy Young S6310
  - samsung i9502 galaxy s4 -> سامسونگ I9502 Galaxy S4
  - samsung galaxy mega 5.8 i9150 -> سامسونگ Galaxy Mega 5.8 I9150
  - samsung galaxy mega 6.3 i9200 -> سامسونگ Galaxy Mega 6.3 I9200
  - samsung galaxy pocket neo s5310 -> سامسونگ Galaxy Pocket Neo S5310
  - samsung galaxy star s5280 -> سامسونگ Galaxy Star S5280
  - samsung galaxy trend ii duos s7572 -> سامسونگ Galaxy Trend II Duos S7572
  - samsung galaxy win i8550 -> سامسونگ Galaxy Win I8550
  - samsung galaxy core i8260 -> سامسونگ Galaxy Core I8260
  - samsung galaxy exhibit t599 -> سامسونگ Galaxy Exhibit T599
  - samsung galaxy s4 cdma -> سامسونگ Galaxy S4 CDMA
  - samsung i9190 galaxy s4 mini -> سامسونگ I9190 Galaxy S4 mini
  - samsung galaxy s4 zoom -> سامسونگ Galaxy S4 zoom
  - samsung i9295 galaxy s4 active -> سامسونگ I9295 Galaxy S4 Active
  - samsung galaxy prevail 2 -> سامسونگ Galaxy Prevail 2
  - samsung gravity q t289 -> سامسونگ Gravity Q T289
  - samsung galaxy note 3 -> سامسونگ Galaxy Note 3
  - samsung galaxy express 2 -> سامسونگ Galaxy Express 2
  - samsung galaxy fresh s7390 -> سامسونگ Galaxy Fresh S7390
  - samsung galaxy light -> سامسونگ Galaxy Light
  - samsung galaxy round g910s -> سامسونگ Galaxy Round G910S
  - samsung galaxy star pro s7260 -> سامسونگ Galaxy Star Pro S7260
  - samsung i9230 galaxy golden -> سامسونگ I9230 Galaxy Golden
  - samsung galaxy grand 2 -> سامسونگ Galaxy Grand 2
  - samsung galaxy s duos 2 s7582 -> سامسونگ Galaxy S Duos 2 S7582
  - samsung galaxy core advance -> سامسونگ Galaxy Core Advance
  - samsung galaxy s4 active lte-a -> سامسونگ Galaxy S4 Active LTE-A
  - samsung galaxy win pro g3812 -> سامسونگ Galaxy Win Pro G3812
  - samsung galaxy grand neo -> سامسونگ Galaxy Grand Neo
  - samsung galaxy note 3 neo -> سامسونگ Galaxy Note 3 Neo
  - samsung galaxy note 3 neo duos -> سامسونگ Galaxy Note 3 Neo Duos
  - samsung galaxy note 4 (usa) -> سامسونگ Galaxy Note 4 (USA)
  - samsung galaxy note pro 12.2 3g -> سامسونگ Galaxy Note Pro 12.2 3G
  - samsung galaxy core lte -> سامسونگ Galaxy Core LTE
  - samsung galaxy s5 -> سامسونگ Galaxy S5
  - samsung galaxy s5 (usa) -> سامسونگ Galaxy S5 (USA)
  - samsung galaxy star trios s5283 -> سامسونگ Galaxy Star Trios S5283
  - samsung g3812b galaxy s3 slim -> سامسونگ G3812B Galaxy S3 Slim
  - samsung galaxy s5 (octa-core) -> سامسونگ Galaxy S5 (octa-core)
  - samsung i8200 galaxy s iii mini ve -> سامسونگ I8200 Galaxy S III mini VE
  - samsung ativ se -> سامسونگ ATIV SE
  - samsung galaxy ace style -> سامسونگ Galaxy Ace Style
  - samsung galaxy k zoom -> سامسونگ Galaxy K zoom
  - samsung galaxy s5 active -> سامسونگ Galaxy S5 Active
  - samsung galaxy ace 4 -> سامسونگ Galaxy Ace 4
  - samsung galaxy ace 4 lte g313 -> سامسونگ Galaxy Ace 4 LTE G313
  - samsung galaxy core ii -> سامسونگ Galaxy Core II
  - samsung galaxy core lite lte -> سامسونگ Galaxy Core Lite LTE
  - samsung galaxy s5 duos -> سامسونگ Galaxy S5 Duos
  - samsung galaxy s5 lte-a g906s -> سامسونگ Galaxy S5 LTE-A G906S
  - samsung galaxy s5 mini -> سامسونگ Galaxy S5 mini
  - samsung galaxy s5 sport -> سامسونگ Galaxy S5 Sport
  - samsung galaxy star 2 -> سامسونگ Galaxy Star 2
  - samsung galaxy young 2 -> سامسونگ Galaxy Young 2
  - samsung i9301i galaxy s3 neo -> سامسونگ I9301I Galaxy S3 Neo
  - samsung galaxy ace nxt -> سامسونگ Galaxy Ace NXT
  - samsung galaxy avant -> سامسونگ Galaxy Avant
  - samsung galaxy star 2 plus -> سامسونگ Galaxy Star 2 Plus
  - samsung galaxy alpha -> سامسونگ Galaxy Alpha
  - samsung galaxy alpha (s801) -> سامسونگ Galaxy Alpha (S801)
  - samsung galaxy s5 lte-a g901f -> سامسونگ Galaxy S5 LTE-A G901F
  - samsung galaxy s5 mini duos -> سامسونگ Galaxy S5 mini Duos
  - samsung galaxy s duos 3 -> سامسونگ Galaxy S Duos 3
  - samsung galaxy ace style lte g357 -> سامسونگ Galaxy Ace Style LTE G357
  - samsung galaxy grand prime -> سامسونگ Galaxy Grand Prime
  - samsung galaxy mega 2 -> سامسونگ Galaxy Mega 2
  - samsung galaxy note 4 -> سامسونگ Galaxy Note 4
  - samsung galaxy note edge -> سامسونگ Galaxy Note Edge
  - samsung galaxy v -> سامسونگ Galaxy V
  - samsung galaxy a3 -> سامسونگ Galaxy A3
  - samsung galaxy a3 duos -> سامسونگ Galaxy A3 Duos
  - samsung galaxy a5 -> سامسونگ Galaxy A5
  - samsung galaxy a5 duos -> سامسونگ Galaxy A5 Duos
  - samsung galaxy note 4 duos -> سامسونگ Galaxy Note 4 Duos
  - samsung galaxy s5 plus -> سامسونگ Galaxy S5 Plus
  - samsung galaxy core lte g386w -> سامسونگ Galaxy Core LTE G386W
  - samsung galaxy core prime -> سامسونگ Galaxy Core Prime
  - samsung galaxy a7 duos -> سامسونگ Galaxy A7 Duos
  - samsung galaxy e5 -> سامسونگ Galaxy E5
  - samsung galaxy e7 -> سامسونگ Galaxy E7
  - samsung galaxy grand max -> سامسونگ Galaxy Grand Max
  - samsung galaxy j1 -> سامسونگ Galaxy J1
  - samsung galaxy j1 4g -> سامسونگ Galaxy J1 4G
  - samsung z1 -> سامسونگ Z1
  - samsung galaxy s6 -> سامسونگ Galaxy S6
  - samsung galaxy s6 edge -> سامسونگ Galaxy S6 edge
  - samsung galaxy s6 (usa) -> سامسونگ Galaxy S6 (USA)
  - samsung galaxy xcover 3 -> سامسونگ Galaxy Xcover 3
  - samsung galaxy j5 -> سامسونگ Galaxy J5
  - samsung galaxy j7 -> سامسونگ Galaxy J7
  - samsung galaxy s4 mini i9195i -> سامسونگ Galaxy S4 mini I9195I
  - samsung galaxy s6 active -> سامسونگ Galaxy S6 active
  - samsung galaxy s6 duos -> سامسونگ Galaxy S6 Duos
  - samsung galaxy a8 -> سامسونگ Galaxy A8
  - samsung galaxy folder -> سامسونگ Galaxy Folder
  - samsung galaxy v plus -> سامسونگ Galaxy V Plus
  - samsung xcover 550 -> سامسونگ Xcover 550
  - samsung galaxy a8 duos -> سامسونگ Galaxy A8 Duos
  - samsung galaxy j1 ace -> سامسونگ Galaxy J1 Ace
  - samsung galaxy note5 -> سامسونگ Galaxy Note5
  - samsung galaxy note5 duos -> سامسونگ Galaxy Note5 Duos
  - samsung galaxy note5 (usa) -> سامسونگ Galaxy Note5 (USA)
  - samsung galaxy s5 neo -> سامسونگ Galaxy S5 Neo
  - samsung galaxy s6 edge+ -> سامسونگ Galaxy S6 edge+
  - samsung galaxy s6 edge+ duos -> سامسونگ Galaxy S6 edge+ Duos
  - samsung galaxy j2 -> سامسونگ Galaxy J2
  - samsung galaxy on5 -> سامسونگ Galaxy On5
  - samsung galaxy on7 -> سامسونگ Galaxy On7
  - samsung galaxy view -> سامسونگ Galaxy View
  - samsung z3 -> سامسونگ Z3
  - samsung galaxy a3 (2016) -> سامسونگ Galaxy A3 (2016)
  - samsung galaxy a5 (2016) -> سامسونگ Galaxy A5 (2016)
  - samsung galaxy a7 (2016) -> سامسونگ Galaxy A7 (2016)
  - samsung galaxy j1 (2016) -> سامسونگ Galaxy J1 (2016)
  - samsung galaxy j1 nxt -> سامسونگ Galaxy J1 Nxt
  - samsung galaxy s7 -> سامسونگ Galaxy S7
  - samsung galaxy s7 edge -> سامسونگ Galaxy S7 edge
  - samsung galaxy j3 (2016) -> سامسونگ Galaxy J3 (2016)
  - samsung galaxy j5 (2016) -> سامسونگ Galaxy J5 (2016)
  - samsung galaxy j7 (2016) -> سامسونگ Galaxy J7 (2016)
  - samsung galaxy express prime -> سامسونگ Galaxy Express Prime
  - samsung galaxy xcover 3 g389f -> سامسونگ Galaxy Xcover 3 G389F
  - samsung galaxy c5 -> سامسونگ Galaxy C5
  - samsung galaxy c7 -> سامسونگ Galaxy C7
  - samsung galaxy j3 pro -> سامسونگ Galaxy J3 Pro
  - samsung galaxy s7 active -> سامسونگ Galaxy S7 active
  - samsung z3 corporate -> سامسونگ Z3 Corporate
  - samsung galaxy j2 (2016) -> سامسونگ Galaxy J2 (2016)
  - samsung galaxy j2 pro (2016) -> سامسونگ Galaxy J2 Pro (2016)
  - samsung galaxy on5 pro -> سامسونگ Galaxy On5 Pro
  - samsung galaxy on7 pro -> سامسونگ Galaxy On7 Pro
  - samsung galaxy note7 -> سامسونگ Galaxy Note7
  - samsung galaxy note7 (usa) -> سامسونگ Galaxy Note7 (USA)
  - samsung z2 -> سامسونگ Z2
  - samsung galaxy a8 (2016) -> سامسونگ Galaxy A8 (2016)
  - samsung galaxy j5 prime -> سامسونگ Galaxy J5 Prime
  - samsung galaxy j7 prime -> سامسونگ Galaxy J7 Prime
  - samsung galaxy on7 (2016) -> سامسونگ Galaxy On7 (2016)
  - samsung galaxy on8 -> سامسونگ Galaxy On8
  - samsung galaxy c9 pro -> سامسونگ Galaxy C9 Pro
  - samsung galaxy grand prime plus -> سامسونگ Galaxy Grand Prime Plus
  - samsung galaxy j2 prime -> سامسونگ Galaxy J2 Prime
  - samsung galaxy j1 mini prime -> سامسونگ Galaxy J1 mini prime
  - samsung galaxy a3 (2017) -> سامسونگ Galaxy A3 (2017)
  - samsung galaxy a5 (2017) -> سامسونگ Galaxy A5 (2017)
  - samsung galaxy a7 (2017) -> سامسونگ Galaxy A7 (2017)
  - samsung galaxy c7 pro -> سامسونگ Galaxy C7 Pro
  - samsung galaxy j3 emerge -> سامسونگ Galaxy J3 Emerge
  - samsung galaxy j7 v -> سامسونگ Galaxy J7 V
  - samsung galaxy c5 pro -> سامسونگ Galaxy C5 Pro
  - samsung galaxy s8 -> سامسونگ Galaxy S8
  - samsung galaxy s8+ -> سامسونگ Galaxy S8+
  - samsung galaxy xcover 4 -> سامسونگ Galaxy Xcover 4
  - samsung z4 -> سامسونگ Z4
  - samsung galaxy j3 (2017) -> سامسونگ Galaxy J3 (2017)
  - samsung galaxy j5 (2017) -> سامسونگ Galaxy J5 (2017)
  - samsung galaxy j7 (2017) -> سامسونگ Galaxy J7 (2017)
  - samsung galaxy j7 max -> سامسونگ Galaxy J7 Max
  - samsung galaxy j7 pro -> سامسونگ Galaxy J7 Pro
  - samsung galaxy folder2 -> سامسونگ Galaxy Folder2
  - samsung galaxy j7 nxt -> سامسونگ Galaxy J7 Nxt
  - samsung galaxy note fe -> سامسونگ Galaxy Note FE
  - samsung galaxy note8 -> سامسونگ Galaxy Note8
  - samsung galaxy s8 active -> سامسونگ Galaxy S8 Active
  - samsung galaxy c7 (2017) -> سامسونگ Galaxy C7 (2017)
  - samsung galaxy j2 (2017) -> سامسونگ Galaxy J2 (2017)
  - samsung galaxy a8 (2018) -> سامسونگ Galaxy A8 (2018)
  - samsung galaxy a8+ (2018) -> سامسونگ Galaxy A8+ (2018)
  - samsung galaxy j2 pro (2018) -> سامسونگ Galaxy J2 Pro (2018)
  - samsung galaxy s9 -> سامسونگ Galaxy S9
  - samsung galaxy s9+ -> سامسونگ Galaxy S9+
  - samsung galaxy j7 prime 2 -> سامسونگ Galaxy J7 Prime 2
  - samsung galaxy j7 duo -> سامسونگ Galaxy J7 Duo
  - samsung galaxy a6 (2018) -> سامسونگ Galaxy A6 (2018)
  - samsung galaxy a6+ (2018) -> سامسونگ Galaxy A6+ (2018)
  - samsung galaxy j4 -> سامسونگ Galaxy J4
  - samsung galaxy j6 -> سامسونگ Galaxy J6
  - samsung galaxy j8 -> سامسونگ Galaxy J8
  - samsung galaxy s light luxury -> سامسونگ Galaxy S Light Luxury
  - samsung galaxy a8 star (a9 star) -> سامسونگ Galaxy A8 Star (A9 Star)
  - samsung galaxy j3 (2018) -> سامسونگ Galaxy J3 (2018)
  - samsung galaxy j7 (2018) -> سامسونگ Galaxy J7 (2018)
  - samsung galaxy on6 -> سامسونگ Galaxy On6
  - samsung galaxy j2 core -> سامسونگ Galaxy J2 Core
  - samsung galaxy note9 -> سامسونگ Galaxy Note9
  - samsung galaxy a7 (2018) -> سامسونگ Galaxy A7 (2018)
  - samsung galaxy j4+ -> سامسونگ Galaxy J4+
  - samsung galaxy j6+ -> سامسونگ Galaxy J6+
  - samsung galaxy a6s -> سامسونگ Galaxy A6s
  - samsung galaxy a9 (2018) -> سامسونگ Galaxy A9 (2018)
  - samsung galaxy j4 core -> سامسونگ Galaxy J4 Core
  - samsung galaxy a8s -> سامسونگ Galaxy A8s
  - samsung galaxy m10 -> سامسونگ Galaxy M10
  - samsung galaxy m20 -> سامسونگ Galaxy M20
  - samsung galaxy a10 -> سامسونگ Galaxy A10
  - samsung galaxy a30 -> سامسونگ Galaxy A30
  - samsung galaxy a50 -> سامسونگ Galaxy A50
  - samsung galaxy fold -> سامسونگ Galaxy Fold
  - samsung galaxy fold 5g -> سامسونگ Galaxy Fold 5G
  - samsung galaxy m30 -> سامسونگ Galaxy M30
  - samsung galaxy s10 -> سامسونگ Galaxy S10
  - samsung galaxy s10+ -> سامسونگ Galaxy S10+
  - samsung galaxy s10 5g -> سامسونگ Galaxy S10 5G
  - samsung galaxy s10e -> سامسونگ Galaxy S10e
  - samsung galaxy a20 -> سامسونگ Galaxy A20
  - samsung galaxy a40 -> سامسونگ Galaxy A40
  - samsung galaxy a70 -> سامسونگ Galaxy A70
  - samsung galaxy a20e -> سامسونگ Galaxy A20e
  - samsung galaxy a2 core -> سامسونگ Galaxy A2 Core
  - samsung galaxy a60 -> سامسونگ Galaxy A60
  - samsung galaxy a80 -> سامسونگ Galaxy A80
  - samsung galaxy view2 -> سامسونگ Galaxy View2
  - samsung galaxy m40 -> سامسونگ Galaxy M40
  - samsung galaxy xcover 4s -> سامسونگ Galaxy Xcover 4s
  - samsung galaxy a10e -> سامسونگ Galaxy A10e
  - samsung galaxy a10s -> سامسونگ Galaxy A10s
  - samsung galaxy a30s -> سامسونگ Galaxy A30s
  - samsung galaxy a50s -> سامسونگ Galaxy A50s
  - samsung galaxy note10 -> سامسونگ Galaxy Note10
  - samsung galaxy note10+ -> سامسونگ Galaxy Note10+
  - samsung galaxy note10 5g -> سامسونگ Galaxy Note10 5G
  - samsung galaxy note10+ 5g -> سامسونگ Galaxy Note10+ 5G
  - samsung galaxy a20s -> سامسونگ Galaxy A20s
  - samsung galaxy a70s -> سامسونگ Galaxy A70s
  - samsung galaxy a90 5g -> سامسونگ Galaxy A90 5G
  - samsung galaxy m10s -> سامسونگ Galaxy M10s
  - samsung galaxy m30s -> سامسونگ Galaxy M30s
  - samsung galaxy xcover fieldpro -> سامسونگ Galaxy Xcover FieldPro
  - samsung galaxy a01 -> سامسونگ Galaxy A01
  - samsung galaxy a51 -> سامسونگ Galaxy A51
  - samsung galaxy a71 -> سامسونگ Galaxy A71
  - samsung galaxy a71 5g -> سامسونگ گلکسی A71 5G
  - samsung galaxy a71 5g uw -> سامسونگ Galaxy A71 5G UW
  - samsung galaxy a quantum -> سامسونگ Galaxy A Quantum
  - samsung galaxy s20 5g uw -> سامسونگ Galaxy S20 5G UW
  - samsung galaxy z fold2 5g -> سامسونگ گلکسی زد فولد 2
  - samsung galaxy note10 lite -> سامسونگ Galaxy Note10 Lite
  - samsung galaxy s10 lite -> سامسونگ Galaxy S10 Lite
  - samsung galaxy xcover pro -> سامسونگ Galaxy Xcover Pro
  - samsung galaxy m31 -> سامسونگ Galaxy M31
  - samsung galaxy s20 -> سامسونگ Galaxy S20
  - samsung galaxy s20+ -> سامسونگ Galaxy S20+
  - samsung galaxy s20 5g -> سامسونگ Galaxy S20 5G
  - samsung galaxy s20+ 5g -> سامسونگ Galaxy S20+ 5G
  - samsung galaxy s20 ultra -> سامسونگ Galaxy S20 Ultra
  - samsung galaxy s20 ultra 5g -> سامسونگ Galaxy S20 Ultra 5G
  - samsung galaxy z flip -> سامسونگ Galaxy Z Flip
  - samsung galaxy a11 -> سامسونگ Galaxy A11
  - samsung galaxy a31 -> سامسونگ Galaxy A31
  - samsung galaxy a41 -> سامسونگ Galaxy A41
  - samsung galaxy m11 -> سامسونگ Galaxy M11
  - samsung galaxy m21 -> سامسونگ Galaxy M21
  - samsung galaxy a21 -> سامسونگ Galaxy A21
  - samsung galaxy a51 5g -> سامسونگ Galaxy A51 5G
  - samsung galaxy j2 core (2020) -> سامسونگ Galaxy J2 Core (2020)
  - samsung galaxy a21s -> سامسونگ Galaxy A21s
  - samsung galaxy m01 -> سامسونگ Galaxy M01
  - samsung galaxy a01 core -> سامسونگ Galaxy A01 Core
  - samsung galaxy m01 core -> سامسونگ Galaxy M01 Core
  - samsung galaxy m01s -> سامسونگ Galaxy M01s
  - samsung galaxy m31s -> سامسونگ Galaxy M31s
  - samsung galaxy z flip 5g -> سامسونگ Galaxy Z Flip 5G
  - samsung galaxy a51 5g uw -> سامسونگ Galaxy A51 5G UW
  - samsung galaxy m51 -> سامسونگ Galaxy M51
  - samsung galaxy note20 -> سامسونگ Galaxy Note20
  - samsung galaxy note20 5g -> سامسونگ Galaxy Note20 5G
  - samsung galaxy note20 ultra -> سامسونگ Galaxy Note20 Ultra
  - samsung galaxy note20 ultra 5g -> سامسونگ Galaxy Note20 Ultra 5G
  - samsung galaxy a42 5g -> سامسونگ Galaxy A42 5G
  - samsung galaxy s20 fe -> سامسونگ Galaxy S20 FE
  - samsung galaxy s20 fe 5g -> سامسونگ Galaxy S20 FE 5G
  - samsung galaxy f41 -> سامسونگ Galaxy F41
  - samsung galaxy m31 prime -> سامسونگ Galaxy M31 Prime
  - samsung galaxy a02s -> سامسونگ Galaxy A02s
  - samsung galaxy a12 -> سامسونگ Galaxy A12
  - samsung galaxy m21s -> سامسونگ Galaxy M21s
  - samsung galaxy a12 (india) -> سامسونگ Galaxy A12 (India)
  - samsung galaxy a13 5g -> سامسونگ گلکسی A13 5G
  - samsung galaxy f52 5g -> سامسونگ گلکسی F52 5G
  - samsung galaxy z flip3 5g -> سامسونگ Galaxy Z Flip3 5G
  - samsung galaxy a02 -> سامسونگ Galaxy A02
  - samsung galaxy a32 5g -> سامسونگ Galaxy A32 5G
  - samsung galaxy m02s -> سامسونگ Galaxy M02s
  - samsung galaxy s21 5g -> سامسونگ Galaxy S21 5G
  - samsung galaxy s21+ 5g -> سامسونگ Galaxy S21+ 5G
  - samsung galaxy s21 ultra 5g -> سامسونگ Galaxy S21 Ultra 5G
  - samsung galaxy a32 -> سامسونگ Galaxy A32
  - samsung galaxy f62 -> سامسونگ Galaxy F62
  - samsung galaxy m02 -> سامسونگ Galaxy M02
  - samsung galaxy m12 (india) -> سامسونگ Galaxy M12 (India)
  - samsung galaxy m62 -> سامسونگ Galaxy M62
  - samsung galaxy a52 -> سامسونگ Galaxy A52
  - samsung galaxy a52 5g -> سامسونگ Galaxy A52 5G
  - samsung galaxy a72 -> سامسونگ Galaxy A72
  - samsung galaxy xcover 5 -> سامسونگ Galaxy Xcover 5
  - samsung galaxy f02s -> سامسونگ Galaxy F02s
  - samsung galaxy f12 -> سامسونگ Galaxy F12
  - samsung galaxy m12 -> سامسونگ Galaxy M12
  - samsung galaxy quantum 2 -> سامسونگ Galaxy Quantum 2
  - samsung galaxy a22 -> سامسونگ Galaxy A22
  - samsung galaxy a22 5g -> سامسونگ Galaxy A22 5G
  - samsung galaxy m32 -> سامسونگ Galaxy M32
  - samsung galaxy f22 -> سامسونگ Galaxy F22
  - samsung galaxy m21 2021 -> سامسونگ Galaxy M21 2021
  - samsung galaxy a03s -> سامسونگ Galaxy A03s
  - samsung galaxy a12 nacho -> سامسونگ Galaxy A12 Nacho
  - samsung galaxy a52s 5g -> سامسونگ Galaxy A52s 5G
  - samsung galaxy m32 5g -> سامسونگ Galaxy M32 5G
  - samsung galaxy z fold3 5g -> سامسونگ Galaxy Z Fold3 5G
  - samsung galaxy f42 5g -> سامسونگ Galaxy F42 5G
  - samsung galaxy m22 -> سامسونگ Galaxy M22
  - samsung galaxy m52 5g -> سامسونگ Galaxy M52 5G
  - samsung galaxy a03 -> سامسونگ Galaxy A03
  - samsung galaxy a03 core -> سامسونگ Galaxy A03 Core
  - samsung galaxy a04 -> سامسونگ گلکسی A04
  - samsung galaxy a04s -> سامسونگ گلکسی A04s
  - samsung galaxy a13 -> سامسونگ گلکسی A13
  - samsung galaxy a23 -> سامسونگ گلکسی A23
  - samsung galaxy a23 5g -> سامسونگ Galaxy A23 5G
  - samsung galaxy a33 5g -> سامسونگ گلکسی A33 5G
  - samsung galaxy a53 5g -> سامسونگ گلکسی A53 5G
  - samsung galaxy m13 5g -> سامسونگ گلکسی M13 5G
  - samsung galaxy m13 (india) -> سامسونگ Galaxy M13 (India)
  - samsung galaxy m53 -> سامسونگ گلکسی M53
  - samsung galaxy s20 fe 2022 -> سامسونگ Galaxy S20 FE 2022
  - samsung galaxy s21 fe 5g -> سامسونگ گلکسی اس 21 اف ای 5G
  - samsung galaxy s22 5g -> سامسونگ Galaxy S22 5G
  - samsung galaxy s22+ 5g -> سامسونگ Galaxy S22+ 5G
  - samsung galaxy s22 ultra 5g -> سامسونگ Galaxy S22 Ultra 5G
  - samsung galaxy xcover6 pro -> سامسونگ Galaxy Xcover6 Pro
  - samsung galaxy z flip4 -> سامسونگ Galaxy Z Flip4
  - samsung galaxy z fold4 -> سامسونگ Galaxy Z Fold4
  - samsung galaxy a73 5g -> سامسونگ Galaxy A73 5G
  - samsung galaxy f23 -> سامسونگ Galaxy F23
  - samsung galaxy m23 -> سامسونگ Galaxy M23
  - samsung galaxy m33 -> سامسونگ Galaxy M33
  - samsung galaxy a13 (sm-a137) -> سامسونگ Galaxy A13 (SM-A137)
  - samsung galaxy m13 -> سامسونگ Galaxy M13
  - samsung galaxy f13 -> سامسونگ Galaxy F13
  - samsung galaxy s23 5g -> سامسونگ Galaxy S23 5G
  - sharp -> شارپ
  - sharp sh530u -> شارپ SH530U
  - sharp aquos crystal -> شارپ Aquos Crystal
  - sharp aquos crystal 2 -> شارپ Aquos Crystal 2
  - sharp aquos xx -> شارپ Aquos Xx
  - sharp ms1 -> شارپ MS1
  - sharp z2 -> شارپ Z2
  - sharp z3 -> شارپ Z3
  - sharp aquos s2 -> شارپ Aquos S2
  - sharp pi -> شارپ Pi
  - sharp r1s -> شارپ R1S
  - sharp aquos s3 -> شارپ Aquos S3
  - sharp aquos s3 mini -> شارپ Aquos S3 mini
  - sharp aquos r2 -> شارپ Aquos R2
  - sharp aquos b10 -> شارپ Aquos B10
  - sharp aquos c10 -> شارپ Aquos C10
  - sharp aquos s3 high -> شارپ Aquos S3 High
  - sharp aquos d10 -> شارپ Aquos D10
  - sharp aquos r2 compact -> شارپ Aquos R2 compact
  - sharp aquos zero -> شارپ Aquos Zero
  - sharp aquos r3 -> شارپ Aquos R3
  - sharp aquos v -> شارپ Aquos V
  - sharp aquos sense4 plus -> شارپ Aquos sense4 plus
  - sharp aquos sense5g -> شارپ Aquos sense5G
  - sharp aquos r5g -> شارپ Aquos R5G
  - sharp aquos zero 2 -> شارپ Aquos Zero 2
  - sharp aquos zero6 -> شارپ Aquos zero6
  - sharp aquos v6 -> شارپ Aquos V6
  - sharp aquos wish -> شارپ Aquos wish
  - sonim -> سونیم
  - sonim xp5s -> سونیم XP5s
  - sonim xp8 -> سونیم XP8
  - sonim xp3 -> سونیم XP3
  - sonim xp3plus -> سونیم XP3plus
  - sonim xp5plus -> سونیم XP5plus
  - sony -> سونی
  - sony xperia 5 plus -> سونی Xperia 5 Plus
  - sony xperia c670x -> سونی Xperia C670X
  - sony xperia h8541 -> سونی Xperia H8541
  - sony xperia m ultra -> سونی Xperia M Ultra
  - sony xperia x ultra -> سونی Xperia X Ultra
  - sony xperia z4 compact -> سونی Xperia Z4 Compact
  - sony xperia z4 ultra -> سونی Xperia Z4 Ultra
  - sony xperia z4v -> سونی Xperia Z4v
  - sony xperia ion lte -> سونی Xperia ion LTE
  - sony xperia neo l -> سونی Xperia neo L
  - sony xperia j -> سونی Xperia J
  - sony xperia tx -> سونی Xperia TX
  - sony xperia v -> سونی Xperia V
  - sony xperia t lte -> سونی Xperia T LTE
  - sony xperia e dual -> سونی Xperia E dual
  - sony xperia z -> سونی Xperia Z
  - sony xperia zl -> سونی Xperia ZL
  - sony xperia l -> سونی Xperia L
  - sony xperia sp -> سونی Xperia SP
  - sony xperia zr -> سونی Xperia ZR
  - sony xperia c -> سونی Xperia C
  - sony xperia m -> سونی Xperia M
  - sony xperia z ultra -> سونی Xperia Z Ultra
  - sony xperia z1 -> سونی Xperia Z1
  - sony xperia e1 -> سونی Xperia E1
  - sony xperia e1 dual -> سونی Xperia E1 dual
  - sony xperia t2 ultra -> سونی Xperia T2 Ultra
  - sony xperia t2 ultra dual -> سونی Xperia T2 Ultra dual
  - sony xperia z1 compact -> سونی Xperia Z1 Compact
  - sony xperia z1s -> سونی Xperia Z1s
  - sony xperia m2 -> سونی Xperia M2
  - sony xperia m2 dual -> سونی Xperia M2 dual
  - sony xperia z2 -> سونی Xperia Z2
  - sony xperia t3 -> سونی Xperia T3
  - sony xperia z2a -> سونی Xperia Z2a
  - sony xperia c3 -> سونی Xperia C3
  - sony xperia c3 dual -> سونی Xperia C3 Dual
  - sony xperia m2 aqua -> سونی Xperia M2 Aqua
  - sony xperia e3 -> سونی Xperia E3
  - sony xperia e3 dual -> سونی Xperia E3 Dual
  - sony xperia z3 -> سونی Xperia Z3
  - sony xperia z3 compact -> سونی Xperia Z3 Compact
  - sony xperia z3 dual -> سونی Xperia Z3 Dual
  - sony xperia z3v -> سونی Xperia Z3v
  - sony xperia e4 -> سونی Xperia E4
  - sony xperia e4 dual -> سونی Xperia E4 Dual
  - sony xperia e4g -> سونی Xperia E4g
  - sony xperia e4g dual -> سونی Xperia E4g Dual
  - sony xperia c4 -> سونی Xperia C4
  - sony xperia c4 dual -> سونی Xperia C4 Dual
  - sony xperia z3+ -> سونی Xperia Z3+
  - sony xperia z3+ dual -> سونی Xperia Z3+ dual
  - sony xperia c5 ultra -> سونی Xperia C5 Ultra
  - sony xperia c5 ultra dual -> سونی Xperia C5 Ultra Dual
  - sony xperia m5 -> سونی Xperia M5
  - sony xperia m5 dual -> سونی Xperia M5 Dual
  - sony xperia z5 -> سونی Xperia Z5
  - sony xperia z5 compact -> سونی Xperia Z5 Compact
  - sony xperia z5 dual -> سونی Xperia Z5 Dual
  - sony xperia z5 premium -> سونی Xperia Z5 Premium
  - sony xperia z5 premium dual -> سونی Xperia Z5 Premium Dual
  - sony xperia xa -> سونی Xperia XA
  - sony xperia xa dual -> سونی Xperia XA Dual
  - sony xperia e5 -> سونی Xperia E5
  - sony xperia xa ultra -> سونی Xperia XA Ultra
  - sony xperia x compact -> سونی Xperia X Compact
  - sony xperia xz -> سونی Xperia XZ
  - sony xperia xa1 -> سونی Xperia XA1
  - sony xperia xa1 ultra -> سونی Xperia XA1 Ultra
  - sony xperia xz premium -> سونی Xperia XZ Premium
  - sony xperia xzs -> سونی Xperia XZs
  - sony xperia l1 -> سونی Xperia L1
  - sony xperia xa1 plus -> سونی Xperia XA1 Plus
  - sony xperia xz1 -> سونی Xperia XZ1
  - sony xperia xz1 compact -> سونی Xperia XZ1 Compact
  - sony xperia r1 (plus) -> سونی Xperia R1 (Plus)
  - sony xperia l2 -> سونی Xperia L2
  - sony xperia xa2 -> سونی Xperia XA2
  - sony xperia xa2 ultra -> سونی Xperia XA2 Ultra
  - sony xperia xz2 -> سونی Xperia XZ2
  - sony xperia xz2 compact -> سونی Xperia XZ2 Compact
  - sony xperia xz2 premium -> سونی Xperia XZ2 Premium
  - sony xperia xa2 plus -> سونی Xperia XA2 Plus
  - sony xperia xz3 -> سونی Xperia XZ3
  - sony xperia 1 -> سونی Xperia 1
  - sony xperia 10 -> سونی Xperia 10
  - sony xperia 10 plus -> سونی Xperia 10 Plus
  - sony xperia l3 -> سونی Xperia L3
  - sony xperia 5 -> سونی Xperia 5
  - sony xperia 10 ii -> سونی Xperia 10 II
  - sony xperia 1 ii -> سونی Xperia 1 II
  - sony xperia l4 -> سونی Xperia L4
  - sony xperia pro -> سونی Xperia Pro
  - sony xperia 5 ii -> سونی Xperia 5 II
  - sony xperia 10 iii -> سونی Xperia 10 III
  - sony xperia 1 iii -> سونی Xperia 1 III
  - sony xperia 5 iii -> سونی Xperia 5 III
  - sony xperia 10 iii lite -> سونی Xperia 10 III Lite
  - sony xperia pro-i -> سونی Xperia Pro-I
  - sony xperia 5 iv -> سونی اکسپریا 5 IV
  - sony xperia 10 iv -> سونی Xperia 10 IV
  - sony xperia 1 iv -> سونی Xperia 1 IV
  - sony ericsson -> سونی اریکسون
  - sony ericsson ericsson xperia arc s -> سونی اریکسون Ericsson Xperia Arc S
  - sony ericsson ericsson xperia neo v -> سونی اریکسون Ericsson Xperia neo V
  - sony ericsson ericsson xperia play -> سونی اریکسون Ericsson Xperia PLAY
  - sony ericsson ericsson xperia pro -> سونی اریکسون Ericsson Xperia pro
  - sony ericsson ericsson xperia ray -> سونی اریکسون Ericsson Xperia ray
  - sony ericsson ericsson xperia x10 -> سونی اریکسون Ericsson Xperia X10
  - sony ericsson ericsson xperia x8 -> سونی اریکسون Ericsson Xperia X8
  - tcl -> تی‌سی‌ال
  - tcl plex -> تی‌سی‌ال Plex
  - tcl 10 5g -> تی‌سی‌ال 10 5G
  - tcl 10 5g uw -> تی‌سی‌ال 10 5G UW
  - tcl 10l -> تی‌سی‌ال تی سی ال 10L
  - tcl 10 plus -> تی‌سی‌ال تی سی ال 10 پلاس
  - tcl 10 pro -> تی‌سی‌ال تی سی ال 10 پرو
  - tcl 10 se -> تی‌سی‌ال تی سی ال 10 SE
  - tcl 20 5g -> تی‌سی‌ال تی سی ال 20 5G
  - tcl movetime -> تی‌سی‌ال MoveTime
  - tcl 20b -> تی‌سی‌ال 20B
  - tcl 20e -> تی‌سی‌ال 20E
  - tcl 20l -> تی‌سی‌ال تی سی ال 20L
  - tcl 20l+ -> تی‌سی‌ال 20L+
  - tcl 20 pro 5g -> تی‌سی‌ال 20 Pro 5G
  - tcl 20s -> تی‌سی‌ال 20S
  - tcl 20 se -> تی‌سی‌ال تی سی ال 20 SE
  - tcl 20y -> تی‌سی‌ال 20Y
  - tcl a30 -> تی‌سی‌ال A30
  - tcl nxtpaper -> تی‌سی‌ال NxtPaper
  - tcl 20 r 5g -> تی‌سی‌ال 20 R 5G
  - tcl a3 -> تی‌سی‌ال A3
  - tcl l10 pro -> تی‌سی‌ال L10 Pro
  - tcl 20 xe -> تی‌سی‌ال 20 XE
  - tcl 306 -> تی‌سی‌ال 306
  - tcl nxtpaper 10s -> تی‌سی‌ال NxtPaper 10s
  - tcl 305 -> تی‌سی‌ال 305
  - tcl 30 v 5g -> تی‌سی‌ال 30 V 5G
  - tcl 30 xe 5g -> تی‌سی‌ال 30 XE 5G
  - tcl 30 -> تی‌سی‌ال 30
  - tcl 30+ -> تی‌سی‌ال 30+
  - tcl 30 5g -> تی‌سی‌ال 30 5G
  - tcl 30e -> تی‌سی‌ال 30E
  - tcl 30 se -> تی‌سی‌ال 30 SE
  - tcl stylus -> تی‌سی‌ال Stylus
  - tecno -> تکنو
  - tecno phantom 6 -> تکنو فانتوم 6
  - tecno phantom 6 plus -> تکنو فانتوم 6 پلاس
  - tecno camon cx -> تکنو Camon CX
  - tecno camon cx manchester city le -> تکنو Camon CX Manchester City LE
  - tecno camon cx air -> تکنو Camon CX ایر
  - tecno spark -> تکنو اسپارک
  - tecno spark plus -> تکنو اسپارک پلاس
  - tecno spark pro -> تکنو اسپارک پرو
  - tecno camon cm -> تکنو Camon CM
  - tecno spark cm -> تکنو اسپارک CM
  - tecno camon x -> تکنو Camon X
  - tecno camon x pro -> تکنو Camon X پرو
  - tecno f2 -> تکنو F2
  - tecno pop 1 -> تکنو پاپ 1
  - tecno phantom 8 -> تکنو فانتوم 8
  - tecno f2 lte -> تکنو F2 LTE
  - tecno pouvoir 1 -> تکنو Pouvoir 1
  - tecno pouvoir 2 -> تکنو Pouvoir 2
  - tecno pop 1 pro -> تکنو پاپ 1 پرو
  - tecno spark 2 -> تکنو اسپارک 2
  - tecno pop 1 lite -> تکنو پاپ 1 لایت
  - tecno pop 1s -> تکنو پاپ 1 اس
  - tecno pouvoir 2 pro -> تکنو Pouvoir 1 پرو
  - tecno camon 11 -> تکنو Camon 11
  - tecno camon 11 pro -> تکنو Camon 11 پرو
  - tecno spark 4 -> تکنو اسپارک 4
  - tecno camon iace2 -> تکنو Camon iACE2
  - tecno camon iace2x -> تکنو Camon iACE2X
  - tecno spark 3 -> تکنو اسپارک 3
  - tecno spark 3 pro -> تکنو اسپارک 3 پرو
  - tecno pop 2 f -> تکنو Pop 2 F
  - tecno pop 2 plus -> تکنو پاپ 2 پلاس
  - tecno pouvoir 3 -> تکنو Pouvoir 3
  - tecno phantom 9 -> تکنو فانتوم 9
  - tecno camon 12 -> تکنو Camon 12
  - tecno pouvoir 3 air -> تکنو Pouvoir 3 ایر
  - tecno pouvoir 3 plus -> تکنو Pouvoir 3 پلاس
  - tecno spark go -> تکنو اسپارک گو
  - tecno camon 12 pro -> تکنو Camon 12 پرو
  - tecno camon 12 air -> تکنو Camon 12 Air
  - tecno pop 3 plus -> تکنو پاپ 3 پلاس
  - tecno spark 4 lite -> تکنو اسپارک 4 لایت
  - tecno camon 15 -> تکنو Camon 15
  - tecno camon 15 air -> تکنو Camon 15 Air
  - tecno camon 15 premier -> تکنو Camon 15 Premier
  - tecno camon 15 pro -> تکنو Camon 15 پرو
  - tecno camon 16 -> تکنو Camon 16
  - tecno camon 16 premier -> تکنو amon 16 Premier
  - tecno camon 16 pro -> تکنو Camon 16 پرو
  - tecno camon 16 s -> تکنو Camon 16 S
  - tecno pop 4 -> تکنو پاپ 4
  - tecno pouvoir 4 -> تکنو Pouvoir 4
  - tecno pouvoir 4 pro -> تکنو Pouvoir 4 پرو
  - tecno pova -> تکنو Pova
  - tecno spark 5 -> تکنو اسپارک 5
  - tecno spark 5 air -> تکنو اسپارک 5 ایر
  - tecno spark 5 pro -> تکنو اسپارک 5 پرو
  - tecno spark 6 -> تکنو اسپارک 6
  - tecno spark 6 air -> تکنو اسپارک 6 ایر
  - tecno spark 6 go -> تکنو اسپارک 6 Go
  - tecno spark go 2020 -> تکنو اسپارک Go 2020
  - tecno spark power 2 -> تکنو اسپارک پاور 2
  - tecno camon 17 -> تکنو Camon 17
  - tecno camon 17p -> تکنو Camon 17P
  - tecno camon 17 pro -> تکنو Camon 17 پرو
  - tecno camon 18i -> تکنو Camon 18i
  - tecno camon 18 premier -> تکنو Camon 18 Premier
  - tecno phantom x -> تکنو فانتوم ایکس
  - tecno pop 5 -> تکنو پاپ 5
  - tecno pop 5 lte -> تکنو Pop 5 LTE
  - tecno pova 2 -> تکنو Pova 2
  - tecno pova neo -> تکنو Pova Neo
  - tecno spark 7 -> تکنو اسپارک 7
  - tecno spark 7p -> تکنو اسپارک 7P
  - tecno spark 7 pro -> تکنو اسپارک 7 پرو
  - tecno spark 7t -> تکنو اسپارک 7T
  - tecno spark 8 -> تکنو اسپارک 8
  - tecno spark 8p -> تکنو اسپارک 8P
  - tecno spark 8 pro -> تکنو اسپارک 8 پرو
  - tecno spark 8t -> تکنو Spark 8T
  - tecno spark go 2021 -> تکنو اسپارک Go 2021
  - tecno spark go 2022 -> تکنو اسپارک Go 2022
  - tecno camon 18 -> تکنو Camon 18
  - tecno camon 18 p -> تکنو Camon 18 P
  - tecno camon 18t -> تکنو Camon 18T
  - tecno pop 5c -> تکنو Pop 5c
  - tecno camon 19 neo -> تکنو Camon 19 نئو
  - tecno pop 5 pro -> تکنو پاپ 5 پرو
  - tecno pop 5x -> تکنو پاپ 5X
  - tecno pop 6 -> تکنو Pop 6
  - tecno pop 6 go -> تکنو Pop 6 Go
  - tecno pop 6 pro -> تکنو Pop 6 Pro
  - tecno pova 5g -> تکنو Pova 5G
  - tecno spark 8c -> تکنو اسپارک 8C
  - tecno spark 9 -> تکنو اسپارک 9
  - tecno spark 9 pro -> تکنو اسپارک 9 پرو
  - tecno spark 9t (india) -> تکنو اسپارک 9T هند
  - tecno pop 5s -> تکنو Pop 5S
  - tecno pova 3 -> تکنو Pova 3
  - tecno camon 19 -> تکنو Camon 19
  - tecno camon 19 pro -> تکنو Camon 19 Pro
  - tecno camon 19 pro 5g -> تکنو Camon 19 Pro 5G
  - tecno spark 9t -> تکنو Spark 9T
  - vivo -> ویوو
  - vivo xplay7 -> ویوو Xplay7
  - vivo y51 -> ویوو Y51
  - vivo xplay3s -> ویوو Xplay3S
  - vivo y15 (2013) -> ویوو Y15 (2013)
  - vivo y22 -> ویوو Y22
  - vivo x3s -> ویوو X3S
  - vivo x5 -> ویوو X5
  - vivo xshot -> ویوو Xshot
  - vivo y11 -> ویوو Y11
  - vivo x5max -> ویوو X5Max
  - vivo y27 -> ویوو Y27
  - vivo y28 -> ویوو Y28
  - vivo x5max+ -> ویوو X5Max+
  - vivo x5pro -> ویوو X5Pro
  - vivo v1 -> ویوو V1
  - vivo y35 -> ویوو Y35
  - vivo v1 max -> ویوو V1 Max
  - vivo y15s (2015) -> ویوو Y15S (2015)
  - vivo y37 -> ویوو Y37
  - vivo y31 (2015) -> ویوو Y31 (2015)
  - vivo x6 -> ویوو X6
  - vivo x6plus -> ویوو X6Plus
  - vivo x6s -> ویوو X6S
  - vivo x6s plus -> ویوو X6S Plus
  - vivo xplay5 -> ویوو Xplay5
  - vivo xplay5 elite -> ویوو Xplay5 Elite
  - vivo v3 -> ویوو V3
  - vivo v3max -> ویوو V3Max
  - vivo x7 -> ویوو X7
  - vivo x7 plus -> ویوو X7 Plus
  - vivo v5 -> ویوو V5
  - vivo x9 -> ویوو X9
  - vivo x9 plus -> ویوو X9 Plus
  - vivo xplay6 -> ویوو Xplay6
  - vivo y67 -> ویوو Y67
  - vivo v5 lite (vivo 1609) -> ویوو V5 Lite (vivo 1609)
  - vivo v5 plus -> ویوو V5 Plus
  - vivo y55s -> ویوو Y55s
  - vivo y25 -> ویوو Y25
  - vivo v5s -> ویوو V5s
  - vivo x9s -> ویوو X9s
  - vivo x9s plus -> ویوو X9s Plus
  - vivo y69 -> ویوو Y69
  - vivo v7+ -> ویوو V7+
  - vivo x20 -> ویوو X20
  - vivo x20 plus -> ویوو X20 Plus
  - vivo y65 -> ویوو Y65
  - vivo v7 -> ویوو V7
  - vivo x20 plus ud -> ویوو X20 Plus UD
  - vivo v9 -> ویوو V9
  - vivo x21 ud -> ویوو X21 UD
  - vivo v9 youth -> ویوو V9 Youth
  - vivo y71 -> ویوو Y71
  - vivo x21i -> ویوو X21i
  - vivo z1 -> ویوو Z1
  - vivo nex a -> ویوو NEX A
  - vivo nex s -> ویوو NEX S
  - vivo v9 6gb -> ویوو V9 6GB
  - vivo y81 -> ویوو Y81
  - vivo z1i -> ویوو Z1i
  - vivo v11 (v11 pro) -> ویوو V11 (V11 Pro)
  - vivo x23 -> ویوو X23
  - vivo y71i -> ویوو Y71i
  - vivo y81i -> ویوو Y81i
  - vivo z3 -> ویوو Z3
  - vivo z3i -> ویوو Z3i
  - vivo y91i -> ویوو Y91i
  - vivo y93 -> ویوو Y93
  - vivo y95 -> ویوو Y95
  - vivo z1 lite -> ویوو Z1 Lite
  - vivo nex dual display -> ویوو NEX Dual Display
  - vivo y93 (mediatek) -> ویوو Y93 (Mediatek)
  - vivo y93s -> ویوو Y93s
  - vivo v15 pro -> ویوو V15 Pro
  - vivo v15 -> ویوو V15
  - vivo x27 -> ویوو X27
  - vivo y91i (india) -> ویوو Y91i (India)
  - vivo x27 pro -> ویوو X27 Pro
  - vivo y17 -> ویوو Y17
  - vivo z3x -> ویوو Z3x
  - vivo y15 -> ویوو Y15
  - vivo z5x -> ویوو Z5x
  - vivo y12 -> ویوو Y12
  - vivo iqoo neo -> ویوو iQOO Neo
  - vivo s1 -> ویوو S1
  - vivo y90 -> ویوو Y90
  - vivo z1pro -> ویوو Z1Pro
  - vivo iqoo pro -> ویوو iQOO Pro
  - vivo iqoo pro 5g -> ویوو iQOO Pro 5G
  - vivo v17 neo -> ویوو V17 Neo
  - vivo nex 3 -> ویوو NEX 3
  - vivo nex 3 5g -> ویوو NEX 3 5G
  - vivo u10 -> ویوو U10
  - vivo v17 pro -> ویوو V17 Pro
  - vivo z1x -> ویوو Z1x
  - vivo iqoo neo 855 -> ویوو iQOO Neo 855
  - vivo u3 -> ویوو U3
  - vivo y11 (2019) -> ویوو Y11 (2019)
  - vivo s1 pro -> ویوو S1 Pro
  - vivo s5 -> ویوو S5
  - vivo u20 -> ویوو U20
  - vivo v17 -> ویوو V17
  - vivo y19 -> ویوو Y19
  - vivo y3 standard -> ویوو Y3 Standard
  - vivo z5i -> ویوو Z5i
  - vivo iqoo neo 855 racing -> ویوو iQOO Neo 855 Racing
  - vivo x30 -> ویوو X30
  - vivo x30 pro -> ویوو X30 Pro
  - vivo y9s -> ویوو Y9s
  - vivo iqoo 3 5g -> ویوو iQOO 3 5G
  - vivo z6 5g -> ویوو Z6 5G
  - vivo nex 3s 5g -> ویوو NEX 3S 5G
  - vivo s6 5g -> ویوو S6 5G
  - vivo iqoo neo3 5g -> ویوو iQOO Neo3 5G
  - vivo v19 -> ویوو V19
  - vivo y50 -> ویوو Y50
  - vivo iqoo z1 -> ویوو iQOO Z1
  - vivo x50 lite -> ویوو X50 Lite
  - vivo y30 -> ویوو Y30
  - vivo y70s -> ویوو Y70s
  - vivo v19 neo -> ویوو V19 Neo
  - vivo x50 5g -> ویوو X50 5G
  - vivo x50 pro -> ویوو X50 Pro
  - vivo x50 pro+ -> ویوو X50 Pro+
  - vivo z5x (2020) -> ویوو Z5x (2020)
  - vivo iqoo u1 -> ویوو iQOO U1
  - vivo iqoo z1x -> ویوو iQOO Z1x
  - vivo x50 -> ویوو X50
  - vivo y12i -> ویوو Y12i
  - vivo y51s -> ویوو Y51s
  - vivo iqoo 5 5g -> ویوو iQOO 5 5G
  - vivo iqoo 5 pro 5g -> ویوو iQOO 5 Pro 5G
  - vivo s1 prime -> ویوو S1 Prime
  - vivo y20 -> ویوو Y20
  - vivo y20i -> ویوو Y20i
  - vivo x50e -> ویوو X50e
  - vivo iqoo u1x -> ویوو iQOO U1x
  - vivo x51 5g -> ویوو X51 5G
  - vivo y11s -> ویوو Y11s
  - vivo y20s -> ویوو Y20s
  - vivo y70 -> ویوو Y70
  - vivo y12s -> ویوو Y12s
  - vivo iqoo u3 -> ویوو iQOO U3
  - vivo y20 2021 -> ویوو Y20 2021
  - vivo y20a -> ویوو Y20A
  - vivo iqoo 7 -> ویوو iQOO 7
  - vivo x60 pro+ -> ویوو X60 Pro+
  - vivo y20g -> ویوو Y20G
  - vivo y31 -> ویوو Y31
  - vivo y31s -> ویوو Y31s
  - vivo iqoo neo5 -> ویوو iQOO Neo5
  - vivo iqoo u3x -> ویوو iQOO U3x
  - vivo iqoo z3 -> ویوو iQOO Z3
  - vivo s9 -> ویوو S9
  - vivo s9e -> ویوو S9e
  - vivo x60 -> ویوو X60
  - vivo x60 pro -> ویوو X60 Pro
  - vivo y30g -> ویوو Y30G
  - vivo y72 5g -> ویوو Y72 5G
  - vivo v21e -> ویوو V21e
  - vivo x60t -> ویوو X60t
  - vivo y12s 2021 -> ویوو Y12s 2021
  - vivo v21e 5g -> ویوو V21e 5G
  - vivo x60t pro+ -> ویوو X60t Pro+
  - vivo y53s -> ویوو Y53s
  - vivo y70t -> ویوو Y70t
  - vivo s10 -> ویوو S10
  - vivo s10 pro -> ویوو S10 Pro
  - vivo y53s 4g -> ویوو Y53s 4G
  - vivo iqoo 8 -> ویوو iQOO 8
  - vivo iqoo 8 pro -> ویوو iQOO 8 Pro
  - vivo y21 -> ویوو Y21
  - vivo y33s -> ویوو Y33s
  - vivo iqoo z5 -> ویوو iQOO Z5
  - vivo x70 pro -> ویوو X70 Pro
  - vivo x70 pro+ -> ویوو X70 Pro+
  - vivo y21s -> ویوو Y21s
  - vivo iqoo z5x -> ویوو iQOO Z5x
  - vivo s10e -> ویوو S10e
  - vivo t1 -> ویوو T1
  - vivo t1x -> ویوو T1x
  - vivo y20t -> ویوو Y20T
  - vivo y33 -> ویوو Y33
  - vivo y71t -> ویوو Y71t
  - vivo y15a -> ویوو Y15a
  - vivo y15s -> ویوو Y15s
  - vivo y50t -> ویوو Y50t
  - vivo y54s -> ویوو Y54s
  - vivo y74s -> ویوو Y74s
  - vivo y76s -> ویوو Y76s
  - vivo iqoo 10 -> ویوو 10 iQOO
  - vivo iqoo 10 pro -> ویوو 10 iQOO پرو
  - vivo iqoo 9 (china) -> ویوو iQOO 9 (China)
  - vivo iqoo 9 se -> ویوو iQOO 9 SE
  - vivo iqoo 9t -> ویوو iQOO 9T
  - vivo iqoo neo5 s -> ویوو iQOO Neo5 S
  - vivo iqoo neo5 se -> ویوو iQOO Neo5 SE
  - vivo iqoo neo 6 -> ویوو iQOO Neo6 هند
  - vivo iqoo neo6 (china) -> ویوو iQOO Neo6 (China)
  - vivo iqoo neo6 se -> ویوو iQOO Neo6 SE
  - vivo iqoo u5 -> ویوو iQOO U5
  - vivo iqoo z6 -> ویوو iQOO Z6
  - vivo iqoo z6 (china) -> ویوو iQOO Z6 چین
  - vivo iqoo z6 lite -> ویوو iQOO Z6 Lite
  - vivo iqoo z6 pro -> ویوو iQOO Z6 پرو
  - vivo iqoo z6x -> ویوو iQOO Z6x
  - vivo s12 -> ویوو S12
  - vivo s12 pro -> ویوو S12 Pro
  - vivo s15 -> ویوو S15
  - vivo s15e -> ویوو S15e
  - vivo t1 5g -> ویوو T1 5G
  - vivo t1 pro -> ویوو T1 پرو
  - vivo t1 (snapdragon 680) -> ویوو T1 اسنپدراگون 680
  - vivo t1 (snapdragon 778g) -> ویوو T1 اسنپدراگون 778G
  - vivo t1x (india) -> ویوو T1x هند
  - vivo t2 -> ویوو T2
  - vivo t2x -> ویوو T2x
  - vivo v25 -> ویوو V25
  - vivo v25e -> ویوو V25e
  - vivo v25 pro -> ویوو V25 Pro
  - vivo x80 pro -> ویوو X80 پرو
  - vivo x fold -> ویوو ایکس فولد
  - vivo y02s -> ویوو Y02s
  - vivo y16 -> ویوو Y16
  - vivo y21g -> ویوو Y21G
  - vivo y22s -> ویوو Y22s
  - vivo y30 5g -> ویوو Y30 5G
  - vivo y32 -> ویوو Y32
  - vivo y33s 5g -> ویوو Y33s 5G
  - vivo y52t -> ویوو Y52t
  - vivo y55 -> ویوو Y55
  - vivo y55s 5g -> ویوو Y55s 5G
  - vivo y75 -> ویوو Y75
  - vivo y75 5g -> ویوو Y75 5G
  - vivo y75s -> ویوو Y75s
  - vivo y77 -> ویوو Y77
  - vivo y77 (china) -> ویوو Y77 چین
  - vivo y77e -> ویوو Y77e
  - vivo y77e (t1) -> ویوو Y77e (t1)
  - vivo iqoo 9 -> ویوو iQOO 9
  - vivo iqoo 9 pro -> ویوو iQOO 9 Pro
  - vivo v23 5g -> ویوو V23 5G
  - vivo v23 pro -> ویوو V23 Pro
  - vivo y21t -> ویوو Y21T
  - vivo y55 5g -> ویوو Y55 5G
  - vivo iqoo u5x -> ویوو iQOO U5x
  - vivo y01 -> ویوو Y01
  - vivo iqoo neo6 -> ویوو iQOO Neo6
  - vivo iqoo z6 44w -> ویوو iQOO Z6 44W
  - vivo t1x 4g -> ویوو T1x 4G
  - vivo x80 -> ویوو X80
  - vivo x note -> ویوو X Note
  - vivo s15 pro -> ویوو S15 Pro
  - vivo y33e -> ویوو Y33e
  - vivo y72t -> ویوو Y72t
  - vivo iqoo u5e -> ویوو iQOO U5e
  - wiko -> ویکو
  - wiko wim -> ویکو WIM
  - wiko wim lite -> ویکو WIM Lite
  - wiko tommy2 -> ویکو Tommy2
  - wiko tommy2 plus -> ویکو Tommy2 Plus
  - wiko view -> ویکو View
  - wiko view prime -> ویکو View Prime
  - wiko view xl -> ویکو View XL
  - wiko view2 -> ویکو View2
  - wiko view2 pro -> ویکو View2 Pro
  - wiko view max -> ویکو View Max
  - wiko view2 go -> ویکو View2 Go
  - wiko view2 plus -> ویکو View2 Plus
  - wiko view3 -> ویکو View3
  - wiko view3 pro -> ویکو View3 Pro
  - xiaomi -> شیائومی
  - xiaomi mi 11x -> شیائومی Mi 11X
  - xiaomi mi 11x pro -> شیائومی Mi 11X Pro
  - xiaomi mi 6c -> شیائومی Mi 6c
  - xiaomi mi 6 plus -> شیائومی Mi 6 Plus
  - xiaomi mi max 4 -> شیائومی Mi Max 4
  - xiaomi mi max 4 pro -> شیائومی Mi Max 4 Pro
  - xiaomi mi mix alpha -> شیائومی Mi Mix Alpha
  - xiaomi mi note plus -> شیائومی Mi Note Plus
  - xiaomi poco m3 pro 5g -> شیائومی Poco M3 Pro 5G
  - xiaomi redmi 20x -> شیائومی Redmi 20X
  - xiaomi redmi pro 2 -> شیائومی Redmi Pro 2
  - xiaomi mi 1s -> شیائومی Mi 1S
  - xiaomi mi 2 -> شیائومی Mi 2
  - xiaomi mi 2a -> شیائومی Mi 2A
  - xiaomi mi 2s -> شیائومی Mi 2S
  - xiaomi mi 3 -> شیائومی Mi 3
  - xiaomi redmi 1s -> شیائومی Redmi 1S
  - xiaomi mi 4 -> شیائومی Mi 4
  - xiaomi redmi note 4g -> شیائومی Redmi Note 4G
  - xiaomi mi 4 lte -> شیائومی Mi 4 LTE
  - xiaomi mi note -> شیائومی Mi Note
  - xiaomi mi note pro -> شیائومی Mi Note Pro
  - xiaomi redmi 2 -> شیائومی Redmi 2
  - xiaomi redmi 2a -> شیائومی Redmi 2A
  - xiaomi mi 4i -> شیائومی Mi 4i
  - xiaomi redmi 2 prime -> شیائومی Redmi 2 Prime
  - xiaomi mi 4c -> شیائومی Mi 4c
  - xiaomi redmi 2 pro -> شیائومی Redmi 2 Pro
  - xiaomi redmi note 3 (mediatek) -> شیائومی Redmi Note 3 (MediaTek)
  - xiaomi redmi note prime -> شیائومی Redmi Note Prime
  - xiaomi redmi 3 -> شیائومی Redmi 3
  - xiaomi mi 4s -> شیائومی Mi 4s
  - xiaomi redmi 3 pro -> شیائومی Redmi 3 Pro
  - xiaomi redmi 3s -> شیائومی Redmi 3s
  - xiaomi redmi 3x -> شیائومی Redmi 3x
  - xiaomi redmi 3s prime -> شیائومی Redmi 3s Prime
  - xiaomi mi 5s -> شیائومی Mi 5s
  - xiaomi mi 5s plus -> شیائومی Mi 5s Plus
  - xiaomi mi mix -> شیائومی Mi Mix
  - xiaomi mi note 2 -> شیائومی Mi Note 2
  - xiaomi redmi 4a -> شیائومی Redmi 4A
  - xiaomi redmi 4 (china) -> شیائومی Redmi 4 (China)
  - xiaomi redmi 4 prime -> شیائومی Redmi 4 Prime
  - xiaomi redmi note 4 -> شیائومی Redmi Note 4
  - xiaomi mi 5c -> شیائومی Mi 5c
  - xiaomi redmi note 4x -> شیائومی Redmi Note 4X
  - xiaomi mi 6 -> شیائومی Mi 6
  - xiaomi mi max 2 -> شیائومی Mi Max 2
  - xiaomi redmi 4 (4x) -> شیائومی Redmi 4 (4X)
  - xiaomi mi a1 (mi 5x) -> شیائومی Mi A1 (Mi 5X)
  - xiaomi mi mix 2 -> شیائومی Mi Mix 2
  - xiaomi mi note 3 -> شیائومی Mi Note 3
  - xiaomi redmi 5a -> شیائومی Redmi 5A
  - xiaomi redmi y1 lite -> شیائومی Redmi Y1 Lite
  - xiaomi redmi y1 (note 5a) -> شیائومی Redmi Y1 (Note 5A)
  - xiaomi redmi 5 -> شیائومی Redmi 5
  - xiaomi redmi 5 plus (redmi note 5) -> شیائومی Redmi 5 Plus (Redmi Note 5)
  - xiaomi redmi note 5 pro -> شیائومی Redmi Note 5 Pro
  - xiaomi mi mix 2s -> شیائومی Mi Mix 2S
  - xiaomi redmi note 5 ai dual camera -> شیائومی Redmi Note 5 AI Dual Camera
  - xiaomi black shark -> شیائومی Black Shark
  - xiaomi mi 8 -> شیائومی Mi 8
  - xiaomi mi 8 explorer -> شیائومی Mi 8 Explorer
  - xiaomi mi 8 se -> شیائومی Mi 8 SE
  - xiaomi redmi s2 (redmi y2) -> شیائومی Redmi S2 (Redmi Y2)
  - xiaomi redmi 6 -> شیائومی Redmi 6
  - xiaomi redmi 6a -> شیائومی Redmi 6A
  - xiaomi mi a2 lite (redmi 6 pro) -> شیائومی Mi A2 Lite (Redmi 6 Pro)
  - xiaomi mi a2 (mi 6x) -> شیائومی Mi A2 (Mi 6X)
  - xiaomi mi max 3 -> شیائومی Mi Max 3
  - xiaomi pocophone f1 -> شیائومی Pocophone F1
  - xiaomi mi 8 lite -> شیائومی Mi 8 Lite
  - xiaomi mi 8 pro -> شیائومی Mi 8 Pro
  - xiaomi redmi note 6 pro -> شیائومی Redmi Note 6 Pro
  - xiaomi black shark helo -> شیائومی Black Shark Helo
  - xiaomi mi mix 3 -> شیائومی Mi Mix 3
  - xiaomi mi play -> شیائومی Mi Play
  - xiaomi redmi 7 -> شیائومی ردمی 7
  - xiaomi redmi k20 pro -> شیائومی می 9 تی پرو (ردمی K20 پرو)
  - xiaomi redmi go -> شیائومی Redmi Go
  - xiaomi redmi note 7 -> شیائومی Redmi Note 7
  - xiaomi mi 9 -> شیائومی Mi 9
  - xiaomi mi 9 explorer -> شیائومی Mi 9 Explorer
  - xiaomi mi 9 se -> شیائومی Mi 9 SE
  - xiaomi mi mix 3 5g -> شیائومی Mi Mix 3 5G
  - xiaomi redmi note 7 pro -> شیائومی Redmi Note 7 Pro
  - xiaomi black shark 2 -> شیائومی Black Shark 2
  - xiaomi redmi k20 -> شیائومی می 9 تی (ردمی K20)
  - xiaomi redmi y3 -> شیائومی Redmi Y3
  - xiaomi redmi 7a -> شیائومی Redmi 7A
  - xiaomi redmi note 7s -> شیائومی Redmi Note 7S
  - xiaomi mi 9t -> شیائومی Mi 9T
  - xiaomi black shark 2 pro -> شیائومی Black Shark 2 Pro
  - xiaomi mi a3 -> شیائومی Mi A3
  - xiaomi mi cc9 -> شیائومی Mi CC9
  - xiaomi mi cc9e -> شیائومی Mi CC9e
  - xiaomi mi 9t pro -> شیائومی Mi 9T Pro
  - xiaomi redmi note 8 -> شیائومی Redmi Note 8
  - xiaomi redmi note 8 pro -> شیائومی Redmi Note 8 Pro
  - xiaomi mi 9 lite -> شیائومی Mi 9 Lite
  - xiaomi mi 9 pro -> شیائومی Mi 9 Pro
  - xiaomi mi 9 pro 5g -> شیائومی Mi 9 Pro 5G
  - xiaomi redmi 8a -> شیائومی Redmi 8A
  - xiaomi redmi k20 pro premium -> شیائومی Redmi K20 Pro Premium
  - xiaomi redmi 8 -> شیائومی Redmi 8
  - xiaomi mi cc9 pro -> شیائومی Mi CC9 Pro
  - xiaomi mi note 10 -> شیائومی Mi Note 10
  - xiaomi mi note 10 pro -> شیائومی Mi Note 10 Pro
  - xiaomi redmi note 8t -> شیائومی Redmi Note 8T
  - xiaomi redmi k30 -> شیائومی Redmi K30
  - xiaomi redmi k30 5g -> شیائومی Redmi K30 5G
  - xiaomi mi 10 5g -> شیائومی Mi 10 5G
  - xiaomi mi 10 pro 5g -> شیائومی Mi 10 Pro 5G
  - xiaomi poco x2 -> شیائومی Poco X2
  - xiaomi redmi 8a dual -> شیائومی Redmi 8A Dual
  - xiaomi black shark 3 -> شیائومی Black Shark 3
  - xiaomi black shark 3 pro -> شیائومی Black Shark 3 Pro
  - xiaomi mi 10 lite 5g -> شیائومی Mi 10 Lite 5G
  - xiaomi redmi k30 pro -> شیائومی Redmi K30 Pro
  - xiaomi redmi k30 pro zoom -> شیائومی Redmi K30 Pro Zoom
  - xiaomi redmi note 9 pro (india) -> شیائومی Redmi Note 9 Pro (India)
  - xiaomi redmi note 9 pro max -> شیائومی Redmi Note 9 Pro Max
  - xiaomi redmi note 9s -> شیائومی Redmi Note 9S
  - xiaomi mi 10 youth 5g -> شیائومی Mi 10 Youth 5G
  - xiaomi mi note 10 lite -> شیائومی Mi Note 10 Lite
  - xiaomi redmi 8a pro -> شیائومی Redmi 8A Pro
  - xiaomi redmi note 9 -> شیائومی Redmi Note 9
  - xiaomi redmi note 9 pro -> شیائومی Redmi Note 9 Pro
  - xiaomi poco f2 pro -> شیائومی Poco F2 Pro
  - xiaomi redmi 10x 4g -> شیائومی Redmi 10X 4G
  - xiaomi redmi 10x 5g -> شیائومی Redmi 10X 5G
  - xiaomi redmi 10x pro 5g -> شیائومی Redmi 10X Pro 5G
  - xiaomi redmi k30 5g racing -> شیائومی Redmi K30 5G Racing
  - xiaomi redmi k30i 5g -> شیائومی Redmi K30i 5G
  - xiaomi redmi 9 -> شیائومی Redmi 9
  - xiaomi redmi 9a -> شیائومی Redmi 9A
  - xiaomi redmi 9c -> شیائومی Redmi 9C
  - xiaomi black shark 3s -> شیائومی Black Shark 3S
  - xiaomi poco m2 pro -> شیائومی Poco M2 Pro
  - xiaomi mi 10 ultra -> شیائومی Mi 10 Ultra
  - xiaomi redmi 9c nfc -> شیائومی Redmi 9C NFC
  - xiaomi redmi 9 (india) -> شیائومی Redmi 9 (India)
  - xiaomi redmi 9 prime -> شیائومی Redmi 9 Prime
  - xiaomi redmi k30 ultra -> شیائومی Redmi K30 Ultra
  - xiaomi mi 10t 5g -> شیائومی Mi 10T 5G
  - xiaomi mi 10t lite 5g -> شیائومی Mi 10T Lite 5G
  - xiaomi mi 10t pro 5g -> شیائومی Mi 10T Pro 5G
  - xiaomi poco m2 -> شیائومی Poco M2
  - xiaomi poco x3 -> شیائومی Poco X3
  - xiaomi poco x3 nfc -> شیائومی Poco X3 NFC
  - xiaomi redmi 9at -> شیائومی Redmi 9AT
  - xiaomi redmi 9i -> شیائومی Redmi 9i
  - xiaomi poco c3 -> شیائومی Poco C3
  - xiaomi redmi k30s -> شیائومی Redmi K30S
  - xiaomi poco m3 -> شیائومی Poco M3
  - xiaomi redmi note 9 4g -> شیائومی Redmi Note 9 4G
  - xiaomi redmi note 9 5g -> شیائومی Redmi Note 9 5G
  - xiaomi redmi note 9 pro 5g -> شیائومی Redmi Note 9 Pro 5G
  - xiaomi mi 11 -> شیائومی Mi 11
  - xiaomi poco m4 pro 5g -> شیائومی پوکو M4 پرو 5G
  - xiaomi redmi 9a sport -> شیائومی Redmi 9A Sport
  - xiaomi redmi 9i sport -> شیائومی Redmi 9i Sport
  - xiaomi redmi 9 power -> شیائومی Redmi 9 Power
  - xiaomi redmi note 10 pro (india) -> شیائومی ردمی نوت 10 پرو هند
  - xiaomi redmi note 11 (china) -> شیائومی Redmi Note 11 (China)
  - xiaomi redmi note 11t 5g -> شیائومی ردمی نوت 11 تی 5G
  - xiaomi mi 10i 5g -> شیائومی Mi 10i 5G
  - xiaomi redmi 9t -> شیائومی Redmi 9T
  - xiaomi redmi note 9t -> شیائومی Redmi Note 9T
  - xiaomi redmi k40 -> شیائومی Redmi K40
  - xiaomi redmi k40 pro -> شیائومی Redmi K40 Pro
  - xiaomi redmi k40 pro+ -> شیائومی Redmi K40 Pro+
  - xiaomi black shark 4 -> شیائومی Black Shark 4
  - xiaomi black shark 4 pro -> شیائومی Black Shark 4 Pro
  - xiaomi mi 10s -> شیائومی Mi 10S
  - xiaomi mi 11i -> شیائومی Mi 11i
  - xiaomi mi 11 lite -> شیائومی Mi 11 Lite
  - xiaomi mi 11 lite 5g -> شیائومی Mi 11 Lite 5G
  - xiaomi mi 11 pro -> شیائومی Mi 11 Pro
  - xiaomi mi 11 ultra -> شیائومی Mi 11 Ultra
  - xiaomi mi mix fold -> شیائومی Mi Mix Fold
  - xiaomi poco f3 -> شیائومی Poco F3
  - xiaomi poco x3 pro -> شیائومی Poco X3 Pro
  - xiaomi redmi note 10 -> شیائومی Redmi Note 10
  - xiaomi redmi note 10 5g -> شیائومی Redmi Note 10 5G
  - xiaomi redmi note 10 pro -> شیائومی Redmi Note 10 Pro
  - xiaomi redmi note 10 pro max -> شیائومی Redmi Note 10 Pro Max
  - xiaomi redmi note 10s -> شیائومی Redmi Note 10S
  - xiaomi redmi note 10 pro (china) -> شیائومی Redmi Note 10 Pro (China)
  - xiaomi poco f3 gt -> شیائومی Poco F3 GT
  - xiaomi poco x3 gt -> شیائومی Poco X3 GT
  - xiaomi redmi note 10t 5g -> شیائومی Redmi Note 10T 5G
  - xiaomi mix 4 -> شیائومی Mix 4
  - xiaomi redmi 10 -> شیائومی Redmi 10
  - xiaomi 11 lite 5g ne -> شیائومی 11 Lite 5G NE
  - xiaomi 11t -> شیائومی 11T
  - xiaomi 11t pro -> شیائومی 11T Pro
  - xiaomi civi -> شیائومی Civi
  - xiaomi poco c31 -> شیائومی Poco C31
  - xiaomi redmi 10 prime -> شیائومی Redmi 10 Prime
  - xiaomi redmi 9 activ -> شیائومی Redmi 9 Activ
  - xiaomi black shark 4s -> شیائومی Black Shark 4S
  - xiaomi black shark 4s pro -> شیائومی Black Shark 4S Pro
  - xiaomi redmi note 10 lite -> شیائومی Redmi Note 10 Lite
  - xiaomi redmi note 11 pro+ -> شیائومی Redmi Note 11 Pro+
  - xiaomi redmi note 11 pro+ 5g -> شیائومی Redmi Note 11 Pro+ 5G
  - xiaomi redmi note 11 pro (china) -> شیائومی Redmi Note 11 Pro (China)
  - xiaomi redmi note 11 4g -> شیائومی Redmi Note 11 4G
  - xiaomi 11i -> شیائومی 11i
  - xiaomi 11i hypercharge 5g -> شیائومی 11i HyperCharge 5G
  - xiaomi 12 -> شیائومی 12
  - xiaomi 12 pro -> شیائومی 12 Pro
  - xiaomi 12x -> شیائومی 12X
  - xiaomi poco f4 gt -> شیائومی پوکو F4 GT
  - xiaomi poco m4 5g -> شیائومی پوکو M4 5G هند
  - xiaomi poco x4 pro 5g -> شیائومی پوکو X4 پرو 5G
  - xiaomi redmi 10 (india) -> شیائومی ردمی 10 هند
  - xiaomi redmi k50 gaming -> شیائومی ردمی K50 گیمینگ
  - xiaomi redmi k50 pro -> شیائومی ردمی K50 پرو
  - xiaomi redmi note 11 pro+ 5g (india) -> شیائومی Redmi Note 11 Pro+ 5G (India)
  - xiaomi redmi note 11s 5g -> شیائومی ردمی نوت 11 اس 5G
  - xiaomi redmi note 11 -> شیائومی Redmi Note 11
  - xiaomi redmi note 11 pro -> شیائومی Redmi Note 11 Pro
  - xiaomi redmi note 11 pro 5g -> شیائومی Redmi Note 11 Pro 5G
  - xiaomi redmi note 11s -> شیائومی Redmi Note 11S
  - xiaomi poco m4 pro -> شیائومی Poco M4 Pro
  - xiaomi redmi 10 2022 -> شیائومی Redmi 10 2022
  - xiaomi black shark 5 -> شیائومی Black Shark 5
  - xiaomi black shark 5 pro -> شیائومی Black Shark 5 Pro
  - xiaomi black shark 5 rs -> شیائومی Black Shark 5 RS
  - xiaomi redmi 10 5g -> شیائومی Redmi 10 5G
  - xiaomi redmi 10a -> شیائومی Redmi 10A
  - xiaomi redmi 10c -> شیائومی Redmi 10C
  - xiaomi redmi k40s -> شیائومی Redmi K40S
  - xiaomi redmi k50 -> شیائومی Redmi K50
  - xiaomi redmi note 11e -> شیائومی Redmi Note 11E
  - xiaomi redmi note 11e pro -> شیائومی Redmi Note 11E Pro
  - xiaomi civi 1s -> شیائومی Civi 1S
  - xiaomi redmi 10 power -> شیائومی Redmi 10 Power
  - xiaomi redmi 10 prime 2022 -> شیائومی Redmi 10 Prime 2022
  - xiaomi redmi note 11se -> شیائومی Redmi Note 11SE
  - xiaomi redmi note 11t pro -> شیائومی Redmi Note 11T Pro
  - xiaomi redmi note 11t pro+ -> شیائومی Redmi Note 11T Pro+
  - xiaomi poco f4 -> شیائومی Poco F4
  - xiaomi poco x4 gt -> شیائومی Poco X4 GT
  - xiaomi 12 pro (dimensity) -> شیائومی 12 Pro (Dimensity)
  - xiaomi 12s -> شیائومی 12S
  - xiaomi 12s pro -> شیائومی 12S Pro
  - yota -> یوتا
  - yota yotaphone -> یوتا YotaPhone
  - yota yotaphone 2 -> یوتا YotaPhone 2
  - yota yotaphone 3 -> یوتا YotaPhone 3
  - zte -> زد تی ای
  - zte blade v20 -> زد تی ای Blade V20
  - zte hawkeye -> زد تی ای Hawkeye
  - zte nubia x 5g -> زد تی ای nubia X 5G
  - zte open l -> زد تی ای Open L
  - zte xiang -> زد تی ای Xiang
  - zte v9 -> زد تی ای V9
  - zte skate -> زد تی ای Skate
  - zte v9+ -> زد تی ای V9+
  - zte racer ii -> زد تی ای Racer II
  - zte tania -> زد تی ای Tania
  - zte warp -> زد تی ای Warp
  - zte avail -> زد تی ای Avail
  - zte chorus -> زد تی ای Chorus
  - zte era -> زد تی ای Era
  - zte grand x v970 -> زد تی ای Grand X V970
  - zte kis v788 -> زد تی ای Kis V788
  - zte nova 3.5 -> زد تی ای Nova 3.5
  - zte nova 4 v8000 -> زد تی ای Nova 4 V8000
  - zte optik -> زد تی ای Optik
  - zte orbit -> زد تی ای Orbit
  - zte pf 100 -> زد تی ای PF 100
  - zte pf112 hd -> زد تی ای PF112 HD
  - zte skate acqua -> زد تی ای Skate Acqua
  - zte t98 -> زد تی ای T98
  - zte v880e -> زد تی ای V880E
  - zte v96 -> زد تی ای V96
  - zte n880e -> زد تی ای N880E
  - zte u880e -> زد تی ای U880E
  - zte grand x lte t82 -> زد تی ای Grand X LTE T82
  - zte grand x in -> زد تی ای Grand X IN
  - zte anthem 4g -> زد تی ای Anthem 4G
  - zte blade iii -> زد تی ای Blade III
  - zte grand era u895 -> زد تی ای Grand Era U895
  - zte warp sequent -> زد تی ای Warp Sequent
  - zte flash -> زد تی ای Flash
  - zte groove x501 -> زد تی ای Groove X501
  - zte kis iii v790 -> زد تی ای Kis III V790
  - zte nubia z5 -> زد تی ای نوبیا Z5
  - zte v887 -> زد تی ای V887
  - zte v889m -> زد تی ای V889M
  - zte avid 4g -> زد تی ای Avid 4G
  - zte v81 -> زد تی ای V81
  - zte blade c v807 -> زد تی ای Blade C V807
  - zte grand memo v9815 -> زد تی ای گرند Memo V9815
  - zte grand s -> زد تی ای Grand S
  - zte director -> زد تی ای Director
  - zte geek v975 -> زد تی ای Geek V975
  - zte grand x pro -> زد تی ای Grand X Pro
  - zte blade g v880g -> زد تی ای Blade G V880G
  - zte grand x2 in -> زد تی ای گرند X2 In
  - zte imperial -> زد تی ای Imperial
  - zte vital n9810 -> زد تی ای Vital N9810
  - zte grand x quad v987 -> زد تی ای Grand X Quad V987
  - zte blade g2 -> زد تی ای Blade G2
  - zte reef -> زد تی ای Reef
  - zte blade v -> زد تی ای بلید V
  - zte warp 4g -> زد تی ای Warp 4G
  - zte blade q -> زد تی ای Blade Q
  - zte blade q maxi -> زد تی ای Blade Q Maxi
  - zte blade q mini -> زد تی ای Blade Q Mini
  - zte grand s flex -> زد تی ای گرند S Flex
  - zte nubia z5s -> زد تی ای نوبیا Z5S
  - zte nubia z5s mini nx403a -> زد تی ای nubia Z5S mini NX403A
  - zte grand s ii s291 -> زد تی ای Grand S II S291
  - zte iconic phablet -> زد تی ای Iconic Phablet
  - zte sonata 4g -> زد تی ای Sonata 4G
  - zte grand memo ii lte -> زد تی ای Grand Memo II LTE
  - zte open c -> زد تی ای Open C
  - zte open ii -> زد تی ای Open II
  - zte nubia x6 -> زد تی ای nubia X6
  - zte redbull v5 v9180 -> زد تی ای Redbull V5 V9180
  - zte star 1 -> زد تی ای Star 1
  - zte blade l2 -> زد تی ای Blade L2
  - zte kis 3 -> زد تی ای Kis 3
  - zte grand s pro -> زد تی ای Grand S Pro
  - zte nubia z7 -> زد تی ای nubia Z7
  - zte nubia z7 max -> زد تی ای nubia Z7 Max
  - zte nubia z7 mini -> زد تی ای nubia Z7 mini
  - zte nubia z5s mini nx405h -> زد تی ای nubia Z5S mini NX405H
  - zte blade vec 3g -> زد تی ای Blade Vec 3G
  - zte blade vec 4g -> زد تی ای Blade Vec 4G
  - zte kis 3 max -> زد تی ای Kis 3 Max
  - zte zmax -> زد تی ای Zmax
  - zte grand xmax -> زد تی ای Grand Xmax
  - zte zinger -> زد تی ای Zinger
  - zte grand s ii -> زد تی ای Grand S II
  - zte grand x plus z826 -> زد تی ای Grand X Plus Z826
  - zte speed -> زد تی ای Speed
  - zte star 2 -> زد تی ای Star 2
  - zte blade q pro -> زد تی ای Blade Q Pro
  - zte blade s6 -> زد تی ای Blade S6
  - zte grand x max+ -> زد تی ای Grand X Max+
  - zte imperial ii -> زد تی ای Imperial II
  - zte blade g -> زد تی ای Blade G
  - zte blade g lux -> زد تی ای Blade G Lux
  - zte blade l3 -> زد تی ای Blade L3
  - zte v5 lux -> زد تی ای V5 Lux
  - zte blade l3 plus -> زد تی ای Blade L3 Plus
  - zte grand s3 -> زد تی ای Grand S3
  - zte nubia z9 max -> زد تی ای nubia Z9 Max
  - zte nubia z9 mini -> زد تی ای nubia Z9 mini
  - zte blade s6 plus -> زد تی ای Blade S6 Plus
  - zte nubia z9 -> زد تی ای نوبیا Z9
  - zte blade a410 -> زد تی ای Blade A410
  - zte blade a460 -> زد تی ای Blade A460
  - zte blade apex 3 -> زد تی ای Blade Apex 3
  - zte blade qlux 4g -> زد تی ای Blade Qlux 4G
  - zte maven -> زد تی ای Maven
  - zte nubia my prague -> زد تی ای nubia My Prague
  - zte sonata 2 -> زد تی ای Sonata 2
  - zte axon lux -> زد تی ای Axon Lux
  - zte axon pro -> زد تی ای Axon Pro
  - zte blade d6 -> زد تی ای Blade D6
  - zte boost max+ -> زد تی ای Boost Max+
  - zte grand x2 -> زد تی ای Grand X2
  - zte obsidian -> زد تی ای Obsidian
  - zte axon -> زد تی ای اکسون
  - zte axon elite -> زد تی ای Axon Elite
  - zte zmax 2 -> زد تی ای Zmax 2
  - zte axon mini -> زد تی ای Axon mini
  - zte blade s7 -> زد تی ای Blade S7
  - zte blade x3 -> زد تی ای Blade X3
  - zte blade x5 -> زد تی ای Blade X5
  - zte blade x9 -> زد تی ای Blade X9
  - zte axon max -> زد تی ای Axon Max
  - zte avid plus -> زد تی ای Avid Plus
  - zte blade a452 -> زد تی ای Blade A452
  - zte blade v plus -> زد تی ای Blade V Plus
  - zte grand x 3 -> زد تی ای Grand X 3
  - zte nubia prague s -> زد تی ای nubia Prague S
  - zte blade v7 -> زد تی ای Blade V7
  - zte blade v7 lite -> زد تی ای Blade V7 Lite
  - zte blade a910 -> زد تی ای Blade A910
  - zte blade l5 plus -> زد تی ای Blade L5 Plus
  - zte blade v7 max -> زد تی ای Blade V7 Max
  - zte nubia z11 mini -> زد تی ای nubia Z11 mini
  - zte axon 7 -> زد تی ای Axon 7
  - zte grand x max 2 -> زد تی ای Grand X Max 2
  - zte blade a2 -> زد تی ای Blade A2
  - zte blade a601 -> زد تی ای Blade A601
  - zte nubia z11 -> زد تی ای nubia Z11
  - zte nubia z11 max -> زد تی ای nubia Z11 Max
  - zte blade a512 -> زد تی ای Blade A512
  - zte blade l110 (a110) -> زد تی ای Blade L110 (A110)
  - zte nubia n1 -> زد تی ای nubia N1
  - zte zmax pro -> زد تی ای Zmax Pro
  - zte blade a610 -> زد تی ای Blade A610
  - zte warp 7 -> زد تی ای Warp 7
  - zte axon 7 max -> زد تی ای اکسون 7 مکس
  - zte axon 7 mini -> زد تی ای Axon 7 mini
  - zte grand x4 -> زد تی ای Grand X4
  - zte nubia z11 mini s -> زد تی ای nubia Z11 mini S
  - zte blade v8 -> زد تی ای Blade V8
  - zte blade v8 pro -> زد تی ای Blade V8 Pro
  - zte blade a2 plus -> زد تی ای Blade A2 Plus
  - zte blade v8 lite -> زد تی ای Blade V8 Lite
  - zte blade v8 mini -> زد تی ای Blade V8 Mini
  - zte nubia n1 lite -> زد تی ای nubia N1 lite
  - zte blade a520 -> زد تی ای Blade A520
  - zte nubia m2 -> زد تی ای nubia M2
  - zte nubia m2 lite -> زد تی ای nubia M2 lite
  - zte nubia n2 -> زد تی ای nubia N2
  - zte quartz -> زد تی ای Quartz
  - zte axon 7s -> زد تی ای Axon 7s
  - zte max xl -> زد تی ای Max XL
  - zte nubia z17 mini -> زد تی ای nubia Z17 mini
  - zte grand x view 2 -> زد تی ای گرند X View 2
  - zte nubia m2 play -> زد تی ای nubia M2 Play
  - zte nubia z17 -> زد تی ای nubia Z17
  - zte blade v7 plus -> زد تی ای Blade V7 Plus
  - zte blade z max -> زد تی ای Blade Z Max
  - zte maven 2 -> زد تی ای Maven 2
  - zte blade a6 -> زد تی ای Blade A6
  - zte nubia z17 lite -> زد تی ای nubia Z17 lite
  - zte tempo x -> زد تی ای Tempo X
  - zte axon m -> زد تی ای Axon M
  - zte blade force -> زد تی ای Blade Force
  - zte blade x -> زد تی ای Blade X
  - zte nubia z17 minis -> زد تی ای nubia Z17 miniS
  - zte nubia z17s -> زد تی ای nubia Z17s
  - zte blade a3 -> زد تی ای Blade A3
  - zte blade v9 -> زد تی ای Blade V9
  - zte blade v9 vita -> زد تی ای Blade V9 Vita
  - zte tempo go -> زد تی ای Tempo Go
  - zte nubia n3 -> زد تی ای nubia N3
  - zte nubia v18 -> زد تی ای nubia V18
  - zte nubia red magic -> زد تی ای nubia Red Magic
  - zte nubia z18 mini -> زد تی ای nubia Z18 mini
  - zte axon 9 pro -> زد تی ای Axon 9 Pro
  - zte nubia z18 -> زد تی ای nubia Z18
  - zte nubia x -> زد تی ای nubia X
  - zte nubia red magic mars -> زد تی ای nubia Red Magic Mars
  - zte blade a7 vita -> زد تی ای Blade A7 Vita
  - zte blade max view -> زد تی ای Blade Max View
  - zte nubia alpha -> زد تی ای نوبیا آلفا
  - zte avid 559 -> زد تی ای Avid 559
  - zte axon 10 pro -> زد تی ای Axon 10 Pro
  - zte axon 10 pro 5g -> زد تی ای Axon 10 Pro 5G
  - zte blade v10 -> زد تی ای Blade V10
  - zte blade v10 vita -> زد تی ای Blade V10 Vita
  - zte blade a3 (2019) -> زد تی ای Blade A3 (2019)
  - zte blade a5 (2019) -> زد تی ای Blade A5 (2019)
  - zte blade l8 -> زد تی ای Blade L8
  - zte blade a7 -> زد تی ای Blade A7
  - zte nubia red magic 3 -> زد تی ای nubia Red Magic 3
  - zte nubia z20 -> زد تی ای nubia Z20
  - zte blade 20 -> زد تی ای Blade 20
  - zte blade vantage 2 -> زد تی ای Blade Vantage 2
  - zte nubia red magic 3s -> زد تی ای nubia Red Magic 3s
  - zte blade 10 prime -> زد تی ای Blade 10 Prime
  - zte blade a7 prime -> زد تی ای Blade A7 Prime
  - zte avid 579 -> زد تی ای Avid 579
  - zte axon 20 5g extreme -> زد تی ای Axon 20 5G Extreme
  - zte blade 20 5g -> زد تی ای Blade 20 5G
  - zte blade a3y -> زد تی ای Blade A3Y
  - zte blade a5 2020 -> زد تی ای Blade A5 2020
  - zte blade v2020 5g -> زد تی ای بلید V2020 5G
  - zte cymbal 2 -> زد تی ای Cymbal 2
  - zte axon 10s pro 5g -> زد تی ای Axon 10s Pro 5G
  - zte axon 11 5g -> زد تی ای Axon 11 5G
  - zte nubia red magic 5g -> زد تی ای nubia Red Magic 5G
  - zte nubia play -> زد تی ای nubia Play
  - zte blade a3 joy -> زد تی ای Blade A3 Joy
  - zte blade a3 prime -> زد تی ای Blade A3 Prime
  - zte axon 11 4g -> زد تی ای Axon 11 4G
  - zte nubia red magic 5g lite -> زد تی ای nubia Red Magic 5G Lite
  - zte gabb z2 -> زد تی ای Gabb Z2
  - zte nubia red magic 5s -> زد تی ای nubia Red Magic 5S
  - zte quest 5 -> زد تی ای Quest 5
  - zte axon 20 5g -> زد تی ای Axon 20 5G
  - zte axon 20 4g -> زد تی ای Axon 20 4G
  - zte blade 20 pro 5g -> زد تی ای Blade 20 Pro 5G
  - zte blade a7s 2020 -> زد تی ای Blade A7s 2020
  - zte avid 589 -> زد تی ای Avid 589
  - zte blade 11 prime -> زد تی ای Blade 11 Prime
  - zte blade a31 -> زد تی ای Blade A31
  - zte blade a31 plus -> زد تی ای Blade A31 Plus
  - zte blade a51 -> زد تی ای Blade A51
  - zte cymbal u -> زد تی ای Cymbal U
  - zte link ii -> زد تی ای Link II
  - zte nubia z30 pro -> زد تی ای nubia Z30 Pro
  - zte s30 -> زد تی ای S30
  - zte s30 pro -> زد تی ای S30 Pro
  - zte s30 se -> زد تی ای S30 SE
  - zte blade x1 5g -> زد تی ای Blade X1 5G
  - zte nubia red magic 6 -> زد تی ای nubia Red Magic 6
  - zte nubia red magic 6 pro -> زد تی ای nubia Red Magic 6 Pro
  - zte axon 30 pro 5g -> زد تی ای Axon 30 Pro 5G
  - zte axon 30 ultra 5g -> زد تی ای Axon 30 Ultra 5G
  - zte nubia red magic 6r -> زد تی ای nubia Red Magic 6R
  - zte axon 30 5g -> زد تی ای Axon 30 5G
  - zte blade v30 -> زد تی ای Blade V30
  - zte blade v30 vita -> زد تی ای Blade V30 Vita
  - zte nubia red magic 6s -> زد تی ای nubia Red Magic 6s
  - zte nubia red magic 6s pro -> زد تی ای nubia Red Magic 6s Pro
  - zte blade a71 -> زد تی ای Blade A71
  - zte blade l9 -> زد تی ای Blade L9
  - zte blade a7p -> زد تی ای Blade A7P
  - zte voyage 20 pro -> زد تی ای Voyage 20 Pro
  - zte axon 40 ultra -> زد تی ای اکسون 40 اولترا
  - zte blade a3 plus -> زد تی ای Blade A3 Plus
  - zte nubia red magic 7 -> زد تی ای نوبیا رد مجیک 7
  - zte nubia red magic 7 pro -> زد تی ای nubia Red Magic 7 Pro
  - zte nubia red magic 7s -> زد تی ای نوبیا رد مجیک 7S
  - zte nubia red magic 7s pro -> زد تی ای نوبیا رد مجیک 7S پرو
  - zte nubia z40 pro -> زد تی ای nubia Z40 Pro
  - zte nubia z40s pro -> زد تی ای nubia Z40S Pro
  - zte blade v40 vita -> زد تی ای Blade V40 Vita
  - zte axon 40 pro -> زد تی ای Axon 40 pro
  - zte blade a52 -> زد تی ای Blade A52
  - zte blade a72 -> زد تی ای Blade A72
  - others -> سایر

### category
- **Title**: دسته‌بندی
- **Type**: object

### divider
- **Title**: سایر فیلتر‌ها
- **Type**: object

### exchange
- **Title**: نمایش معاوضه‌ها
- **Type**: object
- **Queries**: 
  - only-exchanges -> نمایش فقط معاوضه‌ها
  - exclude-exchanges -> حذف معاوضه‌ها

### goods-business-type
- **Title**: نوع آگهی‌دهنده
- **Type**: object
- **Queries**: 
  - all -> همه
  - personal -> شخصی
  - marketplace -> فروشگاه

### has-photo
- **Title**: فقط عکس‌دار
- **Type**: boolean

### has_installment_sale
- **Title**: امکان خرید اقساطی
- **Type**: boolean

### internal_storage
- **Title**: حافظهٔ داخلی
- **Type**: object
 - **Items Type**: array
- **Queries**: 
  - 512MB -> ۵۱۲ مگابایت
  - 1GB -> ۱ گیگابایت
  - 2GB -> ۲ گیگابایت
  - 3GB -> ۳ گیگابایت
  - 4GB -> ۴ گیگابایت
  - 8GB -> ۸ گیگابایت
  - 13GB -> ۱۳ گیگابایت
  - 16GB -> ۱۶ گیگابایت
  - 20GB -> ۲۰ گیگابایت
  - 32GB -> ۳۲ گیگابایت
  - 64GB -> ۶۴ گیگابایت
  - 128GB -> ۱۲۸ گیگابایت
  - 256GB -> ۲۵۶ گیگابایت
  - 512GB -> ۵۱۲ گیگابایت
  - 640GB -> ۶۴۰ گیگابایت
  - 1TB -> ۱ ترابایت

### originality
- **Title**: اصالت برند
- **Type**: object
- **Queries**: 
  - original -> اصل
  - fake -> غیر اصل

### price
- **Title**: قیمت
- **Type**: object
 - **Minimum**: 0
 - **Maximum**: N/A

### ram_memory
- **Title**: مقدار رم
- **Type**: object
 - **Items Type**: array
- **Queries**: 
  - 512MB -> ۵۱۲ مگابایت
  - 768MB -> ۷۶۸ مگابایت
  - 1GB -> ۱ گیگابایت
  - 1.5GB -> ۱.۵ گیگابایت
  - 2GB -> ۲ گیگابایت
  - 3GB -> ۳ گیگابایت
  - 4GB -> ۴ گیگابایت
  - 6GB -> ۶ گیگابایت
  - 8GB -> ۸ گیگابایت
  - 10GB -> ۱۰ گیگابایت
  - 12GB -> ۱۲ گیگابایت
  - 16GB -> ۱۶ گیگابایت
  - 18GB -> ۱۸ گیگابایت

### sim_card_slot
- **Title**: تعداد سیم‌کارت
- **Type**: object
 - **Items Type**: array
- **Queries**: 
  - 1 -> ۱
  - 2 -> ۲
  - +3 -> ۳ و بیشتر

### sort
- **Title**: ترتیب نمایش آگهی‌ها براساس
- **Type**: object
- **Queries**: 
  - quality_and_sort_date -> quality_and_sort_date
  - sort_date -> sort_date
  - cheapest -> cheapest
  - most_expensive -> most_expensive
  - production_year -> production_year
  - usage -> usage
  - most_popular -> most_popular
  - most_relevant -> most_relevant

### status
- **Title**: وضعیت کالا
- **Type**: object
 - **Items Type**: array
- **Queries**: 
  - new -> نو
  - like-new -> در حد نو
  - used -> کارکرده
  - repair-needed -> نیازمند تعمیر

### urgent
- **Title**: فقط فوری‌ها
- **Type**: boolean



---

### Category: mobile-tablet



### category
- **Title**: دسته‌بندی
- **Type**: object

### divider
- **Title**: سایر فیلتر‌ها
- **Type**: object

### exchange
- **Title**: نمایش معاوضه‌ها
- **Type**: object
- **Queries**: 
  - only-exchanges -> نمایش فقط معاوضه‌ها
  - exclude-exchanges -> حذف معاوضه‌ها

### goods-business-type
- **Title**: نوع آگهی‌دهنده
- **Type**: object
- **Queries**: 
  - all -> همه
  - personal -> شخصی
  - marketplace -> فروشگاه

### has-photo
- **Title**: فقط عکس‌دار
- **Type**: boolean

### price
- **Title**: قیمت
- **Type**: object
 - **Minimum**: 0
 - **Maximum**: N/A

### sort
- **Title**: ترتیب نمایش آگهی‌ها براساس
- **Type**: object
- **Queries**: 
  - quality_and_sort_date -> quality_and_sort_date
  - sort_date -> sort_date
  - cheapest -> cheapest
  - most_expensive -> most_expensive
  - production_year -> production_year
  - usage -> usage
  - most_popular -> most_popular
  - most_relevant -> most_relevant

### status
- **Title**: وضعیت کالا
- **Type**: object
 - **Items Type**: array
- **Queries**: 
  - new -> نو
  - like-new -> در حد نو
  - used -> کارکرده
  - repair-needed -> نیازمند تعمیر

### urgent
- **Title**: فقط فوری‌ها
- **Type**: boolean



---

### Category: mobile-tablet-accessories



### category
- **Title**: دسته‌بندی
- **Type**: object

### divider
- **Title**: سایر فیلتر‌ها
- **Type**: object

### exchange
- **Title**: نمایش معاوضه‌ها
- **Type**: object
- **Queries**: 
  - only-exchanges -> نمایش فقط معاوضه‌ها
  - exclude-exchanges -> حذف معاوضه‌ها

### goods-business-type
- **Title**: نوع آگهی‌دهنده
- **Type**: object
- **Queries**: 
  - all -> همه
  - personal -> شخصی
  - marketplace -> فروشگاه

### has-photo
- **Title**: فقط عکس‌دار
- **Type**: boolean

### price
- **Title**: قیمت
- **Type**: object
 - **Minimum**: 0
 - **Maximum**: N/A

### sort
- **Title**: ترتیب نمایش آگهی‌ها براساس
- **Type**: object
- **Queries**: 
  - quality_and_sort_date -> quality_and_sort_date
  - sort_date -> sort_date
  - cheapest -> cheapest
  - most_expensive -> most_expensive
  - production_year -> production_year
  - usage -> usage
  - most_popular -> most_popular
  - most_relevant -> most_relevant

### status
- **Title**: وضعیت کالا
- **Type**: object
 - **Items Type**: array
- **Queries**: 
  - new -> نو
  - like-new -> در حد نو
  - used -> کارکرده
  - repair-needed -> نیازمند تعمیر

### urgent
- **Title**: فقط فوری‌ها
- **Type**: boolean



---

### Category: modem-and-network-equipment



### category
- **Title**: دسته‌بندی
- **Type**: object

### divider
- **Title**: سایر فیلتر‌ها
- **Type**: object

### exchange
- **Title**: نمایش معاوضه‌ها
- **Type**: object
- **Queries**: 
  - only-exchanges -> نمایش فقط معاوضه‌ها
  - exclude-exchanges -> حذف معاوضه‌ها

### goods-business-type
- **Title**: نوع آگهی‌دهنده
- **Type**: object
- **Queries**: 
  - all -> همه
  - personal -> شخصی
  - marketplace -> فروشگاه

### has-photo
- **Title**: فقط عکس‌دار
- **Type**: boolean

### lan_ports_quantity
- **Title**: تعداد پورت LAN
- **Type**: object
- **Queries**: 
  - 0-port -> بدون پورت
  - 1-port -> ۱ پورت
  - 2-ports -> ۲ پورت
  - 3-ports -> ۳ پورت
  - 4-ports -> ۴ پورت
  - +4-ports -> بیشتر از ۴ پورت

### modem_router_type
- **Title**: نوع مودم یا روتر
- **Type**: object
 - **Items Type**: array
- **Queries**: 
  - adsl -> ADSL
  - td-lte -> TD-LTE
  - wireless-portable-modem -> مودم بی‌سیم قابل حمل

### price
- **Title**: قیمت
- **Type**: object
 - **Minimum**: 0
 - **Maximum**: N/A

### sort
- **Title**: ترتیب نمایش آگهی‌ها براساس
- **Type**: object
- **Queries**: 
  - quality_and_sort_date -> quality_and_sort_date
  - sort_date -> sort_date
  - cheapest -> cheapest
  - most_expensive -> most_expensive
  - production_year -> production_year
  - usage -> usage
  - most_popular -> most_popular
  - most_relevant -> most_relevant

### status
- **Title**: وضعیت کالا
- **Type**: object
 - **Items Type**: array
- **Queries**: 
  - new -> نو
  - like-new -> در حد نو
  - used -> کارکرده
  - repair-needed -> نیازمند تعمیر

### urgent
- **Title**: فقط فوری‌ها
- **Type**: boolean



---

### Category: moquette



### category
- **Title**: دسته‌بندی
- **Type**: object

### divider
- **Title**: سایر فیلتر‌ها
- **Type**: object

### exchange
- **Title**: نمایش معاوضه‌ها
- **Type**: object
- **Queries**: 
  - only-exchanges -> نمایش فقط معاوضه‌ها
  - exclude-exchanges -> حذف معاوضه‌ها

### goods-business-type
- **Title**: نوع آگهی‌دهنده
- **Type**: object
- **Queries**: 
  - all -> همه
  - personal -> شخصی
  - marketplace -> فروشگاه

### has-photo
- **Title**: فقط عکس‌دار
- **Type**: boolean

### price
- **Title**: قیمت
- **Type**: object
 - **Minimum**: 0
 - **Maximum**: N/A

### sort
- **Title**: ترتیب نمایش آگهی‌ها براساس
- **Type**: object
- **Queries**: 
  - quality_and_sort_date -> quality_and_sort_date
  - sort_date -> sort_date
  - cheapest -> cheapest
  - most_expensive -> most_expensive
  - production_year -> production_year
  - usage -> usage
  - most_popular -> most_popular
  - most_relevant -> most_relevant

### status
- **Title**: وضعیت کالا
- **Type**: object
 - **Items Type**: array
- **Queries**: 
  - new -> نو
  - like-new -> در حد نو
  - used -> کارکرده
  - repair-needed -> نیازمند تعمیر

### urgent
- **Title**: فقط فوری‌ها
- **Type**: boolean



---

### Category: motorcycles



### brand_model
- **Title**: برند
- **Type**: object
 - **Items Type**: array
- **Queries**: 
  - ROOT -> همه‌ی برند‌ها
  - apachi -> آپاچی
  - apachi 200 -> آپاچی 200
  - apachi 200 new face -> آپاچی 200 نیو فیس
  - apachi 200 basic -> آپاچی 200 ساده
  - apachi 180 -> آپاچی 180
  - apachi 160 -> آپاچی 160
  - apachi 150 -> آپاچی 150
  - ashil -> آشیل
  - ashil wave-misc -> آشیل طرح ویو
  - ashil wave-misc 125 -> آشیل طرح ویو 125
  - ashil CG -> آشیل CG
  - ashil CG 200 -> آشیل CG 200
  - ashil CG 150 -> آشیل CG 150
  - ashil CG 125 -> آشیل CG 125
  - amico -> آمیکو
  - amico CG -> آمیکو CG
  - amico CG 125 -> آمیکو CG 125
  - amico golsar -> آمیکو گلسار
  - amico race-misc -> آمیکو طرح ریس
  - amico race-misc 250 -> آمیکو طرح ریس 250
  - amico 70 -> آمیکو 70
  - amico trail -> آمیکو طرح تریل
  - amico trail 186 -> آمیکو طرح تریل 186
  - ehsan -> احسان
  - ehsan wave-misc -> احسان طرح ویو
  - ehsan trail -> احسان طرح تریل
  - ehsan trail 250 -> احسان طرح تریل 250
  - ehsan CG -> احسان CG
  - ehsan CG shekari -> احسان EH شکاری 150
  - ehsan CG 200 -> احسان CG 200
  - ehsan CG 150 -> احسان CG 150
  - ehsan CG 125 -> احسان CG 125
  - energi -> انرژی
  - energi CG -> انرژی CG
  - energi CG 125 -> انرژی CG 125
  - ashimashi -> اشی مشی
  - ashimashi CG -> اشی مشی CG
  - ashimashi CG 125 -> اشی مشی CG 125
  - scooter-other -> اسکوتر(سایر)
  - sym lucky -> اس وای ام لاکی
  - sym lucky 250 -> اس وای ام لاکی 250
  - sym lucky 200 -> اس وای ام لاکی 200
  - sym lucky 180 -> اس وای ام لاکی 180
  - sym lucky 125 -> اس وای ام لاکی 125
  - stels -> استلز
  - stels 850 -> استلز 850
  - stels 850 atv -> استلز 850 4 چرخ
  - mv agusta -> ام وی اگوستا
  - mv agusta 1080 -> ام وی اگوستا 1080
  - mv agusta 800 -> ام وی اگوستا 800
  - nsu -> ان اس یو
  - nsu 50 -> ان اس یو 50
  - irandocharkh -> ایران دوچرخ
  - irandocharkh atv -> ایران دوچرخ 4 چرخ
  - irandocharkh atv 500 -> ایران دوچرخ 4 چرخ 500
  - irandocharkh atv 300 -> ایران دوچرخ 4 چرخ 300
  - irandocharkh atv 250 -> ایران دوچرخ 4 چرخ 250
  - irandocharkh atv 150 -> ایران دوچرخ 4 چرخ 150
  - irandocharkh bravo -> ایران دوچرخ براوو
  - irandocharkh wave-misc -> ایران دوچرخ آوا ( طرح ویو )
  - irandocharkh azma -> ایران دوچرخ ازما
  - irandocharkh azma 200 -> ایران دوچرخ ازما 200
  - irandocharkh azma 150 -> ایران دوچرخ ازما 150
  - irandocharkh azma 125 -> ایران دوچرخ ازما 125
  - irandocharkh arshia -> ایران دوچرخ عرشیا
  - irandocharkh arshia 200 -> ایران دوچرخ عرشیا 200
  - irandocharkh arshia 150 -> ایران دوچرخ عرشیا 150
  - irandocharkh arshia 125 -> ایران دوچرخ عرشیا 125
  - irandocharkh trail -> ایران دوچرخ طرح تریل
  - irandocharkh trail 250 -> ایران دوچرخ طرح تریل 250
  - irandocharkh trail 200 -> ایران دوچرخ طرح تریل 200
  - irandocharkh irdoco -> ایران دوچرخ ایردوکو
  - irandocharkh irdoco 150 -> ایران دوچرخ ایردوکو 150
  - izh-roosta -> ایژ روستا
  - izh-roosta 350 -> ایژ روستا 350
  - izh-roosta 250 -> ایژ روستا 250
  - bmw -> بی ام و
  - bmw 1100 -> بی ام و 1100
  - bocxoa -> باکوا
  - bocxoa 175 -> باکوا 175
  - bajaj -> باجاج
  - bajaj discover -> باجاج دیسکاور
  - bajaj discover 150 -> باجاج دیسکاور 150
  - bajaj discover 125 -> باجاج دیسکاور 125
  - bajaj vespa-misc -> باجاج وسپا ( چیتک )
  - bajaj vespa-misc 115 -> باجاج وسپا ( چیتک ) 115
  - bajaj pulsar -> باجاج پولسار
  - bajaj pulsar 2-candle -> باجاج پولسار 180 دو شمع
  - bajaj pulsar 1-candle -> باجاج پولسار 180 تک شمع
  - bajaj puls-rs -> باجاج پالس RS
  - bajaj puls-rs 200 -> باجاج پالس RS 200
  - bajaj puls-rs 250 -> باجاج پالس RS 250
  - bajaj puls-ns -> باجاج پالس NS
  - bajaj puls-ns 250 -> باجاج پالس NS 250
  - bajaj puls-ns 200 -> باجاج پالس NS 200
  - bajaj puls-ns 160 -> باجاج پالس NS 160
  - bajaj puls-ns 150 -> باجاج پالس NS 150
  - bajaj puls -> باجاج پالس
  - bajaj puls 220 -> باجاج پالس 220
  - bajaj puls 200 -> باجاج پالس 200
  - bajaj puls 180 -> باجاج پالس 180
  - bajaj puls 135 -> باجاج پالس 135
  - bajaj as -> باجاج AS
  - bajaj as 150 -> باجاج AS 150
  - bajaj avenger -> باجاج اونجر
  - bajaj avenger 220 -> باجاج اونجر 220
  - bajaj avenger 200 -> باجاج اونجر 200
  - bermoda -> برمودا
  - bermoda CG -> برمودا CG
  - bermoda CG 200 -> برمودا CG 200
  - bermoda CG 150 -> برمودا CG 150
  - bermoda CG 125 -> برمودا CG 125
  - baluch -> بلوچ
  - baluch CG -> بلوچ CG
  - baluch CG 150 -> بلوچ CG 150
  - baluch CG 125 -> بلوچ CG 125
  - electric-other -> برقی (سایر)
  - electric-other 2500w -> برقی (سایر) 2500 وات
  - electric-other 2000w -> برقی (سایر) 2000 وات
  - electric-other 1200w -> برقی (سایر) 1200 وات
  - electric-other 1000w -> برقی (سایر) 1000 وات
  - boxer -> بوکسر(باکسر)
  - boxer 180kld -> بوکسر(باکسر) 180 KLD
  - boxer 150 -> بوکسر(باکسر) 150
  - boxer 125 -> بوکسر(باکسر) 125
  - benelli -> بنلی
  - benelli 300race -> بنلی 300 ریس
  - benelli 300 -> بنلی 300
  - benelli 300 2-sylinder -> بنلی 300 دو سیلندر
  - benelli 300 1-sylinder -> بنلی 300 تک سیلندر
  - benelli 250 -> بنلی 250
  - benelli 250 2-sylinder -> بنلی 250 دو سیلندر
  - benelli 250 1-sylinder -> بنلی 250 تک سیلندر
  - benelli 150 -> بنلی 150
  - benelli mini -> بنلی مینی
  - benelli mini 135 -> بنلی مینی 135
  - benelli seta -> بنلی ستا
  - benelli seta 125 -> بنلی ستا 125
  - behpar -> به پر
  - behpar 200 -> به پر 200
  - behran -> بهران
  - behran CG -> بهران CG
  - behran CG 125 -> بهران CG 125
  - pusar -> پاسار
  - pusar 220 -> پاسار 220
  - pusar 180 -> پاسار 180
  - pusar 125 -> پاسار 125
  - pajang -> پاژنگ
  - pajang gaseous -> پاژنگ گازی
  - pajang 250 -> پاژنگ 250
  - pajang 150 -> پاژنگ 150
  - parvaz -> پرواز
  - parvaz scooter -> پرواز اسکوتر
  - parvaz scooter 100 -> پرواز اسکوتر 100
  - parvaz trail -> پرواز تریل
  - parvaz trail 200 -> پرواز تریل 200
  - parvaz wave-misc -> پرواز طرح ویو
  - parvaz wave-misc 125 -> پرواز طرح ویو 125
  - parvaz GS -> پرواز GS
  - parvaz GS 200 -> پرواز GS 200
  - parvaz CG -> پرواز CG
  - parvaz CG 200 -> پرواز CG 200
  - parvaz CG 150 -> پرواز CG 150
  - parvaz CG 125 -> پرواز CG 125
  - peugeot -> پژو
  - peugeot gaseous -> پژو گازی
  - polaris -> پولاریس
  - polaris atv -> پولاریس 4 چرخ
  - piaggio -> پیاجینو
  - piaggio bravo -> پیاجینو براوو
  - piaggio medley150 -> پیاجینو مدلی 150
  - piaggio liberty150 -> پیاجینو لیبرتی 150
  - pishtaz -> پیشتاز
  - pishtaz trail200 -> پیشتاز تریل 200
  - pishtaz 150 -> پیشتاز 150
  - pishtaz 125 -> پیشتاز 125
  - pishro -> پیشرو
  - pishro trail -> پیشرو گلد ( طرح تریل )
  - pishro trail 250 -> پیشرو گلد ( طرح تریل ) 250
  - pishro trail 200 -> پیشرو گلد ( طرح تریل ) 200
  - pishro pars -> پیشرو پارس
  - pishro pars 250 -> پیشرو پارس 250
  - pishro pars 200 -> پیشرو پارس 200
  - pishro wave-misc -> پیشرو پیام ( طرح ویو )
  - pishro wave-misc 150 -> پیشرو پیام ( طرح ویو ) 150
  - pishro wave-misc 135 -> پیشرو پیام ( طرح ویو ) 135
  - pishro wave-misc 125 -> پیشرو پیام ( طرح ویو ) 125
  - pishro CGL -> پیشرو CGL
  - pishro CGL 200 -> پیشرو CGL 200
  - pishro CGL 150 -> پیشرو CGL 150
  - pishro CGL 125 -> پیشرو CGL 125
  - pishro CG -> پیشرو CG
  - pishro CG 200 -> پیشرو CG 200
  - pishro CG 150 -> پیشرو CG 150
  - pishro CG 125 -> پیشرو CG 125
  - pishro 100 -> پیشرو 100
  - pishro mini -> پیشرو مینی
  - pishro mini 75 -> پیشرو مینی 75
  - pishro 70 -> پیشرو 70
  - tara -> تارا
  - tara 125 -> تارا 125
  - tera-motor -> ترا موتور
  - tera-motor electric -> ترا موتور برقی
  - tera-motor electric 1500w -> ترا موتور برقی وات 1500
  - taktaz -> تک تاز
  - taktaz 150 -> تک تاز 150
  - taktaz 135 -> تک تاز 135
  - taktaz 125 -> تک تاز 125
  - takro -> تکرو
  - takro 200 -> تکرو 200
  - takro 50 -> تکرو 50
  - talash -> تلاش
  - talash trail -> تلاش طرح تریل
  - talash trail 150 -> تلاش طرح تریل 150
  - talash CG -> تلاش CG
  - talash CG 150 -> تلاش CG 150
  - talash CG 125 -> تلاش CG 125
  - talash taban -> تلاش تابان
  - talash taban 150 -> تلاش تابان 150
  - talash 70 -> تلاش 70
  - tizpar -> تیزپر
  - tiztak -> تیزتک
  - tiztak CG -> تیزتک CG
  - tiztak CG 150 -> تیزتک CG 150
  - tiztak CG 125 -> تیزتک CG 125
  - tondar-shahab -> تندر شهاب
  - tondar-shahab CG -> تندر شهاب CG
  - tondar-shahab CG 200 -> تندر شهاب CG 200
  - tondar-shahab CG 150 -> تندر شهاب CG 150
  - tondar-shahab CG 125 -> تندر شهاب CG 125
  - tondar-shahab javan -> تندر شهاب جوان ( طرح هارلی )
  - tondar-shahab javan 150 -> تندر شهاب جوان ( طرح هارلی ) 150
  - tandis -> تندیس
  - tandis CDi -> تندیس CDI
  - tandis CDi 125 -> تندیس CDI 125
  - tvs -> تی وی اس
  - tvs wego -> تی وی اس ویگو
  - tvs wego 110 -> تی وی اس ویگو 110
  - tvs neo -> تی وی اس نئو
  - tvs neo 125 -> تی وی اس نئو 125
  - tvs jupiter -> تی وی اس ژوپیتر
  - tvs jupiter 110 -> تی وی اس ژوپیتر 110
  - tvs rockz -> تی وی اس راکز
  - tvs rockz 125 -> تی وی اس راکز 125
  - tvs dazz -> تی وی اس داز
  - tvs dazz 110 -> تی وی اس داز 110
  - tvs hlx150 -> تی وی اس HLX 150
  - tvs hlx150 150 -> تی وی اس HLX 150 150
  - tizro -> تیزرو
  - tizro CGL -> تیزرو CGL
  - tizro CGL 200 -> تیزرو CGL 200
  - tizro CGL 150 -> تیزرو CGL 150
  - tizro CGL 125 -> تیزرو CGL 125
  - tizro CG -> تیزرو CG
  - tizro CG 125 -> تیزرو CG 125
  - tourist -> توریست
  - tourist CG -> توریست CG
  - tourist CG 125 -> توریست CG 125
  - samen -> ثامن
  - samen 200 -> ثامن 200
  - jetro -> جترو(اصفهان سیکلت)
  - jetro atv -> جترو(اصفهان سیکلت) 4 چرخ
  - jetro tornado -> جترو(اصفهان سیکلت) تورنادو
  - jetro tornado 250 -> جترو(اصفهان سیکلت) تورنادو 250
  - jetro trail -> جترو(اصفهان سیکلت) طرح تریل
  - jetro trail 200 -> جترو(اصفهان سیکلت) طرح تریل 200
  - jetro trail 150 -> جترو(اصفهان سیکلت) طرح تریل 150
  - jetro harly-misc -> جترو(اصفهان سیکلت) طرح هارلی
  - jetro mini-cross -> جترو(اصفهان سیکلت) مینی کراس
  - jetro mini-cross 100 -> جترو(اصفهان سیکلت) مینی کراس 100
  - jetro mini-cross 90 -> جترو(اصفهان سیکلت) مینی کراس 90
  - jetro 70 -> جترو(اصفهان سیکلت) 70
  - java -> جاوا
  - java gaseous -> جاوا گازی
  - jahanro -> جهان رو
  - jahanro CR -> جهان رو CR
  - jahanro CR 225 -> جهان رو CR 225
  - jahanro 90 -> جهان رو 90
  - jahanro zebra -> جهان رو زبرا
  - jahanro zebra 150 -> جهان رو زبرا 150
  - jahanro kangaroo -> جهان رو کانگورو
  - jahanro kangaroo 150 -> جهان رو کانگورو 150
  - jahanro electric -> جهان رو برقی
  - jahanro electric 4000w -> جهان رو برقی 4000 وات
  - jahan-hamta -> جهان همتا
  - jahan-hamta hamtaz-cruiser -> جهان همتا همتازکروزر
  - jahan-hamta hamtaz-cruiser 150 -> جهان همتا همتازکروزر 150
  - jahan-hamta hamtaz -> جهان همتا همتاز
  - jahan-hamta hamtaz 200 -> جهان همتا همتاز 200
  - jahan-hamta falat -> جهان همتا فلات
  - jahan-hamta falat 250 -> جهان همتا فلات 250
  - jahan-hamta falat 200 -> جهان همتا فلات 200
  - atv-other -> 4 چرخ (سایر)
  - atv-other 1300 -> 4 چرخ (سایر) 1300
  - atv-other 400 -> 4 چرخ (سایر) 400
  - atv-other 350 -> 4 چرخ (سایر) 350
  - atv-other 250 -> 4 چرخ (سایر) 250
  - atv-other 200 -> 4 چرخ (سایر) 200
  - atv-other 150 -> 4 چرخ (سایر) 150
  - atv-other 125 -> 4 چرخ (سایر) 125
  - daiichi -> دایچی
  - daiichi 250 -> دایچی 250
  - daiichi 200 -> دایچی 200
  - daiichi 150 -> دایچی 150
  - daiichi 135 -> دایچی 135
  - daiichi wave-misc130 -> دایچی طرح ویو 130
  - daiichi 130 -> دایچی 130
  - daiichi 125 -> دایچی 125
  - delta -> دلتا (شاهین موتور)
  - delta electric -> دلتا (شاهین موتور) برقی
  - delta electric 1000w -> دلتا (شاهین موتور) برقی 1000 وات
  - delta CRT -> دلتا (شاهین موتور) CRT
  - delta CRT 160 -> دلتا (شاهین موتور) CRT 160
  - delta CG -> دلتا (شاهین موتور) CG
  - delta CG 125 -> دلتا (شاهین موتور) CG 125
  - sabin-motor -> سابین موتور
  - sabin-motor wave-misc -> سابین موتور طرح ویو
  - sabin-motor wave-misc 125 -> سابین موتور طرح ویو 125
  - sabin-motor CG -> سابین موتور CG
  - sabin-motor CG 125 -> سابین موتور CG 125
  - sabin-motor CB -> سابین موتور CB
  - sabin-motor CB 125 -> سابین موتور CB 125
  - daelim -> دایلیم
  - daelim 250 -> دایلیم 250
  - daelim 250 type 2 -> دایلیم 250 تیپ 2
  - daelim 250 type 1 -> دایلیم 250 تیپ 1
  - daelim 250 basic -> دایلیم 250 ساده
  - derbi -> دربی
  - derbi 160 -> دربی 160
  - dolphin -> دلفین
  - dolphin vespa-misc -> دلفین طرح وسپا
  - dolphin vespa-misc 150 -> دلفین طرح وسپا 150
  - dandy -> دندی
  - dandy electric -> دندی برقی
  - dnepr -> دنیپر
  - dnepr 650 -> دنیپر 650
  - dino -> دینو
  - dino trail -> دینو طرح تریل
  - dino 160 -> دینو 160
  - dino CBR-misc -> دینو طرح CBR
  - dino CBR-misc 250 -> دینو طرح CBR 250
  - dino wind -> دینو ویند
  - dino wind 200 -> دینو ویند 200
  - dino wind 170 -> دینو ویند 170
  - dino RZ3 -> دینو RZ3
  - dino RZ3 250 -> دینو RZ3 250
  - dino Z2 -> دینو Z2
  - dino Z2 200 -> دینو Z2 200
  - dino fiddel3 -> دینو فیدل 3
  - dino fiddel3 200 -> دینو فیدل 3 200
  - dino fiddel -> دینو فیدل
  - dino fiddel 200 -> دینو فیدل 200
  - dino kavan -> دینو کاوان
  - dino kavan 125 -> دینو کاوان 125
  - dino CG -> دینو CG
  - dino CG 200 -> دینو CG 200
  - dino CG 150 -> دینو CG 150
  - dino CG 125 -> دینو CG 125
  - dino boxer-misc -> دینو طرح بوکسر
  - dino boxer-misc 150 -> دینو طرح بوکسر 150
  - rapido -> راپیدو
  - rapido CG -> راپیدو CG
  - rapido CG 125 -> راپیدو CG 125
  - reks -> رکس
  - reks gaseous -> رکس گازی
  - regal-raptor -> رگال رپتور
  - regal-raptor falcon -> رگال رپتور فالکن
  - regal-raptor daytona -> رگال رپتور دیتونا
  - regal-raptor tracher -> رگال رپتور ترکر
  - regal-raptor bobber -> رگال رپتور بابر
  - regal-raptor spyder -> رگال رپتور اسپایدر
  - regal-raptor NAC250 -> رگال رپتور NAC 250
  - roobin -> روبین
  - ravan -> روان
  - ravan CG -> روان CG
  - ravan CG 125 -> روان CG 125
  - ravan wave-misc -> روان طرح ویو
  - ravan trail -> روان طرح تریل
  - ravan trail 200 -> روان طرح تریل 200
  - roadwin -> رود وین
  - roadwin 135 -> رود وین 135
  - rayka -> ریکا
  - rayka CG -> ریکا CG
  - rayka CG 125 -> ریکا CG 125
  - rieju -> ریجو
  - rieju cross -> ریجو کراس
  - rieju cross 200 -> ریجو کراس 200
  - zomorod-kavir -> زمرد کویر
  - zomorod-kavir 150 -> زمرد کویر 150
  - zomorod-kavir 125 -> زمرد کویر 125
  - zomorod-kavir 200 -> زمرد کویر 200
  - zomorod-kavir wave-misc -> زمرد کویر طرح ویو
  - zomorod-kavir wave-misc 125 -> زمرد کویر طرح ویو 125
  - zontes -> زونتس
  - zontes 250 -> زونتس 250
  - xigma -> زیگما
  - xigma sachs -> زیگما ساچ
  - xigma wave-misc -> زیگما طرح ویو
  - xigma wave-misc 135 -> زیگما طرح ویو 135
  - xigma CS -> زیگما CS
  - xigma CS 170 -> زیگما CS 170
  - xigma CG -> زیگما CG
  - xigma CG 125 -> زیگما CG 125
  - saman -> سامان
  - saman roofed -> سامان سقف دار
  - saman roofed 150 -> سامان سقف دار 150
  - sepand -> سپند
  - sepand CG -> سپند CG
  - sepand CG 125 -> سپند CG 125
  - 3-wheels -> 3 چرخ
  - 3-wheels other -> 3 چرخ سایر
  - 3-wheels electric -> 3 چرخ برقی
  - 3-wheels vespa-3 -> 3 چرخ وسپا
  - 3-wheels 200 -> 3 چرخ 200
  - 3-wheels 150 -> 3 چرخ 150
  - 3-wheels 125 -> 3 چرخ 125
  - savin -> ساوین
  - savin 200 -> ساوین 200
  - savin 150 -> ساوین 150
  - savin 125 -> ساوین 125
  - soco -> سوکو
  - soco electric -> سوکو برقی
  - soco electric 1200w -> سوکو برقی 1200 وات
  - suzuki -> سوزوکی
  - suzuki 650 -> سوزوکی 650
  - suzuki 600 -> سوزوکی 600
  - suzuki 300 -> سوزوکی 300
  - suzuki 250 -> سوزوکی 250
  - suzuki atv -> سوزوکی 4 چرخ
  - suzuki atv 90 -> سوزوکی 4 چرخ 90
  - suzuki pakeshti -> سوزوکی پاکشتی
  - suzuki pakeshti address -> سوزوکی پاکشتی ادرس
  - suzuki pakeshti verde -> سوزوکی پاکشتی ورد
  - suzuki pakeshti basket -> سوزوکی پاکشتی بسکت
  - suzuki pakeshti pallet -> سوزوکی پاکشتی پالت
  - suzuki pakeshti lets -> سوزوکی پاکشتی لتس
  - suzuki CG -> سوزوکی CG
  - suzuki CG 150 -> سوزوکی CG 150
  - suzuki CG 125 -> سوزوکی CG 125
  - suzuki mini -> سوزوکی مینی 80
  - suzuki VC4 -> سوزوکی VC4
  - suzuki GP -> سوزوکی GP
  - suzuki GP 125 -> سوزوکی GP 125
  - suzuki hayabusa -> سوزوکی هایابوسا
  - suzuki hayabusa 1300 -> سوزوکی هایابوسا 1300
  - suzuki gixxer -> سوزوکی جیکسر
  - suzuki gixxer 150 -> سوزوکی جیکسر 150
  - suzuki b-king -> سوزوکی بی کینگ
  - suzuki b-king 1400 -> سوزوکی بی کینگ 1400
  - suzuki TSR -> سوزوکی TSR
  - suzuki TSR 250 -> سوزوکی TSR 250
  - suzuki TSR 200 -> سوزوکی TSR 200
  - suzuki TS -> سوزوکی TS
  - suzuki TS 185 -> سوزوکی TS 185
  - suzuki TS 125 -> سوزوکی TS 125
  - suzuki RV -> سوزوکی RV
  - suzuki RV 50 -> سوزوکی RV 50
  - suzuki RMX -> سوزوکی RMX
  - suzuki RMX 450 -> سوزوکی RMX 450
  - suzuki RMX 250 -> سوزوکی RMX 250
  - suzuki RM_Z -> سوزوکی RM_Z
  - suzuki RM_Z 250 -> سوزوکی RM_Z 250
  - suzuki trail -> سوزوکی RM تریل
  - suzuki trail 250 -> سوزوکی RM تریل 250
  - suzuki trail 125 -> سوزوکی RM تریل 125
  - suzuki RF -> سوزوکی RF
  - suzuki RF 400 -> سوزوکی RF 400
  - suzuki intorda -> سوزوکی اینتوردا
  - suzuki inazuma -> سوزوکی اینازوما
  - suzuki inazuma 250 -> سوزوکی اینازوما 250
  - suzuki DR -> سوزوکی DR
  - suzuki DR 625 -> سوزوکی DR 625
  - suzuki DR 250 -> سوزوکی DR 250
  - suzuki DR 200 -> سوزوکی DR 200
  - suzuki djebel -> سوزوکی دجیبل
  - suzuki djebel 250 -> سوزوکی دجیبل 250
  - suzuki djebel 200 -> سوزوکی دجیبل 200
  - suzuki GSF -> سوزوکی GSF
  - suzuki bandit -> سوزوکی بندیت
  - suzuki bandit 1200 -> سوزوکی بندیت 1200
  - suzuki bandit 400 -> سوزوکی بندیت 400
  - suzuki bandit 600 -> سوزوکی بندیت 600
  - suzuki bandit 250 -> سوزوکی بندیت 250
  - suzuki ax 100 -> سوزوکی ax 100
  - suzuki X7 -> سوزوکی X7
  - suzuki X7 250 -> سوزوکی X7 250
  - suzuki GSX R -> سوزوکی GSX R
  - suzuki GSX R 1000 -> سوزوکی GSX R 1000
  - suzuki GSX R 750 -> سوزوکی GSX R 750
  - suzuki GSX R 600 -> سوزوکی GSX R 600
  - suzuki GSX -> سوزوکی GSX
  - suzuki GSX 1400 -> سوزوکی GSX 1400
  - suzuki GSX 1300 -> سوزوکی GSX 1300
  - suzuki GSX 1000 -> سوزوکی GSX 1000
  - suzuki GSX 750 -> سوزوکی GSX 750
  - suzuki GSX 600 -> سوزوکی GSX 600
  - suzuki GSX 400 -> سوزوکی GSX 400
  - suzuki GSX 250 -> سوزوکی GSX 250
  - suzuki GSR -> سوزوکی GSR
  - suzuki GSR 1000 -> سوزوکی GSR 1000
  - suzuki GSR 750 -> سوزوکی GSR 750
  - suzuki GSR 600 -> سوزوکی GSR 600
  - suzuki GSR 150 -> سوزوکی GSR 150
  - suzuki GS -> سوزوکی GS
  - suzuki GS 750 -> سوزوکی GS 750
  - suzuki GS 1000 -> سوزوکی GS 1000
  - suzuki GS 550 -> سوزوکی GS 550
  - suzuki GS 155 -> سوزوکی GS 155
  - suzuki GS 150 -> سوزوکی GS 150
  - suzuki GS 125 -> سوزوکی GS 125
  - cf-motor -> سی اف موتو
  - cf-motor NK 150 -> سی اف موتو NK 150
  - shabab -> شباب
  - shabab electric -> شباب برقی
  - shabab electric 1500w -> شباب برقی 1500 وات
  - shabab wave-misc -> شباب طرح ویو
  - shabab wave-misc 130 -> شباب طرح ویو 130
  - shabab 220 -> شباب 220
  - shabab 200 -> شباب 200
  - shabab 180 -> شباب 180
  - shabab 150 -> شباب 150
  - shooka -> شوکا
  - shooka vespa-misc -> شوکا طرح وسپا
  - shooka wave-misc -> شوکا طرح ویو
  - shooka wave-misc SYM 130 -> شوکا طرح ویو SYM 130
  - shooka wave-misc SYM 125 -> شوکا طرح ویو SYM 125
  - sahra -> صحرا
  - sahra CG -> صحرا CG
  - sahra CG 125 -> صحرا CG 125
  - kawasaki -> کاوازاکی
  - kawasaki mini -> کاوازاکی مینی تریل
  - kawasaki mini 100 -> کاوازاکی مینی تریل 100
  - kawasaki atv -> کاوازاکی 4 چرخ
  - kawasaki atv 250 hi -> کاوازاکی 4 چرخ 250 های کیپس
  - kawasaki GSR -> کاوازاکی GSR
  - kawasaki GSR 750 -> کاوازاکی GSR 750
  - kawasaki GTO -> کاوازاکی GTO
  - kawasaki GTO 125 -> کاوازاکی GTO 125
  - kawasaki GTO 100 -> کاوازاکی GTO 100
  - kawasaki axm -> کاوازاکی axm
  - kawasaki axm 100 -> کاوازاکی axm 100
  - kawasaki GPZ -> کاوازاکی GPZ
  - kawasaki GPZ 400 -> کاوازاکی GPZ 400
  - kawasaki GPX -> کاوازاکی GPX
  - kawasaki GPX 750 -> کاوازاکی GPX 750
  - kawasaki versys -> کاوازاکی ورسیس
  - kawasaki versys 1000 -> کاوازاکی ورسیس 1000
  - kawasaki versys 650 -> کاوازاکی ورسیس 650
  - kawasaki versys x 250 -> کاوازاکی ورسیس X 250
  - kawasaki ninja -> کاوازاکی نینجا
  - kawasaki ninja 300 -> کاوازاکی نینجا 300
  - kawasaki ninja 250 -> کاوازاکی نینجا 250
  - kawasaki magnum -> کاوازاکی مگنوم
  - kawasaki magnum 80 -> کاوازاکی مگنوم 80
  - kawasaki D-tracker -> کاوازاکی دی ترکر
  - kawasaki D-tracker 250 -> کاوازاکی دی ترکر 250
  - kawasaki D-tracker 150 -> کاوازاکی دی ترکر 150
  - kawasaki estrella -> کاوازاکی استرلا
  - kawasaki estrella 250 -> کاوازاکی استرلا 250
  - kawasaki stockman -> کاوازاکی استاکمن
  - kawasaki stockman 250 -> کاوازاکی استاکمن 250
  - kawasaki ZZR -> کاوازاکی ZZR
  - kawasaki ZZR 1400 -> کاوازاکی ZZR 1400
  - kawasaki ZZR 400 -> کاوازاکی ZZR 400
  - kawasaki ZZR 250 -> کاوازاکی ZZR 250
  - kawasaki ZZR 150 hi -> کاوازاکی ZZR 150 های کیپس
  - kawasaki ZXR -> کاوازاکی ZXR
  - kawasaki ZXR 400 -> کاوازاکی ZXR 400
  - kawasaki ZXR 250 -> کاوازاکی ZXR 250
  - kawasaki ZX -> کاوازاکی ZX
  - kawasaki ZX 1100 -> کاوازاکی ZX 1100
  - kawasaki ZX 900 -> کاوازاکی ZX 900
  - kawasaki ZX 300 -> کاوازاکی ZX 300
  - kawasaki ZX 200 -> کاوازاکی ZX 200
  - kawasaki ZX 150 -> کاوازاکی ZX 150
  - kawasaki ZX 14 -> کاوازاکی ZX 14
  - kawasaki ZX 12 -> کاوازاکی ZX 12
  - kawasaki ZX 10 -> کاوازاکی ZX 10
  - kawasaki Z -> کاوازاکی Z
  - kawasaki Z 1000 -> کاوازاکی Z 1000
  - kawasaki Z 800 -> کاوازاکی Z 800
  - kawasaki Z 650 -> کاوازاکی Z 650
  - kawasaki Z 300 -> کاوازاکی Z 300
  - kawasaki Z 250 -> کاوازاکی Z 250
  - kawasaki Z 125 -> کاوازاکی Z 125
  - kawasaki KX -> کاوازاکی KX
  - kawasaki KX 450 F -> کاوازاکی KX 450 F
  - kawasaki KX 250 F -> کاوازاکی KX 250 F
  - kawasaki KX 85 -> کاوازاکی KX 85
  - kawasaki KX 65 -> کاوازاکی KX 65
  - kawasaki KSR -> کاوازاکی KSR
  - kawasaki KSR 110 -> کاوازاکی KSR 110
  - kawasaki KSR 80 -> کاوازاکی KSR 80
  - kawasaki KMX -> کاوازاکی KMX
  - kawasaki KMX 200 -> کاوازاکی KMX 200
  - kawasaki KMX 125 -> کاوازاکی KMX 125
  - kawasaki KMX 50 -> کاوازاکی KMX 50
  - kawasaki KLX -> کاوازاکی KLX
  - kawasaki KLX 450 F -> کاوازاکی KLX 450 F
  - kawasaki KLX 250 -> کاوازاکی KLX 250
  - kawasaki KLX 150 -> کاوازاکی KLX 150
  - kawasaki KLX 125 -> کاوازاکی KLX 125
  - kawasaki KLR -> کاوازاکی KLR
  - kawasaki KLR 650 -> کاوازاکی KLR 650
  - kawasaki KDX -> کاوازاکی KDX
  - kawasaki KDX 520 -> کاوازاکی KDX 250
  - kawasaki KDX 200 -> کاوازاکی KDX 200
  - kawasaki KDX 125 -> کاوازاکی KDX 125
  - kawasaki ER6N -> کاوازاکی ER6N
  - kawasaki ER6N 650 -> کاوازاکی ER6N 650
  - kawasaki fury -> کاوازاکی فیوری
  - kawasaki fury 125 -> کاوازاکی فیوری 125
  - kawasaki 100 -> کاوازاکی 100
  - kawasaki 100 sport -> کاوازاکی 100 اسپرت
  - kawasaki 100 basic -> کاوازاکی 100 ساده
  - cafe-racer -> کافه ریسر
  - cafe-racer 250 -> کافه ریسر 250
  - cafe-racer 200 -> کافه ریسر 200
  - cafe-racer 125 -> کافه ریسر 125
  - kayo -> کایو
  - kayo mini -> کایو مینی جی پی
  - kayo mini 150 -> کایو مینی جی پی 150
  - kayo mini 110 -> کایو مینی جی پی 110
  - kayo cross -> کایو 250 کراس
  - kayo 250 -> کایو 250
  - kayo 150 -> کایو 150
  - kabir -> کبیر
  - kabir electric -> کبیر برقی
  - kabir electric 1500w -> کبیر برقی 1500 وات
  - kabir EVO 150 -> کبیر EVO 150
  - kabir KLD 180 -> کبیر KLD 180
  - kabir trail -> کبیر طرح تریل
  - kabir trail 200 -> کبیر طرح تریل 200
  - kabir wave-misc -> کبیر طرح ویو
  - kabir CGL -> کبیر CGL
  - kabir CGL 150 -> کبیر CGL 150
  - kabir CG -> کبیر CG
  - kabir CG 200 -> کبیر CG 200
  - kabir CG 150 -> کبیر CG 150
  - kabir CG 125 -> کبیر CG 125
  - kasir -> کثیر ( رهرو )
  - kasir sport 150 -> کثیر ( رهرو ) 150 اسپرت
  - kasir CGL -> کثیر ( رهرو ) CGL
  - kasir CGL 150 -> کثیر ( رهرو ) CGL 150
  - kasir CG -> کثیر ( رهرو ) CG
  - kasir CG 200 -> کثیر ( رهرو ) CG 200
  - kasir CG 185 -> کثیر ( رهرو ) CG 185
  - kasir CG 125 -> کثیر ( رهرو ) CG 125
  - can-am -> کن ام
  - can-am spyder -> کن ام اسپایدر
  - can-am spyder F3 -> کن ام اسپایدر F3
  - can-am ATV -> کن ام ATV
  - can-am ATV 1000 -> کن ام ATV 1000
  - can-am DS -> کن ام DS
  - can-am DS 250 -> کن ام DS 250
  - can-am XDS max -> کن ام XDS max
  - can-am XDS max 1000 -> کن ام XDS max 1000
  - kavir-motor -> کویر موتور
  - kavir-motor TGB -> کویر موتور تی جی بی
  - kavir-motor electric -> کویر موتور برقی
  - kavir-motor electric 1500 -> کویر موتور برقی 1500
  - kavir-motor atv -> کویر موتور 4 چرخ
  - kavir-motor atv 400 -> کویر موتور 4 چرخ 400
  - kavir-motor mini -> کویر موتور مینی
  - kavir-motor mini 70 -> کویر موتور مینی 70
  - kavir-motor RKV -> کویر موتور RKV
  - kavir-motor RKV 200 -> کویر موتور RKV 200
  - kavir-motor trail -> کویر موتور تریل
  - kavir-motor trail 250 -> کویر موتور تریل 250
  - kavir-motor trail 200 -> کویر موتور تریل 200
  - kavir-motor trail 125 -> کویر موتور تریل 125
  - kavir-motor wave-misc -> کویر موتور طرح ویو
  - kavir-motor wave-misc crystal -> کویر موتور طرح ویو کریستال
  - kavir-motor wave-misc radisson -> کویر موتور طرح ویو رادیسون
  - kavir-motor S4 -> کویر موتور S4
  - kavir-motor S4 150 -> کویر موتور S4 150
  - kavir-motor CGL ( GLX ) -> کویر موتور CGL ( GLX )
  - kavir-motor CGL ( GLX ) 150 -> کویر موتور CGL ( GLX ) 150
  - kavir-motor CG -> کویر موتور CG
  - kavir-motor CG 200 -> کویر موتور CG 200
  - kavir-motor CG 150 -> کویر موتور CG 150
  - kavir-motor CG 125 -> کویر موتور CG 125
  - KTM -> کی تی ام
  - KTM mini-cross -> کی تی ام مینی کراس
  - KTM mini-cross 70 -> کی تی ام مینی کراس 70
  - KTM cross -> کی تی ام کراس
  - KTM cross 625 -> کی تی ام کراس 625
  - KTM cross 400 -> کی تی ام کراس 400
  - KTM cross 250 -> کی تی ام کراس 250
  - KTM cross 200 -> کی تی ام کراس 200
  - KTM duke -> کی تی ام دوک
  - KTM duke 400 -> کی تی ام دوک 400
  - KTM duke 250 -> کی تی ام دوک 250
  - KTM duke 200 -> کی تی ام دوک 200
  - KTM duke 125 -> کی تی ام دوک 125
  - KTM RC -> کی تی ام RC
  - KTM RC 250 -> کی تی ام RC 250
  - KTM RC 200 -> کی تی ام RC 200
  - keeway -> کی وی
  - keeway 150 ajax -> کی وی 150 آژاکس
  - keeway 150 -> کی وی 150
  - kian -> کیان
  - kian 125 -> کیان 125
  - kymco -> کیمکو
  - kymco 110 -> کیمکو 110
  - kymco agility -> کیمکو آجیلیتی
  - kymco agility 200 -> کیمکو آجیلیتی 200
  - kymco agility 150 -> کیمکو آجیلیتی 150
  - gas-gas -> گس گس
  - gas-gas teryal -> گس گس تریال
  - gas-gas 250 -> گس گس 250
  - gas-gas 200 -> گس گس 200
  - loncen -> لانسن
  - loncen 225 -> لانسن 225
  - lifan -> لیفان
  - lifan harly-misc -> لیفان طرح هارلی
  - lifan mini -> لیفان مینی
  - lifan mini 70 -> لیفان مینی 70
  - lifan electric -> لیفان برقی
  - lifan electric 2000w -> لیفان برقی 2000 وات
  - lifan electric 1500w -> لیفان برقی 1500 وات
  - lifan 160 -> لیفان 160
  - lifan KPS -> لیفان KPS
  - lifan KPS 200 -> لیفان KPS 200
  - lifan wave-misc -> لیفان طرح ویو
  - lifan wave-misc 135 -> لیفان طرح ویو 135
  - lifan wave-misc 125 -> لیفان طرح ویو 125
  - lifan CG -> لیفان CG
  - lifan CG 200 -> لیفان CG 200
  - lifan CG 150 -> لیفان CG 150
  - lifan CG 125 -> لیفان CG 125
  - mado-motor -> مادو موتور
  - mado-motor electric -> مادو موتور برقی
  - mado-motor electric 2000w -> مادو موتور برقی 2000 وات
  - mahindra -> ماهیندرا
  - mahindra vespa-misc -> ماهیندرا طرح وسپا
  - mahindra vespa-misc 110 -> ماهیندرا طرح وسپا 110
  - matinkhodro-sivan -> متین خودرو( سیوان )
  - matinkhodro-sivan gaseous -> متین خودرو( سیوان ) گازی
  - matinkhodro-sivan wave-misc -> متین خودرو( سیوان ) طرح ویو
  - matinkhodro-sivan wave-misc 125 -> متین خودرو( سیوان ) طرح ویو 125
  - matinkhodro-sivan MKZ -> متین خودرو( سیوان ) MKZ
  - matinkhodro-sivan MKZ 139 -> متین خودرو( سیوان ) MKZ 139
  - matinkhodro-sivan 250 -> متین خودرو( سیوان ) 250
  - matinkhodro-sivan trail -> متین خودرو( سیوان ) تریل
  - matinkhodro-sivan trail 200 -> متین خودرو( سیوان ) تریل 200
  - matinkhodro-sivan CG -> متین خودرو( سیوان ) CG
  - matinkhodro-sivan CG 200 -> متین خودرو( سیوان ) CG 200
  - matinkhodro-sivan CG 150 -> متین خودرو( سیوان ) CG 150
  - matinkhodro-sivan CG 125 -> متین خودرو( سیوان ) CG 125
  - modenas -> مدناس
  - modenas galkse -> مدناس گلکسی
  - modenas 175 -> مدناس 175 جاگو
  - modenas 130 -> مدناس 130
  - modenas 120 -> مدناس 120
  - modenas 110 -> مدناس 110
  - mehran -> مهران
  - mehran CG -> مهران CG
  - mehran CG 125 -> مهران CG 125
  - megelli -> مگلی
  - megelli 250 -> مگلی 250
  - megelli 200 -> مگلی 200
  - megelli 150 -> مگلی 150
  - mini-other -> مینی (سایر)
  - mini-other 125 -> مینی (سایر) 125
  - mini-other 100 -> مینی (سایر) 100
  - mini-other 30 -> مینی (سایر) 30
  - moto-guzzi -> موتو گودسی
  - moto-guzzi 1000 -> موتو گودسی 1000
  - novin-cyclet -> نوین سیکلت
  - novin-cyclet electric -> نوین سیکلت برقی
  - novin-cyclet electric 3000w -> نوین سیکلت برقی 3000 وات
  - natali -> ناتالی
  - nami -> نیرو محرکه ( نامی )
  - nami electric -> نیرو محرکه ( نامی ) برقی
  - nami electric 2000w -> نیرو محرکه ( نامی ) برقی 2000 وات
  - nami electric 1500w -> نیرو محرکه ( نامی ) برقی 1500 وات
  - nami 250 -> نیرو محرکه ( نامی ) 250
  - nami 200 -> نیرو محرکه ( نامی ) 200
  - nami harly-misc -> نیرو محرکه ( نامی ) طرح هارلی
  - nami harly-misc 200 -> نیرو محرکه ( نامی ) طرح هارلی 200
  - nami apachi-misc -> نیرو محرکه ( نامی ) طرح اپاچی
  - nami apachi-misc 200 -> نیرو محرکه ( نامی ) طرح اپاچی 200
  - nami apachi-misc 170 -> نیرو محرکه ( نامی ) طرح اپاچی 170
  - nami CGL -> نیرو محرکه ( نامی ) CGL
  - nami CGL 150 -> نیرو محرکه ( نامی ) CGL 150
  - nami CG -> نیرو محرکه ( نامی ) CG
  - nami CG 200 -> نیرو محرکه ( نامی ) CG 200
  - nami CG 150 -> نیرو محرکه ( نامی ) CG 150
  - nami CG 125 -> نیرو محرکه ( نامی ) CG 125
  - nami trail -> نیرو محرکه ( نامی ) تریل
  - nami trail 250 -> نیرو محرکه ( نامی ) تریل 250
  - nami trail 200 -> نیرو محرکه ( نامی ) تریل 200
  - nami wave-misc -> نیرو محرکه ( نامی ) طرح ویو
  - nami wave-misc 125 -> نیرو محرکه ( نامی ) طرح ویو 125
  - nami vespa-misc -> نیرو محرکه ( نامی ) طرح وسپا
  - nami vespa-misc 150 -> نیرو محرکه ( نامی ) طرح وسپا 150
  - nami RX 249 -> نیرو محرکه ( نامی ) RX 249
  - vespa -> وسپا
  - vespa classic -> وسپا کلاسیک
  - vespa LML -> وسپا ال ام ال
  - vespa primavera -> وسپا پریماورا
  - vespa primavera 250 -> وسپا پریماورا 250
  - vespa primavera 150 -> وسپا پریماورا 150
  - vespa piaggio -> وسپا پیاژیو
  - vespa piaggio 150 -> وسپا پیاژیو 150
  - vespa piaggio 50 -> وسپا پیاژیو 50
  - vespa PS -> وسپا پی اس
  - vespa PS 150 -> وسپا پی اس 150
  - vespa sprint -> وسپا اسپرینت
  - vespa sprint 150 -> وسپا اسپرینت 150
  - vespa sprint 125 -> وسپا اسپرینت 125
  - vespa LX -> وسپا ال ایکس
  - vespa LX 150 -> وسپا ال ایکس 150
  - vespa GTV -> وسپا GTV
  - vespa GTV 300 -> وسپا GTV 300
  - vespa GTS -> وسپا GTS
  - vespa GTS 300 -> وسپا GTS 300
  - vespa GTS 250 -> وسپا GTS 250
  - vespa GTS 150 -> وسپا GTS 150
  - vespa 946 -> وسپا 946
  - volga -> ولگا
  - volga VLT -> ولگا VLT
  - volga VLT 150 -> ولگا VLT 150
  - volga VLS -> ولگا VLS
  - volga VLS 150 -> ولگا VLS 150
  - winner -> وینر
  - winner 250 -> وینر 250
  - winner 200 -> وینر 200
  - hartford -> هارتفورد
  - hartford 200 -> هارتفورد 200
  - hartford 150 -> هارتفورد 150
  - haojue -> هائوجیو
  - haojue 150 -> هائوجیو 150
  - harley-davidson -> هارلی دیویدسون
  - husqvarna -> هاسکوارنا
  - husqvarna 250 -> هاسکوارنا 250
  - heram-speed -> هرم اسپید
  - heram-speed wave-misc -> هرم اسپید طرح ویو
  - heram-speed wave-misc 130 -> هرم اسپید طرح ویو 130
  - hormoz -> هرمز
  - hormoz 200 -> هرمز 200
  - hormoz CG -> هرمز CG
  - hormoz CG 125 -> هرمز CG 125
  - hamtaz -> همتاز
  - hamtaz atv -> همتاز 4 چرخ
  - hamtaz atv 200 -> همتاز 4 چرخ 200
  - hamtaz electric -> همتاز برقی
  - hamtaz 150 -> همتاز 150
  - hamtaz 110 -> همتاز 110
  - hamtaz wave-misc -> همتاز طرح ویو
  - hamtaz wave-misc 125 -> همتاز طرح ویو 125
  - hamtaz feral -> همتاز SH شکاری
  - hamtaz feral 200 -> همتاز SH شکاری 200
  - hamtaz feral 150 -> همتاز SH شکاری 150
  - hamtaz CGL -> همتاز CGL
  - hamtaz CGL 200 -> همتاز CGL 200
  - hamtaz CGL 150 -> همتاز CGL 150
  - hamtaz CG -> همتاز CG
  - hamtaz CG 200 -> همتاز CG 200
  - hamtaz CG 125 -> همتاز CG 125
  - honda -> هوندا
  - honda pakeshti -> هوندا پاکشتی
  - honda horent -> هوندا هورنت
  - honda horent 600 E -> هوندا هورنت 600 E
  - honda 90 -> هوندا 90
  - honda 70 -> هوندا 70
  - honda 50 -> هوندا 50
  - honda wave-misc-repsol -> هوندا ویو طرح رپسول
  - honda wave-misc-repsol 150 -> هوندا ویو طرح رپسول 150
  - honda wave-misc-repsol 125 -> هوندا ویو طرح رپسول 125
  - honda titan -> هوندا تیتان
  - honda titan 150 -> هوندا تیتان 150
  - honda click -> هوندا کلیک
  - honda click 150 -> هوندا کلیک 150
  - honda click 125 -> هوندا کلیک 125
  - honda blade -> هوندا بلید
  - honda blade 125 -> هوندا بلید 125
  - honda wave -> هوندا ویو
  - honda wave 125 -> هوندا ویو 125
  - honda gold-wing -> هوندا گلدوینگ
  - honda gold-wing 1800 -> هوندا گلدوینگ 1800
  - honda gold-wing 1600 -> هوندا گلدوینگ 1600
  - honda gold-wing 1200 -> هوندا گلدوینگ 1200
  - honda gold-wing 1000 -> هوندا گلدوینگ 1000
  - honda Degree -> هوندا Degree
  - honda Degree 250 -> هوندا Degree 250
  - honda XR -> هوندا XR
  - honda XR 650 -> هوندا XR 650
  - honda XR 250 -> هوندا XR 250
  - honda HRC -> هوندا HRC
  - honda HRC 1000 -> هوندا HRC 1000
  - honda HRC 600 -> هوندا HRC 600
  - honda HRC 250 -> هوندا HRC 250
  - honda XL-trail -> هوندا XL تریل
  - honda XL-trail 250 -> هوندا XL تریل 250
  - honda XL-trail 200 -> هوندا XL تریل 200
  - honda XL-trail 125 -> هوندا XL تریل 125
  - honda NSR -> هوندا NSR
  - honda NSR 150 -> هوندا NSR 150
  - honda NSR 50 -> هوندا NSR 50
  - honda AX1 -> هوندا AX1
  - honda AX1 250 -> هوندا AX1 250
  - honda CRF -> هوندا CRF
  - honda CRF 450 -> هوندا CRF 450
  - honda CRF 250 -> هوندا CRF 250
  - honda CRF 50 -> هوندا CRF 50
  - honda CRM -> هوندا CRM
  - honda CRM 250 -> هوندا CRM 250
  - honda CR -> هوندا CR
  - honda CR 500 -> هوندا CR 500
  - honda CR 250 -> هوندا CR 250
  - honda CR 125 -> هوندا CR 125
  - honda CR 85 -> هوندا CR 85
  - honda CBX -> هوندا CBX
  - honda CBX 750 -> هوندا CBX 750
  - honda CBX 250 -> هوندا CBX 250
  - honda CBK -> هوندا CBK
  - honda CBK 750 -> هوندا CBK 750
  - honda CBF -> هوندا CBF
  - honda CBF 150 -> هوندا CBF 150
  - honda CBF 125 -> هوندا CBF 125
  - honda CBR-repsol -> هوندا CBR رپسول
  - honda CBR-repsol 1000 -> هوندا CBR رپسول 1000
  - honda CBR-repsol 600 -> هوندا CBR رپسول 600
  - honda CBR-repsol 300 -> هوندا CBR رپسول 300
  - honda CBR-repsol 250 -> هوندا CBR رپسول 250
  - honda CBR -> هوندا CBR
  - honda CBR 1100 -> هوندا CBR 1100
  - honda CBR 1000 -> هوندا CBR 1000
  - honda CBR 750 -> هوندا CBR 750
  - honda CBR 600 -> هوندا CBR 600
  - honda CBR 400 -> هوندا CBR 400
  - honda CBR 300 -> هوندا CBR 300
  - honda CBR 250 -> هوندا CBR 250
  - honda CBR 150 -> هوندا CBR 150
  - honda CB-1 -> هوندا CB 1
  - honda CB-1 400 -> هوندا CB 1 400
  - honda CB -> هوندا CB
  - honda CB 1300 -> هوندا CB 1300
  - honda CB 1000 -> هوندا CB 1000
  - honda CB 750 -> هوندا CB 750
  - honda CB 650 -> هوندا CB 650
  - honda CB 300 -> هوندا CB 300
  - honda CB 250 -> هوندا CB 250
  - honda CB 150 -> هوندا CB 150
  - honda CGL -> هوندا CGL
  - honda CGL 150 -> هوندا CGL 150
  - honda CGL 125 -> هوندا CGL 125
  - honda CD -> هوندا CD
  - honda CD 185 -> هوندا CD 185
  - honda CDI -> هوندا CDI
  - honda CDI 125 -> هوندا CDI 125
  - honda CG -> هوندا CG
  - honda CG 125 -> هوندا CG 125
  - hirmand -> هیرمند
  - hirmand wave-misc -> هیرمند طرح ویو
  - hirmand wave-misc 125 -> هیرمند طرح ویو 125
  - hirmand CG -> هیرمند CG
  - hirmand CG 150 -> هیرمند CG 150
  - hirmand CG 125 -> هیرمند CG 125
  - hero -> هیرو
  - hero hunk -> هیرو هانک
  - hero hunk 150 -> هیرو هانک 150
  - hero dash -> هیرو دش
  - hero dash 120 -> هیرو دش 120
  - hero thriller -> هیرو تریلر
  - hero thriller 150 -> هیرو تریلر 150
  - hero pleasure -> هیرو پلیژر
  - hero pleasure 110 -> هیرو پلیژر 110
  - hilton -> هیلتون
  - hilton CG -> هیلتون CG
  - hilton CG 125 -> هیلتون CG 125
  - hilton electric -> هیلتون برقی
  - hilton electric 2000w -> هیلتون برقی 2000 وات
  - hilton electric 1500w -> هیلتون برقی 1500 وات
  - hyosung -> هیوسانگ
  - hyosung 650 -> هیوسانگ 650
  - hyosung trail -> هیوسانگ تریل
  - hyosung trail 200 -> هیوسانگ تریل 200
  - hyosung trail 150 -> هیوسانگ تریل 150
  - hyosung trail 125 -> هیوسانگ تریل 125
  - hyosung GT 250 -> هیوسانگ GT 250
  - hyosung GT 250 N -> هیوسانگ GT 250 N
  - hyosung GT 250 RC -> هیوسانگ GT 250 RC
  - hyosung GT 250 R -> هیوسانگ GT 250 R
  - hyosung aquila -> هیوسانگ اکوئیلا
  - hyosung aquila 250 -> هیوسانگ اکوئیلا 250
  - yamarks -> یامارکس
  - yamarks atv -> یامارکس 4 چرخ
  - yamarks atv 250 -> یامارکس 4 چرخ 250
  - Yamaha -> یاماها
  - Yamaha 3-wheels -> یاماها 3 چرخ
  - Yamaha 3-wheels 125 -> یاماها 3 چرخ 125
  - Yamaha pakeshti -> یاماها پاکشتی
  - Yamaha pakeshti jog -> یاماها پاکشتی جوگ
  - Yamaha pakeshti gear -> یاماها پاکشتی گی ار
  - Yamaha pakeshti vox -> یاماها پاکشتی وکس
  - Yamaha pakeshti vino -> یاماها پاکشتی وینو
  - Yamaha YZF -> یاماها YZF
  - Yamaha YZF 250 -> یاماها YZF 250
  - Yamaha YZ -> یاماها YZ
  - Yamaha YZ 450 -> یاماها YZ 450
  - Yamaha YZ 400 -> یاماها YZ 400
  - Yamaha YZ 250 -> یاماها YZ 250
  - Yamaha YZ 125 -> یاماها YZ 125
  - Yamaha YD -> یاماها YD
  - Yamaha YD 125 -> یاماها YD 125
  - Yamaha YD 100 -> یاماها YD 100
  - Yamaha YB -> یاماها YB
  - Yamaha YB 125 -> یاماها YB 125
  - Yamaha WR -> یاماها WR
  - Yamaha WR 450 F -> یاماها WR 450 F
  - Yamaha WR 250 F -> یاماها WR 250 F
  - Yamaha WR 200 -> یاماها WR 200
  - Yamaha TZR -> یاماها TZR
  - Yamaha TZR 250 -> یاماها TZR 250
  - Yamaha TDR -> یاماها TDR
  - Yamaha TDR 250 -> یاماها TDR 250
  - Yamaha DT -> یاماها DT
  - Yamaha DT 200 -> یاماها DT 200
  - Yamaha DT 175 -> یاماها DT 175
  - Yamaha DT 125 -> یاماها DT 125
  - Yamaha PW -> یاماها PW
  - Yamaha PW 50 -> یاماها PW 50
  - Yamaha R -> یاماها R
  - Yamaha R 25 -> یاماها R 25
  - Yamaha R 15 -> یاماها R 15
  - Yamaha R 6 -> یاماها R 6
  - Yamaha R 3 -> یاماها R 3
  - Yamaha R 1 -> یاماها R 1
  - Yamaha RX -> یاماها RX
  - Yamaha RX 135 -> یاماها RX 135
  - Yamaha RX 100 -> یاماها RX 100
  - Yamaha RS-super -> یاماها RS سوپر
  - Yamaha RS-super 150 -> یاماها RS سوپر 150
  - Yamaha RS-super 125 -> یاماها RS سوپر 125
  - Yamaha FZX -> یاماها FZX
  - Yamaha FZX 750 -> یاماها FZX 750
  - Yamaha FZR -> یاماها FZR
  - Yamaha FZR 1000 -> یاماها FZR 1000
  - Yamaha FZR 250 -> یاماها FZR 250
  - Yamaha FZS -> یاماها FZS
  - Yamaha FZS 160 -> یاماها FZS 160
  - Yamaha FZS 150 -> یاماها FZS 150
  - Yamaha FZ -> یاماها FZ
  - Yamaha FZ 1000 -> یاماها FZ 1000
  - Yamaha FZ 600 -> یاماها FZ 600
  - Yamaha FZ 200 -> یاماها FZ 200
  - Yamaha trail -> یاماها تریل
  - Yamaha trail 400 -> یاماها تریل 400
  - Yamaha trail 250 -> یاماها تریل 250
  - Yamaha trail 125 -> یاماها تریل 125
  - Yamaha trail 100 -> یاماها تریل 100
  - Yamaha lanza -> یاماها لانزا
  - Yamaha 200 -> یاماها 200
  - Yamaha mini -> یاماها مینی 80
  - Yamaha grizzly-atv -> یاماها گریزلی 4 چرخ
  - Yamaha raptor-atv -> یاماها رپتور 4 چرخ
  - Yamaha raptor-atv 700 -> یاماها رپتور 4 چرخ 700
  - Yamaha raptor-atv 250 -> یاماها رپتور 4 چرخ 250
  - Yamaha tricker -> یاماها تریکر
  - Yamaha tricker 250 -> یاماها تریکر 250
  - Yamaha babry -> یاماها ببری
  - Yamaha babry 400 -> یاماها ببری 400
  - samin -> ثمین
  - samin electric -> ثمین برقی
  - samin electric 1000w -> ثمین برقی 1000w
  - other -> سایر

### category
- **Title**: دسته‌بندی
- **Type**: object

### divider
- **Title**: سایر فیلتر‌ها
- **Type**: object

### exchange
- **Title**: نمایش معاوضه‌ها
- **Type**: object
- **Queries**: 
  - only-exchanges -> نمایش فقط معاوضه‌ها
  - exclude-exchanges -> حذف معاوضه‌ها

### has-photo
- **Title**: فقط عکس‌دار
- **Type**: boolean

### non-negotiable
- **Title**: حذف توافقی‌ها
- **Type**: boolean

### post-type
- **Title**: نوع آگهی
- **Type**: object
- **Queries**: 
  - فروشی -> فروشی
  - درخواستی -> درخواستی

### price
- **Title**: قیمت
- **Type**: object
 - **Minimum**: 0
 - **Maximum**: N/A

### production-year
- **Title**: مدل (سال تولید)
- **Type**: object
 - **Minimum**: 0
 - **Maximum**: N/A

### sort
- **Title**: ترتیب نمایش آگهی‌ها براساس
- **Type**: object
- **Queries**: 
  - quality_and_sort_date -> quality_and_sort_date
  - sort_date -> sort_date
  - cheapest -> cheapest
  - most_expensive -> most_expensive
  - production_year -> production_year
  - usage -> usage
  - most_popular -> most_popular
  - most_relevant -> most_relevant

### urgent
- **Title**: فقط فوری‌ها
- **Type**: boolean

### usage
- **Title**: کارکرد
- **Type**: object
 - **Minimum**: 0
 - **Maximum**: N/A



---

### Category: movies-and-music



### category
- **Title**: دسته‌بندی
- **Type**: object

### divider
- **Title**: سایر فیلتر‌ها
- **Type**: object

### exchange
- **Title**: نمایش معاوضه‌ها
- **Type**: object
- **Queries**: 
  - only-exchanges -> نمایش فقط معاوضه‌ها
  - exclude-exchanges -> حذف معاوضه‌ها

### goods-business-type
- **Title**: نوع آگهی‌دهنده
- **Type**: object
- **Queries**: 
  - all -> همه
  - personal -> شخصی
  - marketplace -> فروشگاه

### has-photo
- **Title**: فقط عکس‌دار
- **Type**: boolean

### price
- **Title**: قیمت
- **Type**: object
 - **Minimum**: 0
 - **Maximum**: N/A

### sort
- **Title**: ترتیب نمایش آگهی‌ها براساس
- **Type**: object
- **Queries**: 
  - quality_and_sort_date -> quality_and_sort_date
  - sort_date -> sort_date
  - cheapest -> cheapest
  - most_expensive -> most_expensive
  - production_year -> production_year
  - usage -> usage
  - most_popular -> most_popular
  - most_relevant -> most_relevant

### status
- **Title**: وضعیت کالا
- **Type**: object
 - **Items Type**: array
- **Queries**: 
  - new -> نو
  - like-new -> در حد نو
  - used -> کارکرده
  - repair-needed -> نیازمند تعمیر

### urgent
- **Title**: فقط فوری‌ها
- **Type**: boolean



---

### Category: mp3-player



### category
- **Title**: دسته‌بندی
- **Type**: object

### divider
- **Title**: سایر فیلتر‌ها
- **Type**: object

### exchange
- **Title**: نمایش معاوضه‌ها
- **Type**: object
- **Queries**: 
  - only-exchanges -> نمایش فقط معاوضه‌ها
  - exclude-exchanges -> حذف معاوضه‌ها

### goods-business-type
- **Title**: نوع آگهی‌دهنده
- **Type**: object
- **Queries**: 
  - all -> همه
  - personal -> شخصی
  - marketplace -> فروشگاه

### has-photo
- **Title**: فقط عکس‌دار
- **Type**: boolean

### price
- **Title**: قیمت
- **Type**: object
 - **Minimum**: 0
 - **Maximum**: N/A

### sort
- **Title**: ترتیب نمایش آگهی‌ها براساس
- **Type**: object
- **Queries**: 
  - quality_and_sort_date -> quality_and_sort_date
  - sort_date -> sort_date
  - cheapest -> cheapest
  - most_expensive -> most_expensive
  - production_year -> production_year
  - usage -> usage
  - most_popular -> most_popular
  - most_relevant -> most_relevant

### status
- **Title**: وضعیت کالا
- **Type**: object
 - **Items Type**: array
- **Queries**: 
  - new -> نو
  - like-new -> در حد نو
  - used -> کارکرده
  - repair-needed -> نیازمند تعمیر

### urgent
- **Title**: فقط فوری‌ها
- **Type**: boolean



---

### Category: musical-instruments



### category
- **Title**: دسته‌بندی
- **Type**: object

### divider
- **Title**: سایر فیلتر‌ها
- **Type**: object

### exchange
- **Title**: نمایش معاوضه‌ها
- **Type**: object
- **Queries**: 
  - only-exchanges -> نمایش فقط معاوضه‌ها
  - exclude-exchanges -> حذف معاوضه‌ها

### goods-business-type
- **Title**: نوع آگهی‌دهنده
- **Type**: object
- **Queries**: 
  - all -> همه
  - personal -> شخصی
  - marketplace -> فروشگاه

### has-photo
- **Title**: فقط عکس‌دار
- **Type**: boolean

### price
- **Title**: قیمت
- **Type**: object
 - **Minimum**: 0
 - **Maximum**: N/A

### sort
- **Title**: ترتیب نمایش آگهی‌ها براساس
- **Type**: object
- **Queries**: 
  - quality_and_sort_date -> quality_and_sort_date
  - sort_date -> sort_date
  - cheapest -> cheapest
  - most_expensive -> most_expensive
  - production_year -> production_year
  - usage -> usage
  - most_popular -> most_popular
  - most_relevant -> most_relevant

### status
- **Title**: وضعیت کالا
- **Type**: object
 - **Items Type**: array
- **Queries**: 
  - new -> نو
  - like-new -> در حد نو
  - used -> کارکرده
  - repair-needed -> نیازمند تعمیر

### urgent
- **Title**: فقط فوری‌ها
- **Type**: boolean



---

### Category: natural-plants



### category
- **Title**: دسته‌بندی
- **Type**: object

### divider
- **Title**: سایر فیلتر‌ها
- **Type**: object

### exchange
- **Title**: نمایش معاوضه‌ها
- **Type**: object
- **Queries**: 
  - only-exchanges -> نمایش فقط معاوضه‌ها
  - exclude-exchanges -> حذف معاوضه‌ها

### goods-business-type
- **Title**: نوع آگهی‌دهنده
- **Type**: object
- **Queries**: 
  - all -> همه
  - personal -> شخصی
  - marketplace -> فروشگاه

### has-photo
- **Title**: فقط عکس‌دار
- **Type**: boolean

### price
- **Title**: قیمت
- **Type**: object
 - **Minimum**: 0
 - **Maximum**: N/A

### sort
- **Title**: ترتیب نمایش آگهی‌ها براساس
- **Type**: object
- **Queries**: 
  - quality_and_sort_date -> quality_and_sort_date
  - sort_date -> sort_date
  - cheapest -> cheapest
  - most_expensive -> most_expensive
  - production_year -> production_year
  - usage -> usage
  - most_popular -> most_popular
  - most_relevant -> most_relevant

### status
- **Title**: وضعیت کالا
- **Type**: object
 - **Items Type**: array
- **Queries**: 
  - new -> نو
  - like-new -> در حد نو
  - used -> کارکرده
  - repair-needed -> نیازمند تعمیر

### urgent
- **Title**: فقط فوری‌ها
- **Type**: boolean



---

### Category: office-decoration



### category
- **Title**: دسته‌بندی
- **Type**: object

### divider
- **Title**: سایر فیلتر‌ها
- **Type**: object

### exchange
- **Title**: نمایش معاوضه‌ها
- **Type**: object
- **Queries**: 
  - only-exchanges -> نمایش فقط معاوضه‌ها
  - exclude-exchanges -> حذف معاوضه‌ها

### goods-business-type
- **Title**: نوع آگهی‌دهنده
- **Type**: object
- **Queries**: 
  - all -> همه
  - personal -> شخصی
  - marketplace -> فروشگاه

### has-photo
- **Title**: فقط عکس‌دار
- **Type**: boolean

### price
- **Title**: قیمت
- **Type**: object
 - **Minimum**: 0
 - **Maximum**: N/A

### sort
- **Title**: ترتیب نمایش آگهی‌ها براساس
- **Type**: object
- **Queries**: 
  - quality_and_sort_date -> quality_and_sort_date
  - sort_date -> sort_date
  - cheapest -> cheapest
  - most_expensive -> most_expensive
  - production_year -> production_year
  - usage -> usage
  - most_popular -> most_popular
  - most_relevant -> most_relevant

### status
- **Title**: وضعیت کالا
- **Type**: object
 - **Items Type**: array
- **Queries**: 
  - new -> نو
  - like-new -> در حد نو
  - used -> کارکرده
  - repair-needed -> نیازمند تعمیر

### urgent
- **Title**: فقط فوری‌ها
- **Type**: boolean



---

### Category: office-rent



### building-age
- **Title**: سن بنا
- **Type**: object
- **Queries**: 
  - {"min": 0, "max": 1} -> حداکثر ۱ سال
  - {"min": 0, "max": 2} -> حداکثر ۲ سال
  - {"min": 0, "max": 5} -> حداکثر ۵ سال
  - {"min": 0, "max": 10} -> حداکثر ۱۰ سال
  - {"min": 0, "max": 15} -> حداکثر ۱۵ سال
  - {"min": 0, "max": 20} -> حداکثر ۲۰ سال
  - {"min": 0, "max": 30} -> حداکثر ۳۰ سال
  - {"min": 30} -> بیش از ۳۰ سال

### business-type
- **Title**: آگهی‌دهنده
- **Type**: object
- **Queries**: 
  - personal -> شخصی
  - real-estate-business -> مشاور املاک

### category
- **Title**: دسته‌بندی
- **Type**: object

### credit
- **Title**: ودیعه
- **Type**: object
 - **Minimum**: 0
 - **Maximum**: N/A

### elevator
- **Title**: با آسانسور
- **Type**: boolean

### floor
- **Title**: طبقه
- **Type**: object
 - **Minimum**: -1
 - **Maximum**: N/A

### has-photo
- **Title**: عکس‌دار
- **Type**: boolean

### has-video
- **Title**: ویدیو‌دار
- **Type**: boolean

### parking
- **Title**: با پارکینگ
- **Type**: boolean

### rent
- **Title**: اجاره
- **Type**: object
 - **Minimum**: 0
 - **Maximum**: N/A

### rooms
- **Title**: تعداد اتاق
- **Type**: object
- **Queries**: 
  - بدون اتاق -> بدون اتاق
  - یک -> ۱
  - دو -> ۲
  - سه -> ۳
  - چهار -> ۴
  - بیشتر -> بیشتر از ۴

### size
- **Title**: متراژ
- **Type**: object
 - **Minimum**: 0
 - **Maximum**: 1000000000

### sort
- **Title**: ترتیب نمایش آگهی‌ها براساس
- **Type**: object
- **Queries**: 
  - quality_and_sort_date -> quality_and_sort_date
  - sort_date -> sort_date
  - cheapest -> cheapest
  - most_expensive -> most_expensive
  - production_year -> production_year
  - usage -> usage
  - most_popular -> most_popular
  - most_relevant -> most_relevant

### urgent
- **Title**: فقط فوری‌ها
- **Type**: boolean

### warehouse
- **Title**: با انباری
- **Type**: boolean



---

### Category: office-sell



### bizzDeed
- **Title**: سند اداری
- **Type**: object
- **Queries**: 
  - True -> دارد
  - False -> ندارد

### building-age
- **Title**: سن بنا
- **Type**: object
- **Queries**: 
  - {"min": 0, "max": 1} -> حداکثر ۱ سال
  - {"min": 0, "max": 2} -> حداکثر ۲ سال
  - {"min": 0, "max": 5} -> حداکثر ۵ سال
  - {"min": 0, "max": 10} -> حداکثر ۱۰ سال
  - {"min": 0, "max": 15} -> حداکثر ۱۵ سال
  - {"min": 0, "max": 20} -> حداکثر ۲۰ سال
  - {"min": 0, "max": 30} -> حداکثر ۳۰ سال
  - {"min": 30} -> بیش از ۳۰ سال

### business-type
- **Title**: آگهی‌دهنده
- **Type**: object
- **Queries**: 
  - personal -> شخصی
  - real-estate-business -> مشاور املاک

### category
- **Title**: دسته‌بندی
- **Type**: object

### elevator
- **Title**: با آسانسور
- **Type**: boolean

### floor
- **Title**: طبقه
- **Type**: object
 - **Minimum**: -1
 - **Maximum**: N/A

### has-photo
- **Title**: عکس‌دار
- **Type**: boolean

### has-video
- **Title**: ویدیو‌دار
- **Type**: boolean

### parking
- **Title**: با پارکینگ
- **Type**: boolean

### price
- **Title**: قیمت کل
- **Type**: object
 - **Minimum**: 0
 - **Maximum**: N/A

### rooms
- **Title**: تعداد اتاق
- **Type**: object
- **Queries**: 
  - بدون اتاق -> بدون اتاق
  - یک -> ۱
  - دو -> ۲
  - سه -> ۳
  - چهار -> ۴
  - بیشتر -> بیشتر از ۴

### size
- **Title**: متراژ
- **Type**: object
 - **Minimum**: 0
 - **Maximum**: 1000000000

### sort
- **Title**: ترتیب نمایش آگهی‌ها براساس
- **Type**: object
- **Queries**: 
  - quality_and_sort_date -> quality_and_sort_date
  - sort_date -> sort_date
  - cheapest -> cheapest
  - most_expensive -> most_expensive
  - production_year -> production_year
  - usage -> usage
  - most_popular -> most_popular
  - most_relevant -> most_relevant

### urgent
- **Title**: فقط فوری‌ها
- **Type**: boolean

### warehouse
- **Title**: با انباری
- **Type**: boolean



---

### Category: offices



### category
- **Title**: دسته‌بندی
- **Type**: object

### divider
- **Title**: سایر فیلتر‌ها
- **Type**: object

### exchange
- **Title**: نمایش معاوضه‌ها
- **Type**: object
- **Queries**: 
  - only-exchanges -> نمایش فقط معاوضه‌ها
  - exclude-exchanges -> حذف معاوضه‌ها

### goods-business-type
- **Title**: نوع آگهی‌دهنده
- **Type**: object
- **Queries**: 
  - all -> همه
  - personal -> شخصی
  - marketplace -> فروشگاه

### has-photo
- **Title**: فقط عکس‌دار
- **Type**: boolean

### price
- **Title**: قیمت
- **Type**: object
 - **Minimum**: 0
 - **Maximum**: N/A

### sort
- **Title**: ترتیب نمایش آگهی‌ها براساس
- **Type**: object
- **Queries**: 
  - quality_and_sort_date -> quality_and_sort_date
  - sort_date -> sort_date
  - cheapest -> cheapest
  - most_expensive -> most_expensive
  - production_year -> production_year
  - usage -> usage
  - most_popular -> most_popular
  - most_relevant -> most_relevant

### status
- **Title**: وضعیت کالا
- **Type**: object
 - **Items Type**: array
- **Queries**: 
  - new -> نو
  - like-new -> در حد نو
  - used -> کارکرده
  - repair-needed -> نیازمند تعمیر

### urgent
- **Title**: فقط فوری‌ها
- **Type**: boolean



---

### Category: other-appliances



### category
- **Title**: دسته‌بندی
- **Type**: object

### divider
- **Title**: سایر فیلتر‌ها
- **Type**: object

### exchange
- **Title**: نمایش معاوضه‌ها
- **Type**: object
- **Queries**: 
  - only-exchanges -> نمایش فقط معاوضه‌ها
  - exclude-exchanges -> حذف معاوضه‌ها

### goods-business-type
- **Title**: نوع آگهی‌دهنده
- **Type**: object
- **Queries**: 
  - all -> همه
  - personal -> شخصی
  - marketplace -> فروشگاه

### has-photo
- **Title**: فقط عکس‌دار
- **Type**: boolean

### price
- **Title**: قیمت
- **Type**: object
 - **Minimum**: 0
 - **Maximum**: N/A

### sort
- **Title**: ترتیب نمایش آگهی‌ها براساس
- **Type**: object
- **Queries**: 
  - quality_and_sort_date -> quality_and_sort_date
  - sort_date -> sort_date
  - cheapest -> cheapest
  - most_expensive -> most_expensive
  - production_year -> production_year
  - usage -> usage
  - most_popular -> most_popular
  - most_relevant -> most_relevant

### status
- **Title**: وضعیت کالا
- **Type**: object
 - **Items Type**: array
- **Queries**: 
  - new -> نو
  - like-new -> در حد نو
  - used -> کارکرده
  - repair-needed -> نیازمند تعمیر

### urgent
- **Title**: فقط فوری‌ها
- **Type**: boolean



---

### Category: oven-baking-appliances



### category
- **Title**: دسته‌بندی
- **Type**: object

### divider
- **Title**: سایر فیلتر‌ها
- **Type**: object

### exchange
- **Title**: نمایش معاوضه‌ها
- **Type**: object
- **Queries**: 
  - only-exchanges -> نمایش فقط معاوضه‌ها
  - exclude-exchanges -> حذف معاوضه‌ها

### goods-business-type
- **Title**: نوع آگهی‌دهنده
- **Type**: object
- **Queries**: 
  - all -> همه
  - personal -> شخصی
  - marketplace -> فروشگاه

### has-photo
- **Title**: فقط عکس‌دار
- **Type**: boolean

### price
- **Title**: قیمت
- **Type**: object
 - **Minimum**: 0
 - **Maximum**: N/A

### sort
- **Title**: ترتیب نمایش آگهی‌ها براساس
- **Type**: object
- **Queries**: 
  - quality_and_sort_date -> quality_and_sort_date
  - sort_date -> sort_date
  - cheapest -> cheapest
  - most_expensive -> most_expensive
  - production_year -> production_year
  - usage -> usage
  - most_popular -> most_popular
  - most_relevant -> most_relevant

### status
- **Title**: وضعیت کالا
- **Type**: object
 - **Items Type**: array
- **Queries**: 
  - new -> نو
  - like-new -> در حد نو
  - used -> کارکرده
  - repair-needed -> نیازمند تعمیر

### urgent
- **Title**: فقط فوری‌ها
- **Type**: boolean



---

### Category: paintings-picture



### category
- **Title**: دسته‌بندی
- **Type**: object

### divider
- **Title**: سایر فیلتر‌ها
- **Type**: object

### exchange
- **Title**: نمایش معاوضه‌ها
- **Type**: object
- **Queries**: 
  - only-exchanges -> نمایش فقط معاوضه‌ها
  - exclude-exchanges -> حذف معاوضه‌ها

### goods-business-type
- **Title**: نوع آگهی‌دهنده
- **Type**: object
- **Queries**: 
  - all -> همه
  - personal -> شخصی
  - marketplace -> فروشگاه

### has-photo
- **Title**: فقط عکس‌دار
- **Type**: boolean

### price
- **Title**: قیمت
- **Type**: object
 - **Minimum**: 0
 - **Maximum**: N/A

### sort
- **Title**: ترتیب نمایش آگهی‌ها براساس
- **Type**: object
- **Queries**: 
  - quality_and_sort_date -> quality_and_sort_date
  - sort_date -> sort_date
  - cheapest -> cheapest
  - most_expensive -> most_expensive
  - production_year -> production_year
  - usage -> usage
  - most_popular -> most_popular
  - most_relevant -> most_relevant

### status
- **Title**: وضعیت کالا
- **Type**: object
 - **Items Type**: array
- **Queries**: 
  - new -> نو
  - like-new -> در حد نو
  - used -> کارکرده
  - repair-needed -> نیازمند تعمیر

### urgent
- **Title**: فقط فوری‌ها
- **Type**: boolean



---

### Category: partnership



### business-type
- **Title**: آگهی‌دهنده
- **Type**: object
- **Queries**: 
  - personal -> شخصی
  - real-estate-business -> مشاور املاک

### category
- **Title**: دسته‌بندی
- **Type**: object

### has-photo
- **Title**: عکس‌دار
- **Type**: boolean

### has-video
- **Title**: ویدیو‌دار
- **Type**: boolean

### sort
- **Title**: ترتیب نمایش آگهی‌ها براساس
- **Type**: object
- **Queries**: 
  - quality_and_sort_date -> quality_and_sort_date
  - sort_date -> sort_date
  - cheapest -> cheapest
  - most_expensive -> most_expensive
  - production_year -> production_year
  - usage -> usage
  - most_popular -> most_popular
  - most_relevant -> most_relevant

### urgent
- **Title**: فقط فوری‌ها
- **Type**: boolean



---

### Category: parts-accessories



### category
- **Title**: دسته‌بندی
- **Type**: object

### divider
- **Title**: سایر فیلتر‌ها
- **Type**: object

### exchange
- **Title**: نمایش معاوضه‌ها
- **Type**: object
- **Queries**: 
  - only-exchanges -> نمایش فقط معاوضه‌ها
  - exclude-exchanges -> حذف معاوضه‌ها

### has-photo
- **Title**: فقط عکس‌دار
- **Type**: boolean

### non-negotiable
- **Title**: حذف توافقی‌ها
- **Type**: boolean

### post-type
- **Title**: نوع آگهی
- **Type**: object
- **Queries**: 
  - فروشی -> فروشی
  - درخواستی -> درخواستی

### price
- **Title**: قیمت
- **Type**: object
 - **Minimum**: 0
 - **Maximum**: N/A

### sort
- **Title**: ترتیب نمایش آگهی‌ها براساس
- **Type**: object
- **Queries**: 
  - quality_and_sort_date -> quality_and_sort_date
  - sort_date -> sort_date
  - cheapest -> cheapest
  - most_expensive -> most_expensive
  - production_year -> production_year
  - usage -> usage
  - most_popular -> most_popular
  - most_relevant -> most_relevant

### urgent
- **Title**: فقط فوری‌ها
- **Type**: boolean



---

### Category: parts-and-accessories



### category
- **Title**: دسته‌بندی
- **Type**: object

### divider
- **Title**: سایر فیلتر‌ها
- **Type**: object

### exchange
- **Title**: نمایش معاوضه‌ها
- **Type**: object
- **Queries**: 
  - only-exchanges -> نمایش فقط معاوضه‌ها
  - exclude-exchanges -> حذف معاوضه‌ها

### goods-business-type
- **Title**: نوع آگهی‌دهنده
- **Type**: object
- **Queries**: 
  - all -> همه
  - personal -> شخصی
  - marketplace -> فروشگاه

### has-photo
- **Title**: فقط عکس‌دار
- **Type**: boolean

### price
- **Title**: قیمت
- **Type**: object
 - **Minimum**: 0
 - **Maximum**: N/A

### sort
- **Title**: ترتیب نمایش آگهی‌ها براساس
- **Type**: object
- **Queries**: 
  - quality_and_sort_date -> quality_and_sort_date
  - sort_date -> sort_date
  - cheapest -> cheapest
  - most_expensive -> most_expensive
  - production_year -> production_year
  - usage -> usage
  - most_popular -> most_popular
  - most_relevant -> most_relevant

### status
- **Title**: وضعیت کالا
- **Type**: object
 - **Items Type**: array
- **Queries**: 
  - new -> نو
  - like-new -> در حد نو
  - used -> کارکرده
  - repair-needed -> نیازمند تعمیر

### urgent
- **Title**: فقط فوری‌ها
- **Type**: boolean



---

### Category: personal



### category
- **Title**: دسته‌بندی
- **Type**: object

### divider
- **Title**: سایر فیلتر‌ها
- **Type**: object

### exchange
- **Title**: نمایش معاوضه‌ها
- **Type**: object
- **Queries**: 
  - only-exchanges -> نمایش فقط معاوضه‌ها
  - exclude-exchanges -> حذف معاوضه‌ها

### goods-business-type
- **Title**: نوع آگهی‌دهنده
- **Type**: object
- **Queries**: 
  - all -> همه
  - personal -> شخصی
  - marketplace -> فروشگاه

### has-photo
- **Title**: فقط عکس‌دار
- **Type**: boolean

### price
- **Title**: قیمت
- **Type**: object
 - **Minimum**: 0
 - **Maximum**: N/A

### sort
- **Title**: ترتیب نمایش آگهی‌ها براساس
- **Type**: object
- **Queries**: 
  - quality_and_sort_date -> quality_and_sort_date
  - sort_date -> sort_date
  - cheapest -> cheapest
  - most_expensive -> most_expensive
  - production_year -> production_year
  - usage -> usage
  - most_popular -> most_popular
  - most_relevant -> most_relevant

### status
- **Title**: وضعیت کالا
- **Type**: object
 - **Items Type**: array
- **Queries**: 
  - new -> نو
  - like-new -> در حد نو
  - used -> کارکرده
  - repair-needed -> نیازمند تعمیر

### urgent
- **Title**: فقط فوری‌ها
- **Type**: boolean



---

### Category: personal-toys



### category
- **Title**: دسته‌بندی
- **Type**: object

### divider
- **Title**: سایر فیلتر‌ها
- **Type**: object

### exchange
- **Title**: نمایش معاوضه‌ها
- **Type**: object
- **Queries**: 
  - only-exchanges -> نمایش فقط معاوضه‌ها
  - exclude-exchanges -> حذف معاوضه‌ها

### goods-business-type
- **Title**: نوع آگهی‌دهنده
- **Type**: object
- **Queries**: 
  - all -> همه
  - personal -> شخصی
  - marketplace -> فروشگاه

### has-photo
- **Title**: فقط عکس‌دار
- **Type**: boolean

### price
- **Title**: قیمت
- **Type**: object
 - **Minimum**: 0
 - **Maximum**: N/A

### sort
- **Title**: ترتیب نمایش آگهی‌ها براساس
- **Type**: object
- **Queries**: 
  - quality_and_sort_date -> quality_and_sort_date
  - sort_date -> sort_date
  - cheapest -> cheapest
  - most_expensive -> most_expensive
  - production_year -> production_year
  - usage -> usage
  - most_popular -> most_popular
  - most_relevant -> most_relevant

### status
- **Title**: وضعیت کالا
- **Type**: object
 - **Items Type**: array
- **Queries**: 
  - new -> نو
  - like-new -> در حد نو
  - used -> کارکرده
  - repair-needed -> نیازمند تعمیر

### urgent
- **Title**: فقط فوری‌ها
- **Type**: boolean



---

### Category: phone



### category
- **Title**: دسته‌بندی
- **Type**: object

### divider
- **Title**: سایر فیلتر‌ها
- **Type**: object

### exchange
- **Title**: نمایش معاوضه‌ها
- **Type**: object
- **Queries**: 
  - only-exchanges -> نمایش فقط معاوضه‌ها
  - exclude-exchanges -> حذف معاوضه‌ها

### goods-business-type
- **Title**: نوع آگهی‌دهنده
- **Type**: object
- **Queries**: 
  - all -> همه
  - personal -> شخصی
  - marketplace -> فروشگاه

### has-photo
- **Title**: فقط عکس‌دار
- **Type**: boolean

### price
- **Title**: قیمت
- **Type**: object
 - **Minimum**: 0
 - **Maximum**: N/A

### sort
- **Title**: ترتیب نمایش آگهی‌ها براساس
- **Type**: object
- **Queries**: 
  - quality_and_sort_date -> quality_and_sort_date
  - sort_date -> sort_date
  - cheapest -> cheapest
  - most_expensive -> most_expensive
  - production_year -> production_year
  - usage -> usage
  - most_popular -> most_popular
  - most_relevant -> most_relevant

### status
- **Title**: وضعیت کالا
- **Type**: object
 - **Items Type**: array
- **Queries**: 
  - new -> نو
  - like-new -> در حد نو
  - used -> کارکرده
  - repair-needed -> نیازمند تعمیر

### urgent
- **Title**: فقط فوری‌ها
- **Type**: boolean



---

### Category: phone-desk



### category
- **Title**: دسته‌بندی
- **Type**: object

### divider
- **Title**: سایر فیلتر‌ها
- **Type**: object

### exchange
- **Title**: نمایش معاوضه‌ها
- **Type**: object
- **Queries**: 
  - only-exchanges -> نمایش فقط معاوضه‌ها
  - exclude-exchanges -> حذف معاوضه‌ها

### goods-business-type
- **Title**: نوع آگهی‌دهنده
- **Type**: object
- **Queries**: 
  - all -> همه
  - personal -> شخصی
  - marketplace -> فروشگاه

### has-photo
- **Title**: فقط عکس‌دار
- **Type**: boolean

### price
- **Title**: قیمت
- **Type**: object
 - **Minimum**: 0
 - **Maximum**: N/A

### sort
- **Title**: ترتیب نمایش آگهی‌ها براساس
- **Type**: object
- **Queries**: 
  - quality_and_sort_date -> quality_and_sort_date
  - sort_date -> sort_date
  - cheapest -> cheapest
  - most_expensive -> most_expensive
  - production_year -> production_year
  - usage -> usage
  - most_popular -> most_popular
  - most_relevant -> most_relevant

### status
- **Title**: وضعیت کالا
- **Type**: object
 - **Items Type**: array
- **Queries**: 
  - new -> نو
  - like-new -> در حد نو
  - used -> کارکرده
  - repair-needed -> نیازمند تعمیر

### urgent
- **Title**: فقط فوری‌ها
- **Type**: boolean



---

### Category: piano-keyboard



### category
- **Title**: دسته‌بندی
- **Type**: object

### divider
- **Title**: سایر فیلتر‌ها
- **Type**: object

### exchange
- **Title**: نمایش معاوضه‌ها
- **Type**: object
- **Queries**: 
  - only-exchanges -> نمایش فقط معاوضه‌ها
  - exclude-exchanges -> حذف معاوضه‌ها

### goods-business-type
- **Title**: نوع آگهی‌دهنده
- **Type**: object
- **Queries**: 
  - all -> همه
  - personal -> شخصی
  - marketplace -> فروشگاه

### has-photo
- **Title**: فقط عکس‌دار
- **Type**: boolean

### price
- **Title**: قیمت
- **Type**: object
 - **Minimum**: 0
 - **Maximum**: N/A

### sort
- **Title**: ترتیب نمایش آگهی‌ها براساس
- **Type**: object
- **Queries**: 
  - quality_and_sort_date -> quality_and_sort_date
  - sort_date -> sort_date
  - cheapest -> cheapest
  - most_expensive -> most_expensive
  - production_year -> production_year
  - usage -> usage
  - most_popular -> most_popular
  - most_relevant -> most_relevant

### status
- **Title**: وضعیت کالا
- **Type**: object
 - **Items Type**: array
- **Queries**: 
  - new -> نو
  - like-new -> در حد نو
  - used -> کارکرده
  - repair-needed -> نیازمند تعمیر

### urgent
- **Title**: فقط فوری‌ها
- **Type**: boolean



---

### Category: pictorial-carpet



### category
- **Title**: دسته‌بندی
- **Type**: object

### divider
- **Title**: سایر فیلتر‌ها
- **Type**: object

### exchange
- **Title**: نمایش معاوضه‌ها
- **Type**: object
- **Queries**: 
  - only-exchanges -> نمایش فقط معاوضه‌ها
  - exclude-exchanges -> حذف معاوضه‌ها

### goods-business-type
- **Title**: نوع آگهی‌دهنده
- **Type**: object
- **Queries**: 
  - all -> همه
  - personal -> شخصی
  - marketplace -> فروشگاه

### has-photo
- **Title**: فقط عکس‌دار
- **Type**: boolean

### price
- **Title**: قیمت
- **Type**: object
 - **Minimum**: 0
 - **Maximum**: N/A

### sort
- **Title**: ترتیب نمایش آگهی‌ها براساس
- **Type**: object
- **Queries**: 
  - quality_and_sort_date -> quality_and_sort_date
  - sort_date -> sort_date
  - cheapest -> cheapest
  - most_expensive -> most_expensive
  - production_year -> production_year
  - usage -> usage
  - most_popular -> most_popular
  - most_relevant -> most_relevant

### status
- **Title**: وضعیت کالا
- **Type**: object
 - **Items Type**: array
- **Queries**: 
  - new -> نو
  - like-new -> در حد نو
  - used -> کارکرده
  - repair-needed -> نیازمند تعمیر

### urgent
- **Title**: فقط فوری‌ها
- **Type**: boolean



---

### Category: plot-old



### business-type
- **Title**: آگهی‌دهنده
- **Type**: object
- **Queries**: 
  - personal -> شخصی
  - real-estate-business -> مشاور املاک

### category
- **Title**: دسته‌بندی
- **Type**: object

### has-photo
- **Title**: عکس‌دار
- **Type**: boolean

### has-video
- **Title**: ویدیو‌دار
- **Type**: boolean

### price
- **Title**: قیمت کل
- **Type**: object
 - **Minimum**: 0
 - **Maximum**: N/A

### size
- **Title**: متراژ
- **Type**: object
 - **Minimum**: 0
 - **Maximum**: N/A

### sort
- **Title**: ترتیب نمایش آگهی‌ها براساس
- **Type**: object
- **Queries**: 
  - quality_and_sort_date -> quality_and_sort_date
  - sort_date -> sort_date
  - cheapest -> cheapest
  - most_expensive -> most_expensive
  - production_year -> production_year
  - usage -> usage
  - most_popular -> most_popular
  - most_relevant -> most_relevant

### urgent
- **Title**: فقط فوری‌ها
- **Type**: boolean



---

### Category: pot-kettle



### category
- **Title**: دسته‌بندی
- **Type**: object

### divider
- **Title**: سایر فیلتر‌ها
- **Type**: object

### exchange
- **Title**: نمایش معاوضه‌ها
- **Type**: object
- **Queries**: 
  - only-exchanges -> نمایش فقط معاوضه‌ها
  - exclude-exchanges -> حذف معاوضه‌ها

### goods-business-type
- **Title**: نوع آگهی‌دهنده
- **Type**: object
- **Queries**: 
  - all -> همه
  - personal -> شخصی
  - marketplace -> فروشگاه

### has-photo
- **Title**: فقط عکس‌دار
- **Type**: boolean

### price
- **Title**: قیمت
- **Type**: object
 - **Minimum**: 0
 - **Maximum**: N/A

### sort
- **Title**: ترتیب نمایش آگهی‌ها براساس
- **Type**: object
- **Queries**: 
  - quality_and_sort_date -> quality_and_sort_date
  - sort_date -> sort_date
  - cheapest -> cheapest
  - most_expensive -> most_expensive
  - production_year -> production_year
  - usage -> usage
  - most_popular -> most_popular
  - most_relevant -> most_relevant

### status
- **Title**: وضعیت کالا
- **Type**: object
 - **Items Type**: array
- **Queries**: 
  - new -> نو
  - like-new -> در حد نو
  - used -> کارکرده
  - repair-needed -> نیازمند تعمیر

### urgent
- **Title**: فقط فوری‌ها
- **Type**: boolean



---

### Category: presell



### business-type
- **Title**: آگهی‌دهنده
- **Type**: object
- **Queries**: 
  - personal -> شخصی
  - real-estate-business -> مشاور املاک

### category
- **Title**: دسته‌بندی
- **Type**: object

### has-photo
- **Title**: عکس‌دار
- **Type**: boolean

### has-video
- **Title**: ویدیو‌دار
- **Type**: boolean

### sort
- **Title**: ترتیب نمایش آگهی‌ها براساس
- **Type**: object
- **Queries**: 
  - quality_and_sort_date -> quality_and_sort_date
  - sort_date -> sort_date
  - cheapest -> cheapest
  - most_expensive -> most_expensive
  - production_year -> production_year
  - usage -> usage
  - most_popular -> most_popular
  - most_relevant -> most_relevant

### urgent
- **Title**: فقط فوری‌ها
- **Type**: boolean



---

### Category: printer-scaner-copier



### category
- **Title**: دسته‌بندی
- **Type**: object

### divider
- **Title**: سایر فیلتر‌ها
- **Type**: object

### exchange
- **Title**: نمایش معاوضه‌ها
- **Type**: object
- **Queries**: 
  - only-exchanges -> نمایش فقط معاوضه‌ها
  - exclude-exchanges -> حذف معاوضه‌ها

### goods-business-type
- **Title**: نوع آگهی‌دهنده
- **Type**: object
- **Queries**: 
  - all -> همه
  - personal -> شخصی
  - marketplace -> فروشگاه

### has-photo
- **Title**: فقط عکس‌دار
- **Type**: boolean

### price
- **Title**: قیمت
- **Type**: object
 - **Minimum**: 0
 - **Maximum**: N/A

### sort
- **Title**: ترتیب نمایش آگهی‌ها براساس
- **Type**: object
- **Queries**: 
  - quality_and_sort_date -> quality_and_sort_date
  - sort_date -> sort_date
  - cheapest -> cheapest
  - most_expensive -> most_expensive
  - production_year -> production_year
  - usage -> usage
  - most_popular -> most_popular
  - most_relevant -> most_relevant

### status
- **Title**: وضعیت کالا
- **Type**: object
 - **Items Type**: array
- **Queries**: 
  - new -> نو
  - like-new -> در حد نو
  - used -> کارکرده
  - repair-needed -> نیازمند تعمیر

### urgent
- **Title**: فقط فوری‌ها
- **Type**: boolean



---

### Category: range-hood



### category
- **Title**: دسته‌بندی
- **Type**: object

### divider
- **Title**: سایر فیلتر‌ها
- **Type**: object

### exchange
- **Title**: نمایش معاوضه‌ها
- **Type**: object
- **Queries**: 
  - only-exchanges -> نمایش فقط معاوضه‌ها
  - exclude-exchanges -> حذف معاوضه‌ها

### goods-business-type
- **Title**: نوع آگهی‌دهنده
- **Type**: object
- **Queries**: 
  - all -> همه
  - personal -> شخصی
  - marketplace -> فروشگاه

### has-photo
- **Title**: فقط عکس‌دار
- **Type**: boolean

### price
- **Title**: قیمت
- **Type**: object
 - **Minimum**: 0
 - **Maximum**: N/A

### sort
- **Title**: ترتیب نمایش آگهی‌ها براساس
- **Type**: object
- **Queries**: 
  - quality_and_sort_date -> quality_and_sort_date
  - sort_date -> sort_date
  - cheapest -> cheapest
  - most_expensive -> most_expensive
  - production_year -> production_year
  - usage -> usage
  - most_popular -> most_popular
  - most_relevant -> most_relevant

### status
- **Title**: وضعیت کالا
- **Type**: object
 - **Items Type**: array
- **Queries**: 
  - new -> نو
  - like-new -> در حد نو
  - used -> کارکرده
  - repair-needed -> نیازمند تعمیر

### urgent
- **Title**: فقط فوری‌ها
- **Type**: boolean



---

### Category: real-estate



### business-type
- **Title**: آگهی‌دهنده
- **Type**: object
- **Queries**: 
  - personal -> شخصی
  - real-estate-business -> مشاور املاک

### category
- **Title**: دسته‌بندی
- **Type**: object

### has-photo
- **Title**: عکس‌دار
- **Type**: boolean

### has-video
- **Title**: ویدیو‌دار
- **Type**: boolean

### sort
- **Title**: ترتیب نمایش آگهی‌ها براساس
- **Type**: object
- **Queries**: 
  - quality_and_sort_date -> quality_and_sort_date
  - sort_date -> sort_date
  - cheapest -> cheapest
  - most_expensive -> most_expensive
  - production_year -> production_year
  - usage -> usage
  - most_popular -> most_popular
  - most_relevant -> most_relevant

### urgent
- **Title**: فقط فوری‌ها
- **Type**: boolean



---

### Category: real-estate-services



### business-type
- **Title**: آگهی‌دهنده
- **Type**: object
- **Queries**: 
  - personal -> شخصی
  - real-estate-business -> مشاور املاک

### category
- **Title**: دسته‌بندی
- **Type**: object

### has-photo
- **Title**: عکس‌دار
- **Type**: boolean

### has-video
- **Title**: ویدیو‌دار
- **Type**: boolean

### sort
- **Title**: ترتیب نمایش آگهی‌ها براساس
- **Type**: object
- **Queries**: 
  - quality_and_sort_date -> quality_and_sort_date
  - sort_date -> sort_date
  - cheapest -> cheapest
  - most_expensive -> most_expensive
  - production_year -> production_year
  - usage -> usage
  - most_popular -> most_popular
  - most_relevant -> most_relevant

### urgent
- **Title**: فقط فوری‌ها
- **Type**: boolean



---

### Category: refrigerator-freezer



### brands
- **Title**: سازنده
- **Type**: object
 - **Items Type**: array
- **Queries**: 
  - آرچلیک -> آرچلیک
  - آزمایش -> آزمایش
  - آنتیک -> آنتیک
  - آی فادر -> آی فادر
  - اسمگ -> اسمگ
  - اسنوا -> اسنوا
  - اکسپریال -> اکسپریال
  - اکسنت -> اکسنت
  - اکولوکس -> اکولوکس
  - ال جی -> ال جی
  - الکترواستیل -> الکترواستیل
  - امرسان -> امرسان
  - ای بی سی -> ای بی سی
  - ایران شرق -> ایران شرق
  - ایستکول -> ایستکول
  - ایکس ویژن -> ایکس ویژن
  - ایندزیت -> ایندزیت
  - برتینو -> برتینو
  - برفاب -> برفاب
  - بکو -> بکو
  - بلومبرگ -> بلومبرگ
  - بنس -> بنس
  - بوش -> بوش
  - پارس -> پارس
  - پلادیوم -> پلادیوم
  - پلار -> پلار
  - تکنوگاز -> تکنوگاز
  - تکنوهاوس -> تکنوهاوس
  - توتال -> توتال
  - توشیبا -> توشیبا
  - تی سی ال -> تی سی ال
  - جنرال الکتریک -> جنرال الکتریک
  - جنرال پویا -> جنرال پویا
  - جنرال هاوس -> جنرال هاوس
  - جی پلاس -> جی پلاس
  - جی سان -> جی سان
  - دوو -> دوو
  - دیپوینت -> دیپوینت
  - ریتون -> ریتون
  - زیرووات -> زیرووات
  - سام -> سام
  - سامسونگ -> سامسونگ
  - سیلور -> سیلور
  - سینجر -> سینجر
  - شارپ -> شارپ
  - فیلور -> فیلور
  - کرال -> کرال
  - کلور -> کلور
  - کندی -> کندی
  - کنوود -> کنوود
  - لایف -> لایف
  - هیوندای -> هیوندای
  - لوپز -> لوپز
  - مایدیا -> مایدیا
  - مجیک -> مجیک
  - مجیک کولینگ -> مجیک کولینگ
  - نیکسان -> نیکسان
  - هاردستون -> هاردستون
  - هاریکا -> هاریکا
  - هافن برگ -> هافن برگ
  - هایر -> هایر
  - هایسنس -> هایسنس
  - هیتاچی -> هیتاچی
  - هیتما -> هیتما
  - هیمالیا -> هیمالیا
  - وست پوینت -> وست پوینت
  - وستل -> وستل
  - ویرپول -> ویرپول
  - یخساران -> یخساران
  - یورو استار -> یورو استار
  - غیره -> غیره

### category
- **Title**: دسته‌بندی
- **Type**: object

### divider
- **Title**: سایر فیلتر‌ها
- **Type**: object

### exchange
- **Title**: نمایش معاوضه‌ها
- **Type**: object
- **Queries**: 
  - only-exchanges -> نمایش فقط معاوضه‌ها
  - exclude-exchanges -> حذف معاوضه‌ها

### goods-business-type
- **Title**: نوع آگهی‌دهنده
- **Type**: object
- **Queries**: 
  - all -> همه
  - personal -> شخصی
  - marketplace -> فروشگاه

### has-photo
- **Title**: فقط عکس‌دار
- **Type**: boolean

### price
- **Title**: قیمت
- **Type**: object
 - **Minimum**: 0
 - **Maximum**: N/A

### sort
- **Title**: ترتیب نمایش آگهی‌ها براساس
- **Type**: object
- **Queries**: 
  - quality_and_sort_date -> quality_and_sort_date
  - sort_date -> sort_date
  - cheapest -> cheapest
  - most_expensive -> most_expensive
  - production_year -> production_year
  - usage -> usage
  - most_popular -> most_popular
  - most_relevant -> most_relevant

### status
- **Title**: وضعیت کالا
- **Type**: object
 - **Items Type**: array
- **Queries**: 
  - new -> نو
  - like-new -> در حد نو
  - used -> کارکرده
  - repair-needed -> نیازمند تعمیر

### urgent
- **Title**: فقط فوری‌ها
- **Type**: boolean



---

### Category: religious



### category
- **Title**: دسته‌بندی
- **Type**: object

### divider
- **Title**: سایر فیلتر‌ها
- **Type**: object

### exchange
- **Title**: نمایش معاوضه‌ها
- **Type**: object
- **Queries**: 
  - only-exchanges -> نمایش فقط معاوضه‌ها
  - exclude-exchanges -> حذف معاوضه‌ها

### goods-business-type
- **Title**: نوع آگهی‌دهنده
- **Type**: object
- **Queries**: 
  - all -> همه
  - personal -> شخصی
  - marketplace -> فروشگاه

### has-photo
- **Title**: فقط عکس‌دار
- **Type**: boolean

### price
- **Title**: قیمت
- **Type**: object
 - **Minimum**: 0
 - **Maximum**: N/A

### sort
- **Title**: ترتیب نمایش آگهی‌ها براساس
- **Type**: object
- **Queries**: 
  - quality_and_sort_date -> quality_and_sort_date
  - sort_date -> sort_date
  - cheapest -> cheapest
  - most_expensive -> most_expensive
  - production_year -> production_year
  - usage -> usage
  - most_popular -> most_popular
  - most_relevant -> most_relevant

### status
- **Title**: وضعیت کالا
- **Type**: object
 - **Items Type**: array
- **Queries**: 
  - new -> نو
  - like-new -> در حد نو
  - used -> کارکرده
  - repair-needed -> نیازمند تعمیر

### urgent
- **Title**: فقط فوری‌ها
- **Type**: boolean



---

### Category: rental



### category
- **Title**: دسته‌بندی
- **Type**: object

### divider
- **Title**: سایر فیلتر‌ها
- **Type**: object

### has-photo
- **Title**: فقط عکس‌دار
- **Type**: boolean

### non-negotiable
- **Title**: حذف توافقی‌ها
- **Type**: boolean

### post-type
- **Title**: نوع آگهی
- **Type**: object
- **Queries**: 
  - ارائه -> ارائه
  - درخواستی -> درخواستی

### price
- **Title**: قیمت
- **Type**: object
 - **Minimum**: 0
 - **Maximum**: N/A

### sort
- **Title**: ترتیب نمایش آگهی‌ها براساس
- **Type**: object
- **Queries**: 
  - quality_and_sort_date -> quality_and_sort_date
  - sort_date -> sort_date
  - cheapest -> cheapest
  - most_expensive -> most_expensive
  - production_year -> production_year
  - usage -> usage
  - most_popular -> most_popular
  - most_relevant -> most_relevant

### urgent
- **Title**: فقط فوری‌ها
- **Type**: boolean



---

### Category: reptile



### category
- **Title**: دسته‌بندی
- **Type**: object

### divider
- **Title**: سایر فیلتر‌ها
- **Type**: object

### exchange
- **Title**: نمایش معاوضه‌ها
- **Type**: object
- **Queries**: 
  - only-exchanges -> نمایش فقط معاوضه‌ها
  - exclude-exchanges -> حذف معاوضه‌ها

### has-photo
- **Title**: فقط عکس‌دار
- **Type**: boolean

### price
- **Title**: قیمت
- **Type**: object
 - **Minimum**: 0
 - **Maximum**: N/A

### sort
- **Title**: ترتیب نمایش آگهی‌ها براساس
- **Type**: object
- **Queries**: 
  - quality_and_sort_date -> quality_and_sort_date
  - sort_date -> sort_date
  - cheapest -> cheapest
  - most_expensive -> most_expensive
  - production_year -> production_year
  - usage -> usage
  - most_popular -> most_popular
  - most_relevant -> most_relevant

### urgent
- **Title**: فقط فوری‌ها
- **Type**: boolean



---

### Category: research



### category
- **Title**: دسته‌بندی
- **Type**: object

### divider
- **Title**: سایر فیلتر‌ها
- **Type**: object

### has-photo
- **Title**: فقط عکس‌دار
- **Type**: boolean

### sort
- **Title**: ترتیب نمایش آگهی‌ها براساس
- **Type**: object
- **Queries**: 
  - quality_and_sort_date -> quality_and_sort_date
  - sort_date -> sort_date
  - cheapest -> cheapest
  - most_expensive -> most_expensive
  - production_year -> production_year
  - usage -> usage
  - most_popular -> most_popular
  - most_relevant -> most_relevant

### urgent
- **Title**: فقط فوری‌ها
- **Type**: boolean



---

### Category: residential-rent



### business-type
- **Title**: آگهی‌دهنده
- **Type**: object
- **Queries**: 
  - personal -> شخصی
  - real-estate-business -> مشاور املاک

### category
- **Title**: دسته‌بندی
- **Type**: object

### credit
- **Title**: ودیعه
- **Type**: object
 - **Minimum**: 0
 - **Maximum**: N/A

### has-photo
- **Title**: عکس‌دار
- **Type**: boolean

### has-video
- **Title**: ویدیو‌دار
- **Type**: boolean

### rent
- **Title**: اجاره
- **Type**: object
 - **Minimum**: 0
 - **Maximum**: N/A

### rent_to_single
- **Title**: مناسب مجرد
- **Type**: boolean

### rooms
- **Title**: تعداد اتاق
- **Type**: object
- **Queries**: 
  - بدون اتاق -> بدون اتاق
  - یک -> ۱
  - دو -> ۲
  - سه -> ۳
  - چهار -> ۴
  - بیشتر -> بیشتر از ۴

### size
- **Title**: متراژ
- **Type**: object
 - **Minimum**: 0
 - **Maximum**: 1000000000

### sort
- **Title**: ترتیب نمایش آگهی‌ها براساس
- **Type**: object
- **Queries**: 
  - quality_and_sort_date -> quality_and_sort_date
  - sort_date -> sort_date
  - cheapest -> cheapest
  - most_expensive -> most_expensive
  - production_year -> production_year
  - usage -> usage
  - most_popular -> most_popular
  - most_relevant -> most_relevant

### urgent
- **Title**: فقط فوری‌ها
- **Type**: boolean

### warehouse
- **Title**: با انباری
- **Type**: boolean



---

### Category: residential-sell



### business-type
- **Title**: آگهی‌دهنده
- **Type**: object
- **Queries**: 
  - personal -> شخصی
  - real-estate-business -> مشاور املاک

### category
- **Title**: دسته‌بندی
- **Type**: object

### has-photo
- **Title**: عکس‌دار
- **Type**: boolean

### has-video
- **Title**: ویدیو‌دار
- **Type**: boolean

### price
- **Title**: قیمت کل
- **Type**: object
 - **Minimum**: 0
 - **Maximum**: N/A

### size
- **Title**: متراژ
- **Type**: object
 - **Minimum**: 0
 - **Maximum**: 1000000000

### sort
- **Title**: ترتیب نمایش آگهی‌ها براساس
- **Type**: object
- **Queries**: 
  - quality_and_sort_date -> quality_and_sort_date
  - sort_date -> sort_date
  - cheapest -> cheapest
  - most_expensive -> most_expensive
  - production_year -> production_year
  - usage -> usage
  - most_popular -> most_popular
  - most_relevant -> most_relevant

### urgent
- **Title**: فقط فوری‌ها
- **Type**: boolean



---

### Category: rhinestones



### category
- **Title**: دسته‌بندی
- **Type**: object

### divider
- **Title**: سایر فیلتر‌ها
- **Type**: object

### exchange
- **Title**: نمایش معاوضه‌ها
- **Type**: object
- **Queries**: 
  - only-exchanges -> نمایش فقط معاوضه‌ها
  - exclude-exchanges -> حذف معاوضه‌ها

### goods-business-type
- **Title**: نوع آگهی‌دهنده
- **Type**: object
- **Queries**: 
  - all -> همه
  - personal -> شخصی
  - marketplace -> فروشگاه

### has-photo
- **Title**: فقط عکس‌دار
- **Type**: boolean

### merchandise-type
- **Title**: نوع بدلیجات
- **Type**: object
 - **Items Type**: array
- **Queries**: 
  - انگشتر -> انگشتر
  - گوشواره -> گوشواره
  - دست‌بند -> دست‌بند
  - زنجیر و گردن‌بند -> زنجیر و گردن‌بند
  - پابند -> پابند
  - ست و نیم‌ست -> ست و نیم‌ست
  - غیره -> غیره

### price
- **Title**: قیمت
- **Type**: object
 - **Minimum**: 0
 - **Maximum**: N/A

### sort
- **Title**: ترتیب نمایش آگهی‌ها براساس
- **Type**: object
- **Queries**: 
  - quality_and_sort_date -> quality_and_sort_date
  - sort_date -> sort_date
  - cheapest -> cheapest
  - most_expensive -> most_expensive
  - production_year -> production_year
  - usage -> usage
  - most_popular -> most_popular
  - most_relevant -> most_relevant

### status
- **Title**: وضعیت کالا
- **Type**: object
 - **Items Type**: array
- **Queries**: 
  - new -> نو
  - like-new -> در حد نو
  - used -> کارکرده
  - repair-needed -> نیازمند تعمیر

### urgent
- **Title**: فقط فوری‌ها
- **Type**: boolean



---

### Category: rodents-rabbits



### category
- **Title**: دسته‌بندی
- **Type**: object

### divider
- **Title**: سایر فیلتر‌ها
- **Type**: object

### exchange
- **Title**: نمایش معاوضه‌ها
- **Type**: object
- **Queries**: 
  - only-exchanges -> نمایش فقط معاوضه‌ها
  - exclude-exchanges -> حذف معاوضه‌ها

### has-photo
- **Title**: فقط عکس‌دار
- **Type**: boolean

### price
- **Title**: قیمت
- **Type**: object
 - **Minimum**: 0
 - **Maximum**: N/A

### sort
- **Title**: ترتیب نمایش آگهی‌ها براساس
- **Type**: object
- **Queries**: 
  - quality_and_sort_date -> quality_and_sort_date
  - sort_date -> sort_date
  - cheapest -> cheapest
  - most_expensive -> most_expensive
  - production_year -> production_year
  - usage -> usage
  - most_popular -> most_popular
  - most_relevant -> most_relevant

### urgent
- **Title**: فقط فوری‌ها
- **Type**: boolean



---

### Category: rubber-carpet



### category
- **Title**: دسته‌بندی
- **Type**: object

### divider
- **Title**: سایر فیلتر‌ها
- **Type**: object

### exchange
- **Title**: نمایش معاوضه‌ها
- **Type**: object
- **Queries**: 
  - only-exchanges -> نمایش فقط معاوضه‌ها
  - exclude-exchanges -> حذف معاوضه‌ها

### goods-business-type
- **Title**: نوع آگهی‌دهنده
- **Type**: object
- **Queries**: 
  - all -> همه
  - personal -> شخصی
  - marketplace -> فروشگاه

### has-photo
- **Title**: فقط عکس‌دار
- **Type**: boolean

### price
- **Title**: قیمت
- **Type**: object
 - **Minimum**: 0
 - **Maximum**: N/A

### sort
- **Title**: ترتیب نمایش آگهی‌ها براساس
- **Type**: object
- **Queries**: 
  - quality_and_sort_date -> quality_and_sort_date
  - sort_date -> sort_date
  - cheapest -> cheapest
  - most_expensive -> most_expensive
  - production_year -> production_year
  - usage -> usage
  - most_popular -> most_popular
  - most_relevant -> most_relevant

### status
- **Title**: وضعیت کالا
- **Type**: object
 - **Items Type**: array
- **Queries**: 
  - new -> نو
  - like-new -> در حد نو
  - used -> کارکرده
  - repair-needed -> نیازمند تعمیر

### urgent
- **Title**: فقط فوری‌ها
- **Type**: boolean



---

### Category: rugs-woolen-cloth



### category
- **Title**: دسته‌بندی
- **Type**: object

### divider
- **Title**: سایر فیلتر‌ها
- **Type**: object

### exchange
- **Title**: نمایش معاوضه‌ها
- **Type**: object
- **Queries**: 
  - only-exchanges -> نمایش فقط معاوضه‌ها
  - exclude-exchanges -> حذف معاوضه‌ها

### goods-business-type
- **Title**: نوع آگهی‌دهنده
- **Type**: object
- **Queries**: 
  - all -> همه
  - personal -> شخصی
  - marketplace -> فروشگاه

### has-photo
- **Title**: فقط عکس‌دار
- **Type**: boolean

### price
- **Title**: قیمت
- **Type**: object
 - **Minimum**: 0
 - **Maximum**: N/A

### sort
- **Title**: ترتیب نمایش آگهی‌ها براساس
- **Type**: object
- **Queries**: 
  - quality_and_sort_date -> quality_and_sort_date
  - sort_date -> sort_date
  - cheapest -> cheapest
  - most_expensive -> most_expensive
  - production_year -> production_year
  - usage -> usage
  - most_popular -> most_popular
  - most_relevant -> most_relevant

### status
- **Title**: وضعیت کالا
- **Type**: object
 - **Items Type**: array
- **Queries**: 
  - new -> نو
  - like-new -> در حد نو
  - used -> کارکرده
  - repair-needed -> نیازمند تعمیر

### urgent
- **Title**: فقط فوری‌ها
- **Type**: boolean



---

### Category: sales-marketing



### category
- **Title**: دسته‌بندی
- **Type**: object

### divider
- **Title**: سایر فیلتر‌ها
- **Type**: object

### employee_gender
- **Title**: جنسیت کارجو
- **Type**: object
- **Queries**: 
  - female -> زن
  - male -> مرد
  - neutral -> فرقی ندارد

### experience
- **Title**: سابقهٔ مورد نیاز
- **Type**: object
 - **Minimum**: N/A
 - **Maximum**: N/A

### has-photo
- **Title**: فقط عکس‌دار
- **Type**: boolean

### health_insurance
- **Title**: با بیمه
- **Type**: boolean

### job_type
- **Title**: نوع همکاری
- **Type**: object
 - **Items Type**: array
- **Queries**: 
  - full_time -> تمام وقت
  - part_time -> پاره وقت
  - contract -> پیمان‌کاری/پروژه‌ای
  - internship -> کارآموزی
  - adaptive -> توافقی
  - other -> سایر

### military_service_status
- **Title**: پایان خدمت/معافیت
- **Type**: object
- **Queries**: 
  - finish_or_exemption_required -> الزامی
  - finish_not_required -> اختیاری

### no_experience_required
- **Title**: بدون نیاز به سابقه
- **Type**: boolean

### payment_method
- **Title**: شیوهٔ پرداخت
- **Type**: object
 - **Items Type**: array
- **Queries**: 
  - monthly -> ماهانه
  - daily -> روزانه
  - hourly -> ساعتی
  - percentage_commission -> پورسانتی/درصدی
  - adaptive -> توافقی
  - other -> سایر

### remote
- **Title**: با امکان دورکاری
- **Type**: boolean

### sort
- **Title**: ترتیب نمایش آگهی‌ها براساس
- **Type**: object
- **Queries**: 
  - quality_and_sort_date -> quality_and_sort_date
  - sort_date -> sort_date
  - cheapest -> cheapest
  - most_expensive -> most_expensive
  - production_year -> production_year
  - usage -> usage
  - most_popular -> most_popular
  - most_relevant -> most_relevant

### urgent
- **Title**: فقط فوری‌ها
- **Type**: boolean



---

### Category: services



### category
- **Title**: دسته‌بندی
- **Type**: object

### has-photo
- **Title**: فقط عکس‌دار
- **Type**: boolean

### sort
- **Title**: ترتیب نمایش آگهی‌ها براساس
- **Type**: object
- **Queries**: 
  - quality_and_sort_date -> quality_and_sort_date
  - sort_date -> sort_date
  - cheapest -> cheapest
  - most_expensive -> most_expensive
  - production_year -> production_year
  - usage -> usage
  - most_popular -> most_popular
  - most_relevant -> most_relevant

### urgent
- **Title**: فقط فوری‌ها
- **Type**: boolean



---

### Category: sewing-accessories



### category
- **Title**: دسته‌بندی
- **Type**: object

### divider
- **Title**: سایر فیلتر‌ها
- **Type**: object

### exchange
- **Title**: نمایش معاوضه‌ها
- **Type**: object
- **Queries**: 
  - only-exchanges -> نمایش فقط معاوضه‌ها
  - exclude-exchanges -> حذف معاوضه‌ها

### goods-business-type
- **Title**: نوع آگهی‌دهنده
- **Type**: object
- **Queries**: 
  - all -> همه
  - personal -> شخصی
  - marketplace -> فروشگاه

### has-photo
- **Title**: فقط عکس‌دار
- **Type**: boolean

### price
- **Title**: قیمت
- **Type**: object
 - **Minimum**: 0
 - **Maximum**: N/A

### sort
- **Title**: ترتیب نمایش آگهی‌ها براساس
- **Type**: object
- **Queries**: 
  - quality_and_sort_date -> quality_and_sort_date
  - sort_date -> sort_date
  - cheapest -> cheapest
  - most_expensive -> most_expensive
  - production_year -> production_year
  - usage -> usage
  - most_popular -> most_popular
  - most_relevant -> most_relevant

### status
- **Title**: وضعیت کالا
- **Type**: object
 - **Items Type**: array
- **Queries**: 
  - new -> نو
  - like-new -> در حد نو
  - used -> کارکرده
  - repair-needed -> نیازمند تعمیر

### urgent
- **Title**: فقط فوری‌ها
- **Type**: boolean



---

### Category: sewing-knitting



### category
- **Title**: دسته‌بندی
- **Type**: object

### divider
- **Title**: سایر فیلتر‌ها
- **Type**: object

### exchange
- **Title**: نمایش معاوضه‌ها
- **Type**: object
- **Queries**: 
  - only-exchanges -> نمایش فقط معاوضه‌ها
  - exclude-exchanges -> حذف معاوضه‌ها

### goods-business-type
- **Title**: نوع آگهی‌دهنده
- **Type**: object
- **Queries**: 
  - all -> همه
  - personal -> شخصی
  - marketplace -> فروشگاه

### has-photo
- **Title**: فقط عکس‌دار
- **Type**: boolean

### price
- **Title**: قیمت
- **Type**: object
 - **Minimum**: 0
 - **Maximum**: N/A

### sort
- **Title**: ترتیب نمایش آگهی‌ها براساس
- **Type**: object
- **Queries**: 
  - quality_and_sort_date -> quality_and_sort_date
  - sort_date -> sort_date
  - cheapest -> cheapest
  - most_expensive -> most_expensive
  - production_year -> production_year
  - usage -> usage
  - most_popular -> most_popular
  - most_relevant -> most_relevant

### status
- **Title**: وضعیت کالا
- **Type**: object
 - **Items Type**: array
- **Queries**: 
  - new -> نو
  - like-new -> در حد نو
  - used -> کارکرده
  - repair-needed -> نیازمند تعمیر

### urgent
- **Title**: فقط فوری‌ها
- **Type**: boolean



---

### Category: sewing-machine



### category
- **Title**: دسته‌بندی
- **Type**: object

### divider
- **Title**: سایر فیلتر‌ها
- **Type**: object

### exchange
- **Title**: نمایش معاوضه‌ها
- **Type**: object
- **Queries**: 
  - only-exchanges -> نمایش فقط معاوضه‌ها
  - exclude-exchanges -> حذف معاوضه‌ها

### goods-business-type
- **Title**: نوع آگهی‌دهنده
- **Type**: object
- **Queries**: 
  - all -> همه
  - personal -> شخصی
  - marketplace -> فروشگاه

### has-photo
- **Title**: فقط عکس‌دار
- **Type**: boolean

### price
- **Title**: قیمت
- **Type**: object
 - **Minimum**: 0
 - **Maximum**: N/A

### sort
- **Title**: ترتیب نمایش آگهی‌ها براساس
- **Type**: object
- **Queries**: 
  - quality_and_sort_date -> quality_and_sort_date
  - sort_date -> sort_date
  - cheapest -> cheapest
  - most_expensive -> most_expensive
  - production_year -> production_year
  - usage -> usage
  - most_popular -> most_popular
  - most_relevant -> most_relevant

### status
- **Title**: وضعیت کالا
- **Type**: object
 - **Items Type**: array
- **Queries**: 
  - new -> نو
  - like-new -> در حد نو
  - used -> کارکرده
  - repair-needed -> نیازمند تعمیر

### urgent
- **Title**: فقط فوری‌ها
- **Type**: boolean



---

### Category: shoe-rack-drawer



### category
- **Title**: دسته‌بندی
- **Type**: object

### divider
- **Title**: سایر فیلتر‌ها
- **Type**: object

### exchange
- **Title**: نمایش معاوضه‌ها
- **Type**: object
- **Queries**: 
  - only-exchanges -> نمایش فقط معاوضه‌ها
  - exclude-exchanges -> حذف معاوضه‌ها

### goods-business-type
- **Title**: نوع آگهی‌دهنده
- **Type**: object
- **Queries**: 
  - all -> همه
  - personal -> شخصی
  - marketplace -> فروشگاه

### has-photo
- **Title**: فقط عکس‌دار
- **Type**: boolean

### price
- **Title**: قیمت
- **Type**: object
 - **Minimum**: 0
 - **Maximum**: N/A

### sort
- **Title**: ترتیب نمایش آگهی‌ها براساس
- **Type**: object
- **Queries**: 
  - quality_and_sort_date -> quality_and_sort_date
  - sort_date -> sort_date
  - cheapest -> cheapest
  - most_expensive -> most_expensive
  - production_year -> production_year
  - usage -> usage
  - most_popular -> most_popular
  - most_relevant -> most_relevant

### status
- **Title**: وضعیت کالا
- **Type**: object
 - **Items Type**: array
- **Queries**: 
  - new -> نو
  - like-new -> در حد نو
  - used -> کارکرده
  - repair-needed -> نیازمند تعمیر

### urgent
- **Title**: فقط فوری‌ها
- **Type**: boolean



---

### Category: shoes-belt-bag



### category
- **Title**: دسته‌بندی
- **Type**: object

### divider
- **Title**: سایر فیلتر‌ها
- **Type**: object

### exchange
- **Title**: نمایش معاوضه‌ها
- **Type**: object
- **Queries**: 
  - only-exchanges -> نمایش فقط معاوضه‌ها
  - exclude-exchanges -> حذف معاوضه‌ها

### goods-business-type
- **Title**: نوع آگهی‌دهنده
- **Type**: object
- **Queries**: 
  - all -> همه
  - personal -> شخصی
  - marketplace -> فروشگاه

### has-color-and-pattern-variety
- **Title**: رنگ و طرح متنوع
- **Type**: boolean

### has-guarantee
- **Title**: فقط دارای ضمانت
- **Type**: boolean

### has-photo
- **Title**: فقط عکس‌دار
- **Type**: boolean

### manufacturer
- **Title**: تولیدکننده
- **Type**: object
- **Queries**: 
  - ایرانی -> ایرانی
  - خارجی -> خارجی

### price
- **Title**: قیمت
- **Type**: object
 - **Minimum**: 0
 - **Maximum**: N/A

### sort
- **Title**: ترتیب نمایش آگهی‌ها براساس
- **Type**: object
- **Queries**: 
  - quality_and_sort_date -> quality_and_sort_date
  - sort_date -> sort_date
  - cheapest -> cheapest
  - most_expensive -> most_expensive
  - production_year -> production_year
  - usage -> usage
  - most_popular -> most_popular
  - most_relevant -> most_relevant

### status
- **Title**: وضعیت کالا
- **Type**: object
 - **Items Type**: array
- **Queries**: 
  - new -> نو
  - like-new -> در حد نو
  - used -> کارکرده
  - repair-needed -> نیازمند تعمیر

### type
- **Title**: مردانه یا زنانه
- **Type**: object
- **Queries**: 
  - زنانه -> زنانه
  - مردانه -> مردانه

### urgent
- **Title**: فقط فوری‌ها
- **Type**: boolean



---

### Category: shop-and-cash



### category
- **Title**: دسته‌بندی
- **Type**: object

### divider
- **Title**: سایر فیلتر‌ها
- **Type**: object

### exchange
- **Title**: نمایش معاوضه‌ها
- **Type**: object
- **Queries**: 
  - only-exchanges -> نمایش فقط معاوضه‌ها
  - exclude-exchanges -> حذف معاوضه‌ها

### goods-business-type
- **Title**: نوع آگهی‌دهنده
- **Type**: object
- **Queries**: 
  - all -> همه
  - personal -> شخصی
  - marketplace -> فروشگاه

### has-photo
- **Title**: فقط عکس‌دار
- **Type**: boolean

### price
- **Title**: قیمت
- **Type**: object
 - **Minimum**: 0
 - **Maximum**: N/A

### sort
- **Title**: ترتیب نمایش آگهی‌ها براساس
- **Type**: object
- **Queries**: 
  - quality_and_sort_date -> quality_and_sort_date
  - sort_date -> sort_date
  - cheapest -> cheapest
  - most_expensive -> most_expensive
  - production_year -> production_year
  - usage -> usage
  - most_popular -> most_popular
  - most_relevant -> most_relevant

### status
- **Title**: وضعیت کالا
- **Type**: object
 - **Items Type**: array
- **Queries**: 
  - new -> نو
  - like-new -> در حد نو
  - used -> کارکرده
  - repair-needed -> نیازمند تعمیر

### urgent
- **Title**: فقط فوری‌ها
- **Type**: boolean



---

### Category: shop-rent



### building-age
- **Title**: سن بنا
- **Type**: object
- **Queries**: 
  - {"min": 0, "max": 1} -> حداکثر ۱ سال
  - {"min": 0, "max": 2} -> حداکثر ۲ سال
  - {"min": 0, "max": 5} -> حداکثر ۵ سال
  - {"min": 0, "max": 10} -> حداکثر ۱۰ سال
  - {"min": 0, "max": 15} -> حداکثر ۱۵ سال
  - {"min": 0, "max": 20} -> حداکثر ۲۰ سال
  - {"min": 0, "max": 30} -> حداکثر ۳۰ سال
  - {"min": 30} -> بیش از ۳۰ سال

### business-type
- **Title**: آگهی‌دهنده
- **Type**: object
- **Queries**: 
  - personal -> شخصی
  - real-estate-business -> مشاور املاک

### category
- **Title**: دسته‌بندی
- **Type**: object

### credit
- **Title**: ودیعه
- **Type**: object
 - **Minimum**: 0
 - **Maximum**: N/A

### has-photo
- **Title**: عکس‌دار
- **Type**: boolean

### has-video
- **Title**: ویدیو‌دار
- **Type**: boolean

### rent
- **Title**: اجاره
- **Type**: object
 - **Minimum**: 0
 - **Maximum**: N/A

### rooms
- **Title**: تعداد اتاق
- **Type**: object
- **Queries**: 
  - بدون اتاق -> بدون اتاق
  - یک -> ۱
  - دو -> ۲
  - سه -> ۳
  - چهار -> ۴
  - بیشتر -> بیشتر از ۴

### size
- **Title**: متراژ
- **Type**: object
 - **Minimum**: 0
 - **Maximum**: 1000000000

### sort
- **Title**: ترتیب نمایش آگهی‌ها براساس
- **Type**: object
- **Queries**: 
  - quality_and_sort_date -> quality_and_sort_date
  - sort_date -> sort_date
  - cheapest -> cheapest
  - most_expensive -> most_expensive
  - production_year -> production_year
  - usage -> usage
  - most_popular -> most_popular
  - most_relevant -> most_relevant

### urgent
- **Title**: فقط فوری‌ها
- **Type**: boolean



---

### Category: shop-restaurant



### category
- **Title**: دسته‌بندی
- **Type**: object

### divider
- **Title**: سایر فیلتر‌ها
- **Type**: object

### employee_gender
- **Title**: جنسیت کارجو
- **Type**: object
- **Queries**: 
  - female -> زن
  - male -> مرد
  - neutral -> فرقی ندارد

### experience
- **Title**: سابقهٔ مورد نیاز
- **Type**: object
 - **Minimum**: N/A
 - **Maximum**: N/A

### has-photo
- **Title**: فقط عکس‌دار
- **Type**: boolean

### health_insurance
- **Title**: با بیمه
- **Type**: boolean

### job_type
- **Title**: نوع همکاری
- **Type**: object
 - **Items Type**: array
- **Queries**: 
  - full_time -> تمام وقت
  - part_time -> پاره وقت
  - contract -> پیمان‌کاری/پروژه‌ای
  - internship -> کارآموزی
  - adaptive -> توافقی
  - other -> سایر

### military_service_status
- **Title**: پایان خدمت/معافیت
- **Type**: object
- **Queries**: 
  - finish_or_exemption_required -> الزامی
  - finish_not_required -> اختیاری

### no_experience_required
- **Title**: بدون نیاز به سابقه
- **Type**: boolean

### payment_method
- **Title**: شیوهٔ پرداخت
- **Type**: object
 - **Items Type**: array
- **Queries**: 
  - monthly -> ماهانه
  - daily -> روزانه
  - hourly -> ساعتی
  - percentage_commission -> پورسانتی/درصدی
  - adaptive -> توافقی
  - other -> سایر

### remote
- **Title**: با امکان دورکاری
- **Type**: boolean

### sort
- **Title**: ترتیب نمایش آگهی‌ها براساس
- **Type**: object
- **Queries**: 
  - quality_and_sort_date -> quality_and_sort_date
  - sort_date -> sort_date
  - cheapest -> cheapest
  - most_expensive -> most_expensive
  - production_year -> production_year
  - usage -> usage
  - most_popular -> most_popular
  - most_relevant -> most_relevant

### urgent
- **Title**: فقط فوری‌ها
- **Type**: boolean



---

### Category: shop-sell



### bizzDeed
- **Title**: سند اداری
- **Type**: object
- **Queries**: 
  - True -> دارد
  - False -> ندارد

### building-age
- **Title**: سن بنا
- **Type**: object
- **Queries**: 
  - {"min": 0, "max": 1} -> حداکثر ۱ سال
  - {"min": 0, "max": 2} -> حداکثر ۲ سال
  - {"min": 0, "max": 5} -> حداکثر ۵ سال
  - {"min": 0, "max": 10} -> حداکثر ۱۰ سال
  - {"min": 0, "max": 15} -> حداکثر ۱۵ سال
  - {"min": 0, "max": 20} -> حداکثر ۲۰ سال
  - {"min": 0, "max": 30} -> حداکثر ۳۰ سال
  - {"min": 30} -> بیش از ۳۰ سال

### business-type
- **Title**: آگهی‌دهنده
- **Type**: object
- **Queries**: 
  - personal -> شخصی
  - real-estate-business -> مشاور املاک

### category
- **Title**: دسته‌بندی
- **Type**: object

### has-photo
- **Title**: عکس‌دار
- **Type**: boolean

### has-video
- **Title**: ویدیو‌دار
- **Type**: boolean

### price
- **Title**: قیمت کل
- **Type**: object
 - **Minimum**: 0
 - **Maximum**: N/A

### rooms
- **Title**: تعداد اتاق
- **Type**: object
- **Queries**: 
  - بدون اتاق -> بدون اتاق
  - یک -> ۱
  - دو -> ۲
  - سه -> ۳
  - چهار -> ۴
  - بیشتر -> بیشتر از ۴

### size
- **Title**: متراژ
- **Type**: object
 - **Minimum**: 0
 - **Maximum**: 1000000000

### sort
- **Title**: ترتیب نمایش آگهی‌ها براساس
- **Type**: object
- **Queries**: 
  - quality_and_sort_date -> quality_and_sort_date
  - sort_date -> sort_date
  - cheapest -> cheapest
  - most_expensive -> most_expensive
  - production_year -> production_year
  - usage -> usage
  - most_popular -> most_popular
  - most_relevant -> most_relevant

### urgent
- **Title**: فقط فوری‌ها
- **Type**: boolean



---

### Category: sim-card



### category
- **Title**: دسته‌بندی
- **Type**: object

### divider
- **Title**: سایر فیلتر‌ها
- **Type**: object

### exchange
- **Title**: نمایش معاوضه‌ها
- **Type**: object
- **Queries**: 
  - only-exchanges -> نمایش فقط معاوضه‌ها
  - exclude-exchanges -> حذف معاوضه‌ها

### has-photo
- **Title**: فقط عکس‌دار
- **Type**: boolean

### price
- **Title**: قیمت
- **Type**: object
 - **Minimum**: 0
 - **Maximum**: N/A

### sort
- **Title**: ترتیب نمایش آگهی‌ها براساس
- **Type**: object
- **Queries**: 
  - quality_and_sort_date -> quality_and_sort_date
  - sort_date -> sort_date
  - cheapest -> cheapest
  - most_expensive -> most_expensive
  - production_year -> production_year
  - usage -> usage
  - most_popular -> most_popular
  - most_relevant -> most_relevant

### type
- **Title**: نوع سیمکارت
- **Type**: object
- **Queries**: 
  - همراه اول -> همراه اول
  - ایرانسل -> ایرانسل
  - رایتل -> رایتل

### urgent
- **Title**: فقط فوری‌ها
- **Type**: boolean



---

### Category: sleep-goods



### category
- **Title**: دسته‌بندی
- **Type**: object

### divider
- **Title**: سایر فیلتر‌ها
- **Type**: object

### exchange
- **Title**: نمایش معاوضه‌ها
- **Type**: object
- **Queries**: 
  - only-exchanges -> نمایش فقط معاوضه‌ها
  - exclude-exchanges -> حذف معاوضه‌ها

### goods-business-type
- **Title**: نوع آگهی‌دهنده
- **Type**: object
- **Queries**: 
  - all -> همه
  - personal -> شخصی
  - marketplace -> فروشگاه

### has-photo
- **Title**: فقط عکس‌دار
- **Type**: boolean

### price
- **Title**: قیمت
- **Type**: object
 - **Minimum**: 0
 - **Maximum**: N/A

### sort
- **Title**: ترتیب نمایش آگهی‌ها براساس
- **Type**: object
- **Queries**: 
  - quality_and_sort_date -> quality_and_sort_date
  - sort_date -> sort_date
  - cheapest -> cheapest
  - most_expensive -> most_expensive
  - production_year -> production_year
  - usage -> usage
  - most_popular -> most_popular
  - most_relevant -> most_relevant

### status
- **Title**: وضعیت کالا
- **Type**: object
 - **Items Type**: array
- **Queries**: 
  - new -> نو
  - like-new -> در حد نو
  - used -> کارکرده
  - repair-needed -> نیازمند تعمیر

### urgent
- **Title**: فقط فوری‌ها
- **Type**: boolean



---

### Category: sport



### category
- **Title**: دسته‌بندی
- **Type**: object

### divider
- **Title**: سایر فیلتر‌ها
- **Type**: object

### exchange
- **Title**: نمایش معاوضه‌ها
- **Type**: object
- **Queries**: 
  - only-exchanges -> نمایش فقط معاوضه‌ها
  - exclude-exchanges -> حذف معاوضه‌ها

### has-photo
- **Title**: فقط عکس‌دار
- **Type**: boolean

### price
- **Title**: قیمت
- **Type**: object
 - **Minimum**: 0
 - **Maximum**: N/A

### sort
- **Title**: ترتیب نمایش آگهی‌ها براساس
- **Type**: object
- **Queries**: 
  - quality_and_sort_date -> quality_and_sort_date
  - sort_date -> sort_date
  - cheapest -> cheapest
  - most_expensive -> most_expensive
  - production_year -> production_year
  - usage -> usage
  - most_popular -> most_popular
  - most_relevant -> most_relevant

### urgent
- **Title**: فقط فوری‌ها
- **Type**: boolean



---

### Category: sport-leisure



### category
- **Title**: دسته‌بندی
- **Type**: object

### divider
- **Title**: سایر فیلتر‌ها
- **Type**: object

### exchange
- **Title**: نمایش معاوضه‌ها
- **Type**: object
- **Queries**: 
  - only-exchanges -> نمایش فقط معاوضه‌ها
  - exclude-exchanges -> حذف معاوضه‌ها

### goods-business-type
- **Title**: نوع آگهی‌دهنده
- **Type**: object
- **Queries**: 
  - all -> همه
  - personal -> شخصی
  - marketplace -> فروشگاه

### has-photo
- **Title**: فقط عکس‌دار
- **Type**: boolean

### price
- **Title**: قیمت
- **Type**: object
 - **Minimum**: 0
 - **Maximum**: N/A

### sort
- **Title**: ترتیب نمایش آگهی‌ها براساس
- **Type**: object
- **Queries**: 
  - quality_and_sort_date -> quality_and_sort_date
  - sort_date -> sort_date
  - cheapest -> cheapest
  - most_expensive -> most_expensive
  - production_year -> production_year
  - usage -> usage
  - most_popular -> most_popular
  - most_relevant -> most_relevant

### status
- **Title**: وضعیت کالا
- **Type**: object
 - **Items Type**: array
- **Queries**: 
  - new -> نو
  - like-new -> در حد نو
  - used -> کارکرده
  - repair-needed -> نیازمند تعمیر

### urgent
- **Title**: فقط فوری‌ها
- **Type**: boolean



---

### Category: stationery



### category
- **Title**: دسته‌بندی
- **Type**: object

### divider
- **Title**: سایر فیلتر‌ها
- **Type**: object

### exchange
- **Title**: نمایش معاوضه‌ها
- **Type**: object
- **Queries**: 
  - only-exchanges -> نمایش فقط معاوضه‌ها
  - exclude-exchanges -> حذف معاوضه‌ها

### goods-business-type
- **Title**: نوع آگهی‌دهنده
- **Type**: object
- **Queries**: 
  - all -> همه
  - personal -> شخصی
  - marketplace -> فروشگاه

### has-photo
- **Title**: فقط عکس‌دار
- **Type**: boolean

### price
- **Title**: قیمت
- **Type**: object
 - **Minimum**: 0
 - **Maximum**: N/A

### sort
- **Title**: ترتیب نمایش آگهی‌ها براساس
- **Type**: object
- **Queries**: 
  - quality_and_sort_date -> quality_and_sort_date
  - sort_date -> sort_date
  - cheapest -> cheapest
  - most_expensive -> most_expensive
  - production_year -> production_year
  - usage -> usage
  - most_popular -> most_popular
  - most_relevant -> most_relevant

### status
- **Title**: وضعیت کالا
- **Type**: object
 - **Items Type**: array
- **Queries**: 
  - new -> نو
  - like-new -> در حد نو
  - used -> کارکرده
  - repair-needed -> نیازمند تعمیر

### urgent
- **Title**: فقط فوری‌ها
- **Type**: boolean



---

### Category: steam-iron



### category
- **Title**: دسته‌بندی
- **Type**: object

### divider
- **Title**: سایر فیلتر‌ها
- **Type**: object

### exchange
- **Title**: نمایش معاوضه‌ها
- **Type**: object
- **Queries**: 
  - only-exchanges -> نمایش فقط معاوضه‌ها
  - exclude-exchanges -> حذف معاوضه‌ها

### goods-business-type
- **Title**: نوع آگهی‌دهنده
- **Type**: object
- **Queries**: 
  - all -> همه
  - personal -> شخصی
  - marketplace -> فروشگاه

### has-photo
- **Title**: فقط عکس‌دار
- **Type**: boolean

### price
- **Title**: قیمت
- **Type**: object
 - **Minimum**: 0
 - **Maximum**: N/A

### sort
- **Title**: ترتیب نمایش آگهی‌ها براساس
- **Type**: object
- **Queries**: 
  - quality_and_sort_date -> quality_and_sort_date
  - sort_date -> sort_date
  - cheapest -> cheapest
  - most_expensive -> most_expensive
  - production_year -> production_year
  - usage -> usage
  - most_popular -> most_popular
  - most_relevant -> most_relevant

### status
- **Title**: وضعیت کالا
- **Type**: object
 - **Items Type**: array
- **Queries**: 
  - new -> نو
  - like-new -> در حد نو
  - used -> کارکرده
  - repair-needed -> نیازمند تعمیر

### urgent
- **Title**: فقط فوری‌ها
- **Type**: boolean



---

### Category: stereo-surround



### category
- **Title**: دسته‌بندی
- **Type**: object

### divider
- **Title**: سایر فیلتر‌ها
- **Type**: object

### exchange
- **Title**: نمایش معاوضه‌ها
- **Type**: object
- **Queries**: 
  - only-exchanges -> نمایش فقط معاوضه‌ها
  - exclude-exchanges -> حذف معاوضه‌ها

### goods-business-type
- **Title**: نوع آگهی‌دهنده
- **Type**: object
- **Queries**: 
  - all -> همه
  - personal -> شخصی
  - marketplace -> فروشگاه

### has-photo
- **Title**: فقط عکس‌دار
- **Type**: boolean

### price
- **Title**: قیمت
- **Type**: object
 - **Minimum**: 0
 - **Maximum**: N/A

### sort
- **Title**: ترتیب نمایش آگهی‌ها براساس
- **Type**: object
- **Queries**: 
  - quality_and_sort_date -> quality_and_sort_date
  - sort_date -> sort_date
  - cheapest -> cheapest
  - most_expensive -> most_expensive
  - production_year -> production_year
  - usage -> usage
  - most_popular -> most_popular
  - most_relevant -> most_relevant

### status
- **Title**: وضعیت کالا
- **Type**: object
 - **Items Type**: array
- **Queries**: 
  - new -> نو
  - like-new -> در حد نو
  - used -> کارکرده
  - repair-needed -> نیازمند تعمیر

### urgent
- **Title**: فقط فوری‌ها
- **Type**: boolean



---

### Category: stoves-heaters-fireplaces



### category
- **Title**: دسته‌بندی
- **Type**: object

### divider
- **Title**: سایر فیلتر‌ها
- **Type**: object

### exchange
- **Title**: نمایش معاوضه‌ها
- **Type**: object
- **Queries**: 
  - only-exchanges -> نمایش فقط معاوضه‌ها
  - exclude-exchanges -> حذف معاوضه‌ها

### goods-business-type
- **Title**: نوع آگهی‌دهنده
- **Type**: object
- **Queries**: 
  - all -> همه
  - personal -> شخصی
  - marketplace -> فروشگاه

### has-photo
- **Title**: فقط عکس‌دار
- **Type**: boolean

### price
- **Title**: قیمت
- **Type**: object
 - **Minimum**: 0
 - **Maximum**: N/A

### sort
- **Title**: ترتیب نمایش آگهی‌ها براساس
- **Type**: object
- **Queries**: 
  - quality_and_sort_date -> quality_and_sort_date
  - sort_date -> sort_date
  - cheapest -> cheapest
  - most_expensive -> most_expensive
  - production_year -> production_year
  - usage -> usage
  - most_popular -> most_popular
  - most_relevant -> most_relevant

### status
- **Title**: وضعیت کالا
- **Type**: object
 - **Items Type**: array
- **Queries**: 
  - new -> نو
  - like-new -> در حد نو
  - used -> کارکرده
  - repair-needed -> نیازمند تعمیر

### urgent
- **Title**: فقط فوری‌ها
- **Type**: boolean



---

### Category: strollers-and-accessories



### category
- **Title**: دسته‌بندی
- **Type**: object

### divider
- **Title**: سایر فیلتر‌ها
- **Type**: object

### exchange
- **Title**: نمایش معاوضه‌ها
- **Type**: object
- **Queries**: 
  - only-exchanges -> نمایش فقط معاوضه‌ها
  - exclude-exchanges -> حذف معاوضه‌ها

### goods-business-type
- **Title**: نوع آگهی‌دهنده
- **Type**: object
- **Queries**: 
  - all -> همه
  - personal -> شخصی
  - marketplace -> فروشگاه

### has-photo
- **Title**: فقط عکس‌دار
- **Type**: boolean

### price
- **Title**: قیمت
- **Type**: object
 - **Minimum**: 0
 - **Maximum**: N/A

### sort
- **Title**: ترتیب نمایش آگهی‌ها براساس
- **Type**: object
- **Queries**: 
  - quality_and_sort_date -> quality_and_sort_date
  - sort_date -> sort_date
  - cheapest -> cheapest
  - most_expensive -> most_expensive
  - production_year -> production_year
  - usage -> usage
  - most_popular -> most_popular
  - most_relevant -> most_relevant

### status
- **Title**: وضعیت کالا
- **Type**: object
 - **Items Type**: array
- **Queries**: 
  - new -> نو
  - like-new -> در حد نو
  - used -> کارکرده
  - repair-needed -> نیازمند تعمیر

### urgent
- **Title**: فقط فوری‌ها
- **Type**: boolean



---

### Category: suite-apartment



### business-type
- **Title**: آگهی‌دهنده
- **Type**: object
- **Queries**: 
  - personal -> شخصی
  - real-estate-business -> مشاور املاک

### category
- **Title**: دسته‌بندی
- **Type**: object

### daily_rent
- **Title**: اجاره روزانه
- **Type**: object
 - **Minimum**: 0
 - **Maximum**: N/A

### has-photo
- **Title**: عکس‌دار
- **Type**: boolean

### has-video
- **Title**: ویدیو‌دار
- **Type**: boolean

### person_capacity
- **Title**: ظرفیت
- **Type**: object
- **Queries**: 
  - {"min": 0, "max": 5} -> حداکثر ۵ نفر
  - {"min": 5, "max": 10} -> بین ۵ تا ۱۰ نفر
  - {"min": 10, "max": 15} -> بین ۱۰ تا ۱۵ نفر
  - {"min": 15, "max": 20} -> بین ۱۵ تا ۲۰ نفر
  - {"min": 20, "max": 25} -> بین ۲۰ تا ۲۵ نفر
  - {"min": 25, "max": 30} -> بین ۲۵ تا ۳۰ نفر
  - {"min": 30} -> بیش از ۳۰ نفر

### rooms
- **Title**: تعداد اتاق
- **Type**: object
- **Queries**: 
  - بدون اتاق -> بدون اتاق
  - یک -> ۱
  - دو -> ۲
  - سه -> ۳
  - چهار -> ۴
  - بیشتر -> بیشتر از ۴

### size
- **Title**: متراژ
- **Type**: object
 - **Minimum**: 0
 - **Maximum**: 1000000000

### sort
- **Title**: ترتیب نمایش آگهی‌ها براساس
- **Type**: object
- **Queries**: 
  - quality_and_sort_date -> quality_and_sort_date
  - sort_date -> sort_date
  - cheapest -> cheapest
  - most_expensive -> most_expensive
  - production_year -> production_year
  - usage -> usage
  - most_popular -> most_popular
  - most_relevant -> most_relevant

### urgent
- **Title**: فقط فوری‌ها
- **Type**: boolean



---

### Category: tablecloths



### category
- **Title**: دسته‌بندی
- **Type**: object

### divider
- **Title**: سایر فیلتر‌ها
- **Type**: object

### exchange
- **Title**: نمایش معاوضه‌ها
- **Type**: object
- **Queries**: 
  - only-exchanges -> نمایش فقط معاوضه‌ها
  - exclude-exchanges -> حذف معاوضه‌ها

### goods-business-type
- **Title**: نوع آگهی‌دهنده
- **Type**: object
- **Queries**: 
  - all -> همه
  - personal -> شخصی
  - marketplace -> فروشگاه

### has-photo
- **Title**: فقط عکس‌دار
- **Type**: boolean

### price
- **Title**: قیمت
- **Type**: object
 - **Minimum**: 0
 - **Maximum**: N/A

### sort
- **Title**: ترتیب نمایش آگهی‌ها براساس
- **Type**: object
- **Queries**: 
  - quality_and_sort_date -> quality_and_sort_date
  - sort_date -> sort_date
  - cheapest -> cheapest
  - most_expensive -> most_expensive
  - production_year -> production_year
  - usage -> usage
  - most_popular -> most_popular
  - most_relevant -> most_relevant

### status
- **Title**: وضعیت کالا
- **Type**: object
 - **Items Type**: array
- **Queries**: 
  - new -> نو
  - like-new -> در حد نو
  - used -> کارکرده
  - repair-needed -> نیازمند تعمیر

### urgent
- **Title**: فقط فوری‌ها
- **Type**: boolean



---

### Category: tablet



### brands
- **Title**: سازنده
- **Type**: object
 - **Items Type**: array
- **Queries**: 
  - Samsung - سامسونگ -> Samsung - سامسونگ
  - Apple - اپل -> Apple - اپل
  - HTC - اچ‌تی‌سی -> HTC - اچ‌تی‌سی
  - Sony Ericsson - سونی اریکسون -> Sony Ericsson - سونی اریکسون
  - Nokia - نوکیا -> Nokia - نوکیا
  - Sony - سونی -> Sony - سونی
  - LG - ال‌جی -> LG - ال‌جی
  - Motorola - موتورلا -> Motorola - موتورلا
  - Huawei - هوآوی -> Huawei - هوآوی
  - BlackBerry - بلک‌بری -> BlackBerry - بلک‌بری
  - Acer - ایسر -> Acer - ایسر
  - Asus - ایسوس -> Asus - ایسوس
  - Dell - دل -> Dell - دل
  - Lenovo - لنوو -> Lenovo - لنوو
  - Amazon - آمازون -> Amazon - آمازون
  - Farassoo - فراسو -> Farassoo - فراسو
  - ZTE - زدتی‌ای -> ZTE - زدتی‌ای
  - ViewSonic - ویوسونیک -> ViewSonic - ویوسونیک
  - MSI - ام‌اس‌آی -> MSI - ام‌اس‌آی
  - Honor - آنر -> Honor - آنر
  - Smart - اسمارت -> Smart - اسمارت
  - GLX - جی‌ال‌ایکس -> GLX - جی‌ال‌ایکس
  - GPlus - جی‌پلاس -> GPlus - جی‌پلاس
  - Xiaomi - شیائومی -> Xiaomi - شیائومی
  - Google - گوگل -> Google - گوگل
  - Microsoft - مایکروسافت -> Microsoft - مایکروسافت
  - نارتب - Nartab -> نارتب - Nartab
  - مارشال - Marshal -> مارشال - Marshal
  - Hyundai - هیوندای -> Hyundai - هیوندای
  - OnePlus - وان‌پلاس -> OnePlus - وان‌پلاس
  - سایر -> سایر

### category
- **Title**: دسته‌بندی
- **Type**: object

### color
- **Title**: رنگ
- **Type**: object
 - **Items Type**: array
- **Queries**: 
  - مشکی -> مشکی
  - سفید -> سفید
  - خاکستری -> خاکستری
  - نقره‌ای -> نقره‌ای
  - بژ -> بژ
  - سرمه‌ای -> سرمه‌ای
  - طلایی -> طلایی
  - آبی -> آبی
  - صورتی -> صورتی
  - قرمز -> قرمز
  - سبز -> سبز
  - سایر -> سایر

### divider
- **Title**: سایر فیلتر‌ها
- **Type**: object

### exchange
- **Title**: نمایش معاوضه‌ها
- **Type**: object
- **Queries**: 
  - only-exchanges -> نمایش فقط معاوضه‌ها
  - exclude-exchanges -> حذف معاوضه‌ها

### goods-business-type
- **Title**: نوع آگهی‌دهنده
- **Type**: object
- **Queries**: 
  - all -> همه
  - personal -> شخصی
  - marketplace -> فروشگاه

### has-photo
- **Title**: فقط عکس‌دار
- **Type**: boolean

### internal_storage
- **Title**: حافظهٔ داخلی
- **Type**: object
 - **Items Type**: array
- **Queries**: 
  - کمتر از ۱۶ گیگابایت -> کمتر از ۱۶ گیگابایت
  - ۱۶ گیگابایت -> ۱۶ گیگابایت
  - ۳۲ گیگابایت -> ۳۲ گیگابایت
  - ۶۴ گیگابایت -> ۶۴ گیگابایت
  - ۱۲۸ گیگابایت -> ۱۲۸ گیگابایت
  - ۲۵۶ گیگابایت -> ۲۵۶ گیگابایت
  - ۵۱۲ گیگابایت -> ۵۱۲ گیگابایت
  - ۱ ترابایت -> ۱ ترابایت
  - بیشتر از ۱ ترابایت -> بیشتر از ۱ ترابایت

### multi_sim_card_support
- **Title**: پشتیبانی از سیم‌کارت
- **Type**: object
- **Queries**: 
  - supported -> با پشتیبانی
  - not-supported -> بدون پشتیبانی
  - any -> همه

### os
- **Title**: سیستم‌عامل
- **Type**: object
 - **Items Type**: array
- **Queries**: 
  - Android -> Android
  - iOS - iPadOS -> iOS - iPadOS
  - Windows -> Windows
  - سایر -> سایر

### price
- **Title**: قیمت
- **Type**: object
 - **Minimum**: 0
 - **Maximum**: N/A

### ram_memory
- **Title**: مقدار رم
- **Type**: object
 - **Items Type**: array
- **Queries**: 
  - کمتر از ۲ گیگابایت -> کمتر از ۲ گیگابایت
  - ۲ گیگابایت -> ۲ گیگابایت
  - ۳ گیگابایت -> ۳ گیگابایت
  - ۴ گیگابایت -> ۴ گیگابایت
  - ۶ گیگابایت -> ۶ گیگابایت
  - ۸ گیگابایت -> ۸ گیگابایت
  - ۱۲ گیگابایت -> ۱۲ گیگابایت
  - بیشتر از ۱۲ گیگابایت -> بیشتر از ۱۲ گیگابایت

### screen_size
- **Title**: اندازهٔ صفحه
- **Type**: object
 - **Items Type**: array
- **Queries**: 
  - ۷ اینچ و کوچکتر -> ۷ اینچ و کوچکتر
  - ۸ تا ۱۰ اینچ -> ۸ تا ۱۰ اینچ
  - ۱۱ تا ۱۳ اینچ -> ۱۱ تا ۱۳ اینچ
  - بزرگتر از ۱۳ اینچ -> بزرگتر از ۱۳ اینچ

### sort
- **Title**: ترتیب نمایش آگهی‌ها براساس
- **Type**: object
- **Queries**: 
  - quality_and_sort_date -> quality_and_sort_date
  - sort_date -> sort_date
  - cheapest -> cheapest
  - most_expensive -> most_expensive
  - production_year -> production_year
  - usage -> usage
  - most_popular -> most_popular
  - most_relevant -> most_relevant

### status
- **Title**: وضعیت کالا
- **Type**: object
 - **Items Type**: array
- **Queries**: 
  - new -> نو
  - like-new -> در حد نو
  - used -> کارکرده
  - repair-needed -> نیازمند تعمیر

### urgent
- **Title**: فقط فوری‌ها
- **Type**: boolean



---

### Category: teaching



### category
- **Title**: دسته‌بندی
- **Type**: object

### expertises
- **Title**: تخصص
- **Type**: object
 - **Items Type**: array
- **Queries**: 
  - ROOT -> همه تخصص‌ها
  - sport-training -> آموزش ورزشی
  - ball-sports -> آموزش ورزش های توپی
  - water-sports -> آموزش ورزش های آبی
  - bodybuilding-sports -> آموزش ورزش های بدن سازی و حرکتی
  - martial-arts -> آموزش ورزش های رزمی
  - riding-sports -> آموزش ورزش های سواری
  - art-education -> آموزش هنری
  - handicraft-training -> آموزش صنایع دستی
  - tailoring-training -> آموزش خیاطی و طراحی لباس
  - cooking-training -> آموزش آشپزی و شیرینی پزی
  - hairdressing-training -> آموزش آرایشگری و زیبایی
  - drawing-arts-training -> آموزش هنرهای تجسمی
  - performing-arts-training -> آموزش هنرهای نمایشی
  - academic-courses -> آموزش تحصیلی و زبان های خارجی
  - school-lessons -> آموزش دروس ابتدایی تا متوسطه
  - university-courses -> آموزش رشته های تخصصی دانشگاهی
  - academic-counseling -> مشاورهٔ تحصیلی
  - foreign-languages -> آموزش زبان های خارجی
  - essay-writing -> آموزش مقاله‌نویسی و مشاورهٔ پایان نامه
  - computer-training-financial-markets -> آموزش کامپیوتر و بازارهای مالی
  - cad-software -> آموزش نرم افزارهای نقشه کشی
  - video-editing-software -> آموزش نرم افزارهای طراحی و ویرایش تصویر و ویدیو
  - general-computer-courses -> آموزش دوره های عمومی کامپیوتر
  - programming-software -> آموزش نرم افزارهای برنامه نویسی
  - seo-digital-marketing -> آموزش سئو و دیجیتال مارکتینگ
  - accounting-software -> آموزش نرم افزارهای حسابداری
  - financial-markets -> آموزش بازارهای مالی و ارزهای دیجیتال
  - car-training -> آموزش خودرو
  - car-electricity -> آموزش برق و کامپیوتر خودرو
  - car-technical -> آموزش فنی خودرو
  - car-detailing -> آموزش بدنه و زیبایی خودرو
  - car-driving -> آموزش رانندگی خودرو
  - technical-skills-training -> آموزش تعمیرات و مهارت های فنی
  - building-electric -> آموزش برق صنعتی و ساختمان
  - electrical-appliances-repairs -> آموزش تعمیرات لوازم برقی
  - digital-equipment-repairs -> آموزش تعمیرات لوازم دیجیتال
  - ventilation-cooling-heating-training -> آموزش تعمیرات لوازم تهویه، سرمایش و گرمایش
  - interior-design-architecture -> آموزش دکوراسیون و معماری ساختمان
  - carpentry-cabinet-making -> آموزش نجاری و کابینت سازی
  - welding-forging -> آموزش جوشکاری و آهنگری
  - piping-installations -> آموزش لوله کشی و تاسیسات
  - teaching-others -> سایر آموزشی

### has-photo
- **Title**: فقط عکس‌دار
- **Type**: boolean

### sort
- **Title**: ترتیب نمایش آگهی‌ها براساس
- **Type**: object
- **Queries**: 
  - quality_and_sort_date -> quality_and_sort_date
  - sort_date -> sort_date
  - cheapest -> cheapest
  - most_expensive -> most_expensive
  - production_year -> production_year
  - usage -> usage
  - most_popular -> most_popular
  - most_relevant -> most_relevant

### urgent
- **Title**: فقط فوری‌ها
- **Type**: boolean



---

### Category: temporary-rent



### business-type
- **Title**: آگهی‌دهنده
- **Type**: object
- **Queries**: 
  - personal -> شخصی
  - real-estate-business -> مشاور املاک

### category
- **Title**: دسته‌بندی
- **Type**: object

### daily_rent
- **Title**: اجاره روزانه
- **Type**: object
 - **Minimum**: 0
 - **Maximum**: N/A

### has-photo
- **Title**: عکس‌دار
- **Type**: boolean

### has-video
- **Title**: ویدیو‌دار
- **Type**: boolean

### rooms
- **Title**: تعداد اتاق
- **Type**: object
- **Queries**: 
  - بدون اتاق -> بدون اتاق
  - یک -> ۱
  - دو -> ۲
  - سه -> ۳
  - چهار -> ۴
  - بیشتر -> بیشتر از ۴

### size
- **Title**: متراژ
- **Type**: object
 - **Minimum**: 0
 - **Maximum**: 1000000000

### sort
- **Title**: ترتیب نمایش آگهی‌ها براساس
- **Type**: object
- **Queries**: 
  - quality_and_sort_date -> quality_and_sort_date
  - sort_date -> sort_date
  - cheapest -> cheapest
  - most_expensive -> most_expensive
  - production_year -> production_year
  - usage -> usage
  - most_popular -> most_popular
  - most_relevant -> most_relevant

### urgent
- **Title**: فقط فوری‌ها
- **Type**: boolean



---

### Category: theatre-and-cinema



### category
- **Title**: دسته‌بندی
- **Type**: object

### divider
- **Title**: سایر فیلتر‌ها
- **Type**: object

### exchange
- **Title**: نمایش معاوضه‌ها
- **Type**: object
- **Queries**: 
  - only-exchanges -> نمایش فقط معاوضه‌ها
  - exclude-exchanges -> حذف معاوضه‌ها

### has-photo
- **Title**: فقط عکس‌دار
- **Type**: boolean

### price
- **Title**: قیمت
- **Type**: object
 - **Minimum**: 0
 - **Maximum**: N/A

### sort
- **Title**: ترتیب نمایش آگهی‌ها براساس
- **Type**: object
- **Queries**: 
  - quality_and_sort_date -> quality_and_sort_date
  - sort_date -> sort_date
  - cheapest -> cheapest
  - most_expensive -> most_expensive
  - production_year -> production_year
  - usage -> usage
  - most_popular -> most_popular
  - most_relevant -> most_relevant

### urgent
- **Title**: فقط فوری‌ها
- **Type**: boolean



---

### Category: ticket



### category
- **Title**: دسته‌بندی
- **Type**: object

### divider
- **Title**: سایر فیلتر‌ها
- **Type**: object

### exchange
- **Title**: نمایش معاوضه‌ها
- **Type**: object
- **Queries**: 
  - only-exchanges -> نمایش فقط معاوضه‌ها
  - exclude-exchanges -> حذف معاوضه‌ها

### has-photo
- **Title**: فقط عکس‌دار
- **Type**: boolean

### price
- **Title**: قیمت
- **Type**: object
 - **Minimum**: 0
 - **Maximum**: N/A

### sort
- **Title**: ترتیب نمایش آگهی‌ها براساس
- **Type**: object
- **Queries**: 
  - quality_and_sort_date -> quality_and_sort_date
  - sort_date -> sort_date
  - cheapest -> cheapest
  - most_expensive -> most_expensive
  - production_year -> production_year
  - usage -> usage
  - most_popular -> most_popular
  - most_relevant -> most_relevant

### urgent
- **Title**: فقط فوری‌ها
- **Type**: boolean



---

### Category: tickets-sports



### category
- **Title**: دسته‌بندی
- **Type**: object

### divider
- **Title**: سایر فیلتر‌ها
- **Type**: object

### exchange
- **Title**: نمایش معاوضه‌ها
- **Type**: object
- **Queries**: 
  - only-exchanges -> نمایش فقط معاوضه‌ها
  - exclude-exchanges -> حذف معاوضه‌ها

### has-photo
- **Title**: فقط عکس‌دار
- **Type**: boolean

### price
- **Title**: قیمت
- **Type**: object
 - **Minimum**: 0
 - **Maximum**: N/A

### sort
- **Title**: ترتیب نمایش آگهی‌ها براساس
- **Type**: object
- **Queries**: 
  - quality_and_sort_date -> quality_and_sort_date
  - sort_date -> sort_date
  - cheapest -> cheapest
  - most_expensive -> most_expensive
  - production_year -> production_year
  - usage -> usage
  - most_popular -> most_popular
  - most_relevant -> most_relevant

### urgent
- **Title**: فقط فوری‌ها
- **Type**: boolean



---

### Category: toolbox



### category
- **Title**: دسته‌بندی
- **Type**: object

### divider
- **Title**: سایر فیلتر‌ها
- **Type**: object

### exchange
- **Title**: نمایش معاوضه‌ها
- **Type**: object
- **Queries**: 
  - only-exchanges -> نمایش فقط معاوضه‌ها
  - exclude-exchanges -> حذف معاوضه‌ها

### goods-business-type
- **Title**: نوع آگهی‌دهنده
- **Type**: object
- **Queries**: 
  - all -> همه
  - personal -> شخصی
  - marketplace -> فروشگاه

### has-photo
- **Title**: فقط عکس‌دار
- **Type**: boolean

### price
- **Title**: قیمت
- **Type**: object
 - **Minimum**: 0
 - **Maximum**: N/A

### sort
- **Title**: ترتیب نمایش آگهی‌ها براساس
- **Type**: object
- **Queries**: 
  - quality_and_sort_date -> quality_and_sort_date
  - sort_date -> sort_date
  - cheapest -> cheapest
  - most_expensive -> most_expensive
  - production_year -> production_year
  - usage -> usage
  - most_popular -> most_popular
  - most_relevant -> most_relevant

### status
- **Title**: وضعیت کالا
- **Type**: object
 - **Items Type**: array
- **Queries**: 
  - new -> نو
  - like-new -> در حد نو
  - used -> کارکرده
  - repair-needed -> نیازمند تعمیر

### urgent
- **Title**: فقط فوری‌ها
- **Type**: boolean



---

### Category: tools-materials-equipment



### category
- **Title**: دسته‌بندی
- **Type**: object

### divider
- **Title**: سایر فیلتر‌ها
- **Type**: object

### exchange
- **Title**: نمایش معاوضه‌ها
- **Type**: object
- **Queries**: 
  - only-exchanges -> نمایش فقط معاوضه‌ها
  - exclude-exchanges -> حذف معاوضه‌ها

### goods-business-type
- **Title**: نوع آگهی‌دهنده
- **Type**: object
- **Queries**: 
  - all -> همه
  - personal -> شخصی
  - marketplace -> فروشگاه

### has-photo
- **Title**: فقط عکس‌دار
- **Type**: boolean

### price
- **Title**: قیمت
- **Type**: object
 - **Minimum**: 0
 - **Maximum**: N/A

### sort
- **Title**: ترتیب نمایش آگهی‌ها براساس
- **Type**: object
- **Queries**: 
  - quality_and_sort_date -> quality_and_sort_date
  - sort_date -> sort_date
  - cheapest -> cheapest
  - most_expensive -> most_expensive
  - production_year -> production_year
  - usage -> usage
  - most_popular -> most_popular
  - most_relevant -> most_relevant

### status
- **Title**: وضعیت کالا
- **Type**: object
 - **Items Type**: array
- **Queries**: 
  - new -> نو
  - like-new -> در حد نو
  - used -> کارکرده
  - repair-needed -> نیازمند تعمیر

### urgent
- **Title**: فقط فوری‌ها
- **Type**: boolean



---

### Category: traditional



### category
- **Title**: دسته‌بندی
- **Type**: object

### divider
- **Title**: سایر فیلتر‌ها
- **Type**: object

### exchange
- **Title**: نمایش معاوضه‌ها
- **Type**: object
- **Queries**: 
  - only-exchanges -> نمایش فقط معاوضه‌ها
  - exclude-exchanges -> حذف معاوضه‌ها

### goods-business-type
- **Title**: نوع آگهی‌دهنده
- **Type**: object
- **Queries**: 
  - all -> همه
  - personal -> شخصی
  - marketplace -> فروشگاه

### has-photo
- **Title**: فقط عکس‌دار
- **Type**: boolean

### price
- **Title**: قیمت
- **Type**: object
 - **Minimum**: 0
 - **Maximum**: N/A

### sort
- **Title**: ترتیب نمایش آگهی‌ها براساس
- **Type**: object
- **Queries**: 
  - quality_and_sort_date -> quality_and_sort_date
  - sort_date -> sort_date
  - cheapest -> cheapest
  - most_expensive -> most_expensive
  - production_year -> production_year
  - usage -> usage
  - most_popular -> most_popular
  - most_relevant -> most_relevant

### status
- **Title**: وضعیت کالا
- **Type**: object
 - **Items Type**: array
- **Queries**: 
  - new -> نو
  - like-new -> در حد نو
  - used -> کارکرده
  - repair-needed -> نیازمند تعمیر

### urgent
- **Title**: فقط فوری‌ها
- **Type**: boolean



---

### Category: training



### category
- **Title**: دسته‌بندی
- **Type**: object

### divider
- **Title**: سایر فیلتر‌ها
- **Type**: object

### exchange
- **Title**: نمایش معاوضه‌ها
- **Type**: object
- **Queries**: 
  - only-exchanges -> نمایش فقط معاوضه‌ها
  - exclude-exchanges -> حذف معاوضه‌ها

### goods-business-type
- **Title**: نوع آگهی‌دهنده
- **Type**: object
- **Queries**: 
  - all -> همه
  - personal -> شخصی
  - marketplace -> فروشگاه

### has-photo
- **Title**: فقط عکس‌دار
- **Type**: boolean

### price
- **Title**: قیمت
- **Type**: object
 - **Minimum**: 0
 - **Maximum**: N/A

### sort
- **Title**: ترتیب نمایش آگهی‌ها براساس
- **Type**: object
- **Queries**: 
  - quality_and_sort_date -> quality_and_sort_date
  - sort_date -> sort_date
  - cheapest -> cheapest
  - most_expensive -> most_expensive
  - production_year -> production_year
  - usage -> usage
  - most_popular -> most_popular
  - most_relevant -> most_relevant

### status
- **Title**: وضعیت کالا
- **Type**: object
 - **Items Type**: array
- **Queries**: 
  - new -> نو
  - like-new -> در حد نو
  - used -> کارکرده
  - repair-needed -> نیازمند تعمیر

### urgent
- **Title**: فقط فوری‌ها
- **Type**: boolean



---

### Category: transport



### category
- **Title**: دسته‌بندی
- **Type**: object

### expertises
- **Title**: تخصص
- **Type**: object
 - **Items Type**: array
- **Queries**: 
  - ROOT -> همه تخصص‌ها
  - tourism-immigration-services -> خدمات گردشگری و مهاجرت
  - residency -> اقامت
  - visa -> ویزا
  - immigration -> مهاجرت
  - tour -> تورهای مسافرتی
  - moving-services -> خدمات باربری و حمل اثاثیه
  - moving-furniture -> اسباب کشی و باربری
  - packing -> بسته بندی و چیدمان وسایل
  - worker -> کارگر جا به جایی
  - ambulance -> خدمات آمبولانس
  - moving-construction-materials -> حمل نخاله و مصالح ساختمانی
  - passenger-transport-services -> جا به جایی مسافر
  - local-transfer -> درون شهری
  - intercity-transfer -> برون شهری
  - school-transfer -> سرویس مدرسه و سازمان(شرکت)
  - transport-others -> سایر حمل و نقل
  - business-services -> خدمات بازرگانی
  - import -> واردات کالا
  - export -> صادرات کالا
  - customs-clearance -> ترخیص کالا از گمرک

### services_profile
- **Title**: فقط متخصصان تأیید هویت شده
- **Type**: boolean

### sort
- **Title**: ترتیب نمایش آگهی‌ها براساس
- **Type**: object
- **Queries**: 
  - quality_and_sort_date -> quality_and_sort_date
  - sort_date -> sort_date
  - cheapest -> cheapest
  - most_expensive -> most_expensive
  - production_year -> production_year
  - usage -> usage
  - most_popular -> most_popular
  - most_relevant -> most_relevant

### urgent
- **Title**: فقط فوری‌ها
- **Type**: boolean



---

### Category: transportation



### category
- **Title**: دسته‌بندی
- **Type**: object

### divider
- **Title**: سایر فیلتر‌ها
- **Type**: object

### employee_gender
- **Title**: جنسیت کارجو
- **Type**: object
- **Queries**: 
  - female -> زن
  - male -> مرد
  - neutral -> فرقی ندارد

### experience
- **Title**: سابقهٔ مورد نیاز
- **Type**: object
 - **Minimum**: N/A
 - **Maximum**: N/A

### has-photo
- **Title**: فقط عکس‌دار
- **Type**: boolean

### health_insurance
- **Title**: با بیمه
- **Type**: boolean

### job_type
- **Title**: نوع همکاری
- **Type**: object
 - **Items Type**: array
- **Queries**: 
  - full_time -> تمام وقت
  - part_time -> پاره وقت
  - contract -> پیمان‌کاری/پروژه‌ای
  - internship -> کارآموزی
  - adaptive -> توافقی
  - other -> سایر

### military_service_status
- **Title**: پایان خدمت/معافیت
- **Type**: object
- **Queries**: 
  - finish_or_exemption_required -> الزامی
  - finish_not_required -> اختیاری

### no_experience_required
- **Title**: بدون نیاز به سابقه
- **Type**: boolean

### payment_method
- **Title**: شیوهٔ پرداخت
- **Type**: object
 - **Items Type**: array
- **Queries**: 
  - monthly -> ماهانه
  - daily -> روزانه
  - hourly -> ساعتی
  - percentage_commission -> پورسانتی/درصدی
  - adaptive -> توافقی
  - other -> سایر

### remote
- **Title**: با امکان دورکاری
- **Type**: boolean

### sort
- **Title**: ترتیب نمایش آگهی‌ها براساس
- **Type**: object
- **Queries**: 
  - quality_and_sort_date -> quality_and_sort_date
  - sort_date -> sort_date
  - cheapest -> cheapest
  - most_expensive -> most_expensive
  - production_year -> production_year
  - usage -> usage
  - most_popular -> most_popular
  - most_relevant -> most_relevant

### urgent
- **Title**: فقط فوری‌ها
- **Type**: boolean



---

### Category: travel-packages



### category
- **Title**: دسته‌بندی
- **Type**: object

### divider
- **Title**: سایر فیلتر‌ها
- **Type**: object

### exchange
- **Title**: نمایش معاوضه‌ها
- **Type**: object
- **Queries**: 
  - only-exchanges -> نمایش فقط معاوضه‌ها
  - exclude-exchanges -> حذف معاوضه‌ها

### has-photo
- **Title**: فقط عکس‌دار
- **Type**: boolean

### price
- **Title**: قیمت
- **Type**: object
 - **Minimum**: 0
 - **Maximum**: N/A

### sort
- **Title**: ترتیب نمایش آگهی‌ها براساس
- **Type**: object
- **Queries**: 
  - quality_and_sort_date -> quality_and_sort_date
  - sort_date -> sort_date
  - cheapest -> cheapest
  - most_expensive -> most_expensive
  - production_year -> production_year
  - usage -> usage
  - most_popular -> most_popular
  - most_relevant -> most_relevant

### urgent
- **Title**: فقط فوری‌ها
- **Type**: boolean



---

### Category: tv-projector



### category
- **Title**: دسته‌بندی
- **Type**: object

### divider
- **Title**: سایر فیلتر‌ها
- **Type**: object

### exchange
- **Title**: نمایش معاوضه‌ها
- **Type**: object
- **Queries**: 
  - only-exchanges -> نمایش فقط معاوضه‌ها
  - exclude-exchanges -> حذف معاوضه‌ها

### goods-business-type
- **Title**: نوع آگهی‌دهنده
- **Type**: object
- **Queries**: 
  - all -> همه
  - personal -> شخصی
  - marketplace -> فروشگاه

### has-photo
- **Title**: فقط عکس‌دار
- **Type**: boolean

### hdmi_ports_quantity
- **Title**: تعداد پورت HDMI
- **Type**: object
- **Queries**: 
  - 0-port -> ندارد
  - 1-port -> ۱ پورت
  - 2-ports -> ۲ پورت
  - +2-ports -> بیشتر از ۲ پورت

### price
- **Title**: قیمت
- **Type**: object
 - **Minimum**: 0
 - **Maximum**: N/A

### sort
- **Title**: ترتیب نمایش آگهی‌ها براساس
- **Type**: object
- **Queries**: 
  - quality_and_sort_date -> quality_and_sort_date
  - sort_date -> sort_date
  - cheapest -> cheapest
  - most_expensive -> most_expensive
  - production_year -> production_year
  - usage -> usage
  - most_popular -> most_popular
  - most_relevant -> most_relevant

### status
- **Title**: وضعیت کالا
- **Type**: object
 - **Items Type**: array
- **Queries**: 
  - new -> نو
  - like-new -> در حد نو
  - used -> کارکرده
  - repair-needed -> نیازمند تعمیر

### urgent
- **Title**: فقط فوری‌ها
- **Type**: boolean

### usb_ports_quantity
- **Title**: تعداد پورت USB
- **Type**: object
- **Queries**: 
  - 0-port -> ندارد
  - 1-port -> ۱ پورت
  - 2-ports -> ۲ پورت
  - +2-ports -> بیشتر از ۲ پورت



---

### Category: tv-stand



### category
- **Title**: دسته‌بندی
- **Type**: object

### divider
- **Title**: سایر فیلتر‌ها
- **Type**: object

### exchange
- **Title**: نمایش معاوضه‌ها
- **Type**: object
- **Queries**: 
  - only-exchanges -> نمایش فقط معاوضه‌ها
  - exclude-exchanges -> حذف معاوضه‌ها

### goods-business-type
- **Title**: نوع آگهی‌دهنده
- **Type**: object
- **Queries**: 
  - all -> همه
  - personal -> شخصی
  - marketplace -> فروشگاه

### has-photo
- **Title**: فقط عکس‌دار
- **Type**: boolean

### price
- **Title**: قیمت
- **Type**: object
 - **Minimum**: 0
 - **Maximum**: N/A

### sort
- **Title**: ترتیب نمایش آگهی‌ها براساس
- **Type**: object
- **Queries**: 
  - quality_and_sort_date -> quality_and_sort_date
  - sort_date -> sort_date
  - cheapest -> cheapest
  - most_expensive -> most_expensive
  - production_year -> production_year
  - usage -> usage
  - most_popular -> most_popular
  - most_relevant -> most_relevant

### status
- **Title**: وضعیت کالا
- **Type**: object
 - **Items Type**: array
- **Queries**: 
  - new -> نو
  - like-new -> در حد نو
  - used -> کارکرده
  - repair-needed -> نیازمند تعمیر

### urgent
- **Title**: فقط فوری‌ها
- **Type**: boolean



---

### Category: vacuums-cleaner



### category
- **Title**: دسته‌بندی
- **Type**: object

### divider
- **Title**: سایر فیلتر‌ها
- **Type**: object

### exchange
- **Title**: نمایش معاوضه‌ها
- **Type**: object
- **Queries**: 
  - only-exchanges -> نمایش فقط معاوضه‌ها
  - exclude-exchanges -> حذف معاوضه‌ها

### goods-business-type
- **Title**: نوع آگهی‌دهنده
- **Type**: object
- **Queries**: 
  - all -> همه
  - personal -> شخصی
  - marketplace -> فروشگاه

### has-photo
- **Title**: فقط عکس‌دار
- **Type**: boolean

### price
- **Title**: قیمت
- **Type**: object
 - **Minimum**: 0
 - **Maximum**: N/A

### sort
- **Title**: ترتیب نمایش آگهی‌ها براساس
- **Type**: object
- **Queries**: 
  - quality_and_sort_date -> quality_and_sort_date
  - sort_date -> sort_date
  - cheapest -> cheapest
  - most_expensive -> most_expensive
  - production_year -> production_year
  - usage -> usage
  - most_popular -> most_popular
  - most_relevant -> most_relevant

### status
- **Title**: وضعیت کالا
- **Type**: object
 - **Items Type**: array
- **Queries**: 
  - new -> نو
  - like-new -> در حد نو
  - used -> کارکرده
  - repair-needed -> نیازمند تعمیر

### urgent
- **Title**: فقط فوری‌ها
- **Type**: boolean



---

### Category: vehicles



### category
- **Title**: دسته‌بندی
- **Type**: object

### divider
- **Title**: سایر فیلتر‌ها
- **Type**: object

### exchange
- **Title**: نمایش معاوضه‌ها
- **Type**: object
- **Queries**: 
  - only-exchanges -> نمایش فقط معاوضه‌ها
  - exclude-exchanges -> حذف معاوضه‌ها

### has-photo
- **Title**: فقط عکس‌دار
- **Type**: boolean

### non-negotiable
- **Title**: حذف توافقی‌ها
- **Type**: boolean

### post-type
- **Title**: نوع آگهی
- **Type**: object
- **Queries**: 
  - فروشی -> فروشی
  - درخواستی -> درخواستی

### price
- **Title**: قیمت
- **Type**: object
 - **Minimum**: 0
 - **Maximum**: N/A

### sort
- **Title**: ترتیب نمایش آگهی‌ها براساس
- **Type**: object
- **Queries**: 
  - quality_and_sort_date -> quality_and_sort_date
  - sort_date -> sort_date
  - cheapest -> cheapest
  - most_expensive -> most_expensive
  - production_year -> production_year
  - usage -> usage
  - most_popular -> most_popular
  - most_relevant -> most_relevant

### urgent
- **Title**: فقط فوری‌ها
- **Type**: boolean



---

### Category: ventilation-cooling-heating



### category
- **Title**: دسته‌بندی
- **Type**: object

### divider
- **Title**: سایر فیلتر‌ها
- **Type**: object

### exchange
- **Title**: نمایش معاوضه‌ها
- **Type**: object
- **Queries**: 
  - only-exchanges -> نمایش فقط معاوضه‌ها
  - exclude-exchanges -> حذف معاوضه‌ها

### goods-business-type
- **Title**: نوع آگهی‌دهنده
- **Type**: object
- **Queries**: 
  - all -> همه
  - personal -> شخصی
  - marketplace -> فروشگاه

### has-photo
- **Title**: فقط عکس‌دار
- **Type**: boolean

### price
- **Title**: قیمت
- **Type**: object
 - **Minimum**: 0
 - **Maximum**: N/A

### sort
- **Title**: ترتیب نمایش آگهی‌ها براساس
- **Type**: object
- **Queries**: 
  - quality_and_sort_date -> quality_and_sort_date
  - sort_date -> sort_date
  - cheapest -> cheapest
  - most_expensive -> most_expensive
  - production_year -> production_year
  - usage -> usage
  - most_popular -> most_popular
  - most_relevant -> most_relevant

### status
- **Title**: وضعیت کالا
- **Type**: object
 - **Items Type**: array
- **Queries**: 
  - new -> نو
  - like-new -> در حد نو
  - used -> کارکرده
  - repair-needed -> نیازمند تعمیر

### urgent
- **Title**: فقط فوری‌ها
- **Type**: boolean



---

### Category: video-dvdplayer



### category
- **Title**: دسته‌بندی
- **Type**: object

### divider
- **Title**: سایر فیلتر‌ها
- **Type**: object

### exchange
- **Title**: نمایش معاوضه‌ها
- **Type**: object
- **Queries**: 
  - only-exchanges -> نمایش فقط معاوضه‌ها
  - exclude-exchanges -> حذف معاوضه‌ها

### goods-business-type
- **Title**: نوع آگهی‌دهنده
- **Type**: object
- **Queries**: 
  - all -> همه
  - personal -> شخصی
  - marketplace -> فروشگاه

### has-photo
- **Title**: فقط عکس‌دار
- **Type**: boolean

### price
- **Title**: قیمت
- **Type**: object
 - **Minimum**: 0
 - **Maximum**: N/A

### sort
- **Title**: ترتیب نمایش آگهی‌ها براساس
- **Type**: object
- **Queries**: 
  - quality_and_sort_date -> quality_and_sort_date
  - sort_date -> sort_date
  - cheapest -> cheapest
  - most_expensive -> most_expensive
  - production_year -> production_year
  - usage -> usage
  - most_popular -> most_popular
  - most_relevant -> most_relevant

### status
- **Title**: وضعیت کالا
- **Type**: object
 - **Items Type**: array
- **Queries**: 
  - new -> نو
  - like-new -> در حد نو
  - used -> کارکرده
  - repair-needed -> نیازمند تعمیر

### urgent
- **Title**: فقط فوری‌ها
- **Type**: boolean



---

### Category: villa



### business-type
- **Title**: آگهی‌دهنده
- **Type**: object
- **Queries**: 
  - personal -> شخصی
  - real-estate-business -> مشاور املاک

### category
- **Title**: دسته‌بندی
- **Type**: object

### daily_rent
- **Title**: اجاره روزانه
- **Type**: object
 - **Minimum**: 0
 - **Maximum**: N/A

### has-photo
- **Title**: عکس‌دار
- **Type**: boolean

### has-video
- **Title**: ویدیو‌دار
- **Type**: boolean

### person_capacity
- **Title**: ظرفیت
- **Type**: object
- **Queries**: 
  - {"min": 0, "max": 5} -> حداکثر ۵ نفر
  - {"min": 5, "max": 10} -> بین ۵ تا ۱۰ نفر
  - {"min": 10, "max": 15} -> بین ۱۰ تا ۱۵ نفر
  - {"min": 15, "max": 20} -> بین ۱۵ تا ۲۰ نفر
  - {"min": 20, "max": 25} -> بین ۲۰ تا ۲۵ نفر
  - {"min": 25, "max": 30} -> بین ۲۵ تا ۳۰ نفر
  - {"min": 30} -> بیش از ۳۰ نفر

### rooms
- **Title**: تعداد اتاق
- **Type**: object
- **Queries**: 
  - بدون اتاق -> بدون اتاق
  - یک -> ۱
  - دو -> ۲
  - سه -> ۳
  - چهار -> ۴
  - بیشتر -> بیشتر از ۴

### size
- **Title**: متراژ
- **Type**: object
 - **Minimum**: 0
 - **Maximum**: 1000000000

### sort
- **Title**: ترتیب نمایش آگهی‌ها براساس
- **Type**: object
- **Queries**: 
  - quality_and_sort_date -> quality_and_sort_date
  - sort_date -> sort_date
  - cheapest -> cheapest
  - most_expensive -> most_expensive
  - production_year -> production_year
  - usage -> usage
  - most_popular -> most_popular
  - most_relevant -> most_relevant

### urgent
- **Title**: فقط فوری‌ها
- **Type**: boolean



---

### Category: violins



### category
- **Title**: دسته‌بندی
- **Type**: object

### divider
- **Title**: سایر فیلتر‌ها
- **Type**: object

### exchange
- **Title**: نمایش معاوضه‌ها
- **Type**: object
- **Queries**: 
  - only-exchanges -> نمایش فقط معاوضه‌ها
  - exclude-exchanges -> حذف معاوضه‌ها

### goods-business-type
- **Title**: نوع آگهی‌دهنده
- **Type**: object
- **Queries**: 
  - all -> همه
  - personal -> شخصی
  - marketplace -> فروشگاه

### has-photo
- **Title**: فقط عکس‌دار
- **Type**: boolean

### price
- **Title**: قیمت
- **Type**: object
 - **Minimum**: 0
 - **Maximum**: N/A

### sort
- **Title**: ترتیب نمایش آگهی‌ها براساس
- **Type**: object
- **Queries**: 
  - quality_and_sort_date -> quality_and_sort_date
  - sort_date -> sort_date
  - cheapest -> cheapest
  - most_expensive -> most_expensive
  - production_year -> production_year
  - usage -> usage
  - most_popular -> most_popular
  - most_relevant -> most_relevant

### status
- **Title**: وضعیت کالا
- **Type**: object
 - **Items Type**: array
- **Queries**: 
  - new -> نو
  - like-new -> در حد نو
  - used -> کارکرده
  - repair-needed -> نیازمند تعمیر

### urgent
- **Title**: فقط فوری‌ها
- **Type**: boolean



---

### Category: volunteers



### category
- **Title**: دسته‌بندی
- **Type**: object

### divider
- **Title**: سایر فیلتر‌ها
- **Type**: object

### has-photo
- **Title**: فقط عکس‌دار
- **Type**: boolean

### sort
- **Title**: ترتیب نمایش آگهی‌ها براساس
- **Type**: object
- **Queries**: 
  - quality_and_sort_date -> quality_and_sort_date
  - sort_date -> sort_date
  - cheapest -> cheapest
  - most_expensive -> most_expensive
  - production_year -> production_year
  - usage -> usage
  - most_popular -> most_popular
  - most_relevant -> most_relevant

### urgent
- **Title**: فقط فوری‌ها
- **Type**: boolean



---

### Category: wall-clock



### category
- **Title**: دسته‌بندی
- **Type**: object

### divider
- **Title**: سایر فیلتر‌ها
- **Type**: object

### exchange
- **Title**: نمایش معاوضه‌ها
- **Type**: object
- **Queries**: 
  - only-exchanges -> نمایش فقط معاوضه‌ها
  - exclude-exchanges -> حذف معاوضه‌ها

### goods-business-type
- **Title**: نوع آگهی‌دهنده
- **Type**: object
- **Queries**: 
  - all -> همه
  - personal -> شخصی
  - marketplace -> فروشگاه

### has-photo
- **Title**: فقط عکس‌دار
- **Type**: boolean

### price
- **Title**: قیمت
- **Type**: object
 - **Minimum**: 0
 - **Maximum**: N/A

### sort
- **Title**: ترتیب نمایش آگهی‌ها براساس
- **Type**: object
- **Queries**: 
  - quality_and_sort_date -> quality_and_sort_date
  - sort_date -> sort_date
  - cheapest -> cheapest
  - most_expensive -> most_expensive
  - production_year -> production_year
  - usage -> usage
  - most_popular -> most_popular
  - most_relevant -> most_relevant

### status
- **Title**: وضعیت کالا
- **Type**: object
 - **Items Type**: array
- **Queries**: 
  - new -> نو
  - like-new -> در حد نو
  - used -> کارکرده
  - repair-needed -> نیازمند تعمیر

### urgent
- **Title**: فقط فوری‌ها
- **Type**: boolean



---

### Category: washing-cleaning



### category
- **Title**: دسته‌بندی
- **Type**: object

### divider
- **Title**: سایر فیلتر‌ها
- **Type**: object

### exchange
- **Title**: نمایش معاوضه‌ها
- **Type**: object
- **Queries**: 
  - only-exchanges -> نمایش فقط معاوضه‌ها
  - exclude-exchanges -> حذف معاوضه‌ها

### goods-business-type
- **Title**: نوع آگهی‌دهنده
- **Type**: object
- **Queries**: 
  - all -> همه
  - personal -> شخصی
  - marketplace -> فروشگاه

### has-photo
- **Title**: فقط عکس‌دار
- **Type**: boolean

### price
- **Title**: قیمت
- **Type**: object
 - **Minimum**: 0
 - **Maximum**: N/A

### sort
- **Title**: ترتیب نمایش آگهی‌ها براساس
- **Type**: object
- **Queries**: 
  - quality_and_sort_date -> quality_and_sort_date
  - sort_date -> sort_date
  - cheapest -> cheapest
  - most_expensive -> most_expensive
  - production_year -> production_year
  - usage -> usage
  - most_popular -> most_popular
  - most_relevant -> most_relevant

### status
- **Title**: وضعیت کالا
- **Type**: object
 - **Items Type**: array
- **Queries**: 
  - new -> نو
  - like-new -> در حد نو
  - used -> کارکرده
  - repair-needed -> نیازمند تعمیر

### urgent
- **Title**: فقط فوری‌ها
- **Type**: boolean



---

### Category: washing-machines



### brands
- **Title**: سازنده
- **Type**: object
 - **Items Type**: array
- **Queries**: 
  - آ ا گ -> آ ا گ
  - آبسال -> آبسال
  - آرچلیک -> آرچلیک
  - آریستون -> آریستون
  - آزمایش -> آزمایش
  - آی فادر -> آی فادر
  - اپکس -> اپکس
  - اسمگ -> اسمگ
  - اسنوا -> اسنوا
  - اکسپریال -> اکسپریال
  - ال جی -> ال جی
  - الگانس -> الگانس
  - امرسان -> امرسان
  - ایکس ویژن -> ایکس ویژن
  - اینترنشنال آنیل -> اینترنشنال آنیل
  - ایندزیت -> ایندزیت
  - برتینو -> برتینو
  - برفاب -> برفاب
  - بکو -> بکو
  - بلومبرگ -> بلومبرگ
  - بوش -> بوش
  - پارس -> پارس
  - پارس خزر -> پارس خزر
  - پاکشوما -> پاکشوما
  - پاناسونیک -> پاناسونیک
  - تک الکتریک -> تک الکتریک
  - تکنوگاز -> تکنوگاز
  - توشیبا -> توشیبا
  - تی سی ال -> تی سی ال
  - تیوان -> تیوان
  - جنرال آدمیرال -> جنرال آدمیرال
  - جنرال هاوس -> جنرال هاوس
  - جی آدمیرال -> جی آدمیرال
  - جی پلاس -> جی پلاس
  - جی سان -> جی سان
  - دکستر -> دکستر
  - دوو -> دوو
  - ریتون -> ریتون
  - زانوسی -> زانوسی
  - زیرووات -> زیرووات
  - زیمنس -> زیمنس
  - ژنوا -> ژنوا
  - سامسونگ -> سامسونگ
  - سامیا -> سامیا
  - سپهر الکتریک -> سپهر الکتریک
  - سینجر -> سینجر
  - شارپ -> شارپ
  - فریدولین -> فریدولین
  - کرال -> کرال
  - کروپ -> کروپ
  - کندی -> کندی
  - لوپز -> لوپز
  - لیدر -> لیدر
  - مایدیا -> مایدیا
  - مجیک -> مجیک
  - هاردستون -> هاردستون
  - هافن برگ -> هافن برگ
  - هایر -> هایر
  - هایسنس -> هایسنس
  - هیتاچی -> هیتاچی
  - هیوندای -> هیوندای
  - وست پوینت -> وست پوینت
  - وستل -> وستل
  - ویرپول -> ویرپول
  - غیره -> غیره

### category
- **Title**: دسته‌بندی
- **Type**: object

### divider
- **Title**: سایر فیلتر‌ها
- **Type**: object

### exchange
- **Title**: نمایش معاوضه‌ها
- **Type**: object
- **Queries**: 
  - only-exchanges -> نمایش فقط معاوضه‌ها
  - exclude-exchanges -> حذف معاوضه‌ها

### goods-business-type
- **Title**: نوع آگهی‌دهنده
- **Type**: object
- **Queries**: 
  - all -> همه
  - personal -> شخصی
  - marketplace -> فروشگاه

### has-photo
- **Title**: فقط عکس‌دار
- **Type**: boolean

### price
- **Title**: قیمت
- **Type**: object
 - **Minimum**: 0
 - **Maximum**: N/A

### sort
- **Title**: ترتیب نمایش آگهی‌ها براساس
- **Type**: object
- **Queries**: 
  - quality_and_sort_date -> quality_and_sort_date
  - sort_date -> sort_date
  - cheapest -> cheapest
  - most_expensive -> most_expensive
  - production_year -> production_year
  - usage -> usage
  - most_popular -> most_popular
  - most_relevant -> most_relevant

### status
- **Title**: وضعیت کالا
- **Type**: object
 - **Items Type**: array
- **Queries**: 
  - new -> نو
  - like-new -> در حد نو
  - used -> کارکرده
  - repair-needed -> نیازمند تعمیر

### urgent
- **Title**: فقط فوری‌ها
- **Type**: boolean



---

### Category: watches



### category
- **Title**: دسته‌بندی
- **Type**: object

### divider
- **Title**: سایر فیلتر‌ها
- **Type**: object

### exchange
- **Title**: نمایش معاوضه‌ها
- **Type**: object
- **Queries**: 
  - only-exchanges -> نمایش فقط معاوضه‌ها
  - exclude-exchanges -> حذف معاوضه‌ها

### gender
- **Title**: مردانه یا زنانه
- **Type**: object
- **Queries**: 
  - زنانه -> زنانه
  - مردانه -> مردانه
  - زنانه و مردانه -> زنانه و مردانه

### goods-business-type
- **Title**: نوع آگهی‌دهنده
- **Type**: object
- **Queries**: 
  - all -> همه
  - personal -> شخصی
  - marketplace -> فروشگاه

### has-photo
- **Title**: فقط عکس‌دار
- **Type**: boolean

### price
- **Title**: قیمت
- **Type**: object
 - **Minimum**: 0
 - **Maximum**: N/A

### sort
- **Title**: ترتیب نمایش آگهی‌ها براساس
- **Type**: object
- **Queries**: 
  - quality_and_sort_date -> quality_and_sort_date
  - sort_date -> sort_date
  - cheapest -> cheapest
  - most_expensive -> most_expensive
  - production_year -> production_year
  - usage -> usage
  - most_popular -> most_popular
  - most_relevant -> most_relevant

### status
- **Title**: وضعیت کالا
- **Type**: object
 - **Items Type**: array
- **Queries**: 
  - new -> نو
  - like-new -> در حد نو
  - used -> کارکرده
  - repair-needed -> نیازمند تعمیر

### urgent
- **Title**: فقط فوری‌ها
- **Type**: boolean

### watch-type
- **Title**: نوع ساعت
- **Type**: object
 - **Items Type**: array
- **Queries**: 
  - آنالوگ -> آنالوگ
  - دیجیتال -> دیجیتال
  - هوشمند -> هوشمند
  - سایر -> سایر



---

### Category: water-cooler



### category
- **Title**: دسته‌بندی
- **Type**: object

### divider
- **Title**: سایر فیلتر‌ها
- **Type**: object

### exchange
- **Title**: نمایش معاوضه‌ها
- **Type**: object
- **Queries**: 
  - only-exchanges -> نمایش فقط معاوضه‌ها
  - exclude-exchanges -> حذف معاوضه‌ها

### goods-business-type
- **Title**: نوع آگهی‌دهنده
- **Type**: object
- **Queries**: 
  - all -> همه
  - personal -> شخصی
  - marketplace -> فروشگاه

### has-photo
- **Title**: فقط عکس‌دار
- **Type**: boolean

### price
- **Title**: قیمت
- **Type**: object
 - **Minimum**: 0
 - **Maximum**: N/A

### sort
- **Title**: ترتیب نمایش آگهی‌ها براساس
- **Type**: object
- **Queries**: 
  - quality_and_sort_date -> quality_and_sort_date
  - sort_date -> sort_date
  - cheapest -> cheapest
  - most_expensive -> most_expensive
  - production_year -> production_year
  - usage -> usage
  - most_popular -> most_popular
  - most_relevant -> most_relevant

### status
- **Title**: وضعیت کالا
- **Type**: object
 - **Items Type**: array
- **Queries**: 
  - new -> نو
  - like-new -> در حد نو
  - used -> کارکرده
  - repair-needed -> نیازمند تعمیر

### urgent
- **Title**: فقط فوری‌ها
- **Type**: boolean



---

### Category: water-cooler-refinery



### category
- **Title**: دسته‌بندی
- **Type**: object

### divider
- **Title**: سایر فیلتر‌ها
- **Type**: object

### exchange
- **Title**: نمایش معاوضه‌ها
- **Type**: object
- **Queries**: 
  - only-exchanges -> نمایش فقط معاوضه‌ها
  - exclude-exchanges -> حذف معاوضه‌ها

### goods-business-type
- **Title**: نوع آگهی‌دهنده
- **Type**: object
- **Queries**: 
  - all -> همه
  - personal -> شخصی
  - marketplace -> فروشگاه

### has-photo
- **Title**: فقط عکس‌دار
- **Type**: boolean

### price
- **Title**: قیمت
- **Type**: object
 - **Minimum**: 0
 - **Maximum**: N/A

### sort
- **Title**: ترتیب نمایش آگهی‌ها براساس
- **Type**: object
- **Queries**: 
  - quality_and_sort_date -> quality_and_sort_date
  - sort_date -> sort_date
  - cheapest -> cheapest
  - most_expensive -> most_expensive
  - production_year -> production_year
  - usage -> usage
  - most_popular -> most_popular
  - most_relevant -> most_relevant

### status
- **Title**: وضعیت کالا
- **Type**: object
 - **Items Type**: array
- **Queries**: 
  - new -> نو
  - like-new -> در حد نو
  - used -> کارکرده
  - repair-needed -> نیازمند تعمیر

### urgent
- **Title**: فقط فوری‌ها
- **Type**: boolean



---

### Category: water-heater-package-radiator



### category
- **Title**: دسته‌بندی
- **Type**: object

### divider
- **Title**: سایر فیلتر‌ها
- **Type**: object

### exchange
- **Title**: نمایش معاوضه‌ها
- **Type**: object
- **Queries**: 
  - only-exchanges -> نمایش فقط معاوضه‌ها
  - exclude-exchanges -> حذف معاوضه‌ها

### goods-business-type
- **Title**: نوع آگهی‌دهنده
- **Type**: object
- **Queries**: 
  - all -> همه
  - personal -> شخصی
  - marketplace -> فروشگاه

### has-photo
- **Title**: فقط عکس‌دار
- **Type**: boolean

### price
- **Title**: قیمت
- **Type**: object
 - **Minimum**: 0
 - **Maximum**: N/A

### sort
- **Title**: ترتیب نمایش آگهی‌ها براساس
- **Type**: object
- **Queries**: 
  - quality_and_sort_date -> quality_and_sort_date
  - sort_date -> sort_date
  - cheapest -> cheapest
  - most_expensive -> most_expensive
  - production_year -> production_year
  - usage -> usage
  - most_popular -> most_popular
  - most_relevant -> most_relevant

### status
- **Title**: وضعیت کالا
- **Type**: object
 - **Items Type**: array
- **Queries**: 
  - new -> نو
  - like-new -> در حد نو
  - used -> کارکرده
  - repair-needed -> نیازمند تعمیر

### urgent
- **Title**: فقط فوری‌ها
- **Type**: boolean



---

### Category: wc-accessories



### category
- **Title**: دسته‌بندی
- **Type**: object

### divider
- **Title**: سایر فیلتر‌ها
- **Type**: object

### exchange
- **Title**: نمایش معاوضه‌ها
- **Type**: object
- **Queries**: 
  - only-exchanges -> نمایش فقط معاوضه‌ها
  - exclude-exchanges -> حذف معاوضه‌ها

### goods-business-type
- **Title**: نوع آگهی‌دهنده
- **Type**: object
- **Queries**: 
  - all -> همه
  - personal -> شخصی
  - marketplace -> فروشگاه

### has-photo
- **Title**: فقط عکس‌دار
- **Type**: boolean

### price
- **Title**: قیمت
- **Type**: object
 - **Minimum**: 0
 - **Maximum**: N/A

### sort
- **Title**: ترتیب نمایش آگهی‌ها براساس
- **Type**: object
- **Queries**: 
  - quality_and_sort_date -> quality_and_sort_date
  - sort_date -> sort_date
  - cheapest -> cheapest
  - most_expensive -> most_expensive
  - production_year -> production_year
  - usage -> usage
  - most_popular -> most_popular
  - most_relevant -> most_relevant

### status
- **Title**: وضعیت کالا
- **Type**: object
 - **Items Type**: array
- **Queries**: 
  - new -> نو
  - like-new -> در حد نو
  - used -> کارکرده
  - repair-needed -> نیازمند تعمیر

### urgent
- **Title**: فقط فوری‌ها
- **Type**: boolean



---

### Category: wind



### category
- **Title**: دسته‌بندی
- **Type**: object

### divider
- **Title**: سایر فیلتر‌ها
- **Type**: object

### exchange
- **Title**: نمایش معاوضه‌ها
- **Type**: object
- **Queries**: 
  - only-exchanges -> نمایش فقط معاوضه‌ها
  - exclude-exchanges -> حذف معاوضه‌ها

### goods-business-type
- **Title**: نوع آگهی‌دهنده
- **Type**: object
- **Queries**: 
  - all -> همه
  - personal -> شخصی
  - marketplace -> فروشگاه

### has-photo
- **Title**: فقط عکس‌دار
- **Type**: boolean

### price
- **Title**: قیمت
- **Type**: object
 - **Minimum**: 0
 - **Maximum**: N/A

### sort
- **Title**: ترتیب نمایش آگهی‌ها براساس
- **Type**: object
- **Queries**: 
  - quality_and_sort_date -> quality_and_sort_date
  - sort_date -> sort_date
  - cheapest -> cheapest
  - most_expensive -> most_expensive
  - production_year -> production_year
  - usage -> usage
  - most_popular -> most_popular
  - most_relevant -> most_relevant

### status
- **Title**: وضعیت کالا
- **Type**: object
 - **Items Type**: array
- **Queries**: 
  - new -> نو
  - like-new -> در حد نو
  - used -> کارکرده
  - repair-needed -> نیازمند تعمیر

### urgent
- **Title**: فقط فوری‌ها
- **Type**: boolean



---

### Category: winter-sports



### category
- **Title**: دسته‌بندی
- **Type**: object

### divider
- **Title**: سایر فیلتر‌ها
- **Type**: object

### exchange
- **Title**: نمایش معاوضه‌ها
- **Type**: object
- **Queries**: 
  - only-exchanges -> نمایش فقط معاوضه‌ها
  - exclude-exchanges -> حذف معاوضه‌ها

### goods-business-type
- **Title**: نوع آگهی‌دهنده
- **Type**: object
- **Queries**: 
  - all -> همه
  - personal -> شخصی
  - marketplace -> فروشگاه

### has-photo
- **Title**: فقط عکس‌دار
- **Type**: boolean

### price
- **Title**: قیمت
- **Type**: object
 - **Minimum**: 0
 - **Maximum**: N/A

### sort
- **Title**: ترتیب نمایش آگهی‌ها براساس
- **Type**: object
- **Queries**: 
  - quality_and_sort_date -> quality_and_sort_date
  - sort_date -> sort_date
  - cheapest -> cheapest
  - most_expensive -> most_expensive
  - production_year -> production_year
  - usage -> usage
  - most_popular -> most_popular
  - most_relevant -> most_relevant

### status
- **Title**: وضعیت کالا
- **Type**: object
 - **Items Type**: array
- **Queries**: 
  - new -> نو
  - like-new -> در حد نو
  - used -> کارکرده
  - repair-needed -> نیازمند تعمیر

### urgent
- **Title**: فقط فوری‌ها
- **Type**: boolean



---

### Category: work-equipment



### category
- **Title**: دسته‌بندی
- **Type**: object

### divider
- **Title**: سایر فیلتر‌ها
- **Type**: object

### exchange
- **Title**: نمایش معاوضه‌ها
- **Type**: object
- **Queries**: 
  - only-exchanges -> نمایش فقط معاوضه‌ها
  - exclude-exchanges -> حذف معاوضه‌ها

### goods-business-type
- **Title**: نوع آگهی‌دهنده
- **Type**: object
- **Queries**: 
  - all -> همه
  - personal -> شخصی
  - marketplace -> فروشگاه

### has-photo
- **Title**: فقط عکس‌دار
- **Type**: boolean

### price
- **Title**: قیمت
- **Type**: object
 - **Minimum**: 0
 - **Maximum**: N/A

### sort
- **Title**: ترتیب نمایش آگهی‌ها براساس
- **Type**: object
- **Queries**: 
  - quality_and_sort_date -> quality_and_sort_date
  - sort_date -> sort_date
  - cheapest -> cheapest
  - most_expensive -> most_expensive
  - production_year -> production_year
  - usage -> usage
  - most_popular -> most_popular
  - most_relevant -> most_relevant

### status
- **Title**: وضعیت کالا
- **Type**: object
 - **Items Type**: array
- **Queries**: 
  - new -> نو
  - like-new -> در حد نو
  - used -> کارکرده
  - repair-needed -> نیازمند تعمیر

### urgent
- **Title**: فقط فوری‌ها
- **Type**: boolean



---

### Category: workspace



### business-type
- **Title**: آگهی‌دهنده
- **Type**: object
- **Queries**: 
  - personal -> شخصی
  - real-estate-business -> مشاور املاک

### category
- **Title**: دسته‌بندی
- **Type**: object

### daily_rent
- **Title**: اجاره روزانه
- **Type**: object
 - **Minimum**: 0
 - **Maximum**: N/A

### has-photo
- **Title**: عکس‌دار
- **Type**: boolean

### has-video
- **Title**: ویدیو‌دار
- **Type**: boolean

### person_capacity
- **Title**: ظرفیت
- **Type**: object
- **Queries**: 
  - {"min": 0, "max": 5} -> حداکثر ۵ نفر
  - {"min": 5, "max": 10} -> بین ۵ تا ۱۰ نفر
  - {"min": 10, "max": 15} -> بین ۱۰ تا ۱۵ نفر
  - {"min": 15, "max": 20} -> بین ۱۵ تا ۲۰ نفر
  - {"min": 20, "max": 25} -> بین ۲۰ تا ۲۵ نفر
  - {"min": 25, "max": 30} -> بین ۲۵ تا ۳۰ نفر
  - {"min": 30} -> بیش از ۳۰ نفر

### rooms
- **Title**: تعداد اتاق
- **Type**: object
- **Queries**: 
  - بدون اتاق -> بدون اتاق
  - یک -> ۱
  - دو -> ۲
  - سه -> ۳
  - چهار -> ۴
  - بیشتر -> بیشتر از ۴

### size
- **Title**: متراژ
- **Type**: object
 - **Minimum**: 0
 - **Maximum**: 1000000000

### sort
- **Title**: ترتیب نمایش آگهی‌ها براساس
- **Type**: object
- **Queries**: 
  - quality_and_sort_date -> quality_and_sort_date
  - sort_date -> sort_date
  - cheapest -> cheapest
  - most_expensive -> most_expensive
  - production_year -> production_year
  - usage -> usage
  - most_popular -> most_popular
  - most_relevant -> most_relevant

### urgent
- **Title**: فقط فوری‌ها
- **Type**: boolean



---

### Category: yarn-lights



### category
- **Title**: دسته‌بندی
- **Type**: object

### divider
- **Title**: سایر فیلتر‌ها
- **Type**: object

### exchange
- **Title**: نمایش معاوضه‌ها
- **Type**: object
- **Queries**: 
  - only-exchanges -> نمایش فقط معاوضه‌ها
  - exclude-exchanges -> حذف معاوضه‌ها

### goods-business-type
- **Title**: نوع آگهی‌دهنده
- **Type**: object
- **Queries**: 
  - all -> همه
  - personal -> شخصی
  - marketplace -> فروشگاه

### has-photo
- **Title**: فقط عکس‌دار
- **Type**: boolean

### price
- **Title**: قیمت
- **Type**: object
 - **Minimum**: 0
 - **Maximum**: N/A

### sort
- **Title**: ترتیب نمایش آگهی‌ها براساس
- **Type**: object
- **Queries**: 
  - quality_and_sort_date -> quality_and_sort_date
  - sort_date -> sort_date
  - cheapest -> cheapest
  - most_expensive -> most_expensive
  - production_year -> production_year
  - usage -> usage
  - most_popular -> most_popular
  - most_relevant -> most_relevant

### status
- **Title**: وضعیت کالا
- **Type**: object
 - **Items Type**: array
- **Queries**: 
  - new -> نو
  - like-new -> در حد نو
  - used -> کارکرده
  - repair-needed -> نیازمند تعمیر

### urgent
- **Title**: فقط فوری‌ها
- **Type**: boolean

## Background

This project originated from the need for data from [Divar](https://divar.ir) advertisements for a machine learning endeavor. To facilitate the data collection process, I extended the functionality of the pydivar library. By expanding the capabilities of this library, the project aims to gather comprehensive data from various categories on the Divar platform. This collected dataset serves as a valuable resource for the machine learning project, enabling the extraction of meaningful insights and patterns from classified ads.

## Discussion and Development

If you have questions or ideas for improvements, you can discuss them in [Github Issues](https://github.com/ali-ardakani/pydivar/issues).

## License

[MIT](LICENSE)