#! /usr/bin/python3
# -*- coding: utf-8 -*-

class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            #item.sell_in = item.sell_in - 1
            if item.name == "Aged Brie":
                if item.quality > 0:
                    item.quality = item.quality + 1
                if item.sell_in < 0:
                    item.quality = item.quality + 1
                if item.quality > 50:
                    item.quality = 50
            elif item.name == "Backstage passes to a TAFKAL80ETC concert":
                # increase by 1, 2 or 3 depending on sell_in value
                if item.sell_in > 10:
                    item.quality = item.quality + 1
                elif item.sell_in <= 10 and item.sell_in > 5:
                    item.quality = item.quality + 2
                elif item.sell_in <= 5 and item.sell_in > 0:
                    item.quality = item.quality + 3 
                elif item.sell_in <= 0:
                    item.quality = 0
                # reset quality to 50 if it goes above 50
                if item.quality > 50:
                    item.quality = 50
            elif item.name == "Conjured Mana Cake":
                if item.quality > 0:
                    item.quality = item.quality - 2
                if item.quality < 0:
                    item.quality = 0
            elif item.name == "Elixir of the Mongoose":
                if item.quality > 0:
                    item.quality = item.quality - 1
                if item.sell_in < 0:
                    item.quality = item.quality - 1
                if item.quality < 0:
                    item.quality = 0
            elif item.name == "+5 Dexterity Vest":
                if item.quality > 0:
                    item.quality = item.quality - 1
                if item.quality < 0:
                    item.quality = 0
            elif item.name == "Sulfuras, Hand of Ragnaros":
                item.quality = 80
            item.sell_in = item.sell_in - 1

class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
