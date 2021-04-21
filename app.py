from flask import Flask, redirect, request

app = Flask(__name__)
app.debug = True


@app.route('/')
def b1():
    param = request.args.get('cmd')

    try:
        # Grabbing the command and the query, if there is one
        query_index = param.index(' ')
        command = param[:query_index]
        print("command is: ", command)
        query = param[query_index:]
        query_found = True
    except ValueError:
        query_found = False
        command = param  # Since no space is found

    # Start parsing commands
    if command == 'yt':
        if not query_found:
            return redirect('https://www.youtube.com')
        else:
            return redirect('https://www.youtube.com/results?search_query={query}'.format(query=query))

    elif command == 'r':
        return redirect('https://www.reddit.com')
    elif command == 'gm':
        return redirect('https://mail.google.com/mail/u/0/')
    elif command == 'gh':
        return redirect('https://www.github.com')
    else:
        return redirect('http://www.google.com/search?q={param}'.format(param=param))
