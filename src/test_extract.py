import unittest
from extract_links_and_images import extract_markdown_images, extract_markdown_links
class TestExtract(unittest.TestCase):
    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
        "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)
    def test_extract_multiple_images(self):
        matches = extract_markdown_images(
            "![cat](cat.png) and ![dog](dog.jpg)"
        )
        self.assertEqual(
            [
                ("cat", "cat.png"),
                ("dog", "dog.jpg"),
            ],
            matches,
        )
    def test_extract_no_images(self):
        matches = extract_markdown_images(
            "This text has no images."
        )
        self.assertEqual([], matches)
    def test_extract_single_link(self):
        matches = extract_markdown_links(
            "Go to [Google](https://google.com)"
        )
        self.assertEqual(
            [("Google", "https://google.com")],
            matches,
        )
    def test_extract_multiple_links(self):
        matches = extract_markdown_links(
            "[Google](https://google.com) and [GitHub](https://github.com)"
        )
        self.assertEqual(
            [
                ("Google", "https://google.com"),
                ("GitHub", "https://github.com"),
            ],
            matches,
        )
    def test_extract_multiple_links(self):
        matches = extract_markdown_links(
            "[Google](https://google.com) and [GitHub](https://github.com)"
        )
        self.assertEqual(
            [
                ("Google", "https://google.com"),
                ("GitHub", "https://github.com"),
            ],
            matches,
        )
    def test_ignore_images_when_extracting_links(self):
        matches = extract_markdown_links(
            "![image](image.png) and [Google](https://google.com)"
        )
        self.assertEqual(
            [("Google", "https://google.com")],
            matches,
        )
    def test_empty_string(self):
        self.assertEqual([], extract_markdown_images(""))
        self.assertEqual([], extract_markdown_links(""))
if __name__ == "__main__":
    unittest.main()