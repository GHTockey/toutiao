from app import createFlaskAPP

app = createFlaskAPP('dev')


@app.route('/')
def route_map():
    return {
        rule.endpoint: rule.rule for rule in app.url_map.iter_rules()
    }
