import scrapy
# scrapy framework
class CompanySpider(scrapy.Spider):
    name = "company"
    allowed_domains = ["trangvangvietnam.com"]
    start_urls = [
        "https://trangvangvietnam.com/categories/1234/cong-ty-xay-dung.html"
    ]

    def parse(self, response):
        companies = response.css(".listing")  # selector tuỳ layout

        for company in companies:
            yield {
                "name": company.css(".company-name::text").get(),
                "phone": company.css(".company-phone::text").get(),
                # Thêm các trường khác sau
            }

        next_page = response.css(".pagination .next::attr(href)").get()
        if next_page:
            yield response.follow(next_page, callback=self.parse)
