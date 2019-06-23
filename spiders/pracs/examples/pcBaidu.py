# coding:utf-8
import re
from urllib import request,parse
from urllib.request import urlopen

url = "https://fe-api.zhaopin.com/c/i/sou?pageSize=90&cityId=530&salary=0,0&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=%E6%B5%8B%E8%AF%95%E5%BC%80%E5%8F%91%E5%B7%A5%E7%A8%8B%E5%B8%88&kt=3&=0&at=051d5b568a734e1d99e4fe5e8adad171&rt=7161a116b728486ead66d2312f74ed87&_v=0.66243185&userCode=712467738&x-zp-page-request-id=16ffe1cf130b47468c188bab6fc14744-1561276964595-774936&x-zp-client-id=3ee57aab-fed5-4db0-84fa-bc8daaec87d0"
ua_headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36",
}

# keyword = input("请输入需要查询的关键字：")
# wd = {"wd":keyword}
#
# fullurl = url + "?" + parse.urlencode(wd)

# print(fullurl)
request = request.Request(url, headers=ua_headers)

response = urlopen(request)
# urls = str(response)
contents = str(response.read())
r = r'positionURL":"(.*?\.htm)","companyLogo'
# r = r'(https://jobs.zhaopin.com/CC000362500J00165373813.htm)'
content = re.findall(r,contents)
print(content)