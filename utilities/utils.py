class Utils:

    @staticmethod
    def assert_page_url_ends_with(url_text, page_end):
        assert url_text.endswith(page_end)
        print(f"Assert page url ends with {page_end}:> passed!")
