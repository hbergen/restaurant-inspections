"""Pull food safety inspection results from King County Public Health API"""

import requests
import xml.etree.ElementTree as ET
import pandas as pd



def get_attribute(node, attribute):
    try:
        return node.find(attribute).text
    except:
        return None


def get_url(**kwargs):
    '''Format URL to request data with parameters

    Kwargs
    ------
    Business_Name - string
    Business_Address - string
    Zip_Code - string
    Inspection_Start - string with valid date in format MM/DD/YYYY
    Inspection_End - string with valid date in format MM/DD/YYYY
    Violation_Points - string with Integer <= 999
    Violation_Red_Points - string with Integer <=999
    City - string
    '''
    if kwargs == None:
        print('Oh no! You forgot to select at least one parameter')
        return
    else:
        url = 'http://info.kingcounty.gov/health/ehs/foodsafety/inspections/XmlRest.aspx?'
        for key in kwargs:
            s = '='.join([key, str(kwargs[key])])
            url = '&'.join([url, s])
        return url


def get_xml(url_request):
    ''' Returns root XML tree structure using King County's API

        Example
        =======
        Returns inspection data in zip code 98101 since 1/1/2016
        >>> url = get_url(Business_Name='TOULOUSE PETIT KITCHEN & LOUNGE')
        >>> get_xml(url)
        Notes
        =====
        The API appears to break using parameter Inspection_Closed_Business
    '''
    response = requests.get(url_request)
    root = ET.fromstring(response.content)
    # Remove the King County data disclaimer
    disclaimer_element = root.find('Disclaimer')
    root.remove(disclaimer_element)
    return root


def get_inspections(business):
    '''Return all inspections for a particular business'''
    inspections = business.findall('Inspection')
    return inspections


def get_violations(business, inspection):
    '''Return all violations for a particular business, inspection combo'''
    violations = inspection.findall('Violation')
    return violations


class Business():
    '''A requested business.

    Example
    -------
    >>> business = Business('Toulouse Petit Kitchen & Lounge')
    >>> business_root = business.root_node
    '''
    def __init__(self, name):
        '''Initialize with the name of the business.'''
        self.name = name.upper()

    @property
    def request_url(self):
        '''Get URL string to request inspections for the business'''
        return get_url(Business_Name=self.name)

    @property
    def root_node(self):
        '''Get the root node of inspections for the requested business'''
        root = get_xml(self.request_url)
        # The business root is the first element from this
        business_root = root[0]
        return business_root

    @property
    def program_identifier(self):
        '''King County Program Identifier for the business'''
        return self.root_node.find('Program_Identifier').text

    @property
    def description(self):
        '''King County description for the business'''
        return self.root_node.find('Description').text

    @property
    def address(self):
        '''King County street address, city, and zip code for the business'''
        address = self.root_node.find('Address').text
        city = self.root_node.find('City').text
        zip_code = self.root_node.find('Zip_Code').text
        return address, city, zip_code

    @property
    def phone_number(self):
        '''King County listed phone number for the business'''
        return self.root_node.find('Phone').text

    @property
    def lat_long(self):
        '''King County listed latitude and longitude for the business'''
        latitude = self.root_node.find('Latitude').text
        longitude = self.root_node.find('Longitude').text
        return latitude, longitude
