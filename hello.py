from cgi import parse_qs

def application(env, start_responce):
	
	query = parse_qs(env['QUERY_STRING'])
	body = []

	for key, values in query.items():
		for item in values:
			body.append(key + '=' + item + "\r\n")


	start_responce('200 OK', [('Content-Type', 'text/plain')])

	return body