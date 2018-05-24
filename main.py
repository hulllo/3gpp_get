import requests
import os

import downloadbar



from bs4 import BeautifulSoup

def geturl(id):
    print('waiting for website responed')
    try:
        r = requests.get('https://portal.3gpp.org/desktopmodules/Specifications/SpecificationDetails.aspx?specificationId={0}'.format(id))
    except  :
        print('website respone fail,retry...')
        r = requests.get('https://portal.3gpp.org/desktopmodules/Specifications/SpecificationDetails.aspx?specificationId={0}'.format(id))
    if r.status_code == 200:
        print('respone successful')
    else:
        print('<{0}>website respone fail,retry...'.format(r.status_code))
        r = requests.get('https://portal.3gpp.org/desktopmodules/Specifications/SpecificationDetails.aspx?specificationId={0}'.format(id))
    soup = BeautifulSoup(r.content, 'lxml')
    tag = soup.find_all('tr', id = 'SpecificationReleaseControl1_rpbReleases_i0_ctl00_specificationsVersionGrid_ctl00__0')
    if tag == []:
        print('item not found\n***\n')
        url = ''
        path = ''
        filename = ''
        return url, path, filename
    tag2 =tag[0].find_all('div', class_='text-center')
    print('newest version is {0}'.format(tag2[1].a.string))
    if tag2[1].a.has_attr('href'):
        url = tag2[1].a['href']
        if url == '':
            print('No download link')
            url = ''
            path = ''
            filename = ''
            return url, path, filename
    else:
        print('No download link\n***\n')
        url = ''
        path = ''
        filename = ''
        return url, path, filename
    urlist = url.split('/')
    path = 'G:/OneDrive/OneDrive/资料/3gpp/{0}/{1}/{2}'.format(urlist[-4], urlist[-3], urlist[-2])
    filename = '{0}/{1}_{2}'.format(path, tag2[1].a.string, urlist[-1])
    return url, path, filename
def download(url, path, filename):
    if os.path.exists(filename):
        print('file exeist')
        return
    else:
        print('downloading...')


    a = os.path.exists(path)
    if a == False:
        print('director do not exeist,Creating...')
        os.makedirs(path)
        a = os.path.exists(path)
        if a == True:
            print('director create successful')
    print('downloading to {0}'.format(filename))
    downloadbar.main(url, filename)
    return filename

if __name__ == '__main__':
    filedic = {
        '38.817-01':'3359',
        '38.101-3':'3285',
        '38.101-3':'3285',
        '38.101-4':'3366',
        '38.306':'3193',
        '38.521-1':'3381',
        '38.521-2':'3385',
        '38.521-3':'3386',
        '38.101':'3201',
        '38.101-1':'3283',
        '38.101-2':'3284',
        '36.101':'2411', 
        '36.306':'2434', 
        '36.521-1':'2469', 
        '36.521-2':'2470', 
        '36.521-3':'2471',
        '25.101':'1151',
        '25.102':'1152',
        '25.306':'1169',
        '34.121':'2362',
        '34.121-1':'2363',
        '34.121-2':'2364',
        '34.122':'2365'
        }
    # filedic = {'38.101-1':'3283'}
    updatelist = []
    for n in filedic:
        print('TS {0} 分析中...'.format(n))
        url, path, filename = geturl(filedic[n])
        if url == '' or path == '' or filename =='':
            continue
        filename = download(url, path, filename)
        if filename == None:
            pass
        else:
            updatelist.append(filename.split('/')[-1])
        print('TS {0} 分析完毕...\n>>>\n'.format(n))
    print('follow files update\n')
    for n in updatelist:
        print(n)
input('Press "Enter" to Exit.')