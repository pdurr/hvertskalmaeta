import unittest
from hvert import determine_site

class TestDetermineContestSite(unittest.TestCase):

    def test_reykjavik(self):
        result = determine_site("Reykjavik")
        self.assertEqual(result, "Reykjavik")

    def test_kopavogur(self):
        result = determine_site("Kopavogur")
        self.assertEqual(result, "Reykjavik")

    def test_akureyri(self):
        result = determine_site("Akureyri")
        self.assertEqual(result, "Akureyri")

    def test_close_call(self):
        result = determine_site("Seltjarnarnes")
        self.assertEqual(result, "Reykjavik")

if __name__ == '__main__':
    unittest.main()
