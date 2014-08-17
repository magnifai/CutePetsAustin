#!/usr/bin/python
# -*- coding: utf-8 -*-

from unittest import TestCase

import meow


class TestMeow(TestCase):

    def setUp(self):
        self.maxDiff = None

    def get_data_file(self, filename):
        with open('tests/data/{}'.format(filename), 'rb') as fh:
            data = fh.read()
        return data

    def test_parse_petharbor_pet_details(self):
        html = self.get_data_file('detail.html')
        pet_details = meow.parse_petharbor_pet_details(html, 666, 69)
        expected = {
            'name': 'Tigger',
            'desc': 'I am a orange tabby, unaltered male, who looks like a Domestic Shorthair mix. I am estimated to be 4 months old. I have been at the shelter since Aug 16, 2014. This information is less than 1 hour old.',
            'url': 'http://www.petharbor.com/pet.asp?uaid=69.666',
        }
        self.assertEquals(expected, pet_details)

    def test_parse_petharbor_pet_details_midnight(self):
        html = self.get_data_file('detail_midnight.html')
        pet_details = meow.parse_petharbor_pet_details(html, 666, 69)
        expected = {
            'name': 'Midnight',
            'desc': 'I am a black, unaltered male, who looks like a Domestic Shorthair mix. I am estimated to be 4 months old. I have been at the shelter since Aug 16, 2014. This information is less than 1 hour old.',
            'url': 'http://www.petharbor.com/pet.asp?uaid=69.666',
        }
        self.assertEquals(expected, pet_details)

    def test_parse_petharbor_pet_details_this_pet(self):
        html = self.get_data_file('detail_thispet.html')
        pet_details = meow.parse_petharbor_pet_details(html, 666, 69)
        expected = {
            'name': None,
            'desc': 'I am a black, unaltered female, who looks like a Domestic Shorthair mix. I am estimated to be 15 weeks old. I have been at the shelter since Aug 16, 2014. This information is less than 1 hour old.',
            'url': 'http://www.petharbor.com/pet.asp?uaid=69.666',
        }
        self.assertEquals(expected, pet_details)
