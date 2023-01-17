import time

from pages.elements_page import TextBoxPage


class TestElements:
    class TestTextBox:

        def test_text_box(self, browser):
            text_box_page = TextBoxPage(browser, 'https://demoqa.com/text-box')
            text_box_page.open()
            text_box_page.fill_all_fields()
            output_name, output_email, output_addr, output_per_addr = text_box_page.check_filled_form()
            print(output_name)
            print(output_email)
            print(output_addr)
            print(output_per_addr)
            time.sleep(5)
