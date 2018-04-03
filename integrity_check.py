import re

original = open('hlj_sitemap.xml')
revised = open('hlj_sitemap_2.xml')

o_urls = []
r_urls = []

i = 0

for line in original:
    if line.startswith('<url>'):
        i += 1
        result = re.search('<url><loc>(.*)</loc><lastmod>', line).group(1)
        result = result.replace('http://', 'https://').lower()
        o_urls.append(result)

for line in revised:
    if line.startswith('<url>'):
        i += 1
        result = re.search('<url><loc>(.*)</loc><lastmod>', line).group(1)
        r_urls.append(result)

mismatches = []

o_urls = list(set(o_urls))

for o_url in o_urls:
    if o_url not in r_urls:
        mismatches.append(o_url)
    else:
        r_urls.remove(o_url)

print(mismatches[0:10])

original.close()
revised.close()
