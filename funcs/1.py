import requests
url = 'https://api.leroymerlin.ru/mobile/notifications?regionsId=34&screenId=pdp'
headera = {'apiKey': 'NLdu-FEUbU-CCrd-otTWYJGhDfZZKYHAxVd-QksZEMMtCUkUKk'}
req = requests.get(url, headers=headera, verify=False )
# print(req.headers)

# print(datetime.isoformat(datetime.now(), 'T'))
# d = datetime.now()
# dz = d.strftime('%Y-%m-%d')
# dzz = d.strftime('%Y-%m-%dT%H:%M:%S+02:00')
#
# print(dz)
# print(dzz)
# s = [1]
# e = [13]
# a = {'a': 1}
# b = {'b': 1}
# print(a.update(b))
# req_json = {'access-token': 'c09192b0-139f-45e0-a380-c1f0cdeaa795',
#             'refresh-token': '993e3fa8-1ba4-4fb5-b9ff-143a0646d730',
#             'expires-in': '10787', 'user':
#                 {'customerNumber': '19994204', 'email': '5sh8gdq@antif.ua',
#                  'phone': '+79111111111', 'firstName': 'Къюеевич', 'lastName': 'Tester'}}
#
# token = req_json['access-token']
# # print(token)
# qheader = {'apikey': 'NLdu-FEUbU-CCrd-otTWYJGhDfZZKYHAxVd-QksZEMMtCUkUKk',
#           'channel': '1', 'mobile-version': '4.6.1', 'Date': '2021-03-16T15:49:29+02:00', 'mobile-platform': 'ios'}


# header['хер'] = token
# print(header)
# header['ass'] = 'gfgfgfg'
# print(header)

req = {
	"appointments": [{
		"startDate": "2021-03-18T00:00:00+03:00",
		"endDate": "2021-03-18T00:00:00+03:00",
		"periods": [{
			"start": "2021-03-18T08:00:00+03:00",
			"end": "2021-03-18T23:00:00+03:00",
			"default": True
		}, {
			"start": "2021-03-18T08:00:00+03:00",
			"end": "2021-03-18T13:00:00+03:00",
			"default": True
		}, {
			"start": "2021-03-18T13:00:00+03:00",
			"end": "2021-03-18T18:00:00+03:00",
			"default": True
		}, {
			"start": "2021-03-18T18:00:00+03:00",
			"end": "2021-03-18T23:00:00+03:00",
			"default": True
		}]
	}, {
		"startDate": "2021-03-19T00:00:00+03:00",
		"endDate": "2021-03-19T00:00:00+03:00",
		"periods": [{
			"start": "2021-03-19T08:00:00+03:00",
			"end": "2021-03-19T23:00:00+03:00",
			"default": True
		}, {
			"start": "2021-03-19T08:00:00+03:00",
			"end": "2021-03-19T13:00:00+03:00",
			"default": True
		}, {
			"start": "2021-03-19T13:00:00+03:00",
			"end": "2021-03-19T18:00:00+03:00",
			"default": True
		}, {
			"start": "2021-03-19T18:00:00+03:00",
			"end": "2021-03-19T23:00:00+03:00",
			"default": True
		}]
	}, {
		"startDate": "2021-03-20T00:00:00+03:00",
		"endDate": "2021-03-20T00:00:00+03:00",
		"periods": [{
			"start": "2021-03-20T08:00:00+03:00",
			"end": "2021-03-20T23:00:00+03:00",
			"default": True
		}, {
			"start": "2021-03-20T08:00:00+03:00",
			"end": "2021-03-20T13:00:00+03:00",
			"default": True
		}, {
			"start": "2021-03-20T13:00:00+03:00",
			"end": "2021-03-20T18:00:00+03:00",
			"default": True
		}, {
			"start": "2021-03-20T18:00:00+03:00",
			"end": "2021-03-20T23:00:00+03:00",
			"default": True
		}]
	}, {
		"startDate": "2021-03-21T00:00:00+03:00",
		"endDate": "2021-03-21T00:00:00+03:00",
		"periods": [{
			"start": "2021-03-21T08:00:00+03:00",
			"end": "2021-03-21T23:00:00+03:00",
			"default": True
		}, {
			"start": "2021-03-21T08:00:00+03:00",
			"end": "2021-03-21T13:00:00+03:00",
			"default": True
		}, {
			"start": "2021-03-21T13:00:00+03:00",
			"end": "2021-03-21T18:00:00+03:00",
			"default": True
		}, {
			"start": "2021-03-21T18:00:00+03:00",
			"end": "2021-03-21T23:00:00+03:00",
			"default": True
		}]
	}, {
		"startDate": "2021-03-22T00:00:00+03:00",
		"endDate": "2021-03-22T00:00:00+03:00",
		"periods": [{
			"start": "2021-03-22T08:00:00+03:00",
			"end": "2021-03-22T23:00:00+03:00",
			"default": True
		}, {
			"start": "2021-03-22T08:00:00+03:00",
			"end": "2021-03-22T13:00:00+03:00",
			"default": True
		}, {
			"start": "2021-03-22T13:00:00+03:00",
			"end": "2021-03-22T18:00:00+03:00",
			"default": True
		}, {
			"start": "2021-03-22T18:00:00+03:00",
			"end": "2021-03-22T23:00:00+03:00",
			"default": True
		}]
	}, {
		"startDate": "2021-03-23T00:00:00+03:00",
		"endDate": "2021-03-23T00:00:00+03:00",
		"periods": [{
			"start": "2021-03-23T08:00:00+03:00",
			"end": "2021-03-23T23:00:00+03:00",
			"default": True
		}, {
			"start": "2021-03-23T08:00:00+03:00",
			"end": "2021-03-23T13:00:00+03:00",
			"default": True
		}, {
			"start": "2021-03-23T13:00:00+03:00",
			"end": "2021-03-23T18:00:00+03:00",
			"default": True
		}, {
			"start": "2021-03-23T18:00:00+03:00",
			"end": "2021-03-23T23:00:00+03:00",
			"default": True
		}]
	}, {
		"startDate": "2021-03-24T00:00:00+03:00",
		"endDate": "2021-03-24T00:00:00+03:00",
		"periods": [{
			"start": "2021-03-24T08:00:00+03:00",
			"end": "2021-03-24T23:00:00+03:00",
			"default": True
		}, {
			"start": "2021-03-24T08:00:00+03:00",
			"end": "2021-03-24T13:00:00+03:00",
			"default": True
		}, {
			"start": "2021-03-24T13:00:00+03:00",
			"end": "2021-03-24T18:00:00+03:00",
			"default": True
		}, {
			"start": "2021-03-24T18:00:00+03:00",
			"end": "2021-03-24T23:00:00+03:00",
			"default": True
		}]
	}],
	"totalPriceDetails": {
		"priceProducts": 1316,
		"priceDelivery": 290,
		"priceLift": 12,
		"totalPrice": 1606
	}
}


print(req['appointments'])
print(req['appointments'][0]['periods'])