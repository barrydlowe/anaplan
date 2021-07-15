# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose

class GildedRoseTest(unittest.TestCase):
    def test_decrease_sell_in(self):
        item = [Item(name="Aged Brie", sell_in=10, quality=20)]
        gilded_rose = GildedRose(item)
        gilded_rose.update_quality()
        self.assertEqual(9, item[0].sell_in)

    def test_decrease_quality_before_sellin_date_passed(self):
        item = [Item(name="+5 Dexterity Vest", sell_in=10, quality=20)]
        gilded_rose = GildedRose(item)
        gilded_rose.update_quality()
        self.assertEqual(19, item[0].quality)

    def test_decrease_quality_double_after_sellin_date_passed(self):
        item = [Item(name="Elixir of the Mongoose", sell_in=-1, quality=20)]
        gilded_rose = GildedRose(item)
        gilded_rose.update_quality()
        self.assertEqual(18, item[0].quality)

    def test_quality_never_negative(self):
        item = [Item(name="Elixir of the Mongoose", sell_in=0, quality=0)]
        gilded_rose = GildedRose(item)
        gilded_rose.update_quality()
        self.assertEqual(0, item[0].quality)

    def test_brie_quality_never_above_max_quality(self):
        item = [Item(name="Aged Brie", sell_in=0, quality=50)]
        gilded_rose = GildedRose(item)
        gilded_rose.update_quality()
        self.assertEqual(50, item[0].quality)

    def test_sulfuras_never_changing(self):
        item = [Item(name="Sulfuras, Hand of Ragnaros", sell_in=5, quality=80)]
        gilded_rose = GildedRose(item)
        gilded_rose.update_quality()
        self.assertEqual(80, item[0].quality)

    def test_backstage_pass_quality_when_sellin_above_ten(self):
        item = [Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=11, quality=10)]
        gilded_rose = GildedRose(item)
        gilded_rose.update_quality()
        self.assertEqual(11, item[0].quality)

    def test_backstage_pass_quality_when_sellin_above_five(self):
        item = [Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=6, quality=10)]
        gilded_rose = GildedRose(item)
        gilded_rose.update_quality()
        self.assertEqual(12, item[0].quality)

    def test_backstage_pass_quality_when_sellin_less_than_five(self):
        item = [Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=3, quality=10)]
        gilded_rose = GildedRose(item)
        gilded_rose.update_quality()
        self.assertEqual(13, item[0].quality)

    def test_backstage_pass_quality_when_sellin_zero(self):
        item = [Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=0, quality=10)]
        gilded_rose = GildedRose(item)
        gilded_rose.update_quality()
        self.assertEqual(0, item[0].quality)

    def test_backstage_pass_quality_when_sellin_less_than_zero(self):
        item = [Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=-1, quality=10)]
        gilded_rose = GildedRose(item)
        gilded_rose.update_quality()
        self.assertEqual(0, item[0].quality)

    def test_conjured_mana_cake_quality_degrades_double_rate(self):
        item = [Item(name="Conjured Mana Cake", sell_in=5, quality=10)]
        gilded_rose = GildedRose(item)
        gilded_rose.update_quality()
        self.assertEqual(8, item[0].quality)

if __name__ == '__main__':
    unittest.main()
