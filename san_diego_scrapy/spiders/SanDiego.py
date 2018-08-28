import scrapy
import json


class Scraper(scrapy.Spider):
    name = "SanDiego"

    def start_requests(self):
        url = "https://arcc-acclaim.sdcounty.ca.gov/Search/GridResults"
        querystring = {"RecordDate": "8%2F16%2F2018"}
        request_data = json.dumps(querystring)
        params = {'X-Requested-With': "XMLHttpRequest",
                  'Cookie': "OpenDocumentInPDF=true; Group4=SearchGridForRecordDate%3D%7B%22SearchTypeRecordDate%22%3A%7B%22NumberOfPages%22%3A%7B%22show%22%3A%221%22%2C%22width%22%3A%2274px%22%7D%2C%22DirectName%22%3A%7B%22show%22%3A%221%22%2C%22width%22%3A%22124px%22%7D%2C%22IndirectName%22%3A%7B%22show%22%3A%221%22%2C%22width%22%3A%22360px%22%7D%2C%22InstrumentNumber%22%3A%7B%22show%22%3A%221%22%2C%22width%22%3A%2299px%22%7D%2C%22RecordDate%22%3A%7B%22show%22%3A%221%22%2C%22width%22%3A%2299px%22%7D%2C%22DocTypeDescription%22%3A%7B%22show%22%3A%221%22%2C%22width%22%3A%22141px%22%7D%2C%22ParcelNumber%22%3A%7B%22show%22%3A%221%22%2C%22width%22%3A%22174px%22%7D%2C%22BookType%22%3A%7B%22show%22%3A%221%22%2C%22width%22%3A%2249px%22%7D%2C%22SecondarySequenceNumber%22%3A%7B%22show%22%3A%221%22%2C%22width%22%3A%2274px%22%7D%2C%22BookPage%22%3A%7B%22show%22%3A%221%22%2C%22width%22%3A%2294px%22%7D%7D%7D; ASP.NET_SessionId=csnskfscbjzwgjxwbqubacg5; AcclaimWebUserPreferencesCookie=UserDefaultSearchGridRowPageSize=25&UserPurchaseHistoryDateType=PurchaseDate&UserDefaultPaymentOption=CreditCard&UserDefaultEmailPaymentConfirmationOption=True&UserDefaultAutoLoadImages=True&UserDefaultAutoCompleteEnabled=False"
                  }
        metadata = {'dont_merge_cookies': True}
        yield scrapy.Request(url, method="POST",
                             body=request_data,
                             headers=params,
                             meta=metadata,
                             callback=self.parse)

    def parse(self, response):
        data = json.loads(response.body)
        # print(data)
        for i in data['data']:
            print(i['TransactionItemId'], i['InstrumentNumber'], i['DirectName'], i['IndirectName'])
